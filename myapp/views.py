
from django.http import HttpResponse
from .models import Type, Item
import calendar
from django.shortcuts import get_object_or_404
from django.views import View

def detail(request, type_no):
    type_obj = get_object_or_404(Type, pk=type_no)
    item_list = type_obj.items.all()  # Assuming ForeignKey from Item to Type

    response = HttpResponse()
    response.write(f'<h1>Items for Type: {type_obj.name}</h1>')
    for item in item_list:
        response.write(f'<p>{item.name} - ${item.price}</p>')

    return response

def about(request, year=None, month=None):
    if year and month:
        month_name = calendar.month_name[int(month)]
        return HttpResponse(f"This is an Online Grocery Store. Welcome to {month_name} {year}.")
    return HttpResponse("This is an Online Grocery Store.")

def index(request):
    type_list = Type.objects.all().order_by('id')
    item_list = Item.objects.all().order_by('-price')[:10]  # Top 10 most expensive items
    response = HttpResponse()
    response.write('<h1>Types:</h1>')
    for type in type_list:
        response.write(f'<p>{type.id}: {type.name}</p>')

    response.write('<h1>Top 10 Items:</h1>')
    for item in item_list:
        response.write(f'<p>{item.name} - ${item.price}</p>')

    return response

# Function-Based View (FBV)
# Pros: Simpler and easier for small, straightforward views.
# Cons: Can become messy if you have to handle many HTTP methods (GET, POST, etc.)
def sample_fbv(request):
    return HttpResponse("This is a Function-Based View")

# Class-Based View (CBV)
# Pros: More reusable and structured, especially for handling multiple HTTP methods like GET, POST.
# Cons: Slightly more complex to understand and set up, especially for simple cases.
class SampleCBV(View):
    def get(self, request):
        return HttpResponse("This is a Class-Based View")
