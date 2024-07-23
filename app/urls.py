from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from .utils import AppEnvironment
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Infertility API 문서",
        default_version="v1",
    ),
    public=True,
    permission_classes=([AllowAny]),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/match/", include("match.urls")),
    path("api/question/", include("question.urls")),
    path("answers/", include("answer.urls")),
]

env: str = AppEnvironment.run_env()
if env == "dev":
    urlpatterns += [
        re_path(
            r"swagger(?P<format>.json|.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
