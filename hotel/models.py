from django.db import models

# Create your models here.
#user registration table
class userreg(models.Model):
    username=models.CharField(max_length=30)
    photo=models.ImageField(max_length=100)
    aadharnumber=models.CharField(max_length=20)
    gender=models.CharField(max_length=6)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    
    dateofbirth=models.DateField()
    address=models.CharField(max_length=100)
    landmark=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    statename=models.CharField(max_length=20)
    countryname=models.CharField(max_length=30)
    pincode=models.IntegerField()
    mobilenumber=models.CharField(max_length=13)

class userfeed(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    dateofstay=models.DateField()
    ratethehotel=models.CharField(max_length=20)
    testimonial=models.CharField(max_length=400)

roomtype=(("single","single"),("double","double"))
numberroom=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"))
roomselect=(("Maharaja Suite","Maharaja Suite"),("Suite","Suite"),("Super Deluxe","Super Deluxe"),("A.C. Deluxe","A.C. Deluxe"),("Premium Rooms","Premium Rooms"))
class rooms(models.Model):
    roomname=models.CharField(max_length=20,choices=roomselect)
    roomchoice=models.CharField(max_length=10,choices=roomtype)
    roomcharge=models.IntegerField(default=0)
    extracharge=models.IntegerField()
    servicecharge=models.IntegerField()
    totalroom=models.IntegerField()

    def __str__(self):
        return self.roomname

class booking(models.Model):
    roomname=models.CharField(max_length=20,choices=roomselect)
    roomtype=models.CharField(max_length=10,choices=roomtype)
    dateofstay=models.DateField()
    useremail = models.ForeignKey(userreg, on_delete=models.CASCADE)
    numberofroom=models.IntegerField(choices=numberroom)
    
menu=(("Breakfast","Breakfast"),("Salad","Salad"),("Snacks","Snacks"),
("South Indian Dishes","South Indian Dishes"),("Dal ","Dal "),("Soup","Soup"),("Vegetables ","Vegetables"),("Raita","Raita"),("Rice","Rice "),("Roti","Roti"),("Cold Beverages ","Cold Beverages "),
("Chinese Dishes","Chinese Dishes"),("Hot Beverages","Hot Beverages "),("Thali Meals ","Thali Meals "),
("Desserts ","Desserts"))

class menucard(models.Model):
    foodtitle=models.CharField(max_length=100,choices=menu)
    foodname=models.CharField(max_length=150)
    price=models.IntegerField(default=0)
  
class perroomperson(models.Model):
    Pbookid=models.CharField(default=1,max_length=20)
    sl=models.CharField(max_length=20,default="1")
    personname=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    mobile=models.CharField(max_length=13)
    aadhar=models.CharField(max_length=20)

support=(("FRONT DESK CLERK","FRONT DESK CLERK"),("PORTERS","PORTERS"),("CONCIERGES","CONCIERGES"),("HOUSEKEEPING","HOUSEKEEPING"),("ROOM SERVICE","ROOM SERVICE"),("WAITER/WAITRESS","WAITER/WAITRESS"),("KITCHEN STAFF","KITCHEN STAFF"))

guest=(("SUPERVISOR OF GUEST SERVICES","SUPERVISOR OF GUEST SERVICES"),("FRONT DESK SUPERVISOR","FRONT DESK SUPERVISOR"),("KITCHEN MANAGER","KITCHEN MANAGER"),("RESTURANT MANAGER","RESTURANT MANAGER"))

adminn=(("MARKETING AND ADVERTISING","MARKETING AND ADVERTISING"),("ACCOUNTING","ACCOUNTING"),("PURCHASING","PURCHASING"),("EVENT PLANNER","EVENT PLANNER"),("ASSISTANT HOTEL MANAGER","ASSISTANT HOTEL MANAGER"),("HOTEL MANAGER","HOTEL MANAGER"))

statusm=(("married","married"),("unmarried","unmarried"))
genderoption=(("MALE","MALE"),("FEMALE","FEMALE"))
class supportstaff(models.Model):
    position=models.CharField(max_length=100,choices=support)
    name=models.CharField(max_length=30)
    photo=models.ImageField(max_length=100)
    fathername=models.CharField(max_length=30)
    aadharnumber=models.CharField(max_length=20)
    dateofjoining=models.DateField(null=True)
    gender=models.CharField(max_length=20,choices=genderoption)   
    marritalstatus=models.CharField(max_length=20,choices=statusm)   
    dateofbirth=models.DateField()
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobilenumber=models.CharField(max_length=13)

class guestservices(models.Model):
    position=models.CharField(max_length=100,choices=guest)
    name=models.CharField(max_length=30)
    photo=models.ImageField(max_length=100)
    fathername=models.CharField(max_length=30)
    aadharnumber=models.CharField(max_length=20)
    dateofjoining=models.DateField(null=True)
    gender=models.CharField(max_length=20,choices=genderoption)   
    marritalstatus=models.CharField(max_length=20,choices=statusm)   
    dateofbirth=models.DateField()
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobilenumber=models.CharField(max_length=13)

class administrative(models.Model):
    position=models.CharField(max_length=100,choices=adminn)
    name=models.CharField(max_length=30)
    photo=models.ImageField(max_length=100)
    fathername=models.CharField(max_length=30)
    aadharnumber=models.CharField(max_length=20)

    dateofjoining=models.DateField(null=True)
    gender=models.CharField(max_length=20,choices=genderoption)   
    marritalstatus=models.CharField(max_length=20,choices=statusm)  
    dateofbirth=models.DateField()
    

    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobilenumber=models.CharField(max_length=13)

