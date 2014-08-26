''' register admin for fms_app '''
from django.contrib import admin
from fms_app.models import Fee , Fees_schedule , Fees_Type , Fine_type , \
Level , Permission , Student_fees , User_permission , Student_payment , \
Student_payment_details , Student_admission

admin.site.register(Level)
admin.site.register(Fees_Type)
admin.site.register(Fee)
admin.site.register(Student_fees)
admin.site.register(User_permission)
admin.site.register(Permission)
admin.site.register(Fine_type)
admin.site.register(Fees_schedule)
admin.site.register(Student_payment)
admin.site.register(Student_payment_details)
admin.site.register(Student_admission)

