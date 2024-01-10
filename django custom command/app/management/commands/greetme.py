from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'this class greet the user'

    def add_arguments(self,parser):
        parser.add_argument('name')
        parser.add_argument('role',nargs='?',default='')

    def handle(self,*args,**kwargs):
        name = kwargs.get('name')
        role = kwargs.get('role')

        if role == 'admin':
            self.stdout.write(self.style.WARNING(f'Hello! {name} Your Special Person You Have All Permission'))
            self.stdout.write(self.style.SUCCESS('Your Most Welcome'))
        else :
            self.stdout.write(self.style.SUCCESS(f"Hello! {name} Your Welcome To Our Project"))