#!/usr/bin/python
# coding=utf-8
from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.template.base import TemplateDoesNotExist
from django.template.loader import get_template
from qrcode.main import QRCode, constants
import datetime


def index(_):
    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def app(_):
    return HttpResponse("Welcome to Baidu Cloud!\n")


def func(request, name):
    try:
        t = get_template(name)
    except TemplateDoesNotExist:
        raise Http404
        
    html = t.render(RequestContext(request))
    return HttpResponse(html)


def qrcode(request):
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    if 'p' in request.POST:
        qr.add_data(request.POST['p'])
    elif 'p' in request.GET:
        qr.add_data(request.GET['p'])
    else :
        return HttpResponse()
    qr.make(fit=True)
    response = HttpResponse()
    qr.make_image().save(response, "PNG")
    return response
