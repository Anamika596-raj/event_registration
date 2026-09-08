from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration


def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", {"events": events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]

        Registration.objects.create(
            event=event,
            name=name,
            email=email
        )

        return redirect("event_detail", event_id=event.id)

    registrations = Registration.objects.filter(event=event)

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "registrations": registrations
        }
    )
def cancel_registration(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)
    event_id = registration.event.id

    registration.delete()

    return redirect("event_detail", event_id=event_id)
