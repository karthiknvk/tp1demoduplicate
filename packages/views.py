from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Destination,Onedaypackage,Twodaypackage,Threedaypackage,Fourdaypackage,Fivedaypackage,Sixdaypackage,Sevendaypackage,Tourpackage
#import json
#from .utils import serialize_destination
#from django.http import JsonResponse
#from django.core.serializers import serialize



# Create your views here.

def logoutview(request):
    auth.logout(request)
    print("logged out")
    return redirect('/')

@login_required
def accountview(request):
    user_profile=request.user
    return render(request,'accountdetails.html',{'user_profile':user_profile})

@login_required
def home(request):
  if request.method=="POST":
    return packageview(request)
    
  else:
    #pricelist=['under 5000','5000-10000','10000-15000','above 15000']
    daylist={'1':'1daypackage','2':'2daypackage'}
    destinationlist=['Kozhikode','Wayanad','Ernakulam','Thiruvananthapuram']
    return render(request,"home.html",{'daylist':daylist,'destinationlist':destinationlist})
  

mainpackagedict=dict()
mainpackagedictcopy=dict()
@login_required
def packageview(request):
  global day
  global destination
  if 'itinerary' in request.POST:
      print("package_details_list 1st time->", mainpackagedict)
      return itineraryview(request, mainpackagedict)
  elif 'filterform' in request.POST:
      #mainpackagedictcopy=dict()
      return landscapefilter(request,mainpackagedictcopy,day)
  else:
    day=request.POST.get('day')
    print('day->',day)
    destination = request.POST.get('destination', '')
    mainpackagedict.clear()
    mainpackagelist=Tourpackage.objects.filter(district=destination,packagecategory=day).select_related('spotname').all()
    print("\n")
    print('mainpackagelist----->',mainpackagelist)
    mainspotnamelist=[]
    for package in mainpackagelist:
      number=str(package.packagenumber)
      count=package.district+number
      print(count,"\n")
      key=count
      packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
      print("packagelist->",packagelist,"\n")
      if key not in mainpackagedict:
        mainpackagedict[key]=[]
      mainpackagedict[key].append(packagelist)
    for key in mainpackagedict:
      print(key,'->',mainpackagedict[key])
    return render(request,'tourpackages.html',{'mainpackagedict':mainpackagedict,'day':day,'district':destination},)

    '''
    if day == '1': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Onedaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)

    elif day == '2': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Twodaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)

    elif day == '5': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Threedaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)

    
    elif day == '7': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Sevendaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)
    
    '''
    
        

    
  
def itineraryview(request, mainpackagedict,):
    if request.method == "POST":
        package_code = request.POST.get('package_code')
        print("package_code->", package_code)
        print("package_details_list2nd time->", mainpackagedict[package_code])
        choosen_package_list=mainpackagedict[package_code]
        print("choosen package list->",choosen_package_list)
        print("choosen package list length->",len(choosen_package_list))
        no_of_days=len(choosen_package_list)//3
        choosen_package_dict=dict()
        inner_dict=dict()
        print("choosen package list length divided by 3->",no_of_days)
        
        for inner_list in choosen_package_list:
          print("choosen package dict now at top->",choosen_package_dict)
          print("innerlist->",inner_list)
          time_key=inner_list[4]
          print("time_key->",time_key)
          inner_dict[time_key]=inner_list
          print("innerdictlength->",len(inner_dict))
          if len(inner_dict)<3:
            print("inner_dict now->",inner_dict)
            #continue
          else :
            print("inner_dict now in else situation->",inner_dict)
            for i in range(1,no_of_days+1):
              print(i)
              day_key='DAY'+str(i)
              print("day_key->",day_key) 
              if day_key not in choosen_package_dict:
                print("key not found")
                print("ENTERED INSIDE")
                choosen_package_dict[day_key]=dict(inner_dict)
                print("choosen package dict first->",choosen_package_dict)
                inner_dict.clear()
                break
              else:
                print("key found,conitnuing to next")
                continue
              #problm
            print("choosen package dict second->",choosen_package_dict)
          print("choosen package dict third->",choosen_package_dict)
        print("choosen package dict at end of for loop->",choosen_package_dict)  

    print("choosen package dict at end->",choosen_package_dict)

    return render(request,'itinerary.html',{'choosen_package_dict':choosen_package_dict})
                 

def landscapefilter(request,mainpackagedictcopy,day):
    if request.method == "POST":
      landscapelist=request.POST.getlist('filter')
      if not landscapelist:
         return
      else:
        mainpackagedictcopy.clear()
        print("landscapelist->",landscapelist)
        print("\nDay->",day)
        print('\nmainpackagedict->',mainpackagedict)
        print('\nmainpackagedictcopy->',mainpackagedictcopy)
        for key,dictitems in mainpackagedict.items():
          print("item in each key")
          print(key,'->',dictitems)
        for item in landscapelist:
          for key,dictitems in mainpackagedict.items():
              if key not in mainpackagedictcopy:
                    for innerdictitems in dictitems:
                      if item in innerdictitems:
                          mainpackagedictcopy[key]=dictitems
        print('\nmainpackagedict->',mainpackagedict)
        print('\nmainpackagedictcopy->',mainpackagedictcopy)
        return render(request,'landscape.html',{'mainpackagedictcopy':mainpackagedictcopy,'day':day,'district':destination})
      

    return render(request,'landscape.html',{'mainpackagedictcopy':mainpackagedictcopy,'landscapelist':landscapelist,},)

    
    
