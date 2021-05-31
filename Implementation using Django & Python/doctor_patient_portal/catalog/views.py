from django.shortcuts import render

# Create your views here.

from catalog.models import AccountInfo

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_accounts = AccountInfo.objects.all().count()

    context = {
        'num_accounts': num_accounts,
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)

from django.views import generic

class SignUp(generic.ListView):
    model = AccountInfo;