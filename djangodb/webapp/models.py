from django.db import models


# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    qmo_level = models.CharField(max_length=15)
    passwd = models.CharField(max_length=10, default='123456')
    passwd2 = models.CharField(max_length=10, default='123456')

    def __str__(self):
        return self.fname + ' ' + self.lname + ' -  QMO Level: ' + self.qmo_level


class Location(models.Model):
    loc_name = models.CharField(max_length=200)
    loc_description = models.CharField(max_length=150)
    loc_risk = models.CharField(max_length=15)
    loc_comment = models.TextField(max_length=500)

    def __str__(self):
        return self.loc_name


class Risk(models.Model):
    door_choices = [
        ("kitchen", "Kitchen"),
        ("store_01", "Store_01"),
        ("store_02", "Store_02"),
        ("store_03", "Store_03"),
        ("playground_01", "Playground_01"),
        ("playground_02", "Playground_02"),
        ("parents_rm_01", "Parents_rm_01"),
        ("parents_rm_02", "Parents_rm_02"),
        ("office_01", "Office_01"),
        ("office_02", "Office_02"),
        ("office_03", "Office+03"),
        ("doctors_office_01", "Doctor's_office_01"),
        ("doctors_office_02", "Doctors_office_02"),
    ]
    member_name = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    door_name = models.CharField(door_choices, max_length=20, null=True, blank=True)

    def __str__(self):
        return self.door_name


class Audit(models.Model):
    audit_loc = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    loc_name = models.CharField(max_length=100,blank=True)
    kitchen = models.CharField(max_length=10, blank=True)
    store_01 = models.CharField(max_length=10, blank=True)
    store_02 = models.CharField(max_length=10, blank=True)
    store_03 = models.TextField(max_length=10, blank=True)
    playground_01 = models.CharField(max_length=10, blank=True)
    playground_02 = models.CharField(max_length=10, blank=True)
    parents_rm_01 = models.CharField(max_length=10, blank=True)
    parents_rm_02 = models.TextField(max_length=10, blank=True)
    office_01 = models.CharField(max_length=10, blank=True)
    office_02 = models.CharField(max_length=10, blank=True)
    office_03 = models.CharField(max_length=10, blank=True)
    doctors_office_01 = models.TextField(max_length=10, blank=True)
    doctors_office_02 = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.loc_name + ' ' + self.kitchen
