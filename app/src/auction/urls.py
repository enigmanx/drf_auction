from django.urls import path
from auction.views.lot_views import LotCreateView, LotDetailView, LotListView
from auction.views.profile_views import ProfileAdminDetailView, ProfileDetailView
from auction.views.bet_views import BetCreateView, BetUpdateView, BetListView, BetSelectView
from auction.views.creature_views import CreatureListView, CreatureCreateView, CreatureDetailView

urlpatterns = [
    path('balance/<int:pk>/', ProfileAdminDetailView.as_view()),
    path('balance/', ProfileDetailView.as_view()),

    path('creatures/', CreatureListView.as_view()),
    path('creature/create/', CreatureCreateView.as_view()),
    path('creature/detail/<int:pk>/', CreatureDetailView.as_view()),

    path('lots/', LotListView.as_view()),
    path('lot/create/', LotCreateView.as_view()),
    path('lot/detail/<int:pk>/', LotDetailView.as_view()),

    path('bets/', BetListView.as_view()),
    path('bet/create/', BetCreateView.as_view()),
    path('bet/update/<int:pk>/', BetUpdateView.as_view()),
    path('bet/select/<int:pk>', BetSelectView.as_view()),
]
