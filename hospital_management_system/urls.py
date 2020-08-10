from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from . import views
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'login', views.LoginView, basename='LoginView')
router.register(r'createuser', views.UserRegistrationViewSet, basename='UserRegistrationViewSet')
# router.register(r'login', views.UserRegistrationViewSet, basename='UserRegistrationViewSet')

urlpatterns = [
    path('hms/', include(router.urls)),
    path('hms/api/', include('rest_framework.urls', namespace='rest_framework')),#this adds login api
    path('', views.index, name='index'),
    path('<int:user_id>/', views.user_details, name='user_details'),
    re_path('login', LoginView.as_view(), name="user_login"),
    re_path('register', views.user_register, name="user_register"),
    re_path('admin', views.admin_login, name="admin_login"),
    re_path('add-patient', views.add_patient, name="add_patient"),
    re_path('contact', views.contact, name="contact"),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('dashboard', USerDashView.as_view(), name='user_dashboard'),
    path('doctor-dashboard', DocDashView.as_view(), name='doctor_dashboard'),
    path('appointment-history', AppointmentHistoryView.as_view(), name='appointment_history'),
    path('doc_appointment_history', DocAppointmentHistoryView.as_view(), name='doc_appointment_history'),
    path('book-appointment', BookAppointmentView.as_view(), name='book_appointment'),
    path('edit-profile', EditProfileView.as_view(), name='edit_profile'),
    path('staff-dashboard', StaffDashView.as_view(), name='staff_dashboard'),
    # path('add-patient', AddPatientView.as_view(), name='add_patient'),
]
