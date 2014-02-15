from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.conf import settings


class SmallForm(forms.Form):
    value = forms.CharField(max_length=10)


def index(request):
    if request.method == 'POST':
        form = SmallForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            request.session['value'] = value

            return HttpResponseRedirect('/stuff/')
    else:
        form = SmallForm()

    request.session['sessionid'] = request.session.session_key

    template = loader.get_template('stuff/index.html')

    context = RequestContext(request, {
        'form': form,
    })

    return HttpResponse(template.render(context))