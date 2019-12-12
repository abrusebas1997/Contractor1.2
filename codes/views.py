from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy


from codes.forms import CodeForm
from codes.models import Code
from django.http import HttpResponse, HttpResponseRedirect


class CodesListView(ListView):
    """ Renders a list of all Codes. """
    model = Code

    def get(self, request):
        """ GET a list of Codes. """
        Codes = self.get_queryset().all()
        return render(request, 'list.html', {
          'Codes': Codes
        })

class CodesDetailView(DetailView):
    """ Renders a specific Code based on it's slug."""
    model = Code

    def get(self, request, slug):
        """ Returns a specific codes Code by slug. """
        Code = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'Code.html', {
          'Code': Code
        })
class CodesCreateView(CreateView):
    form_class = CodeForm
    template_name = "new_Code.html"

    def post(self, request, *args, **kwargs):
        form = CodeForm(request.POST)
        if form.is_valid():
            codes = form.save()
            codes.save()
            return HttpResponseRedirect(reverse_lazy("codes-list-Code", args=[codes.slug]))
