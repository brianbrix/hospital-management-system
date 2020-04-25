# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    updationdate = models.CharField(db_column='updationDate', max_length=255)  # Field name made lowercase.

    def __str__(self):
        return self.username
    class Meta:
        managed = False
        db_table = 'admin'


class Appointment(models.Model):
    doctorspecialization = models.CharField(db_column='doctorSpecialization', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doctorid = models.IntegerField(db_column='doctorId', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    consultancyfees = models.IntegerField(db_column='consultancyFees', blank=True, null=True)  # Field name made lowercase.
    appointmentdate = models.CharField(db_column='appointmentDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.CharField(db_column='appointmentTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postingdate = models.DateTimeField(db_column='postingDate', blank=True, null=True)  # Field name made lowercase.
    userstatus = models.IntegerField(db_column='userStatus', blank=True, null=True)  # Field name made lowercase.
    doctorstatus = models.IntegerField(db_column='doctorStatus', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.
    doc_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctors(models.Model):
    specilization = models.CharField(max_length=255, blank=True, null=True)
    doctorname = models.CharField(db_column='doctorName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)
    docfees = models.CharField(db_column='docFees', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactno = models.BigIntegerField(blank=True, null=True)
    docemail = models.CharField(db_column='docEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctors'


class Doctorslog(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    userip = models.CharField(max_length=16, blank=True, null=True)
    logintime = models.DateTimeField(db_column='loginTime', blank=True, null=True)  # Field name made lowercase.
    logout = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctorslog'


class Doctorspecilization(models.Model):
    specilization = models.CharField(max_length=255, blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctorspecilization'


class Tblcontactus(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    contactno = models.BigIntegerField(blank=True, null=True)
    msg_subject = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    postingdate = models.DateTimeField(db_column='PostingDate', blank=True, null=True)  # Field name made lowercase.
    adminremark = models.TextField(db_column='AdminRemark', blank=True, null=True)  # Field name made lowercase.
    lastupdationdate = models.DateTimeField(db_column='LastupdationDate', blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcontactus'


class Tblmedicalhistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patientid = models.IntegerField(db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    bloodpressure = models.CharField(db_column='BloodPressure', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bloodsugar = models.CharField(db_column='BloodSugar', max_length=200)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=100, blank=True, null=True)  # Field name made lowercase.
    temperature = models.CharField(db_column='Temperature', max_length=200, blank=True, null=True)  # Field name made lowercase.
    medicalpres = models.TextField(db_column='MedicalPres', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmedicalhistory'


class Tblpatient(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='Docid', blank=True, null=True)  # Field name made lowercase.
    patientname = models.CharField(db_column='PatientName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    patientcontno = models.BigIntegerField(db_column='PatientContno', blank=True, null=True)  # Field name made lowercase.
    patientemail = models.CharField(db_column='PatientEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    patientgender = models.CharField(db_column='PatientGender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    patientadd = models.TextField(db_column='PatientAdd', blank=True, null=True)  # Field name made lowercase.
    patientage = models.IntegerField(db_column='PatientAge', blank=True, null=True)  # Field name made lowercase.
    patientmedhis = models.TextField(db_column='PatientMedhis', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='UpdationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpatient'


class Userlog(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    userip = models.CharField(max_length=16, blank=True, null=True)
    logintime = models.DateTimeField(db_column='loginTime', blank=True, null=True)  # Field name made lowercase.
    logout = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userlog'


class Users(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName')  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    regdate = models.DateTimeField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.firstname

    class Meta:
        managed = False
        db_table = 'users'
