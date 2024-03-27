from django.urls import path,include
from .import views
urlpatterns = [
   path('',views.home,name='home'),
   path('about',views.about,name='about'),
   path('services',views.services,name='services'),
    path('login',views.login,name='login'),
    path('crmpage',views.crmpage,name='crmpage'),
    path('crmcontent',views.crmcontent,name='crmcontent'),
    path('drag',views.drag,name='drag'),
    path('signin',views.signin,name='signin'),
    path('appdetails',views.appdetails,name='appdetails'),
    path('save_image',views.save_image,name='save_image'),
    path('crmloginpage',views.crmloginpage,name='crmloginpage'),
    path('archive_app/<int:id>',views.archive_app,name='archive_app'),
    path('archiveremove/<int:id>',views.archiveremove,name='archiveremove'),
    path('crmarchive',views.crmarchive,name='crmarchive'),
    path('demo',views.demo,name='demo'),
    path('log_out',views.log_out,name='log_out')
    ]