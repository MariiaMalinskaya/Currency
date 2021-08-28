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


from currency.views import contact_us, rate_list, response_codes, index


from django.contrib import admin
from django.urls import path

# from currency.views import generate_password

urlpatterns = [
    path('admin/', admin.site.urls),

    # currency
    path ('',index),
    path('contact-us/', contact_us),
    path('rate/list/',rate_list),
    path('response-codes',response_codes),
    # path('hello-world/', hello_world),

    # path('gen-pass/', generate_password)

]
