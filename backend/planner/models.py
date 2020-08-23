from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Validators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Course(models.Model):
    account                 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_name             = models.CharField(max_length=150, verbose_name="Course Name")
    exam_weight             = models.IntegerField(default=0, verbose_name="Exam Weight")
    homework_weight         = models.IntegerField(default=0, verbose_name="Homework Weight")
    quiz_weight             = models.IntegerField(default=0, verbose_name="Quiz Weight")
    essay_weight            = models.IntegerField(default=0, verbose_name="Essay Weight")
    final_weight            = models.IntegerField(default=0, verbose_name="Final Weight")
    midterm_weight          = models.IntegerField(default=0, verbose_name="Midterm Weight")
    lab_weight              = models.IntegerField(default=0, verbose_name="Lab Weight")
    extra_credit_weight     = models.IntegerField(default=0, verbose_name="Extra-Credit Weight")
    grade                   = models.IntegerField(default=100, verbose_name="Grade")

    def clean_title(self):
        course_name = self.course_name
        self.course_name = course_name.title()

    def __str__(self):
        return self.course_name


class CourseAssignment(models.Model):
    REPEAT_CHOICES = [('NEVER', 'Never'), ('DAILY', 'Every Day'), ('WEEKDAY', 'Every Weekday'),
                      ('WEEKLY', 'Every Week'), ('BIWEEKLY', 'Every 2 Weeks'),
                      ('MONTHLY', 'Every Month'), ('YEARLY', 'Every Year')]

    ASSIGNMENT_ROLES = [("Exam", "Exam"), ("Homework", "Homework"), ("Quiz", "Quiz"),
                        ("Essay", "Essay"), ("Final", "Final"), ("Midterm", "Midterm"),
                        ('Lab', 'Lab'), ('Extra Credit', 'Extra Credit')]
 
    course                      = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_title            = models.CharField(max_length=150, verbose_name="Assignment Title")
    assignment_detail           = models.TextField(max_length=350, verbose_name="Assignment Detail", blank=True, null=True)
    assignment_due_date         = models.DateTimeField(blank=True, null=True, verbose_name="Assignment Due Date")
    assignment_role             = models.CharField(max_length=30, verbose_name="Assignment Role", choices=ASSIGNMENT_ROLES)
    assignment_duration         = models.DurationField(verbose_name="Assignment Duration")
    repeat                      = models.CharField(max_length=15, verbose_name="Repeat", choices=REPEAT_CHOICES, default='NEVER')
    end_repeat                  = models.DateField(verbose_name="Repeat Cycle", null=True, blank=True)
    grade                       = models.IntegerField(verbose_name="Grade", default=100)

    def clean_title(self):
        assignment_title = self.assignment_title
        self.assignment_title = assignment_title.title()

    def repeat_check(self):
        if self.repeat != "Never" and self.end_repeat is None:
            raise ValidationError(
                {'end_repeat': ('This field cannot be empty.')})

    def __str__(self):
        return self.event_title


class Event(models.Model):
    account     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=135, verbose_name="Title")
    details     = models.TextField(max_length=350, verbose_name="Details", blank=True, null=True)
    duration    = models.DurationField(verbose_name="Duration")
    location    = models.CharField(max_length=450, verbose_name="Location", blank=True, null=True)

    def clean_title(self):
        title = self.title
        self.title = title.title()

    def __str__(self):
        return self.title