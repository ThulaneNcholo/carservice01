from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'project/index.html')

def MechanicView(request):
    return render(request,'project/mechanic.html')

def CarInformation(request):
    return render(request,'project/carInfo.html')

def CarService(request):
    return render(request,'project/carService.html')

def AutoshopList(request):
    return render(request,'project/autoshops.html')

def CompanyProfile(request):
    return render(request, 'project/company.html')

def TowService(request):
    return render(request, 'project/towService.html')

def TowServiceResults(request):
    return render(request, 'project/towServiceResults.html')

def ProfilePage(request):
    return render(request, 'project/profile.html')

def MyServices(request):
    return render(request, 'project/myServices.html')


# Admin Views 

def Dashboard(request):
    return render(request, 'admin/dashboard.html')

def CompanyEdit(request):
    return render(request, 'admin/companyEdit.html')