from django.contrib import admin

from .models import City, Category, Job, Employer


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'employer', 'job_type', 'slug', 'created_at', 'salary')
    list_filter = ('employer', 'job_type', 'created_at', 'salary')


admin.site.register(City)
admin.site.register(Category)
admin.site.register(Job, JobAdmin)
admin.site.register(Employer)
