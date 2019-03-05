import csv
import json
from datetime import datetime, date

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from agriculture import models, date_time_util
from django.forms.models import model_to_dict


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def index(request):
    weblist = models.WebInfo.objects.all()
    info = dict()
    for web in weblist:
        _id = web.id
        name = web.web_name
        url = web.web_url
        status = web.status
        info['name'+str(_id)] = name
        info['url'+str(_id)] = url
        info['status'+str(_id)] = status
    return render(request, 'index.html', info)


def web_edit(request):
    if request.method == 'GET':
        _id = request.GET.get('_id')
        info = models.WebInfo.objects.filter(id=_id).first()
        message = {"web_id": info.id, "web_name": info.web_name, "web_url": info.web_url, "status": info.status}
        return render(request, 'model/web_edit.html', message)


def edit_info(request):
    _id = request.POST.get('_id')
    web_name = request.POST.get('web_name')
    web_url = request.POST.get('web_url')
    safe = request.POST.get('status[safe]')
    leak = request.POST.get('status[leak]')
    danger = request.POST.get('status[danger]')
    offline = request.POST.get('status[offline]')
    online = request.POST.get('status[online]')

    status = ''
    if safe is not None:
        status += 'safe,'
    if leak is not None:
        status += 'leak,'
    if danger is not None:
        status += 'danger,'
    if offline is not None:
        status += 'offline,'
    if online is not None:
        status += 'online,'
    if status.endswith(','):
        status = status[:len(status)-1]
    models.WebInfo.objects.filter(id=_id).update(web_name=web_name, web_url=web_url, status=status)
    return HttpResponse('success')


def web_detail(request):
    _id = request.GET.get('_id')
    detail = models.WebDetail.objects.filter(web_id=_id).first()
    page_object = dict()
    if detail is not None:
        detail = model_to_dict(detail)
        page_object['web_id'] = detail.get('web_id')
        page_object['whois_info'] = json.loads(detail.get('whois_info'))
        page_object['ip_info'] = json.loads(detail.get('ip_info'))
        page_object['threat_info'] = json.loads(detail.get('threat_info'))
        page_object['leak_info'] = json.loads(detail.get('leak_info'))
        page_object['server_info'] = json.loads(detail.get('server_info'))
        page_object['network_info'] = json.loads(detail.get('network_info'))
    else:
        page_object['web_id'] = _id

    return render(request, 'model/detail.html', page_object)


def intel_list(request):
    return render(request, 'model/intelligence2.html')


def intelligence_record(request):
    page = request.GET.get("page")
    limit = request.GET.get('limit')
    page = int(page)
    limit = int(limit)
    _from = limit*(page-1)
    count = models.IntelligenceRecord.objects.count()
    record = models.IntelligenceRecord.objects.order_by('create_time')[_from:_from+limit]
    data_list = []
    for info in record.all():
        data_list.append(model_to_dict(info))
    response_data = dict()
    response_data['code'] = 0
    response_data['count'] = count
    response_data['data'] = data_list
    print(data_list)
    return HttpResponse(json.dumps(response_data, cls=CJsonEncoder), content_type="application/json")


def import_intel(request):
    _file = request.FILES.get("file", None)
    file_name = _file.name
    print(file_name)
    if file_name.find('csv') == -1:
        return HttpResponse(json.dumps({"message": "上传文本格式错误！"}), status=200)
    for chunk in _file.readlines():
        for row in csv.reader([str(chunk)]):
            times = date_time_util.get_date_format(date_time_util.date_str_to_timestamp(row[1], '%Y/%m/%d %H:%M'))
            models.IntelligenceRecord.objects.create(key=row[0].decode(), tag=row[2].decode(), create_time=times).save()
    message = {
        "code": 0,
        "message": "上传成功"
    }
    return HttpResponse(json.dumps(message), status=200)


def edit_web_detail(request):
    if request.method == 'POST':
        info = request.POST.get('info')
        _id = request.POST.get('_id')
        info_obj = json.loads(info)
        whois_info = info_obj.get('whois_info')
        ip_info = info_obj.get('ip_info')
        threat_info = info_obj.get('threat_info')
        leak_info = info_obj.get('leak_info')
        server_info = info_obj.get('server_info')
        network_info = info_obj.get('network_info')

        whois_info = json.dumps(whois_info)
        ip_info = json.dumps(ip_info)
        threat_info = json.dumps(threat_info)
        leak_info = json.dumps(leak_info)
        server_info = json.dumps(server_info)
        network_info = json.dumps(network_info)

        if models.WebDetail.objects.filter(web_id=_id).count() == 0:
            models.WebDetail.objects.create(web_id=_id, whois_info=whois_info, ip_info=ip_info, threat_info=threat_info,
                                            leak_info=leak_info, server_info=server_info, network_info=network_info).save()
        else:
            models.WebDetail.objects.filter(web_id=_id).update(whois_info=whois_info, ip_info=ip_info, threat_info=threat_info,
                                                               leak_info=leak_info, server_info=server_info, network_info=network_info)
        return HttpResponse('success')
    elif request.method == 'GET':
        _id = request.GET.get('_id')
        detail = models.WebDetail.objects.filter(web_id=_id).first()
        print(model_to_dict(detail))
        return render(request, 'model/detail.html', model_to_dict(detail))


def web_detail_edit_page(request):
    _id = request.GET.get('_id')
    return render(request, 'model/detail_edit.html', {"id": _id})


def article_page(request):
    keyword = request.GET.get('key')
    article_array = []
    if keyword is not None:
        article_list = models.ArticleRecord.objects.filter(Q(article_title__contains=keyword) | Q(content__contains=keyword)).all()[0:10]
        for article in article_list:
            article_array.append(model_to_dict(article))
    else:
        article_list = models.ArticleRecord.objects.all()[0:10]
        for article in article_list:
            article_array.append(model_to_dict(article))

    return render(request, 'article/article.html', {"article": article_array})


def article_import_page(request):
    return render(request, 'article/article_import.html')


def article_import(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title, content)
    models.ArticleRecord.objects.create(article_title=title, content=content, create_time=date_time_util.get_normal_date_format()).save()
    return HttpResponse('success')

