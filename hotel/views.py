from django.shortcuts import render,redirect
from django.contrib import messages

from hotel.models import *
from django.http import HttpResponse, JsonResponse

from django.conf import settings
from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage
import time
# Create your views here.
def signuppage(request):

   if request.method == 'POST' and request.FILES['userphoto']:

      myfile = request.FILES['userphoto']
      fs = FileSystemStorage()
      filename = fs.save(myfile.name, myfile)
      uploaded_file_url = fs.url(filename)
      print(uploaded_file_url)
      # photo.objects.create(image=uploaded_file_url)

      # print(request.POST)
      name = request.POST.get('name')
      fatername = request.POST.get('fathername')
      aadharnumber = request.POST.get('aadharnumber')
      gender = request.POST.get('gender')
      email = request.POST.get('email')
      if len( userreg.objects.filter(email=email)):
         messages.info(request, "email id is already exits..please try another email")

         return redirect('/signup')

      password = request.POST.get('password')
      repassword= request.POST.get('repassword')
      date = request.POST.get('date')
      address = request.POST.get('address1')
      landmark = request.POST.get('landmark')
      city = request.POST.get('city')
      statename = request.POST.get('statename')
      country = request.POST.get('country')
      pincode = request.POST.get('pincode')
      mobile = request.POST.get('mobile')
     # ckeck = request.POST.get('check')

      userreg.objects.create(
         username = name,
         photo=uploaded_file_url,
         aadharnumber=aadharnumber,
         gender=gender,
         email=email,
         password=password,
         dateofbirth=date,
         address=address,
         landmark=landmark,
         city=city,
         statename=statename,
         countryname=country,
         pincode=pincode,
         mobilenumber=mobile,

      )
      print(name)
      print(email)
      print(gender)
      print(myfile)
   else:
      print("error")
   
   return render(request,'registration.html')

def login(req):
   if req.method=="POST":
      email = req.POST.get('useremail')
      password = req.POST.get('password')
      print(email,password)
      res=  userreg.objects.filter(email=email, password=password)
      if len(res):
         req.session['username'] = email
         messages.info(req, "Login Success")
         return redirect('/userabout')
      else:
         messages.info(req, "user name Or Password is incorrect")
         return redirect('/login')
      
   
   return render(req, 'login.html')

def logout(req):
   del req.session['username']
   messages.info(req, "Logout  Successfully")
   
   return redirect('/login')



def aboutus(request):
   return render(request,'aboutus.html')

def banquet(request):
   return render(request,'banquet.html')

def contact(request):
   return render(request,'contact.html')

def default(request):
   return render(request,'default.html')

def feedback(request):
   if request.method == 'POST':
      name = request.POST.get('username')
      email = request.POST.get('email')
      dateofstay = request.POST.get('dateofstay')
      ratethehotel = request.POST.get('rate')
      testimonial = request.POST.get('testimonial')
      print(request.POST)
      userfeed.objects.create(
         username = name,
         email=email,
         dateofstay=dateofstay,
         ratethehotel=ratethehotel,
         testimonial=testimonial,
      )
   else:
      print("error")

   return render(request,'feedback.html')

def MASALAGRILL(request):
   return render(request,'MASALAGRILL.html')

def roombooking(request):
   ttime=time.time()
   if request.method == 'POST':
      for i in range(request.session['rroom']):
         SL = request.POST.getlist('SL')[i]
         username = request.POST.getlist('username')[i]
         age = request.POST.getlist('age')[i]
         gender= request.POST.getlist('gender')[i]
         mobile= request.POST.getlist('mobile')[i]
         aadharnumber= request.POST.getlist('aadharnumber')[i]
         email = request.session['username']
         
         print(username,age,gender,mobile,aadharnumber)
         perroomperson.objects.create(
            sl=SL,
            personname=username,
            age=age,
            gender=gender,
            mobile=mobile,
            aadhar=aadharnumber,
            Pbookid=ttime

         )
      print(request.POST)
      
      res=  userreg.objects.filter(email=email)
      print(res)
      
     
      # booking.objects.create(
      #    roomname = roomname,
      #    roomtype=roomtype,
      #    dateofstay=dateofstay,
      #    numberofroom=numberroom,
      #    useremail=res[0],
      # )
      
      # return  redirect('/success/{}'.format(ttime))
      return render(request, 'successbook.html', {'ttime': ttime})
   
   data = getData(request)
   print(data)
   return render(request,'booking.html', {'user': data[0]}) 


# def success_view(req, time):
#    return render(req, 'successbook.html', {'time': time})

def roomgallery(request):
   return render(request,'roomgallery.html')

def room(request):
   return render(request,'rooms.html')

def roomtraffi(request):
   return render(request,'roomtraffi.html')

def skybar(request):
   return render(request,'skybar.html')

def theloop(request):
   return render(request,'theloop.html')

def roomdetail(request):
   data = getData(request)
   print(data)
   value=request.session['rroom']
   
   return render(request,'persondetail.html',{'user': data[0],'number':range(value)}) 

def getData(req):
   email = req.session['username']
   data = userreg.objects.filter(email=email)
   return data

def userabout(request):
   data = getData(request)
   print(data)
   return render(request,'useraboutus.html', {'user': data[0]}) 

def baseprofile(request):
   return render(request,'baseprofile.html')

def maintemplate(request):
   return render(request,'maintemplate.html')
   
def userhelp(request):
   data = getData(request)
   print(data)
   return render(request,'userhelp.html', {'user': data[0]}) 

def displayroom(request):
   data = getData(request)
   print(data)
   return render(request,'displayroom.html', {'user': data[0]}) 

def checkAva(request):
   if (request.method == 'POST'):
      roomname = ''
      roomtype = ''
      dateofstay =''
      noofroom = ''
      for i in request.POST:
         roomname = json.loads(i)['data'][0]
         roomtype = json.loads(i)['data'][1]
         dateofstay = json.loads(i)['data'][2]
         noofroom = json.loads(i)['data'][3]
       
      value=0
      
      if (roomtype=="single"):
         value=1*int(noofroom)
      elif(roomtype=="double"):
         value=2*int(noofroom)
      request.session['rroom']=value
      print(value,"hello")    
      b=rooms.objects.filter(roomname=roomname,roomchoice=roomtype).values()
      print(b)
      return JsonResponse(list(b), safe=False)
   
   return JsonResponse({'result': "AAAAAA"})

def menuview(request):
   data = getData(request)
   print(data)
   return render(request,'menu.html', {'user': data[0]}) 

import json
def menudata(request):
   a = ''
   for i in request.POST:
      print(i)
      a = i
   print('AAAA', a)
   b=menucard.objects.filter(foodtitle=a).values()
   # print(b)
   #print(JsonResponse(list(b), safe=False))
   return JsonResponse(list(b), safe=False)


def userpassword(request):
   data = getData(request)
   print(data)
   return render(request,'userpassword.html', {'user': data[0]}) 
   
def editprofile(request):
   data = getData(request)
   print(data)
   return render(request,'editprofile.html', {'user': data[0]}) 

def bookinghistory(request, ttime):
   data = getData(request)
   print(data)
   print(ttime)
   persons = perroomperson.objects.filter(Pbookid=ttime)
   # res=  perroomperson.objects.filter()

   return render(request,'bookinghistory.html', {'user': data[0], 'persons': persons})

def roompayment(request):
   data = getData(request)
   print(data)
   return render(request,'roompayment.html', {'user': data[0]})

def checkout(request):
   data = getData(request)
   print(data)
   return render(request,'checkout.html', {'user': data[0]})
