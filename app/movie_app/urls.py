from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('genres', GenreViewSet, basename='genres')
router.register('ratings', RatingViewSet, basename='ratings')
router.register('favorite', FavoriteViewSet, basename='favorite')
router.register('favorite_movie', FavoriteMovieViewSet, basename='favorite-movie')

urlpatterns = [
    path('users/', ProfileListApiView.as_view(), name="user"),
    path('users/<int:pk>/', ProfileDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
         name='user-detail'),

    path("actors/", ActorListApiView.as_view(), name="actors"),
    path('actors/<int:pk>/', ActorDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
         name='actors-detail'),

    path("movies/", MovieListApiView.as_view(), name="movies"),
    path('movies/<int:pk>/', MovieDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
         name='movies-detail'),

    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('', include(router.urls)),

    path('directors/', DirectorListApiView.as_view(), name='directors'),
    path('directors/<int:pk>/',
         DirectorDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
         name='director-detail'),

    path('history/', HistoryListApiView.as_view(), name="history"),
    path('history/<int:pk>', HistoryDetailViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
         name="history-detail"),
]
