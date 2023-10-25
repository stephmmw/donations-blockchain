from django.shortcuts import render
from datetime import datetime

# Create your views here.

class Block():
    pass

# Interface
def index(request):
    if request.method == "POST":
        timestamp = str(datetime.now().isoformat())
        name = request.POST["name"]
        amount = request.POST["amount"] 
        
        print('\nDonation \nName: '+ name + '\nAmount: ' + amount+ '\nTimestamp: ' + timestamp)    
    
    app = 'Donations'
    context = {
        "app": app,
        "title": 'Donations',
    }
    template_name = "index.html"
    return render(request, template_name, context)