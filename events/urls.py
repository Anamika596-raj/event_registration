from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
    path("cancel/<int:registration_id>/", views.cancel_registration, name="cancel_registration"),
]
