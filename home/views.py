from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.

def home(request):
	text = _("This is some random text")
	print(text)
	return render(request, 'common/index.html')
