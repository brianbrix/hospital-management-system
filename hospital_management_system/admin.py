from django.contrib import admin

# Register your models here.

from .models import *
# admin.site.register(Users)

# REQUIRED_FIELDS = ['firstname', 'lastname', 'password']
#     USERNAME_FIELD = 'email'
#     is_anonymous = False
#     is_authenticated = True
#     objects = UserManager()
#
#     class Meta:
#         managed = False
#         db_table = 'users'
#
#     def __str__(self):
#         return self.email