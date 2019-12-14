from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


from project.forms import CodeForm
from project.models import Code
from django.http import HttpResponse, HttpResponseRedirect



class Home(generic.CreateView):
    def get(self, request):
        return render(request, 'base.html')

class CodeListView(generic.ListView):
    """ Renders a list of all projects. """
    model = Code

    def get(self, request):
        """ GET a list of projects. """
        codes = self.get_queryset().all()
        return render(request, 'list.html', {
          'codes': codes
        })

class CodeDetailView(generic.DetailView):
    """ Renders a specific project based on it's slug."""
    model = Code

    def get(self, request, slug):
        """ Returns a specific projects project by slug. """
        code = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'code.html', {
          'code': code
        })
class CodeCreateView(generic.CreateView):
    form_class = CodeForm
    template_name = "new_code.html"

    def post(self, request, *args, **kwargs):
        form = CodeForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return HttpResponseRedirect(reverse_lazy("code-details-project", args=[project.slug]))

class CodeUpdateView(generic.UpdateView):
    model = Code
    fields = ['title','content']
    template_name = 'new_code.html'

class CodeDeleteView(generic.DeleteView):
    model = Code
    success_url = reverse_lazy('code-list-project')
    template_name = 'confirm_delete.html'
