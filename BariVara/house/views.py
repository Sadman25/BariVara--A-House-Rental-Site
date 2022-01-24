from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import advertisement,image,comment
from .forms import advertisementForm, imageForm
# Create your views here.

@login_required(login_url='loginPage')
def homePage(request):
    return render (request, 'homepage.html')


def createAdvertisement(request):
    newAdvertisement = advertisementForm()
    additionalImages= imageForm()

    if request.method == 'POST':
        newAdvertisement = advertisementForm(request.POST,request.FILES)
        additionalImages= request.FILES.getlist('image')

        if newAdvertisement.is_valid():
            advertisement = newAdvertisement.save(commit=False)
            advertisement.owner = request.user
            advertisement.save()
            #saving image one by one
            for i in additionalImages:
                photo = image.objects.create(
                    advertisement = advertisement,
                    image = i
                )

            return redirect('homePage')

    else:
        context = {'newAdvertisement':newAdvertisement,
        'additionalImages':additionalImages }
        return render (request, 'create_advertisement.html',context)