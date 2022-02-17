from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pytz
from datetime import datetime
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect

from .forms import ImageForm
# Create your views here.
from .models import Listing, Alllisting

def index(request):

    if request.user.is_anonymous:
        return render(request, "AppGarage/index.html")

    return render(request, "AppGarage/index.html")

def getListings(request):
    lists = Listing.objects.all()
    data = serializers.serialize('json', lists)
    return HttpResponse(data, content_type="application/json")

def magbenta(request):
    if request.method == 'POST':
        # try:
        filledForm = ImageForm(request.POST, request.FILES)
        if filledForm.is_valid():
            filledForm.save()
            imgObj = filledForm.instance
            return render(request, "AppGarage/create.html", {'filledForm': imgObj})
        # except:
        #     return render(request, "AppGarage/index.html")
    emptyForm = ImageForm(use_required_attribute=False)
    return render(request, "AppGarage/create.html", {'form': emptyForm})

def BagongBenta(request):
    if request.method == "POST":
        listtable = Listing()
        ltz = pytz.timezone('Asia/Manila')
        now = datetime.now(ltz)
        dt = now.strftime("%A %d %B %Y %X ")
        try:
            listtable.owner = request.user.username
        except:
            pass
        listtable.owner = 'Not A registered User'

        listtable.title = request.POST.get('title')
        listtable.description = request.POST.get('description')
        listtable.price = request.POST.get('price')
        listtable.category = request.POST.get('category')
        if request.POST.get('link'):
            listtable.link = request.POST.get('link')
        else:#default link
            listtable.link = "https://nas-national-prod.s3.amazonaws.com/styles/hero_image/s3/_web_apa_2016_rock-pigeon_laura_perrotta_kk.jpg?itok=JbOQMi8b"
        listtable.time = dt
        listtable.save()
        all = Alllisting()
        items = Listing.objects.all()

        for i in items:
            try:
                if Alllisting.objects.get(listingid=i.id):
                    pass
            except:
                all.listingid = i.id
                all.title = i.title
                all.description = i.description
                all.link = i.link
                all.save()
        return redirect('index')
        # return HttpResponseRedirect(reverse("index"))

        # return HttpResponse('Done')

        # return redirect('auction:index')
    else:
        # return HttpResponse('Failed')
        # return HttpResponseRedirect(reverse("index"))

        return redirect('index')

