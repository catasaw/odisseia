from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/issues_dashboard.html')