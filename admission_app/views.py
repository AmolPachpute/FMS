from django.shortcuts import render
from schools.models import Institution , StudentGroup , Academic_Year , Child , Relations ,Student
from admission_app.forms import Cus_Admission_Form , EducationDetailsForm, ParentsDetailsForm
from admission_app.models import StudentPersonalDetails
from django.http import HttpResponse , HttpResponseRedirect
from fms_app.models import Fee , Student_payment
def admission(request):

    try:
        ins_id = request.session['ins_id']
        ins_obj = Institution.objects.get(id=ins_id)
    except Exception:
        return HttpResponse('<html><body><h3>Broken Session.Please <a href="/fms/" >login</h3></body></html'
                            '>')
    form = Cus_Admission_Form(ins_obj)

    return render(request, 'admit_student.html', locals())

def add_admission(request):

    try:
        ins_id = request.session['ins_id']
        ins_obj = Institution.objects.get(id=ins_id)
    except Exception:
        return HttpResponse('<html><body><h3>Broken Session</h3></body></html'
                            '>')
    form1 = Cus_Admission_Form(ins_obj)
    record_added = False
    if request.method == "POST":
        form = form1(request.POST)
        if form.is_valid():
            form2 = form.save(commit = False)
            form2.created_by = request.user
            form2 = form.save()
            student_gr_obj = StudentGroup.objects.get(id = request.POST.get('student_group'))
            request.session['student_group_id'] = request.POST.get('student_group')
            academic_obj = Academic_Year.objects.get(id = request.POST.get('academic'))
            request.session['academic'] = academic_obj
            student_pd_obj = StudentPersonalDetails.objects.create( child = form2 , student_group = student_gr_obj , academic = academic_obj )
            request.session['student_pd_id'] = student_pd_obj.id
            request.session['child'] = form2
            Student.objects.create(child = form2,sms_features = True)
            record_added = True
            return HttpResponseRedirect('/admission/add_education_details/')
        else:
            pass

    return render(request, 'admit_student.html', locals())

def add_education_details(request):

    record_added = False
    try:

        student_pd_id = request.session['student_pd_id']
        ins_id = request.session['ins_id']
        ins_obj = Institution.objects.get(id=ins_id)
    except Exception:
        return HttpResponse('<html><body><h3>Broken Session.</body></html'
                            '>')
    if request.method == "POST":
        form = EducationDetailsForm(request.POST)
        if form.is_valid():
            form1=form.save(commit = False)
            student_pd_obj = StudentPersonalDetails.objects.get(id = student_pd_id)
            form1.student = student_pd_obj
            form1.save()
            record_added = True
            return HttpResponseRedirect('/admission/add_parent_details/')
        else:
            return render(request, 'education_details.html', locals())
    else:
        form = EducationDetailsForm()

    return render(request, 'education_details.html', locals())

def add_parent_details(request):

    record_added = False
    try:
        student_pd_id = request.session['student_pd_id']

    except Exception:
        return HttpResponse('<html><body><h3>Broken Session.</body></html'
                            '>')

    if request.method == "POST":
        form = ParentsDetailsForm(request.POST)
        if form.is_valid():
            form1=form.save(commit = False)
            student_pd_obj = StudentPersonalDetails.objects.get(id = student_pd_id)
            form1.child = student_pd_obj.child
            form1.save()

            record_added = True
            parents_list = Relations.objects.filter(child = form1.child)
            return HttpResponseRedirect('/admission/success/')
    else:
        form = ParentsDetailsForm()

    return render(request, 'add_parent_details.html', locals())

def successfull_form_submit(request):

    try:
      student_pd_id = request.session['student_pd_id']
    except Exception:
        return HttpResponse('<html><body><h3>Broken Session.</body></html'
                            '>')
    if request.method == "GET":
        student_pd_obj = StudentPersonalDetails.objects.get(id = student_pd_id)
        parents_list = Relations.objects.filter(child = student_pd_obj.child)
    else:
        if request.POST.get('parent'):

            parent_id = int(request.POST.get('parent'))
            relations_obj = Relations.objects.get(id = parent_id)
            relations_obj.is_emergency_contact = True
            relations_obj.save()
            return HttpResponseRedirect('/admission/select_fees_types/')
    return render(request,'success.html',locals())

def select_fees_types(request):

    record_added = False
    try:
        student_group_id = request.session['student_group_id']
        student_pd_id = request.session['student_pd_id']
        ins_id = request.session['ins_id']
        child = request.session['child']
        ins_obj = Institution.objects.get(id=ins_id)
        academic_obj = request.session['academic']
    except Exception:
        return HttpResponse('<html><body><h3>Broken Session.</body></html'
                            '>')
    if request.method == "GET":
        student_group = StudentGroup.objects.get(id = student_group_id)
        fee_list = Fee.objects.filter(semister__institution = ins_obj , academic = academic_obj , semister = student_group, is_active = 2)
        request.session['fee_list'] = fee_list
    else:

        post_data_dict = request.POST # its a query dictionary
        fees_type_dict = dict(post_data_dict.iterlists()) ## converts querydic to dict
        fees_type_list = fees_type_dict['fees_type'] # extracts list of fees_types from dictionary
        student_pd_obj = StudentPersonalDetails.objects.get(id = student_pd_id)
        student_obj = Student.objects.get(child = child)
        for i in fees_type_list:
            fee_obj = Fee.objects.get(fees_type = i)
            Student_payment.objects.create(student = student_obj , fee = fee_obj , status = "not paid" , created_by = request.user)
        record_added = True
    return render(request,'select_fees_types.html',locals())
