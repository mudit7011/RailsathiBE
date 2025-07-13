from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item
import json

@csrf_exempt
def item_list(request):
    if request.method == 'GET':
        items = Item.objects.all()
        data = [{"id": item.id, "name": item.name, "description": item.description} for item in items]
        return JsonResponse(data, safe=False)


    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get("name")
            description = data.get("description")

            item = Item.objects.create(name=name, description=description)
            return JsonResponse({"id": item.id, "name": item.name, "description": item.description}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
