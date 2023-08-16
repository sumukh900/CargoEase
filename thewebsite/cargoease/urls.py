from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('consignee_sign_up/', views.consignee_sign_up, name='consignee_sign_up'),
	path('consignee_login/', views.consignee_login, name='consignee_login'),
	path('consignee_dashboard/', views.consignee_dashboard, name='consignee_dashboard'),
	path('carrier_signup/', views.carrier_signup, name='carrier_signup'),
	path('carrier_login/', views.carrier_login, name='carrier_login'),
	path('carrier_dashboard/', views.carrier_dashboard, name='carrier_dashboard'),
	path('carrier_addroute/', views.carrier_addroute, name='carrier_addroute'),
	path('get_consigner_info/', views.get_consigner_info, name='get_consigner_info'),
	path('get_carriers_for_sourcedest/', views.get_carriers_for_sourcedest, name='get_carriers_for_sourcedest'),
	path('payments/', views.payments, name='payments'),



]