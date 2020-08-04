from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from . import views
from rest_framework import routers

from .views import LoginView, USerDashView, AppointmentHistoryView, BookAppointmentView

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
    # path('login/', LoginView.as_view(), name="user_login"),
    re_path('register', views.user_register, name="user_register"),
    re_path('admin', views.admin_login, name="admin_login"),
    # path('admin/', views.admin_login, name="admin_login"),
    re_path('doctor', views.doctor_login, name="doctor_login"),
    # path('doctor/', views.doctor_login, name="doctor_login"),
    # path('contact/', views.contact, name="contact"),
    re_path('contact', views.contact, name="contact"),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('dashboard', views.show_dashboard, name='dashboard')
    path('dashboard', USerDashView.as_view(), name='user_dashboard'),
    path('appointmenthistory', AppointmentHistoryView.as_view(), name='appointment_history'),
    path('bookappointment', BookAppointmentView.as_view(), name='book_appointment'),
]
