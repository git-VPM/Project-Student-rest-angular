from math import dist
from django.db import models
from django.template.defaultfilters import date

# Create your models here.

DISTRICT_CHOICES = (
    ('Alappuzha', 'ALA'),
    ('Ernakulam', 'EKM'),
    ('Idukki', 'IDU'),
    ('Kannur', 'KNR'),
    ('Kasaragod', 'KSD'),
    ('Kollam', 'KLM'),
    ('Kottayam', 'KTM'),
    ('Kozhikode', 'KKD'),
    ('Malappuram', 'MPM'),
    ('Palakkad', 'PKD'),
    ('Pathanamthitta', 'PTA'),
    ('Thiruvananthapuram', 'TVM'),
    ('Thrissur', 'TCR'),
    ('Wayanad', 'WND'),
)


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70)
    reg = models.CharField(unique=True, max_length=70)
    gender = models.CharField(max_length=512)
    dob = models.DateField()
    address = models.TextField()
    fk_dist = models.ForeignKey(
        'Dist', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return self.name


class Dist(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_name = models.CharField(max_length=50)
    vchr_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dist'

    def __str__(self):
        return self.vchr_name

# create table dist(pk_bint_id BIGSERIAL PRIMARY KEY,vchr_name varchar(50) not null),vchr_code varchar(50) not null;

# alter table student_student add column fk_dist_id BIGINT REFERENCES dist(pk_bint_id);


# insert into dist (vchr_name, vchr_code) values('Alappuzha', 'ALA');
# insert into dist(vchr_name, vchr_code) values('Ernakulam', 'EKM');
# insert into dist(vchr_name, vchr_code) values('Idukki', 'IDU');
# insert into dist(vchr_name, vchr_code) values('Kannur', 'KNR');
# insert into dist(vchr_name, vchr_code) values('Kasaragod', 'KSD');
# insert into dist(vchr_name, vchr_code) values('Kollam', 'KLM');
# insert into dist(vchr_name, vchr_code) values('Kottayam', 'KTM');
# insert into dist(vchr_name, vchr_code) values('Kozhikode', 'KKD');
# insert into dist(vchr_name, vchr_code) values('Malappuram', 'MPM');
# insert into dist(vchr_name, vchr_code) values('Palakkad', 'PKD');
# insert into dist(vchr_name, vchr_code) values('Pathanamthitta', 'PTA');
# insert into dist(vchr_name, vchr_code) values('Thiruvananthapuram', 'TVM');
# insert into dist(vchr_name, vchr_code) values('Thrissur', 'TCR');
# insert into dist(vchr_name, vchr_code) values('Wayanad', 'WND');


# (Alappuzha, Ernakulam, Idukki, Kannur, Kasaragod, Kollam, Kottayam, Kozhikode,
#  Malappuram, Palakkad, Pathanamthitta, Thiruvananthapuram, Thrissur, Wayanad)
