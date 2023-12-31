from django.shortcuts import render , redirect , HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from django import template
from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa
from .utils import render_to_pdf #created in step 4
from django.db import IntegrityError
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from DOCTOR.models import *
from PATIENT.models import *
from COMMON_APP.models import *
from core.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request , 'home.html',{"user":None})

def register(request) :
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['post'])
        try:
            user = User.objects.get(username=request.POST['username'])
            print(user)
            return render(request,'register.html')
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['pass1'])
            if request.POST['post'] == 'Patient':
                new = Patient(phone=request.POST['phone'],name=request.POST['name'],email=request.POST['email'],username=user)
                try:
                    new.save()  
                except IntegrityError:
                    print('Phone already exists!')
                    return render(request, 'register.html')

                c_patient = Invoice(patient = new , outstanding = 0 , paid = 0)
                c_patient.save()

                return render(request,'login.html')
            else:
                new = Docter(phone=request.POST['phone'],name=request.POST['name'],email=request.POST['email'],username=user)
                try:
                    new.save()  
                except IntegrityError:
                    print('Phone already exists!')
                    return render(request, 'register.html')
                return render(request,'login.html')
    
    else:
        return render(request , 'register.html')


# Login
def login(request):
    if request.method == 'POST':
        try:
            # Check User in DB
            uname = request.POST['username']
            pwd = request.POST['pass1']
            user_authenticate = auth.authenticate(username=uname, password=pwd)
            if user_authenticate is not None:
                user = User.objects.get(username=uname)
                try:
                    data = Patient.objects.get(username=user)
                    print(data)
                    print('Patient has been Logged')
                    auth.login(request, user_authenticate)
                    return redirect('dashboard', user="P")
                except:
                    try:
                        data = Docter.objects.get(username=user)
                        auth.login(request, user_authenticate)
                        print('Doctor has been Logged')
                        return redirect('dashboard', user="D")
                    except:
                        return redirect('/')
            else:
                print('Login Failed')
                return render(request, 'login.html')
        except:
            return render(request, 'login.html')
    return render(request, 'login.html')


# Logout
def logout(request):
    auth.logout(request)
    print('Logout')
    return redirect('/login')


# Feedback
def feedback(request):
	status = False
	if request.user:
		status = request.user
	user_id = User.objects.get(username=request.user)
	print(user_id)
	patient = Patient.objects.get(username = user_id)
	data = Prescription2.objects.filter(patient = patient)
	return render(request , 'feedback.html',{"data":data , 'user' : "P" , 'status' : status})

# Profile
def profile(request, user):
    print(request.user)
    userid = User.objects.get(username=request.user)
    status = False
    if request.user:
        status = request.user
    if request.method == "POST":
        print(request.POST['name'])
        if user == "P":
            update = Patient.objects.get(username=userid)
            update.name = request.POST['name']
            update.phone = request.POST['phone']
            update.email = request.POST['email']
            update.gender = request.POST['gender']
            update.age = request.POST['age']
            update.blood = request.POST['blood']
            update.address = request.POST['address']


            update.case = request.POST['case']
            try:
                myfile = request.FILES['report']
                fs = FileSystemStorage(location='media/report/')
                filename = fs.save(myfile.name,myfile)
            # print(name,file)
                url = fs.url(filename)
                print(url)
                update.medical = url
            except:
                pass
            update.save()
            return redirect('dashboard',user = user)
        else:
            update = Docter.objects.get(username=userid)
            update.name = request.POST['name']
            update.phone = request.POST['phone']
            update.email = request.POST['email']
            update.gender = request.POST['gender']
            update.age = request.POST['age']
            update.blood = request.POST['blood']
            update.address = request.POST['address']
            update.save()
            return redirect('dashboard',user = user)


    if user == "P":
        userdata = Patient.objects.get(username=userid)
        return render(request  , 'patient_profile.html',{'userdata' : userdata , 'user':user, "status": status})

    else:
        userdata  = Docter.objects.get(username=userid)
        return render(request  , 'docter_profile.html',{'userdata' : userdata , 'user':user, "status": status})


    return redirect('/')

def dashboard(request , user):
    print(user)
    status = False
    if request.user:
        status = request.user
    if user == "AnonymousUser":
        return redirect('home')
    
    return render(request , 'home.html', {'user':user, "status": status})


def create_appointment(request , user):
    status = False
    if request.user:
        status = request.user

    if request.method == "POST":
        d_id = int(request.POST['docter'])
        p_id = int(request.POST['patient'])

        docter = Docter.objects.get(pk=d_id)
        patient = Patient.objects.get(pk=p_id)
        machine = request.POST['machine']
        organ = request.POST['organs']
        p_id = int(request.POST['patient'])
        date_and_time = request.POST['appointmentDates']
        wheelchair = request.POST.get('wheelchairNeeded', 'No')
        weight = request.POST['weight']
        print(wheelchair)
        new_appointment = Appointment(docterid = docter , patientid = patient, machine=machine, organ=organ ,time = date_and_time.split("T")[1] ,  date = date_and_time.split("T")[0], wheelchair=wheelchair, weight=weight,)
        new_appointment.save()
        send_confirmation(new_appointment)
        return redirect('myappointment')

    patient_names = Patient.objects.all()
    docter_names = Docter.objects.all() 

    return render(request , 'create_appointment.html' , {'user':user, "status": status , "patient_names" : patient_names , 
        "docter_names" : docter_names })

# Delete Patient
def delete_patient(request , id ):
    data = Patient.objects.get(id=id)
    data.delete()
    return redirect('receptionist_dashboard' , user="R")

