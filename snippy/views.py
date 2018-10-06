from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.context_processors import csrf
from forms import SignupForm

# seperate view function for each url pattern and each web-page
def index(request):
	return render(request, 'oncotator/index.html', {})

def tools(request):
	return render(request, 'oncotator/tools.html', {})

def works(request):
	return render(request, 'oncotator/how_it_works.html', {})

def contact(request):
	return render(request, 'oncotator/contact_us.html', {})

def signup(request):
	return render(request, 'oncotator/sign_up.html', {})

def login(request):
	return render(request, 'oncotator/login.html', {})

@login_required(login_url='/login/')
def snptools(request):
        return render(request, 'oncotator/snp_tools.html', {})

def signup_form(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    args = {}
    args.update(csrf(request))
    args['form'] = SignupForm()
    return render_to_response('oncotator/sign_up_form.html', args)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
