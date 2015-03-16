import os
from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from mysite import settings
from frontpage.models import Genre, Game
import models

# Create your views here.
def home(request):
	games = Game.objects.all()
	context = {"games":games}

	#genre = Genre.objects.all()
	#rock = "awesome"
	#context = {"genre":rock}
	return render(request, 'frontpage/frontpage.html', context)

"""
def home(request):
	genre = models.Genre.objects.all()
	return render_to_response("frontpage.html", 
														{"genre": genre},
														context_instance=RequestContext(request))
                             # {"curations": all_curations},
 """                            