"""zhangyanweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.views.generic.edit import FormView
from django.conf.urls import include
from mysite.form import BlogForm

app_name = "mysite"
urlpatterns = [
    url(r'^$',views.CoverView.as_view(),name = 'cover' ),
    url(r'index/$',views.IndexView.as_view(),name = 'index'),
    url(r'profile/$',views.ProfileView.as_view(),name = 'profile'),
    url(r'notebook/$',views.NotebookView.as_view(),name = 'notebook'),
    url(r'notebook/(?P<id>\d+)/$',views.NotebookDetail,name='notebook_detail'),
    url(r'project/$',views.ProjectView.as_view(),name = 'project'),
    url(r'notebook/create/$', FormView.as_view(template_name="mysite/notebook_form.html",form_class=BlogForm)),
]
