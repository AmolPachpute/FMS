from django import forms
from schools.models import StudentGroup , Child , Academic_Year , Relations
from admission_app.models import PreviousEducationDetails
def Cus_Admission_Form(ins_obj):

    class AdmissionForm(forms.ModelForm):

        studentgroupList = StudentGroup.objects.filter(active = 2 , institution = ins_obj)
        student_group = forms.ModelChoiceField(label='StudentGroup' , queryset=studentgroupList)
        academic_list = Academic_Year.objects.all()
        academic = forms.ModelChoiceField(queryset = academic_list)
        class Meta:   
            model = Child
            exclude = ('created_on' , 'created_by')

    return AdmissionForm



class EducationDetailsForm(forms.ModelForm):

        class Meta:   
            model = PreviousEducationDetails
            exclude = ('student' )
            
class ParentsDetailsForm(forms.ModelForm):

        class Meta:   
            model = Relations
            exclude = ('child')
           

