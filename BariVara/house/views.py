from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import advertisement,image,comment
from .forms import advertisementForm, imageForm
from accounts.models import profile
from accounts.forms import userRegistration,profileRegistration
# Create your views here.

@login_required(login_url='loginPage')
def homePage(request):
    advertisements = advertisement.objects.all().order_by('-id') #Latest products will be shown at 1st
    context = {'advertisements':advertisements}
    return render (request, 'homepage.html',context)

@login_required(login_url='loginPage')
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

@login_required(login_url='loginPage')
def advertisementDetails(request,pk):
    advertisement_details = advertisement.objects.get(id=pk)  #Contains information of a particular product
    advertisement_images = image.objects.filter(advertisement=advertisement.objects.get(id=pk)) #Contains information of a particular product's images
    
    context = {'advertisement_details':advertisement_details,
    'advertisement_images':advertisement_images,
    }
    return render (request,'advertisement_details.html',context)

@login_required(login_url='loginPage')
def myAdvertisements(request):
    advertisements = advertisement.objects.all().order_by('-id')
    context = {'advertisements':advertisements}
    return render (request, 'my_advertisements.html',context)

@login_required(login_url='loginPage')
def searchByArea(request):
    query = request.GET.get('query')
    if query:
        advertisements = advertisement.objects.filter(area__area__icontains=query)
        context = {'advertisements':advertisements}
        return render(request,'search.html',context)
    else:
        return redirect('homePage')

@login_required(login_url='loginPage')
def myProfile(request,pk):

    previousInfo = profile.objects.get(id=pk)
    editUser = userRegistration(instance=request.user)
    editProfile = profileRegistration(instance=previousInfo)

    if request.method == 'POST':
        editUser = userRegistration(request.POST,instance=userRegistration(instance=request.user))
        editProfile = profileRegistration(request.POST,request.FILES,instance=previousInfo)
        if editUser.is_valid() and editProfile.is_valid():
            editUser.save()
            editProfile.save()
            return redirect('/')
    
    else:
        context = {'previousInfo':previousInfo,
        'editUser':editUser,
        'editProfile':editProfile}
        return render (request, 'my_profile.html',context)   