from settings import *

DEBUG = True
TEMPLATE_DEBUG = True

LOCAL_INSTALLED_APPS = ('debug_toolbar', 'django_extensions', 'django_coverage', 'django_nose')
INSTALLED_APPS += LOCAL_INSTALLED_APPS

SOUTH_TESTS_MIGRATE = False
SOUTH_DATABASE_ADAPTER='south.db.psycopg2'
SKIP_SOUTH_TESTS = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'badsanta.db'),
        'USER': '', 
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = '76t)b6$z*$^wfgcnti5ce8_m@6a=l*o)w4=$68rb!3+v#fopw8'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Debug toolbar configuration
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
    }


INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

LOGGING['handlers']['default'] = {
    'level': 'DEBUG',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': os.path.join(PROJECT_DIR, '../../' 'logs', 'badsanta.log'),
    'maxBytes': 1024 * 1024 * 10,
    'backupCount': 50,
    'formatter': 'standard',
}

LOGGING['formatters'] = LOGGING.get('formatters') or {}
LOGGING['formatters']['standard'] = {
    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
}
