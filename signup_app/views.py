from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user
from .models import Contacts
from .forms import NewUserForm, Contactsform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
contacts = Contacts.objects.all()
def Homepage(request):
    return render(request, 'homepage.html', context={'contacts':contacts})

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("Homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
				print(msg)
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"form":form, 'contacts':contacts})

def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now signed in as {username}.")
				return redirect("Homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form, 'contacts':contacts})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("Homepage")

def contactadd(request):
	if request.method == "POST":
		form = Contactsform(request.POST)
		if form.is_valid():
			form.save()
		messages.success(request,"You have successfully added the contact.")
	form = Contactsform()
	return render(request=request, template_name="contactadd.html", context={"form":form})