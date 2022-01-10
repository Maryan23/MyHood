from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.user_profile, name='profile'),
    path('accounts/profile/', views.index,name='profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood/',views.create_hood,name = 'create_hood'),
    path('hoods',views.hoods,name='hoods'),
    path('hood/<str:hood_name>',views.specific_hood,name='specific_hood'),
    path('join_hood/<str:hood_name>', views.join_hood, name='join_hood'),

]