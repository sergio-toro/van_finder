from finder.models import Result
from django.views.generic import ListView
from django.http import JsonResponse


class ResultsListView(ListView):
    model = Result
    template_name = 'list.html'
    context_object_name = 'results_list'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            queryset = Result.objects.filter(title__search=search)
        else:
            queryset = Result.objects.all()

        queryset = queryset.order_by('viewed', '-created', 'pk')

        return queryset

    def post(self, request):
        result_id = request.POST.get('id', None)
        action = request.POST.get('action', None)
        if not result_id or not action:
            return JsonResponse({"success": False})

        result = Result.objects.get(pk=result_id)
        if not result:
            return JsonResponse({"success": False})

        if action == 'viewed':
            result.viewed = not result.viewed
            result.save()

        response = {
            "success": True,
            "result": {
                "id": result.id,
                "viewed": result.viewed,
            },
        }
        return JsonResponse(response)
