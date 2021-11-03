from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words = user_text.split()
	number_of_words = len(words)
	reversed_text = user_text[::-1]
	return render(request,'reverse.html',{'usertext':user_text, 'reversed_text':reversed_text, 'number_of_words':number_of_words})