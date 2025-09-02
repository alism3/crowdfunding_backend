from django.urls import path
from . import views

urlpatterns = [
  path('fundraisers/', views.FundraiserList.as_view()),
  path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),
  path('pledges/', views.PledgeList.as_view()),
  path('pledges/<int:pk>/', views.PledgeDetail.as_view())
  ] #Now my new view can be accessed by adding fundraisers/ to the end of our back-end's address
