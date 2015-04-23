from django.conf.urls import patterns, url, include
from django.contrib import admin

from django_auth_policy.forms import (StrictAuthenticationForm,
                                      StrictPasswordChangeForm)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'testsite.views.login', name='login',
        kwargs={'authentication_form': StrictAuthenticationForm,
                'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        name='password_change',
        kwargs={'password_change_form': StrictPasswordChangeForm,
                'template_name': 'change_password.html',
                'post_change_redirect': '/',
                }),
    url(r'^$', 'testsite.views.login_required_view', name='login_required_view'),
    url(r'^another/$', 'testsite.views.another_view', name='another_view'),
)
