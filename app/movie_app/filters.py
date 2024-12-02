from  django_filters import FilterSet
from .models import *



class Movie_filter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            "country": ['exact'],
            'actor': ['exact'],
            'genre': ['exact'],
            'year': ['gt', 'lt'],
            'status_movie': ['exact']
        }