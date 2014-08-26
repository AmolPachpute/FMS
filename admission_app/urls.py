from django.conf.urls import patterns, url
from admission_app import views

urlpatterns = patterns('',
    # Examples:

    url(r'^$', views.admission, name='admission'),
    url(r'^add_admission/$', views.add_admission, name='admission'),
    url(r'^add_education_details/$', views.add_education_details, name='add_education_details'),
    url(r'^add_parent_details/$', views.add_parent_details, name='add_parent_details'),
    url(r'^success/$', views.successfull_form_submit, name='success'),
    url(r'^select_fees_types/$', views.select_fees_types, name='select_fees_types'),
)
