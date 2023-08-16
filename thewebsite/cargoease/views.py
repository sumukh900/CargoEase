from django.shortcuts import render,redirect
from .forms import ConsigneeForm
from django.contrib import messages
from .models import User
from .models import Carrier
from .models import Route
from .forms import CarrierSignUpForm
from .forms import NewRouteForm



def homepage(request):
    if request.method == 'POST':
        start_point = request.POST.get('start_point', '')
        end_point = request.POST.get('end_point', '')
        # Process the inputs or redirect to a different page based on the user's choice.

    return render(request, 'homepage.html')


def consignee_sign_up(request):
	if request.method == 'POST':
		form = ConsigneeForm(request.POST)
		if form.is_valid():
			print("***********inside form************")
            # Process the form data and save the user.
			User = form.save()
		messages.success(request,('You have successfully signed up for CargoEase as consignee'))
		return redirect('consignee_login')
	else:
		form = ConsigneeForm()
		return render(request, 'consignee_sign_up.html', {'form': form})

def consignee_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		success = myauthenticate(username, password)
		all_users = User.objects.all()

		if success == True:
			user = User.objects.get(username=username) 
			request.session['user'] = {
				'username': user.username,
				'first_name': user.first_name,
				'last_name': user.last_name,
            		}
			return redirect('consignee_dashboard')
		else:
			messages.success(request,('Either username or password or incorrect. Try Again!!!'))
			return render(request, 'consignee_login.html')
	else:
		return render(request, 'consignee_login.html') 

def myauthenticate(username, password):
	all_users = User.objects.all()
	listusers = list(all_users)
	for x in listusers:
		if ((x.username == username)) and ((x.password == password)):
			return True

	return False

def consignee_dashboard(request):
	all_routes = Route.objects.all()
	return render(request, 'consignee_dashboard.html', { "routes": all_routes }) 

def carrier_signup(request):
	if request.method == 'POST':
		cform = CarrierSignUpForm(request.POST)
		if cform.is_valid():
			carrier = cform.save()
			messages.success(request,('You have successfully signed up for CargoEase as carrier'))
		return redirect('carrier_login')  # Redirect to the login page
	else:
		cform = CarrierSignUpForm()
		return render(request, 'carrier_signup.html', {'form': cform})

def carrier_login(request):
	if request.method == 'POST':
		carrier_id = request.POST['carrier_id']
		password = request.POST['password']
		success = mycarrierauthenticate(carrier_id, password)
		all_carriers = Carrier.objects.all()

		if success == True:
			carrier = Carrier.objects.get(carrier_id=carrier_id)  # Fetch the user object
			request.session['carrier'] = {
				'carrier_id': carrier.carrier_id,
				'first_name': carrier.first_name,
				'last_name': carrier.last_name,
            		}
			return redirect('carrier_dashboard')
		else:
			messages.success(request,('Either username or password or incorrect. Try Again!!!'))
			return render(request, 'carrier_login.html')
	else:
		return render(request, 'carrier_login.html')

def mycarrierauthenticate(carrier_id, password):
	all_carrier = Carrier.objects.all()
	listcarriers = list(all_carrier)
	for x in listcarriers:
		if ((x.carrier_id == carrier_id)) and ((x.password == password)):
			return True

	return False

def carrier_dashboard(request):
	return render(request, 'carrier_dashboard.html')

def carrier_addroute(request):
	if request.method == 'POST':
		cform = NewRouteForm(request.POST)
		if cform.is_valid():
			Route = cform.save()
			messages.success(request,('You have successfully added a new route as carrier'))
		return redirect('carrier_dashboard')  
	else:
		cform = NewRouteForm()
		return render(request, 'carrier_addroute.html', {'form': cform})


def get_consigner_info(request):
	if request.method == 'POST':	
		source = request.POST['source']
		destination = request.POST['destination']
		routes = getcarrierforsourcendes(source,destination)
		request.distance = routes[0].distance
		carrier_ids = [Route.carrier_id for Route in routes]
		request.route_id = Route.route_id
		setreqeustattributes(request)
		routecarriers = Carrier.objects.filter(carrier_id__in=carrier_ids)
		return render(request, 'get_carriers_for_sourcedest.html',{'carriers': routecarriers})
	else:
		return render(request, 'consignee_dashboard.html')

def getcarrierforsourcendes(source, destination):
	all_routes = Route.objects.filter(source=source, destination=destination)
	return list(all_routes)

def get_carriers_for_sourcedest(request):
	print("inside Method get_carriers_for_sourcedest ")
	return render(request,'payments.html')

def payments(request):
	return render(request, 'payments.html')

def setreqeustattributes(request):
	request.source = request.POST['source']
	request.destination = request.POST['destination']
	request.weight = request.POST['weight']
	request.length = request.POST['length']
	request.breadth = request.POST['width']
	request.height = request.POST['height']
	return request



