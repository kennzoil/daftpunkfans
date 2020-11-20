from django.shortcuts import render


def render_index(request):
    return render(request, 'index.html', {})


def render_butts(request):
    return render(request, 'butts.html', {'name': 'Buttman'})


def render_discovery(request):
    if request.method == 'POST' and 'run_script' in request.POST:

        return render(request, 'name_favorite.html', {})

    else:
        return render(request, 'discovery.html')
