''' models for fms_app '''
from django.db import models
from schools.models import Institution, Academic_Year, current_academic, \
    Stream, Student, StudentGroup
from django.contrib.auth.models import User


class Permission(models.Model):
    ''' permissions for particular user '''

    name = models.CharField(max_length=100)

    class Meta:
        ''' validation for duplicate records '''

        unique_together = ('name', )

    def __unicode__(self):
        ''' return unicode strings '''
        return self.name


class User_permission(models.Model):
    ''' users for particular institution '''

    institution = models.ForeignKey(Institution)
    user = models.ForeignKey(User)
    permissions = models.ManyToManyField(Permission)

    def __unicode__(self):
        ''' return unicode string '''
        return self.user.username

    class Meta:
        ''' validations for unique records '''

        unique_together = ('user', 'institution')


class Level(models.Model):
    ''' level in a ainstitution '''

    institution = models.ForeignKey(Institution)
    stream = models.ForeignKey(Stream)
    name = models.CharField(max_length=100)
    description = \
        models.TextField('Section description. Appears in section home page',
                         blank=True, null=True)
    slug = models.SlugField('SEO friendly url, use only aplhabets and hyphen'
                            , max_length=60)
    created_by = models.ForeignKey(User)
    createdOn = models.DateTimeField(auto_now_add=True)
    modifiedOn = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    class Meta:
        ''' validations for uniqueness of record '''
        unique_together = ('institution', 'name')


class Fees_Type(models.Model):
    ''' model for types of fees in a institution '''

    institution = models.ForeignKey(Institution)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __unicode__(self):
        ''' return unicode strings '''
        return self.name

    def get_fee_object(self):
        ''' return fee object '''
        return Fee.objects.filter(fees_type=self)

    class Meta:
        ''' validations for unique values '''

        unique_together = ('institution', 'name')


payment_choices = (('fixed', 'fixed'), ('recursive', 'recursive'))
installments_choices = ((1, 1), (2, 2), (3, 3), (4, 4))


class Fee(models.Model):
    ''' models for fee according to academic '''

    # institution = models.ForeignKey(Institution)

    fees_type = models.ForeignKey(Fees_Type)
    amount = models.IntegerField(max_length=20)
    academic = models.ForeignKey(Academic_Year, default=current_academic)
    semister = models.ForeignKey(StudentGroup)
    payment_type = models.CharField(max_length=50, blank=True, null=True,
                                    choices=payment_choices)
    fist_payment = models.IntegerField('Minimun First Payment(Rs)',
                                       max_length=20, blank=True, null=True)
    installments = models.IntegerField('Number of installments',
                                       max_length=20, blank=True, null=True,
                                       choices=installments_choices)
    is_active = models.BooleanField()

    def __unicode__(self):
        ''' return unicode strings '''
        return '%s - %s - %s' % (self.semister.stream, self.semister.name,
                                 self.fees_type.name)

    class Meta:
        ''' validations for unique records '''
        unique_together = ('fees_type', 'semister')

fee_status_choices = [('not paid', 'not paid'),('paid', 'paid'), ('pending', 'pending')]

class Student_fees(models.Model):
    ''' fee for particular student '''

    institution = models.ForeignKey(Institution)
    student = models.ForeignKey(Student)
    fee = models.ForeignKey(Fee)
    fee_status = models.CharField(max_length=50, choices=fee_status_choices,
                                  default='pending')

    def __unicode__(self):
        ''' return unicode string '''
        return unicode(self.student.child.first_name)

    class Meta:
        ''' validations for uniques values '''
        unique_together = ('student', 'fee')


class Fine_type(models.Model):
    ''' model for types of fines '''

    institution = models.ForeignKey(Institution)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    fine_amount = models.IntegerField(max_length=20)
    is_active = models.BooleanField()

    def __unicode__(self):
        ''' return unicode strings '''
        return unicode(self.name)

    class Meta:
        ''' vlidations for unique ness of records '''
        unique_together = ('name', 'fine_amount')


class Fees_schedule(models.Model):
    ''' models for schedule of the fees '''

    institution = models.ForeignKey(Institution)
    fee = models.ForeignKey(Fee)
    start_date = models.DateField()
    end_date = models.DateField()
    fees_amount = models.IntegerField(max_length=20)
    end_data_fine_type = models.ForeignKey(Fine_type)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    

    def __unicode__(self):
        ''' return unicode strings '''
        return '%s-%s' % (self.start_date , self.fee.semister.stream)

class Student_payment(models.Model):
    ''' student's payment and fees status '''

    student = models.ForeignKey(Student)
    fee = models.ForeignKey(Fee)
    status = models.CharField(max_length = 50 , choices = fee_status_choices)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        ''' return unicode strings '''
        return '%s' % (self.student.child.first_name)

    class Meta:
        ''' vlidations for unique ness of records '''
        unique_together = ('student', 'fee')

payment_mode_choices = (('DD' , 'DD') , ('cheque' , 'cheque') , ('cash' , 'cash'))

class Student_payment_details(models.Model):
    ''' storing of date and time of the paid fees '''

    student_payment = models.ForeignKey(Student_payment)
    student_group = models.ForeignKey(StudentGroup)
    payment_mode = models.CharField(max_length = 100 , choices = payment_mode_choices)
    amount = models.IntegerField(max_length = 20)
    created_on = models.DateTimeField(auto_now_add = True)

class Student_admission(models.Model):
    student = models.ForeignKey(Student)
    academic_year = models.ForeignKeyacademic = models.ForeignKey(Academic_Year , default=current_academic)
    semister = models.ForeignKey(StudentGroup)
    created_on = models.DateTimeField(auto_now_add = True)
