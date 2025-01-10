from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[
            ("student", "Student"),
            ("teacher", "Teacher"),
            ("admin", "Admin"),
        ],
    )

    def __str__(self):
        return self.user.username


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="courses_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} in {self.course.title}"


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    file = models.FileField(upload_to="lesson/")
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
