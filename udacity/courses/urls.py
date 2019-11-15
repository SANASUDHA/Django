from django.urls import path
from .views import DummyListView, DummyDetailView, DummyCreateView, DummyUpdateView, DummyDeleteView

#<app>/<model>_<typeview>.html
urlpatterns = [
		path("",DummyListView.as_view(),name='dummy-list'),
		path("detail/<int:pk>",DummyDetailView.as_view(), name='dummy-detail'),
		path("detail/new",DummyCreateView.as_view(), name='create-detail'),
		path("detail/update/<int:pk>",DummyUpdateView.as_view(), name ='update-detail'),
		path("detail/delete/<int:pk>",DummyDeleteView.as_view(), name='delete-detail')
]