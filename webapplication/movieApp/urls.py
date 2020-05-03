from django.conf.urls import url
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from movieApp import views
from rest_framework import routers
 
 
router = routers.DefaultRouter()
#router.register(r'movies', views.MovieView)
urlpatterns = [
	url(r'^movies/$', views.MovieView.as_view()),
	url(r'^signup/', views.createUser),
	#insert movie id into movie_list
	url(r'^addMovieToList/', views.addMovieToList),
	#delete movie id from movie_list
	url(r'^deleteMoviefromList/', views.addMovieToList),
	url(r'^addMovieToList/', views.addMovieToList),
	path(r'api-token-auth/', views.authentication),
    path(r'api-token-refresh/', refresh_jwt_token),
	#path('index', views.index),
    url(r'^$', include(router.urls)),
]