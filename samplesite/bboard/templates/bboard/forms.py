from django.forms import ModelForm
from django.views.generic.edit import CreateView

from bboard.models import Bb

class BbCreateView(CreateView):
    template_name = "bboard/create.html"
    form_class = BbForm
    success_ulr = "/bboard/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context

class BbForm(ModelForm):
    class Meta:
        model = Bb
        field = ("title", "content", "price", "rubric")







