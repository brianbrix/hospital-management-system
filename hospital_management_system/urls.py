from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'createuser', views.UserRegistrationViewSet, basename='UserRegistrationViewSet')
router.register(r'permission-detail', views.UserRegistrationViewSet, basename='UserRegistrationViewSet')
urlpatterns = [
    path('hms/', include(router.urls)),
    path('hms/api/', include('rest_framework.urls', namespace='rest_framework')),#this adds login api
    path('', views.index, name='index'),
    path('<int:user_id>/', views.user_details, name='user_details'),
    path('login', views.user_login, name="user_login"),
    path('register', views.user_register, name="user_register"),
    path('admin', views.admin_login, name="admin_login"),
    path('admin/', views.admin_login, name="admin_login"),
    path('doctor', views.doctor_login, name="doctor_login"),
    path('doctor/', views.doctor_login, name="doctor_login"),
    path('contact/', views.contact, name="contact"),
    path('contact', views.contact, name="contact"),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
