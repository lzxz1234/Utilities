#!/usr/bin/python
# coding=utf-8
import time
import itertools
import requests
from settings import QINIU
from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template.loader import get_template
from qiniu import Auth, put_data


key_seq = itertools.count(start=int(time.time()), step=1)
q = Auth(QINIU['access_key'], QINIU['secret_key'])


def index(_):
    return HttpResponseRedirect('/func/share.html')


def save(request):
    key = short_int(key_seq.next())
    content = request.POST.get('content') or request.GET.get('content')
    token = q.upload_token(QINIU['bucket'], key, 60)
    put_data(token, key, content)
    return HttpResponseRedirect('/t/' + key)


def preview(_, key):
    t = get_template("preview.html")
    base_url = 'http://%s/%s' % (QINIU['domain'], key)
    private_url = q.private_download_url(base_url)
    r = requests.get(private_url)
    if r.status_code == 200:
        html = t.render(Context({'content': r.text, 'key': key}))
        return HttpResponse(html)
    else:
        raise Http404


def short_int(num):
    result = []
    symbol = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    symbol.extend([chr(x) for x in range(ord('A'), ord('Z') + 1)])
    symbol.extend([str(x) for x in range(10)])
    while True:
        if num == 0: break
        num, rem = divmod(num, len(symbol))
        result.append(symbol[rem])
    return ''.join([str(x) for x in result[::-1]])