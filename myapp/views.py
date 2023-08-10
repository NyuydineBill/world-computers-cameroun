from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    testimony = Testimony.objects.all()
    context = {
        'testimony':testimony
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def all_in_one(request):
    item=AllInOne.objects.all()
    context={'item':item}
    return render(request,'AllInOne/all in one.html',context)

def create_all_in_one(request):
    if request.method == 'POST':
        form=AllInOneForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_in_one')
    else:
        form=AllInOneForm()
    context={
        'form':form
    }
    return render(request,'AllInOne/AllInOne_create.html',context)


def all_in_one_delete(request, pk):
    all_in_one = AllInOne.objects.get(id = pk)

    all_in_one.delete()
    return redirect('desktops')

def all_in_one_details(request,pk):
    all_in_one=AllInOne.objects.get(id=pk)
    context={
        'all_in_one':all_in_one
    }
    return render(request,'AllInOne/AllInOne_details.html',context)

def all_in_one_update(request, pk):
    all_in_one = AllInOne.objects.get(id = pk)
    if request.method == 'POST':
        form = AllInOneForm(request.POST or None, request.FILES or None, instance= all_in_one)
        if form.is_valid():
            form.save()
            return redirect('all_in_one')
    else:
        form = AllInOneForm(instance= all_in_one)

    context={
        'form' : form
    }
    return render(request, 'AllInOne/AllInOne_update.html', context)





def desktops(request):
    item=Desktop.objects.all()
    context={'item':item}
    return render(request,'desktop/desktops.html',context)

def create_desktops(request):
    if request.method == 'POST':
        form=DesktopForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('desktops')
    else:
        form=DesktopForm()
    context={
        'form':form
    }
    return render(request,'desktop/desktop_create.html',context)


def desktops_delete(request, pk):
    desktops = Desktop.objects.get(id = pk)

    desktops.delete()
    return redirect('desktops')

def desktops_details(request,pk):
    desktops=Desktop.objects.get(id=pk)
    context={
        'desktops':desktops
    }
    return render(request,'desktop/desktop_details.html',context)

def desktops_update(request, pk):
    desktops = Desktop.objects.get(id = pk)
    if request.method == 'POST':
        form = DesktopForm(request.POST or None, request.FILES or None, instance= desktops)
        if form.is_valid():
            form.save()
            return redirect('desktops')
    else:
        form = DesktopForm(instance= desktops)

    context={
        'form' : form
    }
    return render(request, 'desktop/desktop_update.html', context)



def laptops(request):
    item=Laptop.objects.all()
    context={'item':item}
    return render(request,'laptops/laptops.html',context)


def create_laptop(request):
    if request.method == 'POST':
        form=LaptopForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('laptops')
    else:
        form=LaptopForm()
    context={
        'form':form
    }
    return render(request,'laptops/laptop_create.html',context)


def laptop_delete(request, pk):
    laptop = Laptop.objects.get(id = pk)

    laptop.delete()
    return redirect('laptops')

def laptop_details(request,pk):
    laptop=Laptop.objects.get(id=pk)
    context={
        'laptop':laptop
    }
    return render(request,'laptops/laptop_details.html',context)

def laptop_update(request, pk):
    laptop = Laptop.objects.get(id = pk)
    if request.method == 'POST':
        form = LaptopForm(request.POST or None, request.FILES or None, instance= laptop)
        if form.is_valid():
            form.save()
            return redirect('laptops')
    else:
        form = LaptopForm(instance= laptop)

    context={
        'form' : form
    }
    return render(request, 'laptops/laptop_update.html', context)






def monitors(request):
    item=Monitor.objects.all()
    context={'item':item}
    return render(request,'monitors/monitors.html',context)



def create_monitor(request):
    if request.method == 'POST':
        form=MonitorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('monitors')
    else:
        form=MonitorForm()
    context={
        'form':form
    }
    return render(request,'monitors/monitor_create.html',context)


def monitor_delete(request, pk):
    monitor = Monitor.objects.get(id = pk)

    monitor.delete()
    return redirect('monitors')

def monitor_details(request,pk):
    monitor=Monitor.objects.get(id=pk)
    context={
        'monitor':monitor
    }
    return render(request,'monitors/monitor_details.html',context)

def monitor_update(request, pk):
    monitor = Monitor.objects.get(id = pk)
    if request.method == 'POST':
        form = MonitorForm(request.POST or None, request.FILES or None, instance= monitor)
        if form.is_valid():
            form.save()
            return redirect('monitors')
    else:
        form = MonitorForm(instance= monitor)

    context={
        'form' : form
    }
    return render(request, 'monitors/monitor_update.html', context)




def smart_tv(request):
    item=SmartTV.objects.all()
    context={'item':item}
    return render(request,'smart tv/smart tv.html',context)

def create_smarttv(request):
    if request.method == 'POST':
        form=SmartTVForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('smart_tv')
    else:
        form=SmartTVForm()
    context={
        'form':form
    }
    return render(request,'smart tv/smarttv_create.html',context)


def smarttv_delete(request, pk):
    smarttv = SmartTV.objects.get(id = pk)

    smarttv.delete()
    return redirect('smart_tv')

def smarttv_details(request,pk):
    smarttv=SmartTV.objects.get(id=pk)
    context={
        'smarttv':smarttv
    }
    return render(request,'smart tv/smarttv_details.html',context)

def smarttv_update(request, pk):
    smarttv = SmartTV.objects.get(id = pk)
    if request.method == 'POST':
        form = SmartTVForm(request.POST or None, request.FILES or None, instance= smarttv)
        if form.is_valid():
            form.save()
            return redirect('smart_tv')
    else:
        form = SmartTVForm(instance= smarttv)

    context={
        'form' : form
    }
    return render(request, 'smart tv/smarttv_update.html', context)



def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('login')
    else:
           
        return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credentials invalid")
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')

def products(request):
    return render(request, "products.html")

@login_required(login_url='login')
def adminsite(request):
    if request.method=='POST':
        laptop=LaptopForm(request.POST)
        if laptop.is_valid():
            laptop = Laptop(name = request.POST['name'],price = request.POST['price'],image=request.POST['image'])
            laptop.save()
            messages.success(request, "added successfully")
            return redirect('adminsite')

        messages.error(request, "successfully added")
    laptop=LaptopForm()
    if request.method=="POST":
        desktop=DesktopForm(request.POST)
        if desktop.is_valid():
            desktop = Desktop(name = request.POST['name'],prices = request.POST['prices'],image=request.POST['image'])
            desktop.save()
            messages.success(request, "added successfully")
            return redirect('adminsite')
        messages.error(request, "not successfully added")

    desktop=DesktopForm()
    if request.method=="POST":
        monitor=MonitorForm(request.POST)
        if monitor.is_valid():
            monitor = Monitor(name = request.POST['name'],pricess = request.POST['pricess'],image=request.POST['image'])
            monitor.save()
            messages.success(request, "added successfully")
            return redirect('adminsite')
        messages.error(request, "successfully added")
    monitor=MonitorForm()

    if request.method=="POST":
        smart_tv=SmartTVForm(request.POST)
        if smart_tv.is_valid():
            smart_tv = SmartTV(name = request.POST['name'],pricesss = request.POST['pricesss'],image=request.POST['image'])
            smart_tv.save()
            messages.success(request, "added successfully")
            return redirect('adminsite')
        messages.error(request, "successfully added")
    smart_tv=SmartTVForm()

    if request.method=="POST":
        others=OthersForm(request.POST)
        if others.is_valid():
            others = Others(name = request.POST['name'],pricesx = request.POST['pricesx'],image=request.POST['image'])
            others.save()
            messages.success(request, "added successfully")
            return redirect('adminsite')
        messages.error(request, "successfully added")
    others=OthersForm()

    if request.method=="POST":
        all=AllInOneForm(request.POST)
        if all.is_valid():
            all = AllInOne(name = request.POST['name'],pricex = request.POST['pricex'],image=request.POST['image'])
            all.save()
            return redirect('adminsite')
        messages.error(request, "successfully added")
    all=AllInOneForm()
    user=User.objects.all()
    context={
            'user':user,
            'laptop':laptop,
            'desktop':desktop,  
            'monitor':monitor,
            'smart_tv':smart_tv,
            'others':others,
            'all':all,
                }

    return render(request,'admin.html',context)

def testimonies(request):

    if request.method == 'POST':
        form = TestimoniesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TestimoniesForm()

    context={
        'form' : form
    }

    return render(request,'testimonies/testimonies.html', context)
 
def add_testimonies(request):
    all_testimonies = Testimony.objects.all()
    context={
        # 'form' : form,
        'all_testimonies' : all_testimonies
    }
    return render(request,'testimonies/add_testimonies.html', context)




 
def create_testimony(request):
    if request.method == 'POST':
        form = TestimoniesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_testimonies')
    else:
        form = TestimoniesForm()
    
    context={
        'form' : form
    }
    return render(request, 'testimonies/create_testimony.html', context)


def delete_testimony(request, pk):
    testimony_delete = Testimony.objects.get(id = pk)
    testimony_delete.delete()
    return redirect('add_testimonies')

def update_testimony(request, pk):
    testimony_update = Testimony.objects.get(id=pk)
    if request.method == 'POST':
        form = TestimoniesForm(request.POST or None, request.FILES or None, instance= testimony_update)
        if form.is_valid():
            form.save()
            return redirect('add_testimonies')
    else:
        form = TestimoniesForm(instance = testimony_update)

    context={
        'form' : form,
        'testimony_update' : testimony_update
    }
 
    return render(request, 'testimonies/update_testimony.html', context)


