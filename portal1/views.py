from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from article.models import User
from forms import RegisterForm
from django.http import HttpResponseRedirect
from django.core.context_processor import csrf
# Create your views here.

def registration(request):
	return render_to_reponse('registration.html',
							{'users':Users.objects.all()})


def create(request):
	if request.POST:
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/Users/all')
		else:
			form = RegisterForm()
	args = {}
	args.update(csrf(request))

	args['form'] = form

	return render_to_response('create_reg.html', args)


def randnum():
    return random.randint(0,99999)

