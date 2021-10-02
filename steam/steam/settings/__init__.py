import os
from django.core.exceptions import ImproperlyConfigured
# Error handler function for get env
def get_env_value(env_variable):
	try:
		return os.environ.get(env_variable)
	except KeyError:
		error_msg = f"Set the {env_variable} environment variable"
		raise ImproperlyConfigured(error_msg)