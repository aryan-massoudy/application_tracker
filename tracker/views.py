# tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, ApplicationForm
from .models import Application

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'tracker/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'tracker/login.html', {'error': 'Invalid credentials'})
    return render(request, 'tracker/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    status_counts = {
        'applied': applications.filter(status='applied').count(),
        'interview': applications.filter(status='interview').count(),
        'rejected': applications.filter(status='rejected').count(),
        'offered': applications.filter(status='offered').count(),
        'accepted': applications.filter(status='accepted').count(),
    }
    context = {
        'applications': applications[:5],  # Show recent 5 applications
        'status_counts': status_counts,
        'total_applications': applications.count(),
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def application_list(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'tracker/application_list.html', {'applications': applications})

@login_required
def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()
    return render(request, 'tracker/application_form.html', {'form': form, 'title': 'Add Application'})

@login_required
def application_update(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'tracker/application_form.html', {'form': form, 'title': 'Update Application'})

@login_required
def application_delete(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        application.delete()
        return redirect('application_list')
    return render(request, 'tracker/application_confirm_delete.html', {'application': application})

@login_required
def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    return render(request, 'tracker/application_detail.html', {'application': application})