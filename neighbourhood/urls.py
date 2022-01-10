from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood/',views.create_hood,name = 'create_hood'),
    path('hoods',views.hoods,name='hoods'),
    path('hood/<str:hood_name>',views.specific_hood,name='specific_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>',views.leave_hood,name='leave_hood'),
    path('create_business/',views.create_business,name = 'create_business'),

]