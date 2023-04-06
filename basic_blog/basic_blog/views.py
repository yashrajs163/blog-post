from django.http import HttpResponse

def home(request):
    return HttpResponse('''<h1> This is a homepage </h1> <br>
    <h2> Hello everyone !! </h2>  <p> how is everythin going..!! </p>''')

    


