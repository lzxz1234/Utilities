#!/usr/bin/python
# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template


class SetRemoteAddrFromForwardedFor(object):
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META :
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip


def ip(request):
    ip = request.META.get("REMOTE_ADDR", None)
    if 'web' in request.GET:
        t = get_template('ip.html')
        ip = t.render(Context({'ip': ip}))
    
    return HttpResponse(ip + '\r\n')


def meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response("meta.html", locals())
