"""
URL configuration for jantaWifiTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from aiEngineerTask.views import home, line_chart, chart_with_dropdown, other_visualization

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('line-chart/', line_chart, name='line_chart'),
    path('chart-with-dropdown/', chart_with_dropdown, name='chart_with_dropdown'),
    path('other-visualization/', other_visualization, name='other_visualization'),
]
