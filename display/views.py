from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):

    date = str(datetime.now().date())
    time = str(datetime.now().time())

    html = f'''
    
    <html>
        <head>
            <meta http-equiv="refresh" content="1">
            <title>Clock</title>
            <style>

            </style>
        </head>
        <body style="background-image:linear-gradient(to right,red,yellow,red)">
            <h1 style="text-align:center;
            background: -webkit-linear-gradient(blue,white);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;">
            Current Date and Time
            </h1>
            
            <div style="background-color: aqua;
            border: 2px solid black;
            height: 120px;
            width: 400px;
            margin: 50px 470px;
            align-items: center;
            box-shadow: 10px 10px 20px blue;">
            
                <h2 style="text-align:center">Date: {date}</h2>
                <h2 style="text-align:center">Time: {time}</h2>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html)
