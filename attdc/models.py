from django.db import models
from django.utils import timezone
import datetime

class Instructor(models.Model):
    instr = models.CharField(max_length = 100)
    def __str__(self):
        return self.instr

class Batch(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    sem = models.IntegerField()
    s_code = models.CharField(max_length = 10)
    subject = models.CharField(max_length = 100)
    e_tot_c = models.IntegerField(default = 0)
    def __str__(self):
        return self.s_code

class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    rol_numb = models.IntegerField()
    name = models.CharField(max_length = 100)
    tot_attdc = models.IntegerField(default=0)
    mac = models.CharField(max_length = 50, default = 'xyz')
    tod_date = models.DateTimeField(default = datetime.datetime.now())
    
    def accept(self):
        time = self.tod_date + datetime.timedelta(minutes = 5)
        now = timezone.now()
        return  time <= now

    def __str__(self):
        return self.name

class Atdc(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()
    get_attdc = models.IntegerField(default = 0)

class S_code(models.Model):
    code = models.CharField(max_length = 10)
    def __str__(self):
        return self.name

class Urls(models.Model): 
    link = models.URLField(max_length = 200)

'''class Ip_handle(models.Model, c_ip):
    ip = models.CharField(max_length = 50, default = '127.0.0.1')

def check(self, std):
    if std.temp_ip in Student.objects.all():
        return std.accept()
    else:
        return True
'''
