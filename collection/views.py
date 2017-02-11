from django.shortcuts import render, redirect

from collection.forms import WorksheetForm
from collection.models import Worksheet

# Create your views here.
def index(request):
    worksheets = Worksheet.objects.all()


    return render(request, 'index.html', {
        'worksheets': worksheets,
    })

def worksheet_detail(request, slug):
    worksheet = Worksheet.objects.get(slug=slug)

    return render(request, 'worksheets/worksheet_detail.html', {
        'worksheet': worksheet,
    })

# add below your worksheet_detail view
def edit_worksheet(request, slug):
    # grab the object
    worksheet = Worksheet.objects.get(slug=slug)
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
