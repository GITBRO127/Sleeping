from django.shortcuts import render
def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)

# Create your views here.
