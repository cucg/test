from .models import RankModel


class RankOperate(object):

    @classmethod
    def get_rank_first(cls,rank_name):
        return RankModel.objects.filter(rank_name=rank_name).first()

    @classmethod
    def rank_update(cls,rank_obj,rank_name,rank_score):
        rank_obj.update(rank_name=rank_name,rank_score=rank_score)

    @classmethod
    def rank_create(cls,rank_name,rank_score):
        RankModel.objects.create(rank_name=rank_name,rank_score=rank_score).save()
    
    @classmethod
    def get_rank_all(cls,score_start=None,score_end=None):
        rank_obj = RankModel.objects.order_by('-rank_score').all()
        if score_start and score_end:
            return rank_obj[score_start-1:score_end]
        return rank_obj

    @classmethod
    def get_current_rank(cls,rank_name):
        return RankModel.objects.filter(rank_name=rank_name).first()
    
