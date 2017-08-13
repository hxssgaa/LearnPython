from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.archive, name='archive'),
    url(r'^create/', views.create_blogpost, name='create_blogpost'),
    # url(r'foo/', views.foo, name='foo'),
    # url(r'bar/', views.bar, name='bar'),
]