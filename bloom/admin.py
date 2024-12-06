from django.contrib import admin
from .models import BloomLevel, Course, CourseOutcome, ProgramOutcome

admin.site.register(BloomLevel)
admin.site.register(Course)
admin.site.register(CourseOutcome)
admin.site.register(ProgramOutcome)

