from django.shortcuts import get_object_or_404, render

from .models import Course, Step


def course_list(req):
    courses = Course.objects.all()
    email = 'questions@learning_site.com'
    return render(req, 'courses/course_list.html', {'courses': courses, 'email':email})


def course_detail(req, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(req, 'courses/course_detail.html', {'course': course})


def step_detail(req, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(req, 'courses/step_detail.html', {'step': step})
