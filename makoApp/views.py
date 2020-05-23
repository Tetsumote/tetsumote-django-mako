from django.shortcuts import render

from django.views.generic import TemplateView

class ClassBasedView(TemplateView):
    template_name = "home.mako"

    def get_context_data(self, **kwargs):
        context = super(ClassBasedView, self).get_context_data(**kwargs)
        context.update({
            'items': [
                'Wow',
                'This is awesome',
                'Don\'t forget to bring some bread honey ;)',
            ],
            'value': 1+1,
        })

        return context