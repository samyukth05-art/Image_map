# Ex03 Places Around Me
# Date:25.11.2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
views.py
```
from django.shortcuts import render

def home(request):
    return render(request, 'chennai.html')

def eg(request):
    return render(request, 'Egmore.html')

def koyam(request):
    return render(request, 'koyambedu.html')

def nungu(request):
    return render(request, 'Nungambakkam.html')

def virug(request):
    return render(request, 'virugambakkam.html')
```
urls.py
```
from django.contrib import admin
from django.urls import path
from mapapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('eg/', views.eg, name='eg'),
    path('koyam/', views.koyam, name='koyam'),
    path('nungu/', views.nungu, name='nungu'),
    path('virug/', views.virug, name='virug'),
]
```
chennai.html
```
{% load static %}
<html>
<head>
    <title>Chennai</title>
    <style>

        img{
            
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
             height: 100vh;
        }
        body{
            overflow: hidden;
        }
    </style>
</head>
<body>
   
    <img src="{% static 'chennai.png' %}" alt="Chennai" usemap="#imap" >
    <map name="imap">
        <area shape="rect" coords="1,2,1803,642" href="{% url 'eg' %}" title="chennai">

    </map>
</body>
</html>
```
Egmore.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1{text-align:center;color: black;}
        img{
            display:block;
            margin-left:auto;
            margin-right:auto;
            width:700px;
            height:250px;
            border-radius: 20px;
        }
        p{
            text-align: justify;
            line-height: 20px;
            padding: 20px;

        }
        
         body {
        background-color:gold;
        }
</style>


    </style>
</head>
<body>
    <h1>
        Egmore
    </h1>
    <img src="{% static 'Egmore.jpg' %}">
   
    
    <p>Egmore is a bustling neighbourhood in the heart of Chennai, known for its blend of history, culture, and modern urban life. It is home to the iconic Egmore Railway Station, one of the city’s major transit hubs, and the Government Museum, a landmark that showcases centuries of South Indian art, archaeology, and natural history. With its tree-lined roads, educational institutions, hospitals, and a mix of old colonial architecture alongside contemporary buildings, Egmore serves as both a commercial center and a residential enclave.</p>
     
</body>
</html>
```
Koyambedu.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1{text-align:center;color: black;}
        img{
            display:block;
            margin-left:auto;
            margin-right:auto;
            width:700px;
            height:250px;
            border-radius: 20px;
        }
        p{
            text-align: justify;
            line-height: 20px;
            padding: 20px;

        }
        
         body {
        background-color:green;
        }
</style>


    </style>
</head>
<body>
    <h1>
        Koyambedu
    </h1>
    <img src="{% static 'koyambedu.jpg' %}">
   
    
    <p>Koyambedu is a major commercial and transportation hub in Chennai, best known for housing one of Asia’s largest wholesale markets for fruits, vegetables, and flowers. The area is also home to the Chennai Mofussil Bus Terminus (CMBT), one of the biggest bus terminals in South Asia, making it a key gateway for travelers across Tamil Nadu and neighboring states. Over the years, Koyambedu has grown into a busy urban center filled with shops, hotels, and residential complexes.</p>
     
</body>
</html>
```
Nungambakkam.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1{text-align:center;color:black;}
        img{
            display:block;
            margin-left:auto;
            margin-right:auto;
            width:700px;
            height:250px;
            border-radius: 20px;
        }
        p{
            text-align: justify;
            line-height: 20px;
            padding: 20px;

        }
        
         body {
        background-color:blue;
        }
</style>


    </style>
</head>
<body>
    <h1>
        Nungambakkam
    </h1>
    <img src="{% static 'Nungambakkam.jpg' %}">
   
    
    <p>Nungambakkam is one of Chennai’s most vibrant and upscale neighbourhoods, known for its mix of culture, commerce, and cosmopolitan lifestyle. It is home to leading educational institutions, foreign consulates, art galleries, and a lively stretch of cafés, restaurants, and boutiques. The area blends quiet residential streets with bustling commercial hubs, making it popular among students, professionals, and families alike.</p>
     
</body>
</html>
```
virugambakkam.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1{text-align:center;color:black;}
        img{
            display:block;
            margin-left:auto;
            margin-right:auto;
            width:700px;
            height:250px;
            border-radius: 20px;
        }
        p{
            text-align: justify;
            line-height: 20px;
            padding: 20px;

        }
        
         body {
        background-color:palevioletred;
        }
</style>


    </style>
</head>
<body>
    <h1>
        Virugambakkam
    </h1>
    <img src="{% static 'virugambakkam.jpg' %}">
   
    
    <p>Virugambakkam is a well-established residential neighbourhood in western Chennai, known for its calm streets, strong community atmosphere, and convenient urban amenities. Once a quiet suburb with open fields and film studios, it has grown into a lively locality filled with schools, parks, markets, and places of worship. The area is well connected through Arcot Road, giving residents easy access to nearby hubs like Vadapalani and Koyambedu.</p>
     
</body>
</html>
```
# OUTPUT
![alt text](<Screenshot 2025-11-30 215615.png>)
![alt text](<Screenshot 2025-11-30 215832.png>)
![alt text](<Screenshot 2025-11-30 221638.png>)
![alt text](<Screenshot 2025-11-30 221821.png>)
![alt text](<Screenshot 2025-11-30 221841.png>)

# RESULT
The program for implementing image maps using HTML is executed successfully.
