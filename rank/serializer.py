from rest_framework import serializers
from .models import RankModel


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankModel
        fields=(
            'rank_name',
            'rank_score'
        )