from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type ='date'
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'Patient_name': "Patient Name:",
            'Patient_phone':"Patient Phone:",
            'Patient_email':"Patient Email",
            'doc_name':"Doctor Name:",
            'booking_date':"Booking Date:",
        }