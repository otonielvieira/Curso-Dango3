from django.http import HttpResponse

def home(request):
    html ='''<html>
    <h1>First Django Project</h1>
    <br>
    <h2>Exploring the Power od Python With Django!!</h2>
    <br>
    <h3>This Project is only .....</h3>
    </html>'''
    return HttpResponse(html)