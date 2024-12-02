from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from django.contrib.auth import authenticate




class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    age = serializers.IntegerField(min_value=18)
    phone_number = serializers.CharField(max_length=15)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = Profile.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            age=validated_data["age"],
            phone_number=validated_data["phone_number"],
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email"),
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Неверные учетные данные.")
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username,
            'email': user.email,
        }



class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']




class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'phone_number', 'status']



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']




class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']




class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name', 'bio', 'age','director_image']





class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']



class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age', 'actor_image']




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']




class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']




class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']




class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    class Meta:
        model = Rating
        fields = ['user', 'movie', 'stars', 'parent', 'text' , 'created_date']




class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user']




class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ['movie']





class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['user', 'movie']




class MovieListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_name','movie_image', 'genre']




class MovieDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    country = CountrySerializer(many=True)
    languages = MovieLanguagesSerializer(many=True)
    actor = ActorListSerializer(many=True)
    director = DirectorListSerializer(many=True)
    moment = MomentsSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['movie_name','movie_image','languages','actor','director', 'genre', 'year', 'country', 'types', 'movie_time',
                  'description', 'movie_trailer','moment', 'movie_image', 'status_movie']

