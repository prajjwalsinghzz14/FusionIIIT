

from django.db import models
import datetime

from applications.academic_information.models import Student

TIME = (
    ('6', '6 a.m.'),
    ('7', '7 a.m.'),
    ('8', '8 a.m.'),
    ('9', '9 a.m.'),	
    ('10', '10 a.m.'),
    ('11', '11 a.m.'),
    ('12', '12 p.m.'),
    ('13', '1 p.m.'),
    ('14', '2 p.m.'),
    ('15', '3 p.m.'),
    ('16', '4 p.m.'),
    ('17', '5 p.m.'),
    ('18', '6 p.m.'),
    ('19', '7 p.m.'),
    ('20', '8 p.m.'),
    ('21', '9 p.m.')
)

FEST = (
    ('1', 'Tarang'),
    ('2', 'Gusto'),
    ('3', 'Abhikalpan')
)

FEST_NAME = (
    ('Tarang', 'Tarang'),
    ('Gusto', 'Gusto'),
    ('Abhikalpan', 'Abhikalpan')
)

CLUB_CATEGORY = (
    ('Technical', 'Technical'),
    ('Cultural', 'Cultural'),
    ('Sports', 'Sports')
)

FEST_DOMAIN =(
    ('Event Management and Infra', 'Event Management and Infra'),
    ('Finance and Accounts', 'Finance and Accounts'),
    ('Marketing and Sponsorship', 'Marketing and Sponsorship'),
    ('Media and Public Relations', 'Media and Public Relations'),
    ('Help desk and Security', 'Help desk and Security'),
    ('Design and Development', 'Design and Development')
)


class Club(models.Model):

    club_id = models.IntegerField(on_delete=models.CASCADE, primary_Key=True)
    club_name = models.CharField(max_length=30)
    club_co = models.ForeignKey(Student, on_delete=models.CASCADE)
    club_coco = models.ForeignKey(Student, on_delete=models.CASCADE)
    faculty_co = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)
    category = models.CharField(max_length=9, choices=CLUB_CATEGORY)

    def __str__(self):
        return str(self.id)

class Club_session(models.Model):

    club_id = models.ForeignKey(Club)
    session_date = models.DateField()
    session_time = models.CharField(max_length=20, choices=TIME)
    session_venue = models.CharField(max_length=20)
    session_topic = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    attachment = models.FileField(upload_to='/Documents')

    def __str__(self):
        return str(self.id)


class Club_member(models.Model):

    club_member_id = models.IntegerField()
    student_id = models.ForeignKey(Student)
    club_id = models.ForeignKey(Club)
    achievement = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)

class Fest(models.Model):
    fest_id = models.IntegerField(max_length=1, choices=FEST)
    name = models.CharField(max_length=9, choices=FEST_NAME)
    convener_name = models.CharField(max_length=25)
    counselor_name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.id)

class Budget_Fest(models.Model):
    fest_id = models.ForeignKey(Fest)
    attachment = models.FileField(upload_to='/Documents')
    description = models.CharField(max_length=1000)
    suggestion = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)

class Club_Budget(models.Model):
    club_id = models.ForeignKey(Club)
    budget_for = models.CharField(max_length=1000)
    attachment = models.FileField(upload_to='/Documents')
    description = models.CharField(max_length=1000)
    suggestion = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)

class Core_Team(models.Model):
    student_id = models.ForeignKey(Student)
    fest_id = models.ForeignKey(Fest)
    domain = models.CharField(max_length=100, choices=FEST_DOMAIN)
    backlog_details = models.CharField(max_length=1000)
    discplinary_actions = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)
