from rest_framework import api_view
from requests import Response

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/roomreservation/rooms',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of rooms'
        },
        {
            'Endpoint': '/patients/',
            'method': 'GET',
            'body' : None,
            'description': 'Returns a list of patients'
        },
        {
            'Endpoint': '/roomreservation/reserve/',
            'method': 'POST',
            'body': {'patient_id': request.data['patient_id']},
            'description': 'Creates new note with data sent in post request'
        },
    ]
    return Response(routes)

