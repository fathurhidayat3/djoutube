# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib
import pafy
import json
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
	return render(request, "myapp/home.html")

# def srchome(request, furl):
# 	if "http" in furl:
# 		myu = urllib.unquote(furl)
# 	else:
# 		myu = furl.split('&')[0]

# 	test = pafy.new(myu)

# 	fstreams = [ str(fst).split('@')[0].split(':')[1] for fst in test.streams ]
# 	vstreams = [ str(vst).split('@')[1] for vst in test.streams ]
# 	ustreams = [ str(ust.url) for ust in test.streams ]

# 	data = json.dumps({
# 		"author" : test.author,
# 		"title" : test.title, 
# 		"videoid" : test.videoid,
# 		"fstreams" : fstreams,
# 		"vstreams" : vstreams,
# 		"ustreams" : ustreams
# 		})

# 	return HttpResponse(data)	

def nghome(request, furl):
	# myu = "https://www.youtube.com/watch?v=P9-4xHVc7uk"
	if "http" in furl:
		myu = urllib.unquote(furl)
	else:
		myu = furl.split('&')[0]

	test = pafy.new(myu)

	fstreams = [ str(fst).split('@')[0].split(':')[1] for fst in test.streams ]
	vstreams = [ str(vst).split('@')[1] for vst in test.streams ]
	ustreams = [ str(ust.url) for ust in test.streams ]

	data = json.dumps({
		"author" : test.author,
		"title" : test.title, 
		"videoid" : test.videoid,
		"fstreams" : fstreams,
		"vstreams" : vstreams,
		"ustreams" : ustreams
		})

	return HttpResponse(data, 
		content_type='application/json')

def search(request):
	return render(request, "myapp/search.html")

def ngsearch(request, fquery):
	query = urllib.quote(fquery)
	page = urllib.urlopen("https://www.youtube.com/results?search_query=" + query)
	soup = BeautifulSoup(page.read(), "html.parser")
	soup.title
	yt = "https://www.youtube.com"
	urldl = [ yt + vid['href'] for vid in soup.findAll(attrs={'class' : 'yt-uix-tile-link'}) 
	if all(["list" not in vid['href'], "user" not in vid['href'], "channel" not in vid['href']]) ]
	titledl = [ vid['title'].encode('ascii', 'ignore') for vid in soup.findAll(attrs={'class' : 'yt-uix-tile-link'})
	if all(["list" not in vid['href'], "user" not in vid['href'], "channel" not in vid['href']]) ]

	data = json.dumps({
		"titledl" : titledl,
		"urldl" : urldl
		})

	return HttpResponse(data, 
		content_type='application/json') 
