from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging


@csrf_exempt
def index(request):
    if request.method =='POST':
        # print('error')
        response = request.headers['x-GitHub-Event']
        # text= {
        #     'event' : response.x-GitHub-Event
        # }
        logger = logging.getLogger(__name__)
        logger.error(response)
        return HttpResponse('hi') 
