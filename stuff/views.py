from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader


class SmallForm(forms.Form):
    value = forms.CharField(max_length=10)


def index(request):
    if request.method == 'POST':
        form = SmallForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/stuff/')
    else:
        form = SmallForm()

    template = loader.get_template('stuff/index.html')
    
    context = RequestContext(request, {
        'form': form,
    })
    
    return HttpResponse(template.render(context))
