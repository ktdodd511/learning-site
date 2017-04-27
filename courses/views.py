from django.shortcuts import get_object_or_404, render

from .models import Course, Step


def course_list(req):
    courses = Course.objects.all()
    return render(req, 'courses/course_list.html', {'courses': courses})


def course_detail(req, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(req, 'courses/course_detail.html', {'course': course})
