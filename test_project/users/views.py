from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    data = {
        "title": "Users",
        "count": 150
    }
    return JsonResponse({"message": "success", "payload": data}, status=200)

@csrf_exempt

def get_users(request, id):

    # query param users/2?user=[name]
    payload = request.GET

    data = {
        "id": id,
        "context": payload
    }
    return JsonResponse({"message": "success", "payload": {"id": id}}, status=200)