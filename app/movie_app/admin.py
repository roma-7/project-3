from django.contrib import admin
from .models import *

class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1


class MovieMomentsInline(admin.TabularInline):
    model = Moments
    extra = 1


class AllAdmin(admin.ModelAdmin):
    inlines = [MovieLanguagesInline, MovieMomentsInline]


admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie, AllAdmin)
admin.site.register(Moments)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(Rating)
admin.site.register(History)