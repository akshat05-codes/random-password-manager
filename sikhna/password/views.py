from django.shortcuts import redirect, render

# Create your views here.
from .models import Note, PasswordEntry
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    entries = PasswordEntry.objects.all().order_by('-created_at')
    notes = Note.objects.all().order_by('-created_at')


    return render(request, 'home.html', {
        'entries': entries,
        'notes': notes
    })




def home(request):
    entries = PasswordEntry.objects.all().order_by('-created_at')
    notes = Note.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'entries': entries,
        'notes': notes
    })


def generate_password(request):

    length = int(request.GET.get('length', 10))

    numbers = request.GET.get('numbers') == "true"
    symbols = request.GET.get('symbols') == "true"
    uppercase = request.GET.get('uppercase') == "true"
    lowercase = request.GET.get('lowercase') == "true"

    characters = ""

    if lowercase:
        characters += "abcdefghijklmnopqrstuvwxyz"

    if uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if numbers:
        characters += "0123456789"

    if symbols:
        characters += "!@#$%^&*()"

    # fallback (if user unchecks everything)
    if characters == "":
        characters = "abcdefghijklmnopqrstuvwxyz"

    password = "".join(random.choice(characters) for _ in range(length))

    return HttpResponse(password)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_note(request):
    if request.method == "POST":
        site = request.POST.get('site')
        username = request.POST.get('username')
        note = request.POST.get('note')

        Note.objects.create(
            site=site,
            username=username,
            note=note
        )

    return HttpResponse("Saved")

def delete_note(request):
    if request.method == "POST":
        id = request.POST.get('id')
        Note.objects.get(id=id).delete()
    return redirect('/')

