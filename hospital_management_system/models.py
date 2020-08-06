# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import time
from datetime import datetime, timedelta

import django
import jwt
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin
from django.db import models
from django.db.models import OuterRef, Subquery
from django.forms import PasswordInput

import hospital_management_system


class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    updationdate = models.CharField(db_column='updationDate', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'admin'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_session'


class AccountManager(BaseUserManager):
    def create_user(self, user_email, firstname, lastname, address, city, gender, password, user_type):
        user = self.model(user_email=user_email, firstname=firstname, lastname=lastname, address=address, city=city,
                          gender=gender,
                          password=password, user_type=user_type)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, password, user_email=None):
        user = self.model(
            user_email=user_email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(user_email=email_)

    class Meta:
        managed = True


class Users(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    address = models.CharField(blank=True, max_length=255,
                               null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    regdate = models.DateTimeField(db_column='regDate', blank=True, null=True,
                                   default=django.utils.timezone.now)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.
    users_ptr = models.CharField(max_length=100, default=False)
    user_type = models.IntegerField(max_length=11, default=False)
    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'user_email'
    is_anonymous = False
    is_authenticated = True
    is_staff = True
    is_superuser = True
    objects = AccountManager()

    @property
    def token(self):
        dt = datetime.now() + timedelta()
        token = jwt.encode({
            'id': self.user_email,
            'exp': int(time.mktime(dt.timetuple()))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return "{} {}".format(str(self.firstname), str(self.lastname)) if self.user_email else "No name"


# class DocAccountManager(BaseUserManager):
#     def create_doctor(self, specialization, doctorname, address, docfees, contactno, docemail, password):
#         doc = self.model(specialization=specialization, doctorname=doctorname, address=address, docfees=docfees,
#                          contactno=contactno, docemail=docemail,
#                          password=password)
#         doc.set_password(password)
#         doc.is_staff = False
#         doc.is_superuser = False
#         doc.save(using=self._db)
#         return doc
#
#     def create_superuser(self):
#         pass
#
#     def get_by_natural_key(self, docemail_):
#         print(docemail_)
#         return self.get(docemail=docemail_)
#
#     class Meta:
#         managed = True
#
#
class Doctorspecilization(models.Model):
    specilization = models.CharField(max_length=255, blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'doctorspecilization'

    def __str__(self):
        return self.specilization


class Doctors(models.Model):
    # doc = models.OneToOneField(
    #     Users,
    #     on_delete=models.CASCADE, parent_link=True
    # )

    specialization = models.ForeignKey(Doctorspecilization, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    docfees = models.CharField(db_column='docFees', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactno = models.BigIntegerField(blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True,
                                        default=django.utils.timezone.now)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'doctors'

    def __str__(self):
        return str(self.user)


class Appointment(models.Model):
    doctorspecialization = models.CharField(db_column='doctorSpecialization', max_length=255, blank=True,
                                            null=True)  # Field name made lowercase.
    doctorid = models.IntegerField(db_column='doctorId', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    consultancyfees = models.IntegerField(db_column='consultancyFees', blank=True,
                                          null=True)  # Field name made lowercase.
    appointmentdate = models.CharField(db_column='appointmentDate', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    appointmenttime = models.CharField(db_column='appointmentTime', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    postingdate = models.DateTimeField(db_column='postingDate', blank=True, null=True)  # Field name made lowercase.
    userstatus = models.IntegerField(db_column='userStatus', blank=True, null=True)  # Field name made lowercase.
    doctorstatus = models.IntegerField(db_column='doctorStatus', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.
    doc_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'appointment'


class Doctorslog(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    userip = models.CharField(max_length=16, blank=True, null=True)
    logintime = models.DateTimeField(db_column='loginTime', blank=True, null=True)  # Field name made lowercase.
    logout = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'doctorslog'


class Tblcontactus(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    contactno = models.BigIntegerField(blank=True, null=True)
    msg_subject = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    postingdate = models.DateTimeField(db_column='PostingDate', blank=True, null=True)  # Field name made lowercase.
    adminremark = models.TextField(db_column='AdminRemark', blank=True, null=True)  # Field name made lowercase.
    lastupdationdate = models.DateTimeField(db_column='LastupdationDate', blank=True,
                                            null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblcontactus'


class Tblmedicalhistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patientid = models.IntegerField(db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    bloodpressure = models.CharField(db_column='BloodPressure', max_length=200, blank=True,
                                     null=True)  # Field name made lowercase.
    bloodsugar = models.CharField(db_column='BloodSugar', max_length=200)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=100, blank=True, null=True)  # Field name made lowercase.
    temperature = models.CharField(db_column='Temperature', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    medicalpres = models.TextField(db_column='MedicalPres', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblmedicalhistory'


class Tblpatient(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='Docid', blank=True, null=True)  # Field name made lowercase.
    patientname = models.CharField(db_column='PatientName', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    patientcontno = models.BigIntegerField(db_column='PatientContno', blank=True,
                                           null=True)  # Field name made lowercase.
    patientemail = models.CharField(db_column='PatientEmail', max_length=200, blank=True,
                                    null=True)  # Field name made lowercase.
    patientgender = models.CharField(db_column='PatientGender', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    patientadd = models.TextField(db_column='PatientAdd', blank=True, null=True)  # Field name made lowercase.
    patientage = models.IntegerField(db_column='PatientAge', blank=True, null=True)  # Field name made lowercase.
    patientmedhis = models.TextField(db_column='PatientMedhis', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='UpdationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblpatient'


class Userlog(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    userip = models.CharField(max_length=16, blank=True, null=True)
    logintime = models.DateTimeField(db_column='loginTime', blank=True, null=True)  # Field name made lowercase.
    logout = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'userlog'
