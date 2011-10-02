from django.template import Context, loader
from users.models import User
from django.http import HttpResponse

def login(request):
	t = loader.get_template("users/login.html")
	c = Context({ })
	return HttpResponse(t.render(c))

def draft(request, user_id):
	t = loader.get_template("users/draft.html")
	c = Context({ })
	return HttpResponse(t.render(c))

def game(request):
	t = loader.get_template("users/game.html")
	c = Context({ })
	return HttpResponse(t.render(c))
