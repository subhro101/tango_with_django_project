from django.shortcuts import render
from django.http import HttpResponse

def index(request):
<<<<<<< HEAD
# Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
=======
    return HttpResponse("Rango says hey there partner!" + "<a href='/rango/about/'>About</a>")
>>>>>>> 82c013063c1edfa2120c9bbdbf604c5d8ec55ae2

def about(request):
    return HttpResponse("Rango says here is the about page." + "<a href='/rango/'>Index</a>")