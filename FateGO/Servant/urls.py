"""webSite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Use include() to add paths from the catalog application
from django.urls import path
from Servant import views

urlpatterns = [
    path('', views.Servant, name='servant'),
    path('a', views.current_datetime, name='current_datetime'),
    path('<int:collectionNo>', views.informationCharacter, name='informationCharacter'),
]

