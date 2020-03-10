from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "attdc"

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('mark', views.mark, name='mark'),
    path('mark1', views.mark1, name='mark1'),
    path('get', views.get, name='get'),
    path('today', views.today, name='today'),

    path('user_ip', views.user_ip, name='user_ip'),
    path('up_file', views.up_file, name='up_file'),
    path('get_batch', views.get_batch, name='get_batch'),
    path('get_batch1', views.get_batch1, name='get_batch1'),
    path('get_batch2', views.get_batch2, name='get_batch2'),
    path('to_up', views.to_up, name='to_up'),
    #path('add_stu', views.add_stu, name='add_stu'),

    path('con_attdc/<int:student_id>', views.con_attdc, name='con_attdc'),
    path('success/<int:student_id>', views.success, name='success'),
    path('fail/<int:student_id>', views.fail, name='fail'),
    
    #path('ip_fail/<int:student_id>', views.ip_fail, name='ip_fail'),
    #path('user_mac', views.user_mac, name='user_mac'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)