from django.shortcuts import render
from django.http import JsonResponse
from .recommend import BloomRecommend


def recommend_view(request):
    latitude = request.GET.get("latitude")
    longitude = request.GET.get("longitude")

    if not latitude or not longitude:
        return JsonResponse({"error": "위도와 경도를 제공해주세요."}, status=400)

    bloom_recommend = BloomRecommend()
    recommendations = bloom_recommend.get_recommendation(latitude, longitude)

    return JsonResponse({"recommendations": recommendations})
