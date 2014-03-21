DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# 'username' | 'email' | 'username_email'
ACCOUNT_AUTHENTICATION_METHOD='email'

# The URL to redirect to after a successful e-mail confirmation, in case no
# user is logged in. Default value is settings.LOGIN_URL.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL='webbify.in/?msg=login'

# The URL to redirect to after a successful e-mail confirmation, in case of
# an authenticated user. Default is settings.LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL='webbify.in'

# Determines the expiration date of email confirmation mails (# of days).
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 10000

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = False

# Subject-line prefix to use for email messages sent. By default, the name
# of the current Site (django.contrib.sites) is used.
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Site] '

SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
# A string pointing to a custom form class (e.g. 'myapp.forms.SignupForm')
# that is used during signup to ask the user for additional input
# (e.g. newsletter signup, birth date). This class should implement a
# 'save' method, accepting the newly signed up user as its only parameter.
# ACCOUNT_SIGNUP_FORM_CLASS = None

# When signing up, let the user type in his password twice to avoid typ-o's.
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# Dictionary containing provider specific settings.
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email',],
        'METHOD': 'oauth2'
        #'LOCALE_FUNC': lambda request: return 'zh_CN'
    },
    'google' : {
        'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    }
}

#########################
# DATABASE SETTINGS
#########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'your2048',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'master',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
    }
}

#####################
# LOCAL SETUP
#####################

SITE_DOMAIN = 'localhost:8000'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'