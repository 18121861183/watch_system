import json

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from agriculture import models


def index(request):
    models.WebInfo.objects.all()
    return render(request, 'index.html')


def web_edit(request):
    _id = request.GET.get('_id')
    info = models.WebInfo.objects.filter(id=_id).first()
    return render(request, 'model/web_edit.html', info)


def web_detail(request):
    _id = request.GET.get('_id')
    detail = models.WebDetail.objects.filter(web_id=_id).first()
    return render(request, 'model/detail.html', detail)


def intel_list(request):
    return render(request, 'model/intelligence.html')


def intelligence_record(request):
    page = request.GET.get("page")
    limit = request.GET.get('limit')
    count = models.IntelligenceRecord.objects.count()
    record = models.IntelligenceRecord.objects.order_by('create_time')[int(page):int(page)+int(limit)]
    print(count, record)
    response_data = dict()
    response_data['code'] = 0
    response_data['count'] = count
    response_data['data'] = []
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def import_intel(request):
    _file = request.FILES['file']
    for chunk in _file.chunks():
        print(chunk)


def edit_web_detail(request):
    if request.method == 'POST':
        whois = request.data['whois']
    elif request.method == 'GET':
        _id = request.GET.get('_id')
        detail = models.WebDetail.objects.filter(web_id=_id).first()
        return render(request, 'model/detail.html', detail)
