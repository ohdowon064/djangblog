from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)

    # instangram/templates/instangram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })

import pandas as pd
from io import StringIO
from urllib.parse import quote
from django.http import HttpResponse

def response_csv(request):
    df = pd.DataFrame([
        [100, 110, 120],
        [200, 210, 220],
        [300, 310, 320]
    ])

    io = StringIO
    df.to_excel(io)
    io.seek(0) # 끝에 있는 파일 커서를 처음으로 이동

    encoded_filename = quote("pandas.xlsx") # quote는 %xx 이스케이프를 사용하여 string의 특수문자를 치환한다.
    response = HttpResponse(io, content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = "attachment; filename*=utf-8''{}".format(encoded_filename)
    # FileRsponse를 사용하면 header를 자동으로 달아준다.
    return response