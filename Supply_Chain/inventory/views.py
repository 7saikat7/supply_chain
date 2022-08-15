from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def add_delivery_details(request):
	if request.POST:
		address = request.POST.get('address','')
		pincode = request.POST.get('pincode','')
		contact = request.POST.get('contact_number','')
		alternate_contact = request.POST.get('alternate_contact','')
		product_category = request.POST.get('product_category','')
		print(product_category)
	return render(request,"inventory/delivery_details_page.html")

