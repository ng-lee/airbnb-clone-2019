from django.utils import timezone
from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import render
from django_countries import countries
from django_countries.fields import country_to_text
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    selected_country_code = request.GET.get("country", "KR")
    selected_room_type_pk = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    selected_amenities = request.GET.getlist("amenities")
    selected_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "selected_country_code": selected_country_code,
        "selected_room_type_pk": selected_room_type_pk,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "instant": instant,
        "superhost": superhost,
        "selected_amenities": selected_amenities,
        "selected_facilities": selected_facilities,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = selected_country_code

    if selected_room_type_pk != 0:
        filter_args["room_type__pk"] = selected_room_type_pk

    rooms = models.Room.objects.filter(**filter_args)

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant:
        filter_args["instant_book"] = True

    if superhost:
        filter_args["host__superhost"] = True

    if len(selected_amenities) > 0:
        for selected_amenity in selected_amenities:
            filter_args["amenities__pk"] = int(selected_amenity)

    if len(selected_facilities) > 0:
        for selected_facility in selected_facilities:
            filter_args["facilities__pk"] = int(selected_facility)

    return render(
        request,
        "rooms/search.html",
        {**form, **choices, "rooms": rooms},
    )
