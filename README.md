# LifeExtension (<b>Varian</b>)
# Mind Map.
https://app.mindmup.com/map/_free/2023/11/afc601e08b0911ee81a2c94217cba2e5

# Radiotherapy Center Scheduling Application

## Introduction
This application is designed to optimize the scheduling of radiotherapy treatments in healthcare centers. Utilizing advanced algorithms, it efficiently allocates time slots on linear accelerators (TrueBeam, VitalBeam, and Unique – Clinac 1 energy) based on patient needs and machine capabilities. Developed using Django, Python, and HTML, it provides a user-friendly interface for healthcare professionals to manage appointments and maximize resource utilization.

## Features
- **Smart Scheduling**: Dynamically matches patients to the appropriate machine based on treatment requirements.
- **Load Balancing**: Evenly distributes workload across machines to minimize idle time.
- **User-Friendly Interface**: Easy-to-use platform for scheduling, rescheduling, and monitoring appointments.
- **Real-Time Updates**: Handles changes in schedule promptly, with alerts for emergencies and maintenance.
- **Data Analytics**: Offers insights into machine utilization and patient wait times.

## Technologies used 
- **Django**
- **Python**
- **Sqlite3**
- **HTML\CSS**
- **RESTAPI**
- **LINUX**
  
## Getting Started

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- Other dependencies listed in `requirements.txt`

### Installation
1. Clone the repository:
   `git clone https://github.com/yourusername/radiotherapy-scheduling.git`
2. Navigate to the project directory:
   `cd radiotherapy-scheduling`
3. Install required packages:
   `pip install -r requirements.txt`
4. Run migrations:
   `python manage.py migrate`
5. Start the Django development server:
   `python manage.py runserver`
6. Access the application through your web browser at `localhost:8000`.

## Usage
- Log in as an administrator to manage appointments and machine schedules.
- Use the dashboard to view upcoming appointments and machine availability.
- Add or edit patient details to reflect changes in treatment requirements.

## Contributing
Contributions to this project are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Our heartfelt thanks to all healthcare professionals in the fight against cancer.
- Special thanks to the Django and Python communities for their invaluable resources.

## Contact
For any inquiries, please open an issue in this repository or contact us directly at [alidinotabekov@gmail.com].


2. Prioritization Rules:
Sort patients based on urgency of treatment.
Prioritize patients who have fewer alternative machine options due to their specific requirements.
3. Machine-Patient Matching:
TrueBeam (1-2): Allocate to any patient, prioritizing those needing advanced treatments.
VitalBeam (3-4): Allocate to patients except large-bodied or those requiring breath-holding treatments.
Unique – Clinac 1 (5): Best for patients with simpler treatments and lower fractionation needs.
4. Scheduling Algorithm:
Use a time-slot-based approach where each machine has slots of 10, 15, 20, 30 minutes.
Check for the earliest available slot that matches the patient's treatment time and machine requirement.
If no slot is available on the desired day, look for the next available slot.
5. Load Balancing:
Distribute workload evenly across machines where possible, taking into account their different capacities.
Implement a fallback mechanism where patients can be reassigned to different machines if their primary choice is unavailable, respecting their treatment constraints.
6. Dynamic Rescheduling:
Allow for dynamic changes in the schedule in case of emergencies, cancellations, or machine maintenance.
Reschedule patients to different machines or times while minimizing disruptions.
