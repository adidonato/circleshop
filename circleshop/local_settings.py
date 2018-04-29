from . import credentials 
# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = credentials.site['SECRET_KEY'] 
NEVERCACHE_KEY = credentials.site['NEVERCACHE_KEY'] 

DATABASES = {
   "default": {
       # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
       "ENGINE": "django.db.backends.postgresql_psycopg2",
       # DB name or path to database file if using sqlite3.
       "NAME": credentials.db['NAME'],
       # Not used with sqlite3.
       "USER": credentials.db['USER'],
       # Not used with sqlite3.
       "PASSWORD": credentials.db['PASSWORD'],
       # Set to empty string for localhost. Not used with sqlite3.
       "HOST": credentials.db['HOST'],
       # Set to empty string for default. Not used with sqlite3.
       "PORT": "",
   }
}





# DATABASES = {
#     "default": {
#     # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
#     "ENGINE": "django.db.backends.sqlite3",
#     # DB name or path to database file if using sqlite3.
#     # "NAME": "flute",
#     "NAME": "",
#     # Not used with sqlite3.
#     "USER": "adidonato", # Use your actual username.
#     # Not used with sqlite3.
#     "PASSWORD": "yoyoyo", # Use your actual password.
#     # Set to empty string for localhost. Not used with sqlite3.
#     "HOST": "localhost", # I have found that placing "localhost" here is required in some cases.
#     # Set to empty string for default. Not used with sqlite3.
#     "PORT": "5432",
#     # See below.
#     }
# }

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True 
EMAIL_PORT = 587 
EMAIL_HOST_USER = credentials.email['USER']
EMAIL_HOST = credentials.email['HOST'] 
EMAIL_HOST_PASSWORD = credentials.email['PASSWORD']

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
# ALLOWED_HOSTS = [""]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }
