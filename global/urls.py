from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from .views import kakao_callback, KakaoLogin


schema_view = get_schema_view(
    openapi.Info(
        title="Infertility API 문서",
        default_version="v1",
    ),
    public=True,
    permission_classes=([AllowAny]),
)

urlpatterns = [
    re_path(
        "swagger(?P<format>.json|.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),

    path("kakao/callback/", kakao_callback, name="kakao_callback"),
    path(
        "kakao/login/finish/", KakaoLogin.as_view(), name="kakao_login_todjango"
    ),
]