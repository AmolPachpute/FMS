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
Institution , Institution_Category , Institution_Management
from django.contrib.auth import authenticate
ins_obj = ''
ins_obj = Institution.objects.get(id = 1)


class SimpleTest(TestCase):

    ''' test cases for fms app '''
    def test_login(self):
        ''' login testinf for valid username and password '''

        # inavalid

        client1 = Client()

        resp = client1.post('/fms/', {'username': '', 'password': ''})
        self.assertEqual(resp.status_code, 200)

        resp = client1.post('/fms/', {'username': 'admin', 'password': 'admin'
                            })
        self.assertEqual(resp.status_code, 200)


    def test_add_view_for_logged_user(self):
        ''' add recordview for user login '''

        client1 = Client()
        User.objects.create_superuser('admin', 'admin@gmail.com',
                'admin')
        resp1 = client1.post('/fms/', {'username': 'admin',
                             'password': 'admin'})
        resp2 = client1.get('/fms/manage/add_fee_type/', {})
        code1 = resp1.status_code
        code2 = resp2.status_code
        self.client = Client()
        self.client.login(username='admin', password='admin')
        ses = {}
        ses = self.client.session
        ses['ins_id'] = 1
        ses.save()
        self.assertEqual(code2, 200)
        self.assertEqual(code1, 200)



    def test_fees_type_count(self):
        ''' fees type count test '''

        count = Fees_Type.objects.all().count()
        self.assertEqual(count, 0)

    def test_add_views(self):
        ''' add view testing '''

        client1 = Client()
        resp = client1.get('/fms/manage/add_fee_type/', {})
        self.assertEqual(resp.status_code, 200)

        resp = client1.post('/fms/manage/add_fee_type/', \
                            {'institution': ins_obj,
                            'name': 'dfsdgsgfdgfdsgfgfdfsd', 'is_active': 0})
        self.assertEqual(resp.status_code, 200)

    def test_add_fees_type(self):
        ''' test add fees type '''

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
        client1 = Client()
        User.objects.create_user('admin', 'admin@gmail.com', 'admin')
        client1.post('/fms/', {'username': 'admin',
                             'password': 'admin'})
        ins_obj = Institution.objects.get(name='VIT')
        resp = client1.post('/fms/manage/add_fee_type/', \
                            {'institution': ins_obj,
                            'name': 'erere', 'is_active': 2})
        count = Fees_Type.objects.all().count()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(count, 2)

    def test_delete_fees_type(self):
        ''' tes delete fees type '''

        Fees_Type.objects.create(institution=ins_obj, name='lion',
                                 is_active='True')
        Fees_Type.objects.create(institution=ins_obj, name='liondfsfa',
                                 is_active='True')
        count = Fees_Type.objects.all().count()
        self.assertEqual(count, 2)
        obj = Fees_Type.objects.get(institution=ins_obj, name='lion')
        obj.delete()
        count = Fees_Type.objects.all().count()
        self.assertEqual(count, 1)

    def test_edit_fees_type(self):
        ''' test edit fees type '''

        Fees_Type.objects.create(institution=ins_obj, name='lion',
                                 is_active='True')
        Fees_Type.objects.create(institution=ins_obj, name='liondfsfa',
                                 is_active='True')
        count = Fees_Type.objects.all().count()
        obj = Fees_Type.objects.get(institution=ins_obj, name='lion')
        obj.is_active = 0
        obj.save()
        f_type = Fees_Type.objects.get(name='lion')
        self.assertEqual(count, 2)
        self.assertEqual(f_type.is_active, False)

    def test_delete(self):
        ''' test delete ing an objects '''

        client1 = Client()

        # invalid data

        resp = \
            client1.get('/fms/manage/delete/?frttype_id=45534534542534343434'
                        , {})
        self.assertEqual(resp.status_code, 200)

    def test_edit_view(self):
        ''' test edit record view '''

        client1 = Client()

        # invalid data

        resp = client1.get('/fms/manage/edit_fee_type/2323233/', {})

        # valid data

        Fees_Type.objects.create(institution=ins_obj, name='lion',
                                 is_active=2)
        resp2 = client1.post('/fms/manage/edit_fee_type/1/',
                             {'name': 'dfsdgsgfdgfdsgfgfdfsd',
                             'is_active': 0})
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(resp.status_code, 200)

    def test_student_payment(self, ):
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
        fees_type_obj = Fees_Type.objects.create(institution=ins_obj, name='lion',
                                 is_active='True')
        Fees_Type.objects.create(institution=ins_obj, name='liondfsfa',
                                 is_active='True')
        client1 = Client()
        User.objects.create_user('admin', 'admin@gmail.com', 'admin')
        client1.post('/fms/', {'username': 'admin',
                             'password': 'admin'})
        ins_obj = Institution.objects.get(name='VIT')

        resp = client1.post('/fms/manage/student_fees/pay/1/')

        self.assertEqual(resp.status_code, 200)
