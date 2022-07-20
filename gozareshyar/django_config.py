import django
from django.conf import settings
from consts import Environmnets


def get_django_config(env):
    if env == Environmnets.PRODUCTION:
        return {'DATABASES':{
            'default': {
                'ENGINE': 'django.db.backends.mysql', 
                'NAME': 'far_db',
                'OPTIONS': {'charset': 'utf8mb4'},
                'USER': 'root',
                'PASSWORD': 'v8+eZ{qhkE/b',
                'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
                'PORT': '3306',
                'CONN_MAX_AGE': 3600,
                }
            },
            'INSTALLED_APPS': [
                
                'far.students',
                'far.store',
                'far.contests',
                'far.tel_files',
            ],

            'TIME_ZONE': 'Asia/Tehran',

            'USE_I18N': True,

            'USE_L10N': True,

            'USE_TZ': True,

        }

    else:
        return {'DATABASES':{
            'default': {
                'ENGINE': 'django.db.backends.mysql', 
                'NAME': 'far_db',
                'OPTIONS': {'charset': 'utf8mb4'},
                'USER': 'root',
                'PASSWORD': '54185418',
                'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
                'PORT': '3306',
                'CONN_MAX_AGE': 3600,
                }
            },
            'INSTALLED_APPS': [
                
                'far.students',
                'far.store',
                'far.contests',
                'far.tel_files',
                
            ],

            'TIME_ZONE': 'Asia/Tehran',

            'USE_I18N': True,

            'USE_L10N': True,

            'USE_TZ': True,


        }