"""settings URL Configuration

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

from currency.views import (
    RateCreateView, RateDeleteView, RateDetailsView, RateListView, RateUpdateView, SourceCreateView, SourceDeleteView,
    SourceDetailsView, SourceListView, SourceUpdateView, ContactUsView

)

from django.urls import path

# from currency.views import generate_password
app_name = 'currency'
urlpatterns = [
    path('contactus/create', ContactUsView.as_view(), name='contact-us'),
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    # path('rate/details/<int:rate_id>/', rate_details),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    # path('source/details/<int:source_id>/', source_details),
    path('source/details/<int:pk>/', SourceDetailsView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    # path('response-codes', response_codes),
    # path('hello-world/', hello_world),

    # path('gen-pass/', generate_password)

]
