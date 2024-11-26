
# Create your views here.
from django.shortcuts import render

def dashboard_view(request):
    # Dummy data for now
    wrapped_data = [
        {"icon": "🎶", "name": "Wrapped 2020"},
        {"icon": "🎧", "name": "Wrapped 2021"},
        {"icon": "📀", "name": "Wrapped 2022"},
        {"icon": "🎼", "name": "Wrapped 2023"},
    ]
    context = {"wrapped_data": wrapped_data}
    return render(request, "dashboard/stats.html", context)
