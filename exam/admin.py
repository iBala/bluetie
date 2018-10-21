from django.contrib import admin

# Register your models here.
from exam.models import question, answer, exam

# Register your models here.
admin.site.register(question)
admin.site.register(answer)
admin.site.register(exam)
