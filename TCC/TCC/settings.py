"""
Django settings for TCC project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4#6l188lbqs&y&oj)3bls(@%3xki(*!cheyhb+6z6aq_fvag1t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'login',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TCC.urls'

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

WSGI_APPLICATION = 'TCC.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

GOOGLE_APPLICATION_CREDENTIALS = {
    "type": "service_account",
    "project_id": "projetointegrador-7141d",
    "private_key_id": "2e6950a3102c5fcf453302f0168a4cee43f67f13",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCk5+cA22QXOMyu\nvaTiS6i6RpTRJAe2OxXuZkjIsHI0Nhm39u7YxW5xbuL/lQ6cdRTEht7rTHTwlALb\n1rRXHWPrYZ8Tr3t18svX6PkyHU3/cOlKiW7d3E9xjk6p461otvZpm9axovduW/PU\nQt+3+wiT8NiKJ85jz2Tng/GwGyNZ18fmewVrxnqvu91y4s7LE0xu9/TtY+37nx6u\nh58o6OBMfml44fbYSh4qWGiyHHpDPZ+cgFDdVQYmZcGodVQtxO48Cg0oyi/sMpkO\nbJXJYhijBxgHMc3kas22p2cYPd679Z12n4mR6z0Cp4MsFqEDBcAC0jH1vLm2h4yc\nlQIb62nhAgMBAAECggEADr85UoOMICKBdWf6uIz9Dgl1Uf2nneWLSMpHXIEg+WfU\nJXY09lgzj/vTW3lUOOwkew23njG0bHZECi5ZasfzUU+l1vAUuZ/ImGqabF+gA8Ww\nayy+qCMFTLml8b3tWkWwZBHeYXzaJTmeZL9FO/H8WqSJbNNx+s2Hb8fGI5JNt0E2\ndxgCEttgy1g7m+AWmMQCkjUPVSldLx22BJKOxzpL6VyZefViSHDSkTrL5SsibXEz\nbdwgrnNTXApesV4vW0uQPhEYR7Zer0XsBBQFwC49dB4UJ2ZOZF5Pt2qqZri6+MRY\n4dG7M6qxylZ/j/jtDnKpSyzdNpgvCaci69zcOii+pQKBgQDoDGrn7JsNDD3TV9ZI\nSbtkN9+kwapCZHH01voD9KBCOO1xyROF5qfiPPZum7Oq2BRULVJYpPOmUA7aWF/C\nBsbVHRVoR3FndRVZYW/CeDHu9evMP7NvZQjprOiD6ofCFvkaFyWDRtayzzTkl+LY\np9/B2DzdWhI5+dOm7kl5jshS/QKBgQC17VPCCS4WD4NIfMwN6PWntiqf2yXtkhec\nux/z/nofhwCRMCgQFxiTLTd4bHr6Int+8+Oc4Y3nZ8Ch+0uEcAIETTADLww3PlYC\nfYm+9tBSdUVOAgbx7uaImBVcWluhYOK2n+lHFjLd6b8K7fG2+gxaUTvNKvbQVan3\nsvTg4hjBtQKBgAQcXDR5m5GSmvHIh5JGRByVZM/dYm/EqcQlns49Ii2qJoKyhjcE\nDAtU+ySge4FWTJ3lI6VQXsSefHTfxeqBBjq2Ri/PvDGSAGvR7xHp4TCTiLbYlgwu\nJQdGuePEXt1QXN9ac56svZbzVsOJ8UnXR35+ny1osBP42ggGBqUxo1jdAoGAHghu\n0lJ3pDatYpMPkKBLpYMiKD+iVETQ1xPhI4N4H6pGwrEje/yEFw/Y321xI8f7gSq8\nAZMOvQvYtiTpA5UGEDW53lyu9JO62TBmQ/s0ytgHN+iHwvrAXf5VUGiuRcbbxnBB\nr3WPsii7XA+J3r4KugI9EBKuqhfqNjT5zgIlOh0CgYEAxso+UrM6d5lzSq9ia7El\nhSfmdUJxEhrf1igansgpmvfYx8cRybdJcWaxb/Ox6O/GP0YLc+Icwk/De1HR8Vjk\nL7ub/wajmX/lRDrGRClczf3wdEjl1PJCR8s6Pzm9pj52PNk10VftEYhyj8kZMRqT\naaLgHJNiag7a8tiv45qPj9w=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-6vsr7@projetointegrador-7141d.iam.gserviceaccount.com",
    "client_id": "108262067636559201753",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6vsr7%40projetointegrador-7141d.iam.gserviceaccount.com"
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
