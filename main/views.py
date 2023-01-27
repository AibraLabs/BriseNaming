from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from main.ray_bns import GetAddress, GetPrice



#from .forms import UserForm


def IndexView(request):

	if request.method == "POST":
		domain_name = request.POST.get("domain_name")

		return HttpResponseRedirect(reverse("main:result", args=[domain_name,]))

	else:

		context = {}
		return render(request, "main/index.html", context )


def AuctionView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/auction.html", context )


def AccountView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/account.html", context )

def CheckOutView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/checkout.html", context )




def FindView(request):

	if request.method == "POST":
		domain_name = request.POST.get("domain_name")

		return HttpResponseRedirect(reverse("main:result", args=[domain_name,]))

	else:

		context = {}
		return render(request, "main/find.html", context )



def ResultView(request, domain_name):

	if request.method == "POST":
		domain_name = request.POST.get("domain_name")

		return HttpResponseRedirect(reverse("main:result", args=[domain_name,]))

	else:
		#name_address = GetAddress(domain_name)
		#name_address = "0x0000000000000"
		name_address = requests.get("https://api.iotexchartapp.com/bns/get-address/%s/" % (domain_name)).json()["address"]
		#return HttpResponse(str(name_address))

		if name_address == "0x0000000000000000000000000000000000000000":
			available = True
		elif name_address == "0xA67f0392a9A70dEB2A0cf8Ae36017B20A8d11756":
		    available = None
		else:
			available = False
		
		#name_price = GetPrice(domain_name)
		name_price = requests.get("https://api.iotexchartapp.com/bns/get-price/%s/" % (domain_name)).json()["price"]


		context = {"domain_name": domain_name, "available": available,
		"name_price": name_price, "name_address": name_address}

		return render(request, "main/result.html", context )



def BuyView(request, domain_name):

	if request.method == "POST":
		pass

	else:

		context = {"domain_name": domain_name}
		return render(request, "main/buy.html", context )



def FinishView(request):

	if request.method == "POST":
		domain_name = request.POST.get("domain_name")

		return HttpResponseRedirect(reverse("main:result", args=[domain_name,]))

	else:

		context = {}
		return render(request, "main/finish.html", context )
		
		

def TransferView(request):
	if request.method == "POST":
		domain_name = request.POST.get("domain_name")

		return HttpResponseRedirect(reverse("main:result", args=[domain_name,]))

	else:

		context = {}
		return render(request, "main/transfer.html", context )
		

def DocsView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/docs.html", context )