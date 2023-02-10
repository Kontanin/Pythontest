"""  URL mapping for the """

from django.urls import path
# from user import views
from .views import CreateUserView
from .serializers import UserSerializer

app_name='user'

urlpatterns =[

    path('create/',views.CreateUserView.as_view(),name='create'),
    path('token/',views.CreateUserView.as_view(),name='token'),
    path('me/',views.ManageMeView.as_view,name='me')
]