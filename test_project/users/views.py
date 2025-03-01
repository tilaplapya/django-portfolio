from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

# Create your views here.
@require_GET
def index(request):
    data = {
        "title": "Users",
        "count": 120
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

@require_POST
@csrf_exempt

def create_user(request):
    payload = request.POST
    data = {
        "name": payload.get("name")
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

def get_users(request, id):

    # query param users/2?user=[name]
    payload = request.GET

    data = {
        "id": id,
        "context": payload
    }
    return JsonResponse({"message": "success", "payload": {"id": id}}, status=200)