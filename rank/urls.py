from django.urls import path,re_path
from rank import views
app_name = 'rank'
urlpatterns = [
    path('v1/rank_record/',views.RankSave.as_view()),
    path('v1/rank_list/',views.RankList.as_view()),
]