from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('banking.urls', namespace='banking'))
]

admin.site.site_header = "Libano Admin"
admin.site.site_title = "Libano Admin Portal"
admin.site.index_title = "Welcome to Libano Admin Panel"