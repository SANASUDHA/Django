from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def resdy(self):
    	import users.signals
