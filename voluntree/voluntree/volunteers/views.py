from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ngos.models import Event, VolunteerApplication
from .models import VolunteerProfile, Certificate

@login_required
def volunteer_dashboard(request):
    profile = getattr(request.user, 'vol_profile', None)
    my_apps = request.user.applications.select_related('event').all()
    certificates = request.user.certificates.all()
    return render(request, 'volunteers/dashboard.html', {
        'profile': profile, 'applications': my_apps, 'certificates': certificates
    })

def browse_events(request):
    qs = Event.objects.filter(date__isnull=False).order_by('date')
    q = request.GET.get('q')
    if q:
        qs = qs.filter(title__icontains=q)  # simple filter; expand as needed
    return render(request, 'volunteers/browse_events.html', {'events': qs})

@login_required
def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    existing = None
    if request.user.is_authenticated and request.user.role == 'volunteer':
        existing = VolunteerApplication.objects.filter(event=event, volunteer=request.user).first()
    if request.method == 'POST' and request.user.role == 'volunteer':
        if existing is None:
            VolunteerApplication.objects.create(event=event, volunteer=request.user)
            return redirect('volunteer_dashboard')
    return render(request, 'volunteers/event_details.html', {'event': event, 'existing': existing})

@login_required
def profile_view(request):
    profile = getattr(request.user, 'vol_profile', None)
    return render(request, 'volunteers/profile.html', {'profile': profile})

@login_required
def certificates_view(request):
    certs = request.user.certificates.all()
    return render(request, 'volunteers/certificates.html', {'certificates': certs})
