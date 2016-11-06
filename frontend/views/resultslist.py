from finder.models import Result
from django.views.generic import ListView


class ResultsListView(ListView):
    model = Result
    template_name = 'list.html'
    context_object_name = 'results_list'
    paginate_by = 10
    ordering = '-created'

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            return Result.objects.filter(title__search=search)
        else:
            return Result.objects.all()
