from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Provider
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

# Create your views here.

@csrf_exempt
def provider_list(request):
    if request.method == 'POST':
        request_json = json.loads(request.body)
        print(request_json)
        query = Q()
        if 'active' in request_json:
            active = True if request_json['active'] == True or str(request_json['active']).lower() == 'true' else False
            query &= Q(active=active)
        if 'skills' in request_json:
            providers = Q(primary_skills__iin=[x.lower() for x in request_json['skills']])
        if 'name' in request_json:
            name = request_json['name']
            query &= Q(first_name__icontains=name) | Q(last_name__icontains=name)
        if 'language' in request_json:
            language = request_json['language']
            query &= Q(language__icontains=language)
        providers = Provider.objects.filter(query)
        return JsonResponse({"data": list(increase_views(providers).values())}, safe=False)
    else:
        providers = Provider.objects.all().values()
        return JsonResponse({"data": list(providers.values())}, safe=False)

def increase_views(providers):
    for pvdr in providers:
        pvdr.views += 1
        pvdr.save()
    return providers