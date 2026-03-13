from django.shortcuts import render, redirect
from .models import Course, Enrollment, Submission

def submit(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        user = request.user

        course = Course.objects.get(id=course_id)
        enrollment = Enrollment.objects.get(user=user, course=course)

        submission = Submission.objects.create(
            enrollment=enrollment
        )

        return redirect('show_exam_result')

    return render(request, 'onlinecourse/result.html')


def show_exam_result(request):
    total_score = 80
    possible_score = 100

    context = {
        'total_score': total_score,
        'possible_score': possible_score
    }

    return render(request, 'onlinecourse/result.html', context)