from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name
    
class About(models.Model):
    abt_name= models.CharField(max_length=50)
    abt_des= models.TextField(max_length=1500)

    def _str_(self):
     return str(self.abt_name) + ' - ' + str(self.abt_des)

class Doctors(models.Model):    
    doc_name=models.CharField(max_length=100)
    doc_specialization=models.CharField(max_length=100)
    doc_email=models.EmailField(max_length=100)
    doc_department=models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='doctors')
    def __str__(self):
        return 'Dr '  +  self.doc_name + '-   ( ' + self.doc_specialization +')'

class Booking(models.Model):
    Patient_name = models.CharField(max_length=100)
    Patient_phone = models.CharField(max_length=10)
    Patient_email = models.EmailField(max_length=100)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE) 
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.doctor) + ' - ' + str(self.booking_date)
    


class Contact(models.Model):
     dep_name = models.CharField(max_length=100)
     dep_phone = models.CharField(max_length=15)

     def __str__(self):
        return self.dep_name