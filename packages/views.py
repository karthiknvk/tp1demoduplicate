from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
#from .models import Set1,Set2,Set3,Set4
#from .models import Packageset
from .models import Destination,Onedaypackage,Twodaypackage,Threedaypackage,Fourdaypackage,Fivedaypackage,Sixdaypackage,Sevendaypackage
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
    daylist=[1,2,3,4,5,6,7]
    destinationlist=['Kozhikode','Wayanad','Ernakulam','Thiruvananthapuram']
    return render(request,"home.html",{'daylist':daylist,'destinationlist':destinationlist})
  


'''
def packageview(request):
  budget=request.POST.get('budget')
  destination = request.POST.get('destination', '')

  if budget=='under 5000':
    packagelist=Set1.objects.all()
  elif budget=='5000-10000':
    packagelist=Set2.objects.all()
  elif budget=='10000-15000':
    packagelist=Set3.objects.all()
  elif budget=='above 15000':  
    packagelist=Set4.objects.all()
  
  return render(request,'tourpackages.html',{'packagelist':packagelist,'budget':budget})
  
 

def packageview(request):
  day=request.POST.get('day')
  destination = request.POST.get('destination', '')
  mainpackagedict=dict()
  if destination:
     mainpackagelist=Packageset.objects.filter(district=destination)
     print(mainpackagelist)
     mainpackagedict={}
     if day == '1':
      for pack in mainpackagelist:
        key=(pack.district,pack.packagnumber)
        list1=pack
        mainpackagedict[key].append({
          'district':pack.district,
          'packagenumber':pack.packagnumber,
          'spotnumber':pack.spotnumber,
          'spotname':pack.spotname,
          'cafespot':pack.cafespot,
          'description':pack.description
        })
      print(mainpackagedict)

     else:
      print('no value')
  else:
    mainpackagelist=Packageset.objects.filter(packagnumber=int(day))
  return render(request,'tourpackages.html',{'mainpackagelist':mainpackagedict,'day':day})

''' 
mainpackagedict=dict()
mainpackagedictcopy=dict()
@login_required
def packageview(request):
  global day
  if 'itinerary' in request.POST:
      print("package_details_list 1st time->", mainpackagedict)
      return itineraryview(request, mainpackagedict)
  elif 'filterform' in request.POST:
      #mainpackagedictcopy=dict()
      return landscapefilter(request,mainpackagedictcopy,day)
  else:
    day=request.POST.get('day')
    destination = request.POST.get('destination', '')
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
        if 'filterform' in request.POST:
          mainpackagedictcopy=mainpackagedict
          return landscapefilter(request,mainpackagedictcopy)
          
        for key in mainpackagedict:  
          print("\n",key,"->",mainpackagedict[key])
          print("\n")
          spotnamelist=[]
          for item in mainpackagedict[key]:
            spotnamelist.append(item[4])
            print('spotname->',item[4]," |||")
          mainspotnamelist.append(spotnamelist)
          print("\n")
        print("\nmainspotnamelist->",mainspotnamelist)    
        '''

    return render(request,'tourpackages.html',{'mainpackagedict':mainpackagedict,'day':day},)
  
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
                 
    '''
                 choosen_package_dict[day_key]=inner_dict
                  for key,items in choosen_package_dict.items():
                  for innerkey,inneritems in items.items():
                  print(key,"->",innerkey,"->",inneritems)
                  print("\n")
    '''
      
    
    
        #package_code=request.POST.get('package_code')
        #print("package_code->",package_code)
        #return redirect("packageview")
       # return itineraryview(request,mainpackagedict,package_code)
      #print(mainpackagelist)


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
        return render(request,'landscape.html',{'mainpackagedictcopy':mainpackagedictcopy,'day':day,})
      

    return render(request,'landscape.html',{'mainpackagedictcopy':mainpackagedictcopy,'landscapelist':landscapelist,},)

    '''
      for item in landscapelist:
         for key,dictitems in mainpackagedictcopy:
            if item in dictitems:
               mainpackagedict[key]=dictitems
      for key in mainpackagedictcopy
      '''
      
    
'''
elif day == '2':
    mainpackagelist=Twodaypackage.objects.filter(district=destination).select_related('spotname').all()
    mainspotnamelist=[]
    for package in mainpackagelist:
      number=str(package.packagnumber)
      count=package.district+number
      print(count,"\n")
      key=count
      packagelist=[package.id,                      #0
                   package.district,                #1
                   package.packagnumber,            #2
                   package.spotnumber,              #3
                   package.spotname,                #4
                   package.spotname.location,       #5
                   package.spotname.landscape,      #6
                   package.spotname.cafespot,       #7
                   package.spotname.description,    #8
                   package.spotname.img             #9
                   ]
      print("packagelist->",packagelist,"\n")
      if key not in mainpackagedict:
        mainpackagedict[key]=[]
      mainpackagedict[key].append(packagelist)
    for key in mainpackagedict:  
      print("\n",key,"->",mainpackagedict[key])
      print("\n")
      spotnamelist=[]
      for item in mainpackagedict[key]:
        spotnamelist.append(item[4])
        print('spotname->',item[4]," |||")
      mainspotnamelist.append(spotnamelist)
      print("\n")
    print("\nmainspotnamelist->",mainspotnamelist)  
'''
    
    
      #return itineraryview(request,mainpackagedict,package_code)
    #print("\n")
'''
      spotinformationlist=[]
      spotinformationtdict={}
      for item in mainpackagedict[key]:
        spotinformationtdict={
          'destinationpackagenumber':item.packagnumber,
          'destinationnumber':item.spotnumber,
          'destinationname':item.spotname
        }
        spotinformationlist.append(spotinformationtdict)
'''  


      

'''
 elif day == '7':
    mainpackagelist=Sevendaypackage.objects.filter(district=destination)
    print(mainpackagelist)   
'''
   
  #else:
    #return render(request,'tourpackages.html',{'mainpackagelist':mainpackagedict,'day':day})
  #return render(request,'tourpackages.html',{'mainpackagedict':mainpackagedict,'day':day,})



'''
def itineraryview(request):
    if request.method=="POST":
      package_code=request.POST.get('package_code')
      print("package_code->",package_code)
    #print("package_code->",package_code)
      print("package_details_list->",mainpackagedict[package_code])
    return render(request,'itinerary.html',)
'''


'''
def itineraryview(request):
  if request.method=="POST":
    package_code=request.POST.get('package_code')
    package_details_list_json = request.POST.get('package_details_list')
    package_details_list = json.loads(package_details_list_json)
    print("package_code->",package_code)
    print("package_details_list->",package_details_list)
    print("\n")
    destinations = [serialize_destination(destination) for destination in
                        [Destination(**item) for item in package_details_list]]

        # Manually serialize to JSON using the default argument
    json_destinations = serialize('json', destinations, use_natural_primary_keys=True)
    print(json_destinations)
    #destinations = [Destination(**item) for item in package_details_list]
    #for destination in destinations:
    #  print(serialize_destination(destination))
    print("\n")
    print("ENDDDD")
    return JsonResponse({'package_details_list': json_destinations})
  return render(request,'itinerary.html',{'package_details_list':package_details_list})
  '''