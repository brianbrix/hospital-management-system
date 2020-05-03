from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.user_details, name='user_details'),
    path('login', views.user_login, name="user_login"),
    path('register', views.user_register, name="user_register"),
    path('admin', views.admin_login, name="admin_login"),
    path('admin/', views.admin_login, name="admin_login"),
    path('doctor', views.admin_login, name="doctor_login"),
    path('doctor/', views.admin_login, name="doctor_login"),
    path('contact/', views.contact, name="contact"),
    path('contact', views.contact, name="contact"),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
