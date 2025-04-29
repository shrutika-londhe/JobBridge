from django.shortcuts import render,redirect
from courses.models import Enrollment

from jobs.models import JobApplication

def dashboard(request):
    user_email = request.session.get('user_email')
    if not user_email:
        return redirect('auth')

    enrollments = Enrollment.objects.all()
    job_applications = JobApplication.objects.all()

    course_count = enrollments.count()
    job_count = job_applications.count()
    profile_completion = 70  # You can later calculate dynamically

    context = {
        'user_email': user_email,
        'enrollments': enrollments,
        'job_applications': job_applications,
        'course_count': course_count,
        'job_count': job_count,
        'profile_completion': profile_completion,
    }

    return render(request, 'profile.html', context)
