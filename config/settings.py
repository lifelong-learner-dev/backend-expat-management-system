"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(1*)mr13hb_^$bg!nz89-o(9+2_fm=iuclskxukf5!h@i7t6*c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

THIRD_PARTY_APPS = [
    "rest_framework",
]

CUSTOM_APPS = [
    "processes.apps.ProcessesConfig",
    "requests.apps.RequestsConfig",
    "additional_information.apps.AdditionalInformationConfig",
    "announcements.apps.AnnouncementsConfig",
    "common.apps.CommonConfig",
    "company_cars_requests.apps.CompanyCarsRequestsConfig",
    "company_cars.apps.CompanyCarsConfig",
    "driving_licenses_preparation_documents.apps.DrivingLicensesPreparationDocumentsConfig",
    "driving_licenses.apps.DrivingLicensesConfig",
    "driving_licenses_requests.apps.DrivingLicensesRequestsConfig",
    "family_residence_permits.apps.Family_residence_permitsConfig",
    "family_residence_permits_preparation_documents.apps.FamilyResidencePermitsPreparationDocumentsConfig",
    "family_residence_permits_requests.apps.FamilyResidencePermitsRequestsConfig",
    "green_cards.apps.Green_cardsConfig",
    "green_cards_preparation_documents.apps.GreenCardsPreparationDocumentsConfig",
    "green_cards_requests.apps.GreenCardsRequestsConfig",
    "house_rent_extensions.apps.HouseRentExtensionsConfig",
    "houses.apps.HousesConfig",
    "moving.apps.MovingConfig",
    "moving_companies.apps.MovingCompaniesConfig",
    "moving_requests.apps.MovingRequestsConfig",
    "pick_ups.apps.Pick_upsConfig",
    "pick_ups_requests.apps.PickUpsRequestsConfig",
    "real_estate_agents.apps.RealEstateAgentsConfig",
    "users.apps.UsersConfig", 
    "work_permits.apps.WorkPermitsConfig",
    "work_permits_requests.apps.WorkPermitsRequestsConfig",
]

SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth

AUTH_USER_MODEL = "users.User"
