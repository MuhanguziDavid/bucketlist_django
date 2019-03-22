from django.shortcuts import render
from django.views.generic import TemplateView

# view for indexpage
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# view for about me page
class AboutPageView(TemplateView):
    template_name = "about.html"
