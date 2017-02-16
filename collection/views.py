from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from collection.forms import WorksheetForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from collection.models import Worksheet

# Create your views here.
def index(request):
    worksheets = Worksheet.objects.all()


    return render(request, 'index.html', {
        'worksheets': worksheets,
    })

def worksheet_detail(request, slug):
    worksheet = Worksheet.objects.get(slug=slug)
    entries = worksheet.entries.all()
    return render(request, 'worksheets/worksheet_detail.html', {
        'worksheet': worksheet,
        'entries': entries,
    })

# add below your worksheet_detail view
@login_required
def edit_worksheet(request, slug):
    # grab the object
    worksheet = Worksheet.objects.get(slug=slug)

    # make sure the logged in user is the owner of the worksheet
    if worksheet.user != request.user:
        raise Http404

    # set the form we're using
    form_class = WorksheetForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=worksheet)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('worksheet_detail', slug=worksheet.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=worksheet)

    # and render the template
    return render(request, 'worksheets/edit_worksheet.html', {
        'worksheet': worksheet,
        'form': form,
    })

def create_worksheet(request):
    form_class = WorksheetForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            worksheet = form.save(commit=False)

            # set the additional details
            worksheet.user = request.user
            worksheet.slug = slugify(worksheet.name)

            # save the object
            worksheet.save()

            # redirect to our newly created worksheet
            return redirect('worksheet_detail', slug=worksheet.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'worksheets/create_worksheet.html', {
        'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        worksheets = Worksheet.objects.filter(name__istartwith=initial)
        worksheets = worksheets.order_by('name')
    else:
        worksheets = Worksheet.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'worksheets': worksheets,
        'initial': initial,
    })
