from django.shortcuts import render
from .models import Event
from datetime import datetime
# Create your views here.
# print(type(Event.objects.all()[0].end_date))
def index(request):
    events = Event.objects.all()
    current_datetime = datetime.now()

    # Format it as "Mon. Day, Year, Hour:Minute AM/PM"
    # formatted_datetime = current_datetime.strftime("%b. %d, %Y, %I:%M %p")
    # date_time_obj1 = datetime.strptime(date_time_str1, "%b. %d, %Y, %I:%M %p")
    # date_time_obj2 = datetime.strptime(date_time_str2, "%b. %d, %Y, %I:%M %p")
    
    # ongoingEvents = list(filter(lambda x: x.end_date>current_datetime and x.start_date<current_datetime, events))
    # upcomingEvents = list(filter(lambda x: x.start_date>current_datetime , events))
    # current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    current_datetime = current_datetime.replace(microsecond = 0)
    ongoingEvents = list()
    upcomingEvents = list()
    pastEvents = list()
    for x in events:
        x.end_date = x.end_date.replace(tzinfo = None)
        x.start_date = x.start_date.replace(tzinfo = None)
        if x.end_date>current_datetime and x.start_date<current_datetime:
            ongoingEvents.append(x)
        if x.start_date>current_datetime:
            upcomingEvents.append(x)
        if x.end_date<current_datetime:
            pastEvents.append(x)
    pastEvents = list(filter(lambda x: x.shown, pastEvents))
        
    # print(ongoingEvents)
    return render(request, "index.html", {"ongoingEvents":ongoingEvents ,"upcomingEvents":upcomingEvents, "pastEvents":pastEvents })

def test(request):
    return render(request,"base.html")