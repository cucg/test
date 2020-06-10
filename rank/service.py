import logging
from django.db import transaction

from .models import RankModel
from .operate import RankOperate
from .serializer import RankSerializer

logger = logging.getLogger(__name__)


def rank_save_service(request):
    try:
        with transaction.atomic():
            rank_name = request.data.get('rank_name')
            rank_score = request.data.get('rank_score')
            # 先判断用户输入是否完整
            if not all ([rank_name,rank_score]):
                msg = '参数不全'
                code = 40101
                logger.info('errcode：{0},errmsg: {1}'.format(code,msg))
            elif int(rank_score) < 1 or int(rank_score) > 10000000:
                msg = '分数超出统计范围'
                code = 40102
                logger.info('errcode：{0},errmsg: {1}'.format(code,msg))
            else:
                rank_obj = RankOperate.get_rank_first(rank_name)
                code = 200
                if rank_obj:
                    '''数据存在则更新'''
                    rank_obj.update(rank_obj=rank_obj,rank_name=rank_name,rank_score=rank_score)
                    msg = '数据更新成功'
                else:
                    '''数据不存在则添加'''
                    RankOperate.rank_create(rank_name=rank_name,rank_score=rank_score)
                    msg = '数据添加成功'
            return code,msg
    except Exception as e:
        logger.error('添加客户端排名失败{}'.format(str(e)))
        return 40601, '添加客户端排名失败{}'.format(str(e))


def rank_list_service(request):
    try:
        rank_name = request.data.get('rank_name')
        score_start = request.data.get('score_start')
        score_end = request.data.get('score_end')
        code = 200
        if not rank_name:
            msg = '查询客户端排名失败:参数不全'
            logger.info('errcode：{0},errmsg: {1}'.format(code,msg))
            return 40101,msg
        if score_start and score_end:
            '''分数范围查询'''
            if score_start > score_end:
                score_start,score_end = score_end,score_start
            rank_obj = RankOperate.get_rank_all(score_start=int(score_start),score_end=int(score_end))
        else:
            '''没有指定查询范围'''
            rank_obj = RankOperate.get_rank_all()
        rank_list = RankSerializer(rank_obj,many=True).data
        rank_current_obj = RankOperate.get_current_rank(rank_name=rank_name)
        rank_current = RankSerializer(rank_current_obj).data
        msg = {
            'rank_list':rank_list,
            'rank_current':rank_current
        }
        return code,msg
    except Exception as e:
        logger.error('查询客户端排名失败{}'.format(str(e)))
        return 40101, '查询客户端排名失败{}'.format(str(e))