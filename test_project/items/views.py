from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_GET
def index(request):
    data = {
        "item_name": "mouse",
        "price": 120
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

def get_itemsparam(request):

    # query param users/2?user=[name]
    payload = request.GET

    data = {
        "context": payload,
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)







@require_POST
@csrf_exempt

def add_item(request, id):
    payload = request.GET
    data = {
        "id": id,
        "context": payload,
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

@require_GET
def get_items(request, id):
    payload = request.GET
    data = {
        "id": 10,
        "item_name": "mouse",
        "price": 120,
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

@require_http_methods(["PUT"])
@csrf_exempt
def update_item(request, id):
    payload = request.GET
    data = {
        "id": 10,
        "item_name": "mouse",
        "price": 120,
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_item(request, id):
    payload = request.GET
    data = {
        "id": 10,
        "item_name": "mouse",
        "price": 120,
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

