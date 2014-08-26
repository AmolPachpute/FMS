''' forms for models '''
from django import forms
from fms_app.models import Fees_Type , Fees_schedule , \
Fine_type , Level , Fee , Student_fees , Student_payment , Student_payment_details
from schools.models import current_academic



class LoginForm(forms.Form):
    ''' login form  for user login '''

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20)


class FeeTypeForm(forms.ModelForm):
    ''' add fee_type form  for fees type model '''

    class Meta:
        ''' fees type model '''

        model = Fees_Type
        exclude = ('institution',)

class LevelsForm(forms.ModelForm):
    ''' level form  for level model'''

    class Meta:
        ''' models for level '''

        model = Level


class FeeForm(forms.ModelForm):
    ''' fee form for fee model '''

    class Meta:
        ''' fee model for fee'''

        model = Fee
        exclude = ('institution', )

    def clean(self):
        ''' validate year and payment modes '''
        cleaned_data = super(FeeForm, self).clean()
        payment_mode = cleaned_data.get('payment_type')
        academic_year = str(cleaned_data.get('academic'))[0:4]
        curr_academic_year = str(current_academic())[0:4]

        if academic_year != curr_academic_year:
            raise forms.ValidationError('year should be current academic year'
                    )

        if payment_mode == 'recursive':
            installments = cleaned_data.get('installments')
            first_payment = int(cleaned_data.get('fist_payment'))
            if not first_payment:
                raise forms.ValidationError("Please Enter Minimum \
         "
                        "           first payment for recursive payment type")
            else:
                amount = int(cleaned_data.get('amount'))
                if first_payment >= amount:
                    raise forms.ValidationError("Minimum first payment "
                            "should \
                                be "
                            "less than  Amount")

            if not installments:
                raise forms.ValidationError("Please Enter installments \
    "
                        "                                for recursive "
                        "payment type")
        return cleaned_data
        # clean method shud always return something mostly cleaned_data


class StudentFeeForm(forms.ModelForm):
    ''' student form for student fees '''

    class Meta:
        ''' models for student fees '''

        model = Student_payment
        exclude = ('institution', )


class FineTypeForm(forms.ModelForm):
    ''' fine type form  for fine type '''

    class Meta:
        ''' fine type model '''

        model = Fine_type
        exclude = ('institution', )


class FeeScheduleForm(forms.ModelForm):
    ''' fees schedule  for fee schedule'''

    class Meta:
        ''' fees schedule model '''

        model = Fees_schedule
        exclude = ('institution', 'fee', 'created_by')

    def clean(self):
        ''' validations for dates '''
        cleaned_data = super(FeeScheduleForm, self).clean()
        start_date = cleaned_data.get('start_date', '')
        end_date = cleaned_data.get('end_date', '')

        if start_date >= end_date:
            raise forms.ValidationError('Start date should be less than end '
                    'date')
        return cleaned_data


        # clean method shud always return something mostly cleaned_data
class StudentPaymentForm(forms.ModelForm):
    class Meta:

        model = Student_payment_details
        exclude = ('student_payment' , 'student_group')
