# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StudentPersonalDetails'
        db.create_table(u'admission_app_studentpersonaldetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('academic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.Academic_Year'])),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.Child'])),
            ('student_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.StudentGroup'])),
        ))
        db.send_create_signal(u'admission_app', ['StudentPersonalDetails'])

        # Adding model 'PreviousEducationDetails'
        db.create_table(u'admission_app_previouseducationdetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admission_app.StudentPersonalDetails'])),
            ('institution_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pasing_year', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('marks', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'admission_app', ['PreviousEducationDetails'])


    def backwards(self, orm):
        # Deleting model 'StudentPersonalDetails'
        db.delete_table(u'admission_app_studentpersonaldetails')

        # Deleting model 'PreviousEducationDetails'
        db.delete_table(u'admission_app_previouseducationdetails')


    models = {
        u'admission_app.previouseducationdetails': {
            'Meta': {'object_name': 'PreviousEducationDetails'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'marks': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pasing_year': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['admission_app.StudentPersonalDetails']"})
        },
        u'admission_app.studentpersonaldetails': {
            'Meta': {'object_name': 'StudentPersonalDetails'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Academic_Year']"}),
            'child': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Child']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.StudentGroup']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'schools.academic_year': {
            'Meta': {'object_name': 'Academic_Year'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'schools.boundary': {
            'Meta': {'ordering': "['name']", 'object_name': 'Boundary'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'}),
            'boundary_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Boundary_Category']", 'null': 'True', 'blank': 'True'}),
            'boundary_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Boundary_Type']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Boundary']", 'null': 'True', 'blank': 'True'})
        },
        u'schools.boundary_category': {
            'Meta': {'object_name': 'Boundary_Category'},
            'boundary_category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'schools.boundary_type': {
            'Meta': {'object_name': 'Boundary_Type'},
            'boundary_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'schools.child': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'unique_together': "(('first_name', 'middle_name', 'last_name'),)", 'object_name': 'Child'},
            'address_line1': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'adhar_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'max_length': '20'}),
            'election_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mt': ('django.db.models.fields.related.ForeignKey', [], {'default': "'kannada'", 'to': u"orm['schools.Moi_Type']"}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'physically_handicapped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pin_code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'student_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'schools.institution': {
            'Meta': {'ordering': "['name']", 'object_name': 'Institution'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'}),
            'boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Boundary']"}),
            'cat': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['schools.Institution_Category']", 'symmetrical': 'False'}),
            'dise_code': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inst_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Institution_address']", 'null': 'True', 'blank': 'True'}),
            'institution_gender': ('django.db.models.fields.CharField', [], {'default': "'co-ed'", 'max_length': '10'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['schools.Moi_Type']", 'symmetrical': 'False'}),
            'mgmt': ('django.db.models.fields.related.ForeignKey', [], {'default': "'ed'", 'to': u"orm['schools.Institution_Management']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'schools.institution_address': {
            'Meta': {'object_name': 'Institution_address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instidentification': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'instidentification2': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'landmark': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'pincode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'route_information': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'schools.institution_category': {
            'Meta': {'object_name': 'Institution_Category'},
            'category_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'schools.institution_management': {
            'Meta': {'ordering': "['name']", 'object_name': 'Institution_Management'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'schools.moi_type': {
            'Meta': {'object_name': 'Moi_Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'schools.stream': {
            'Meta': {'object_name': 'Stream'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Institution']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Stream']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '60'})
        },
        u'schools.studentgroup': {
            'Meta': {'ordering': "['name', 'section']", 'unique_together': "(('institution', 'stream', 'name', 'section'),)", 'object_name': 'StudentGroup'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'}),
            'group_type': ('django.db.models.fields.CharField', [], {'default': "'Class'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Institution']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'section': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Stream']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['admission_app']