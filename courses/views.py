from http import HTTPStatus
import pytz
import json
from http import HTTPStatus
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from courses.models import Event, ConnectionPlatform
from profiles.models import ContactMethod, AcceptedCrypto

"""
HTML RENDERS
"""


def event_index(request):
    template = "courses/events.html"
    events = Event.objects.all()
    print("events:%s" % events)
    for event in events:
        print(event.event_type)
    context = {"events": events, "event_index_active": "active"}
    return render(request, template, context)


def event_detail(request, event_id):
    template = "courses/event_detail.html"
    event = get_object_or_404(Event, id=event_id)

    contact_methods = ContactMethod.objects.filter(user=event.owner)
    accepted_cryptos = AcceptedCrypto.objects.filter(user=event.owner)

    context = {"event": event, "contact_methods": contact_methods, "accepted_cryptos": accepted_cryptos}
    return render(request, template, context)


def event_recorded_online(request):
    template = "courses/event_recorded_online.html"
    context = {"event_index_active": "active"}
    return render(request, template, context)


def event_recurrent_localized(request):
    template = "courses/event_recurrent_localized.html"
    context = {"event_index_active": "active"}
    return render(request, template, context)


def event_singular_online(request):
    template = "courses/event_singular_online.html"
    context = {"event_index_active": "active"}
    return render(request, template, context)


def event_create(request):
    if request.method == "GET":
        template = "courses/event_create.html"
        platforms = ConnectionPlatform.objects.filter(deleted=False)

        context = {"event_index_active": "active", "platforms": platforms}
        return render(request, template, context)

    elif request.method == "POST":

        event_type_description = request.POST.get("event_type_description")
        event_recurrent = bool(request.POST.get("event_recurrent"))
        title = request.POST.get("title")
        description = request.POST.get("description")
        platform_name = request.POST.get("platform_name")
        other_platform = request.POST.get("other_platform")
        date_start = datetime.strptime(request.POST.get("date_start"), "%d/%m/%Y")
        date_end = datetime.strptime(request.POST.get("date_end"), "%d/%m/%Y")
        time_day = datetime.strptime(request.POST.get("time_day"), "%I:%M %p")
        time_zone = request.POST.get("time_zone")
        record_date = datetime.strptime(request.POST.get("record_date"), "%d/%m/%Y")
        schedule_description = request.POST.get("schedule_description")

        # Event Type
        if event_type_description == "pre_recorded":
            is_recorded = True
        elif event_type_description in ["live_course", "event_single"]:
            is_recorded = False
        else:
            is_recorded = False

        if event_type_description in ["pre_recorded", "live_course"]:
            event_type = "COURSE"
        elif event_type_description in ["event_single", "event_recurrent"]:
            event_type = "EVENT"
        else:
            event_type = "COURSE"  # loggear exceptions

        # Connection Platform
        try:
            platform_obj = ConnectionPlatform.objects.get(name=platform_name)
        except Exception as e:
            platform_obj = None
            print(e)

        # Date & Time
        time_zone_obj = pytz.timezone("Etc/"+time_zone)  # pytz format
        date_start = date_start.replace(tzinfo=time_zone_obj)
        date_end = date_end.replace(tzinfo=time_zone_obj)
        record_date = record_date.replace(tzinfo=time_zone_obj)

        print("date_start: %s" % date_start)
        print("date_end: %s" % date_end)
        print("time_day: %s" % time_day)
        print("time_zone: %s" % time_zone)

        created_event = Event.objects.create(
            event_type=event_type,
            is_recorded=is_recorded,
            is_reccurrent=event_recurrent,
            owner=request.user,
            title=title,
            description=description,
            platform=platform_obj,
            other_platform=other_platform,
            date_start=date_start,
            date_end=date_end,
            date_recorded=record_date,
            schedule_description=schedule_description
        )

        print("event_type_description: %s" % event_type_description)
        print("title: %s" % title)
        print("description: %s" % description)
        print("platform_name: %s" % platform_name)
        print("other_platform: %s" % other_platform)

        return HttpResponse("Printed!!")


"""
API CALLS
"""
