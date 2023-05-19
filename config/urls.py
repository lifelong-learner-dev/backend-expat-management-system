"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/work_permits_requests/', include('work_permits_requests.urls')),
    path('api/v1/work_permits/', include('work_permits.urls')),
    path('api/v1/real_estate_agents/', include('real_estate_agents.urls')),
    path('api/v1/pick_ups_requests/', include('pick_ups_requests.urls')),
    path('api/v1/pick_ups/', include('pick_ups.urls')),
    path('api/v1/houses/', include('houses.urls')),
    path('api/v1/moving/', include('moving.urls')),
    path('api/v1/moving_requests/', include('moving_requests.urls')),
    path('api/v1/moving_preparation_documents/', include('moving_preparation_documents.urls')),
    path('api/v1/moving_companies/', include('moving_companies.urls')),
    path('api/v1/house_rent_extensions/', include('house_rent_extensions.urls')),
    path('api/v1/green_cards_requests/', include('green_cards_requests.urls')),
    path('api/v1/green_cards_preparation_documents/', include('green_cards_preparation_documents.urls')),
    path('api/v1/green_cards/', include('green_cards.urls')),
    path('api/v1/family_residence_permits_requests/', include('family_residence_permits_requests.urls')),
    path('api/v1/family_residence_permits_preparation_documents/', include('family_residence_permits_preparation_documents.urls')), 
    path('api/v1/family_residence_permits/', include('family_residence_permits.urls')),
    path('api/v1/driving_licenses_requests/', include('driving_licenses_requests.urls')),
    path('api/v1/driving_licenses_preparation_documents/', include('driving_licenses_preparation_documents.urls')),
    path('api/v1/driving_licenses/', include('driving_licenses.urls')),
    path('api/v1/company_cars_requests/', include('company_cars_requests.urls')),
    path('api/v1/company_cars/', include('company_cars.urls')),
    path('api/v1/announcements/', include('announcements.urls')),
    path('api/v1/additional_information/', include('additional_information.urls')),

]