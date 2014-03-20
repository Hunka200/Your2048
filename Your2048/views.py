import re, os
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist,Template, RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.conf import settings
from django.forms import ModelForm

from Your2048.models import Game

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['url', 'name', 'desc', 'tile2', 'tile4', 'tile8', 'tile16', 'tile32', 'tile64', 'tile128', 'tile256', 'tile512', 'tile1024', 'tile2048']

def home(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            f = GameForm(request.POST, request.FILES)
            if f.is_valid():
                Game.objects.filter(owner = request.user).delete()
                game = f.save(commit=False)
                game.owner = request.user
                game.save()
                return HttpResponseRedirect('/' + game.url)
            else:
                print f.errors
                return HttpResponseRedirect('/?msg=fail')
        else:
            initial = {}
            try:
                game = Game.objects.get(owner = request.user)
                initial['url'] = game.url
                initial['name'] = game.name
                initial['desc'] = game.desc
                initial['i1'] = game.i1
                initial['i2'] = game.i2
                initial['i3'] = game.i3
                initial['i4'] = game.i4
                initial['i5'] = game.i5
                initial['i6'] = game.i6
                initial['i7'] = game.i7
                initial['i8'] = game.i8
                initial['i9'] = game.i9
                initial['i10'] = game.i10
                initial['i11'] = game.i11
            except:
                pass

            form = GameForm(initial = initial)
            ctx = {'form': form}
            return render_to_response('setup.html', RequestContext(request,ctx))
    else:
        ctx = {}
        return render_to_response('login.html', RequestContext(request, ctx))

def game(request, url):
    try:
        game = Game.objects.get(url = url)
        ctx = {'game': game}
        return render_to_response('index.html', RequestContext(request,ctx))
    except Game.DoesNotExist:
        return HttpResponseRedirect('/')
