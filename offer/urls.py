from django.urls import path, include
from .views import (
    OfferListView, OfferDetailView, OfferCreateView, OfferUpdateView,
    OfferDeleteView, StudentEnrollmentView, EnrolledStudentsListView,
    WaitingListView
)
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import OfferViewSet

router = DefaultRouter()
router.register('offers', OfferViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('offers/', OfferListView.as_view(), name='offer_list'),
    path('offers/<int:offer_id>/', OfferDetailView.as_view(), name='offer_detail'),
    path('offers/create/', OfferCreateView.as_view(), name='offer_create'),
    path('offers/update/<int:offer_id>/', OfferUpdateView.as_view(), name='offer_update'),
    path('offers/delete/<int:offer_id>/', OfferDeleteView.as_view(), name='offer_delete'),
    path('offers/enroll/<int:offer_id>/', StudentEnrollmentView.as_view(), name='student_enroll'),
    path('offers/enrolled-students/<int:offer_id>/', EnrolledStudentsListView.as_view(), name='enrolled_students_list'),
    path('offers/waiting-list/<int:offer_id>/', WaitingListView.as_view(), name='waiting_list'),
]
