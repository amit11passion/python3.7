from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('<html><head><title>Login page</title></head><body>'
                        ' <form>Username:<br><input type="text" name="username"><br>'
                        'Password:<br><input type="text" name="password">'
                        '<br><br><input type="submit"></form> </body></html>')
