from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST, require_GET
import json


items = []


@require_GET
def index(request):
    search_query = request.GET.get("search", "")
    if search_query:
        filtered_items = [item for item in items if search_query.lower() in item["name"].lower()]
        return JsonResponse({"items": filtered_items}, status=200)
    return JsonResponse({"items": items}, status=200)


@csrf_exempt
@require_POST
def add_item(request):
    try:
        data = json.loads(request.body) if request.body else request.POST
        if "name" not in data or "price" not in data:
            return JsonResponse({"error": "Missing 'name' or 'price' field"}, status=400)
        
        new_item = {
            "id": len(items) + 1,
            "name": data["name"],
            "price": float(data["price"])
        }
        items.append(new_item)
        return JsonResponse({"message": "Item added successfully", "item": new_item}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)


@require_GET
def get_item(request, item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return JsonResponse({"item": item}, status=200)
    return JsonResponse({"error": "Item not found"}, status=404)


@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request, item_id):
    try:
        data = json.loads(request.body) if request.body else request.POST
        item = next((item for item in items if item["id"] == item_id), None)
        if not item:
            return JsonResponse({"error": "Item not found"}, status=404)
        
        item["name"] = data.get("name", item["name"])
        item["price"] = float(data.get("price", item["price"]))
        return JsonResponse({"message": "Item updated successfully", "item": item}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, item_id):
    global items
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return JsonResponse({"error": "Item not found"}, status=404)
    
    items = [item for item in items if item["id"] != item_id]
    return JsonResponse({"message": "Item deleted successfully"}, status=200)
