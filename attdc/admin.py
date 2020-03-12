from django.contrib import admin
#from django.contrib.auth.models import Group
from .models import Instructor, Batch, Student, PassWord

admin.site.site_header = 'Attendance App'

admin.site.register(Instructor)
admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(PassWord)
#admin.site.unregister(Group)
#admin.site.register(Atdc)


 