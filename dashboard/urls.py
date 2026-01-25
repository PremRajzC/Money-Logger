from django.urls import path

from .views import dashboard, analytics, survival_dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("analytics/", analytics, name="analytics"),
    path("survival/", survival_dashboard, name="survival"),
]
