from django.urls import path
from . import views

urlpatterns = [
    #this is the index and home page urlpaths 
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('products',views.products,name='products'),
    path('contact',views.contact,name='contact'),

    # the all products urlpaths
    path('all_in_one',views.all_in_one,name='all_in_one'),
    path('all_in_one/all_in_one_update<str:pk>',views.all_in_one_update,name='all_in_one_update'),
    path('all_in_one/all_in_one_delete<str:pk>',views.all_in_one_delete,name='all_in_one_delete'),
    path('all_in_one/create_all_in_one',views.create_all_in_one,name='create_all_in_one'),
    path('all_in_one/all_in_one_details<str:pk>',views.all_in_one_details,name='all_in_one_details'),



    #desktop paths
    path('desktops',views.desktops,name='desktops'),
    path('desktops/desktops_update<str:pk>',views.desktops_update,name='desktops_update'),
    path('desktops/desktops_delete<str:pk>',views.desktops_delete,name='desktops_delete'),
    path('desktops/create_desktops',views.create_desktops,name='create_desktops'),
    path('desktops/desktops_details<str:pk>',views.desktops_details,name='desktops_details'),


    #laptoppaths
    path('laptops',views.laptops,name='laptops'),
    path('laptops/laptop_update<str:pk>',views.laptop_update,name='laptop_update'),
    path('laptops/laptop_delete<str:pk>',views.laptop_delete,name='laptop_delete'),
    path('laptops/create_laptop',views.create_laptop,name='create_laptop'),
    path('laptops/laptop_details<str:pk>',views.laptop_details,name='laptop_details'),

    #monitorpaths
    path('monitors',views.monitors,name='monitors'),
    path('monitors/monitor_update<str:pk>',views.monitor_update,name='monitor_update'),
    path('monitors/monitor_delete<str:pk>',views.monitor_delete,name='monitor_delete'),
    path('monitors/create_monitor',views.create_monitor,name='create_monitor'),
    path('monitors/monitor_details<str:pk>',views.monitor_details,name='monitor_details'),



#smart tv paths
    path('smart_tv',views.smart_tv,name='smart_tv'),
    path('smarttv/smarttv_update<str:pk>',views.smarttv_update,name='smarttv_update'),
    path('smarttv/smarttv_delete<str:pk>',views.smarttv_delete,name='smarttv_delete'),
    path('smarttv/create_smarttv',views.create_smarttv,name='create_smarttv'),
    path('smarttv/smarttv_details<str:pk>',views.smarttv_details,name='smarttv_details'),



    ###User authentication

    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('adminsite',views.adminsite,name='adminsite'),


     #Testimonies 
    path('testimonies', views.testimonies, name='testimonies'),
    path('testimonies/create_testimony', views.create_testimony, name='create_testimony'),
    path('testimonies/add_testimonies', views.add_testimonies, name='add_testimonies'),
    path('testimonies/delete_testimony<str:pk>', views.delete_testimony, name='delete_testimony'),
    path('testimonies/update_testimony<str:pk>', views.update_testimony, name='update_testimony'),

]
