from django.contrib import admin

from lms.models import Course, Lesson, UserProfile, Enrollment

admin.site.register(Lesson)
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Enrollment)
