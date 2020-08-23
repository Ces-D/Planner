from django.contrib import admin

from .models import Course, CourseAssignment, Event


class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "grade",)
    search_fields = ("course_name", "grade")
    readonly_field = ("account")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ("course", "assignment_title",
                    "assignment_due_date", "assignment_role", "grade",)
    search_fields = ()
    filter_horizontal = ()
    list_filter = ("course",)
    fieldsets = ()


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location")
    search_fields = ("title", "location")
    readonly_field = ("account")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Event, EventAdmin)
admin.site.register(CourseAssignment, CourseAssignmentAdmin)
admin.site.register(Course, CourseAdmin)