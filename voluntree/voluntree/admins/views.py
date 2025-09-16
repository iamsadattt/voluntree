from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ngos.models import NGO
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('home')
    pending_ngos = NGO.objects.filter(verified=False)
    return render(request, 'admins/dashboard.html', {'pending_ngos': pending_ngos})

@login_required
def ngo_approval(request, ngo_id):
    if request.user.role != 'admin':
        return redirect('home')
    ngo = get_object_or_404(NGO, id=ngo_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            ngo.verified = True
            ngo.save()
        elif action == 'reject':
            ngo.user.delete()  # or set flag; be careful
            return redirect('admin_dashboard')
    return render(request, 'admins/ngo_approval.html', {'ngo': ngo})

@login_required
def reports_view(request):
    if request.user.role != 'admin':
        return redirect('home')
    # sample summary - customize
    total_events = sum([ngo.events.count() for ngo in NGO.objects.all()])
    total_ngos = NGO.objects.count()
    total_volunteers = User.objects.filter(role='volunteer').count()
    return render(request, 'admins/reports.html', {
        'total_events': total_events,
        'total_ngos': total_ngos,
        'total_volunteers': total_volunteers
    })
