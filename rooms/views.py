from django.utils import timezone
from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import render
from django_countries import countries
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
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "selected_country_code": selected_country_code,
        "selected_room_type_pk": selected_room_type_pk,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
    }

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
