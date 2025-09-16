from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NGO, Event, VolunteerApplication
from .forms import EventForm
from accounts.models import User

@login_required
def ngo_dashboard(request):
    # only for NGOs
    try:
        ngo = request.user.ngo_profile
    except NGO.DoesNotExist:
        return redirect('home')
    events = ngo.events.all()
    return render(request, 'ngos/dashboard.html', {'ngo': ngo, 'events': events})

@login_required
def create_event(request):
    try:
        ngo = request.user.ngo_profile
    except NGO.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            ev = form.save(commit=False)
            ev.ngo = ngo
            ev.save()
            return redirect('ngo_dashboard')
    else:
        form = EventForm()
    return render(request, 'ngos/create_event.html', {'form': form})

@login_required
def manage_events(request):
    try:
        ngo = request.user.ngo_profile
    except NGO.DoesNotExist:
        return redirect('home')
    events = ngo.events.all()
    return render(request, 'ngos/manage_events.html', {'events': events})

@login_required
def view_applications(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.ngo.user:
        return redirect('home')
    applications = event.applications.select_related('volunteer').all()
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        action = request.POST.get('action')
        app = get_object_or_404(VolunteerApplication, id=app_id)
        if action in ['approved','rejected']:
            app.status = action
            app.save()
    return render(request, 'ngos/applications.html', {'event': event, 'applications': applications})
