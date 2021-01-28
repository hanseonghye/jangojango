from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# IsAuthenticated - 로그인 여부 확인
# JSONWebTokenAuthentication - JWT 인증을 확인하기 위해 사용
# permission_classes((IsAuthenticated,)) - 권한을 체크함. 여기서는 로그인했는지만 체크
# @authentication_classes((JSONWebTokenAuthentication,)) - JWT 토큰을 확인함 토큰에 이상이 있으면 에러 리턴

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def example(request):
    print ("aaaaaaa")
    return HttpResponse(None, content_type="text/json-comment-filtered")