def myappointment(request):
    status = False
    if request.user:
        status = request.user
    user_id = User.objects.get(username=request.user)
    patient= Patient.objects.get(username=user_id)
    data = Appointment.objects.filter(patientid=patient)
    doctors = Docter.objects.all()
    return render(request , 'my_appointment.html' , {'data':data, 'user' :"P" , 'doctors': doctors, 'status':status, 'user_name':patient})


# Doctor Appointsments

def docter_appointment(request):
    status = False
    if request.user:
        status = request.user
    user_id = User.objects.get(username=request.user)
    docter= Docter.objects.get(username=user_id)
    data = Appointment.objects.all()

    return render(request , 'doctorappointments.html' , {'data':data, 'user' :"D" , 'status':status})


# Docter Prescription

def docter_prescription(request):
    status = False
    if request.user:
        status = request.user
    user_id = User.objects.get(username=request.user)
    docter = Docter.objects.get(username=user_id)
    print(docter)
    pers   = Prescription2.objects.filter(docter = docter)
    print(len(pers))
    for i in pers:
        print(i.patient)
    return render(request , 'docter_prescription.html' , {'pers':pers, 'user' :"D" , 'status':status})

def room_reservation(request):
    status = False
    if request.user:
        status = request.user
    user_id = User.objects.get(username=request.user)
    patient = Patient.objects.get(username=user_id)
    data = Rooms.objects.all()
    return render(request , 'room_reservation.html' , { 'data' : data, 'user' :"P" , 'patient' : patient, 'status' : status})

def reserve_room(request):
    status = False
    if request.user:
        status = request.user
    user_id = User.objects.get(username=request.user)

    if request.method == 'POST':

        patient = Patient.objects.get(id=user_id)

        rooms = int(request.POST['rooms'].split('room',1)[1])

        room_number = Rooms.objects.get(room_number=rooms)
        date_and_time = request.POST['appointmentDates']

        new_room_reservation = RoomReservation(room_number=room_number,date=date_and_time,patient_id=patient.id)
        new_room_reservation.save()
        return redirect('room_reservation')

    patient_names = Patient.objects.all()
    docter_names = Docter.objects.all() 

    return render(request , 'room_reservation.html' , {'user':request.user, "status": status , "patient_names" : patient_names , 
        "docter_names" : docter_names })

def reserved_rooms(request):
    status = False
    if request.user:
        status = request.user
    user_id = User.objects.get(username=request.user)
    docter = Docter.objects.get(username=user_id)
    data = RoomReservation.objects.all()

    return render(request , 'reserved_rooms.html' , { 'data' : data , 'user' :"D" , 'status' : status })


# Create Prescription 
def create_prescription(request):
    status = False
    if request.user:
        status = request.user
    if request.method == 'POST':

        appointment = Appointment.objects.get(id=request.POST['appointment'])
        
        user_id = User.objects.get(username=request.user)
        docter = Docter.objects.get(username=user_id)
        new_prescrition = Prescription2(symptoms = request.POST['symptoms'] , prescription = request.POST['prescription'] , patient = appointment.patientid , docter = docter , appointment = appointment)
        new_prescrition.save()
        return redirect('docter_prescription')
    user_id = User.objects.get(username=request.user)
    docter = Docter.objects.get(username=user_id)
    data = Appointment.objects.filter(docterid=docter, status=0)
    print(data)

    return render(request , 'create_prescription.html',{"data":data , 'user' : "D" , 'status' : status})


# Mediacal History

def medical_history(request):
    status = False
    if request.user:
        status = request.user
    user_id = User.objects.get(username=request.user)
    print(user_id)
    patient = Patient.objects.get(username = user_id)
    data = Prescription2.objects.filter(patient = patient)
    print(data)
    return render(request , 'medical_history.html',{"data":data , 'user' : "P" , 'status' : status})



    # => Docter Update
def update_docter(request , id):
    status = False
    if request.user:
        status = request.user
    if request.method == "POST":
        update = Docter.objects.get(id=id)
        update.name = request.POST['name']
        update.phone = request.POST['phone']
        update.email = request.POST['email']
        update.gender = request.POST['gender']
        update.age = request.POST['age']
        update.blood = request.POST['blood']
        update.address = request.POST['address']
        update.department = request.POST['department']
        update.salary = request.POST['salary']
        update.status = request.POST['status']
        update.attendance = request.POST['attendance']
        update.save()
        return redirect('hr_dashboard')
    data = Docter.objects.get(id= id)
    return render(request , 'update_docter.html' , {"userdata" : data , 'user' : "H" , 'status' : status})


# HR Accounting
def hr_accounting(request):
    status = False
    if request.user:
        status = request.user
    individual = Invoice.objects.all()
    consulation =  Prescription2.objects.all()
    
    return render(request , 'hr_accounting.html' , {'individual' : individual , 'consulation' : consulation , 'user' : 'H' , 'status' : status})


# Send Confirmation
def send_confirmation(a):
	p = Patient.objects.get(id=a.patientid.id)
	d = Docter.objects.get(id=a.docterid.id)
	email = p.email
	subject = 'Book Confirmation'
	message = '''Dear {},

We are thrilled to inform you that your recent appointment for Life Extension has been successfully processed. Thank you for choosing us for your literary needs.

Book Details:
Date: {}
Time: {}

Best regards,
{}
Life Extension kft.
'''.format(p.name,a.date,a.time,d.name)
	recepient = [email]
	send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)