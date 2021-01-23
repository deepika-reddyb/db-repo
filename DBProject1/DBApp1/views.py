from django.shortcuts import render
from DBApp1.models import Employee
# Create your views here.
def view1(request):
    e=Employee.objects.all()
    d={'emp':e}
    return render(request,'DBApp1/1.html',d)