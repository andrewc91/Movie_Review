from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from ..login_app.models import User
from .models import Director, Movie, Review
from django.contrib import messages

# Create your views here.

def index(request):
    if not 'user_id' in request.session:
        return redirect(reverse('users:index'))
    else:
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "movies": Movie.objects.all(),
            "reviews": Review.objects.all(),
        }
        return render(request, 'movie_app/index.html', context)

def new(request):
    if not 'user_id' in request.session:
        return redirect(reverse('users:index'))

    context = {
        "directors": Director.objects.all(),
    }
    return render(request, 'movie_app/new.html', context)

def watch(request):
    if not 'user_id' in request.session:
        return redirect(reverse('users:index'))
    return render(request, 'movie_app/watch.html')

def create(request):
    if request.method == 'POST':
        result_director = Director.objects.director_validator(request.POST)
        result_movie = Movie.objects.movie_validator(request.POST)
        result_review = Review.objects.review_validator(request.POST)
        if result_director[0] == False or result_movie[0] == False or result_review[0] == False:
            for error in result_director[1]:
                messages.error(request, error, extra_tags="director")
            for error in result_movie[1]:
                messages.error(request, error, extra_tags="movie")
            for error in result_review[1]:
                messages.error(request, error, extra_tags="review")
            return redirect(reverse('movies:new'))
        else:
            if 'new_director' in request.POST:
                director = Director.objects.create(name=request.POST['new_director'])
            else:
                director = Director.objects.get(id=request.POST['select_director'])

            movie = Movie.objects.create(title=request.POST['movie'], director=director)

            context = {
                'user': User.objects.get(id=request.session['user_id']),
                'movie': movie,
                'rating': request.POST['rating'],
                'description': request.POST['description'],
            }
            review = Review.objects.create(**context)
            return redirect(reverse('movies:index'))

def show(request):
    if not 'user_id' in request.session:
        return redirect(reverse('users:index'))
    return render(request, 'movie_app/show.html')
