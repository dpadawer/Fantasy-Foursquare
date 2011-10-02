from django.template import Context, loader
from fantasyfoursquare.models import User, Place
from django.http import HttpResponse

def login(request):
	t = loader.get_template("users/login.html")
	c = Context({ })
	return HttpResponse(t.render(c))

def draft(request, user_id):
	places = Place.objects.all().order_by("type")
	t = loader.get_template("users/draft.html")
	c = Context({
		'places' : places
	})
	return HttpResponse(t.render(c))

def game(request):
	t = loader.get_template("users/game.html")
	c = Context({ })
	return HttpResponse(t.render(c))
