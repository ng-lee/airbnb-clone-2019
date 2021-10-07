from django.contrib import admin
from . import models


@admin.register(models.ReviewModel)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    pass
