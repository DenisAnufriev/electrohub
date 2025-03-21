
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        # название нашей документации
        title="Electronics store API",
        # версия документации
        default_version="v1.0.0",
        # описание нашей документации
        description="Retail chain API description",
        terms_of_service="https://localhost/policies/terms/",
        license=openapi.License(name="Retail chain API License"),
    ),
    public=True,
    # в разрешениях можем сделать доступ только авторизованным пользователям.
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("electrohub.urls", namespace="electrohub")),
    path("users/", include("users.urls", namespace="users")),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
