from django.contrib import admin

from .models import City, Category, Job, Employer


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'employer', 'job_type', 'slug', 'created_at', 'salary', 'category', 'is_active')
    list_filter = ('employer', 'job_type', 'created_at', 'salary', 'is_active', 'is_hot')


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'legal_form', 'slug', 'email', 'phone', 'hr_name', 'is_trust')
    list_filter = ('name', 'is_trust')


admin.site.register(City)
admin.site.register(Category)
admin.site.register(Job, JobAdmin)
admin.site.register(Employer, EmployerAdmin)
