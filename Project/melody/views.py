from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from .forms import SongForm
from .models import *

# Create your views here.
class MelodyIndexView(View):
	def get(self, request):
		return render(request, 'melody/index.html')
	def post(self, request):
		if request.method == 'POST':
			return render(request, 'melody/songRegister.html')

class MelodyRegistrationView(View):
	def get(self, request):
		return render(request, 'melody/songRegister.html')
	def post(self, request):
		form = SongForm(request.POST)
		# songTitle = request.POST.get("songtitle")
		# print(songTitle)
		# artists = request.POST.get("artist")
		# print(artists)	
		if form.is_valid():
			title = request.POST.get("songtitle")
			genre = request.POST.get("genre")
			artist = request.POST.get("artist")
			date = request.POST.get("dateRelease")
			producer = request.POST.get("producer")
			songwriter = request.POST.get("songwriter")
			form = Song(songtitle = title, genre = genre, artist = artist, dateRelease = date, producer = producer, songwriter = songwriter)
			form.save()
			return HttpResponse("Song has been added!!!")
		else:
			print(form.errors)
			return HttpResponse("Form is invalid")		