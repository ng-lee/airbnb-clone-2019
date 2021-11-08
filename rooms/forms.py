from django import forms
from django.db.models import fields
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere", required=False)
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(
        empty_label="Any Kind",
        queryset=models.RoomType.objects.all(),
        required=False,
    )
    price = forms.IntegerField(required=False, label="Max Price")
    guests = forms.IntegerField(required=False, label="Minimum Guests")
    bedrooms = forms.IntegerField(required=False, label="Minimum Bedrooms")
    beds = forms.IntegerField(required=False, label="Minimum Beds")
    baths = forms.IntegerField(required=False, label="Minimum Baths")
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = (
            "caption",
            "file",
        )

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        photo.room = models.Room.objects.get(pk=pk)
        photo.save()


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = (
            "name",
            "description",
            "country",
            "city",
            "price",
            "address",
            "guests",
            "beds",
            "bedrooms",
            "baths",
            "check_in",
            "check_out",
            "instant_book",
            "room_type",
            "amenities",
            "facilities",
            "house_rules",
        )

    def save(self, user, *args, **kwargs):
        room = super().save(commit=False)
        return 
