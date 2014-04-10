from django.shortcuts import render
from django.http import HttpResponseRedirect
from gindex.gindex_logic.gindex import ProjectRepositoryService
from gindex.gindex_logic.gindex import GIndex
from gindex.gindex_logic.gindex_conectors import GithubConnector
from gindex.forms import RepositoryRequestForm


# Create your views here.

def gindex_for(user, repo):
    service = ProjectRepositoryService(GithubConnector())
    project = service.find(user, repo)
    gindex_calc = GIndex()
    gindex = gindex_calc.calculate(project)
    return gindex


def repository_form(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RepositoryRequestForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            gindex = gindex_for(form.cleaned_data['user'],
                                form.cleaned_data['repository_name'])
            return render(request, 'gindex.html', {'user': form.cleaned_data['user'],
                                                   'repo_name': form.cleaned_data['repository_name'],
                                                   'gindex': gindex})
    else:
        form = RepositoryRequestForm() # An unbound form

    return render(request, 'repo_form.html', {
        'form': form,
    })