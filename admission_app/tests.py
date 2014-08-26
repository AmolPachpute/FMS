"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from fms_app.models import Fees_Type
from django.test import Client
from django.contrib.auth.models import User
from schools.models import Moi_Type , Boundary, \
Institution , Institution_Category , Institution_Management , Stream ,Academic_Year ,\
StudentGroup
from django.contrib.auth import authenticate
ins_obj = ''
ins_obj = Institution.objects.get(id = 1)

class SimpleTest(TestCase):
    def test_admission_login(self):
        ''' login testinf for valid username and password '''

        # inavalid

        client1 = Client()
        User.objects.create_user('admin', 'admin@gmail.com', 'admin')
        resp = client1.post('/fms/', {'username': 'admin', 'password': 'admin'
                            })
        self.assertEqual(resp.status_code, 200)
        
    def test_admission_objects(self):

        client1 = Client()
        cat_obj = Institution_Category.objects.create(name='Degree',
                category_type=8)
        moi_obj = Moi_Type.objects.create(name='Hindi')
        mgmt_obj = Institution_Management.objects.create(name='Vichardhara')
        b1_obj = Boundary.objects.create(name='VIT')
        b2_obj = Boundary.objects.create(parent=b1_obj, name='Pune Zone')
        ins_obj = Institution.objects.create(boundary=b2_obj, name=b1_obj,
                mgmt=mgmt_obj)
        ins_obj.cat.add(cat_obj)
        ins_obj.languages.add(moi_obj)
        Fees_Type.objects.create(institution=ins_obj, name='lion',
                                 is_active='True')
        Fees_Type.objects.create(institution=ins_obj, name='liondfsfa',
                                 is_active='True')
        
        stream_obj = Stream.objects.create(institution=ins_obj, name = 'BE-CSc')
        academic_obj = Academic_Year.objects.create(name = '2013-2014')
        StudentGroup.objects.create(institution=ins_obj, stream = stream_obj , name = 'I-sem')
        resp1 = client1.get('/admission/' )
        self.assertEqual(resp1.status_code, 200)
        
    def test_add_admission2(self):

        client1 = Client()
        moi_obj = Moi_Type.objects.create(name='Hindi')
        mgmt_obj = Institution_Management.objects.create(name='Vichardhara')
        b1_obj = Boundary.objects.create(name='VIT')
        b2_obj = Boundary.objects.create(parent=b1_obj, name='Pune Zone')
        ins_obj = Institution.objects.create(boundary=b2_obj, name=b1_obj,
                mgmt=mgmt_obj)
        cat_obj = Institution_Category.objects.create(name='Degree',
                category_type=8)
        ins_obj.cat.add(cat_obj)
        ins_obj.languages.add(moi_obj)
       
        stream_obj = Stream.objects.create(institution=ins_obj, name = 'BE-CSc')
        academic_obj = Academic_Year.objects.create(name = '2013-2014')
        
        StudentGroup.objects.create(institution=ins_obj, stream = stream_obj , name = 'I-sem')
        resp1 = client1.post('/admission/', {'first_name': 'admin22',
                             'middle_name': 'admin22' , 'last_name': 'admin22','student_group': 1,'academic': 1} )
        self.assertEqual(resp1.status_code, 200)