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

import requests
from django.http import HttpResponse
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def response_pillow_image(request):
    ttf_path = "/Library/Fonts/Arial Unicode.ttf"

    # 이미지 파일 다운로드 혹은 로컬 디스크 상의 이미지 직접 열기
    image_url = "http://www.flowermeaning.com/flower-pics/calla-Lily-Meaning.jpg"
    res = requests.get(image_url) # 서버로 HTTP get 요청하여 응답 획득
    io = BytesIO(res.content) # 응답의 Raw Body 메모리 파일객체 BytesIO 인스턴스 생성
    io.seek(0) # 파일의 처음으로 커서 이동

    canvas = Image.open(io).convert("RGBA") # 이미지 파일을 열고, RGBA 모드로 변환
    font = ImageFont.truetype(ttf_path, 40) # 지정 경로의 TrueType 폰트, 폰트크기 40
    draw = ImageDraw.Draw(canvas) # canvas에 대한 ImageDraw 객체 획득

    text = "Ask Company"
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin
    draw.rectangle((left, top, right, bottom), (255, 255, 244))
    draw.text((15, 15), text, font=font, fill=(20, 20, 20))

    response = HttpResponse
    canvas.save(response, format="PNG") # HttpResponse의 file-like 특성(=> write할 수 있음) 활용
    # response.write 할 수 있는 특성, 파일류의 인터페이스 지원
    return response
