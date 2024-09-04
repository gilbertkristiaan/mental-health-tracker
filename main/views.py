from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306274951',
        'name': 'Gilbert Kristian',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)