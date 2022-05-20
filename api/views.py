import json
# from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data["title"] = model_data.title
#         data["content"] = model_data.content
#         data["price"] = model_data.price
#     return JsonResponse(data)

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data)
#     return JsonResponse(data)

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data)
#         print(data)
#         json_data_string = json.dumps(data)
#     return HttpResponse(json_data_string, headers={'Content-Type': 'application/json'})

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)