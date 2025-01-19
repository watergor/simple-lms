from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from lms.models import Lesson, Course, UserProfile, Enrollment


@login_required
def index(request):
    return render(request, "home/index.html", context={})


class LessonListView(LoginRequiredMixin, generic.ListView):
    model = Lesson
    paginate_by = 5
    context_object_name = "lesson_list"
    template_name = "lms/lesson_list.html"


class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course
    paginate_by = 5
    context_object_name = "course_list"
    template_name = "lms/course_list.html"


class UserListView(generic.ListView):
    model = UserProfile
    paginate_by = 5
    context_object_name = "user_list"
    template_name = "lms/user_list.html"
