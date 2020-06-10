from django.http import JsonResponse

import logging
from rest_framework.views import APIView

from .service import rank_save_service,rank_list_service
# Create your views here.

logger = logging.getLogger(__name__)

class RankSave(APIView):
    '''
    客户端分数记录
    '''
    def post(self,request):
        code,msg = rank_save_service(request)
        return JsonResponse({'code':code,'msg':msg})


class RankList(APIView):
    '''
    客户端分数查询
    '''
    def get(self,request):
        code,msg = rank_list_service(request)
        return JsonResponse({'code':code,'msg':msg})
