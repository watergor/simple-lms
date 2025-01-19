from django.urls import path
from lms.views import LessonListView, UserListView, CourseListView, index

urlpatterns = [
    path("", index, name="index"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("lessons/", LessonListView.as_view(), name="lesson-list"),
    path("courses/",CourseListView.as_view(), name="course-list"),
]

app_name = "lms"
