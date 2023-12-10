from django.shortcuts import render
from Blogsection.models import popular
from Blogsection.models import latest
from Blogsection.models import trending
from Blogsection.models import aboutus
from Blogsection.models import allblogs



def home(request):
    
     BlogData = popular.objects.all() 
     UnescoData = latest.objects.all()
     FeaturedData = trending.objects.all()[:3]
     data={
        
        'blogData':BlogData,
        'unescoData':UnescoData,
        'featuredData':FeaturedData

     }

     return render(request, 'index.html',data)

def  tdetails(request,blogsid):
      
      TrendingDetails = trending.objects.get(id=blogsid)
      data={
            'TrendingDetails':TrendingDetails
      }
      return render(request,"trendingsdetails.html",data)


def  pdetails(request,blogsid):
      
      PopularDetails = popular.objects.get(id=blogsid)
      data={
            'PopularDetails':PopularDetails
      }
      return render(request,"popularsdetails.html",data)


def  ldetails(request,blogsid):
      
      LatestDetails = latest.objects.get(id=blogsid)
      data={
            'LatestDetails':LatestDetails
      }
      return render(request,"latestsdetails.html",data)

def about(request):

      AboutData = aboutus.objects.all()
      data={
            'aboutData':AboutData
      }
      return render(request,"aboutus.html",data)


def blog(request):

      BlogsData = allblogs.objects.all()
      data={
            'blogsData':BlogsData
      }
      return render(request,"blogs.html",data)


def news(request):
      return render(request,"newsletter.html")


def contact(request):
      return render(request,"contactus.html")

