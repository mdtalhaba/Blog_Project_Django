from django.urls import path
from posts.views import add_post, edit_post, delete_post, AddPostCreateView, EditPostView, DeletePostView, DetailsPostView

urlpatterns = [
    # path('add/', add_post, name='add_post'),
    path('add/', AddPostCreateView.as_view(), name='add_post'),
    # path('edit/<int:id>', edit_post, name='edit_post'),
    path('edit/<int:id>/', EditPostView.as_view(), name='edit_post'),
    # path('delete/<int:id>', delete_post, name='delete_post'),
    path('delete/<int:id>/', DeletePostView.as_view(), name='delete_post'),
    path('details/<int:id>/', DetailsPostView.as_view(), name='details_post'),
]
