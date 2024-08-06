import os
from .gpt import BloomAI  # BloomAI 클래스가 정의된 모듈
from dotenv import load_dotenv
import requests

load_dotenv()

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

class BloomRecommend:
    recommend_template = """
    이곳에서는 대한민국 행정구역의 자치구, 자치시, 군 이 세 가지를 묶어서 지역이라고 명한다.
    현재 사용자의 위도와 경도를 파악해서 사용자가 어떤 지역에 있는지 파악한다.
    파악했으면 영화관, 체육시설, 캠핑장, 공방, 공원 이 다섯 개의 활동 중 한 개의 활동을 랜덤으로 정해서 사용자가 위치한 지역과 동일한 지역에 위치한 활동을 7개 뽑는다.
    활동의 이름, 장소, 대표 사진을 반환해야 한다.
    """

    def __init__(self):
        self.bloom_ai = BloomAI()

    def get_region_name(self, latitude, longitude):
        url = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
        params = {
            'coords': f'{longitude},{latitude}',
            'output': 'json',
            'orders': 'legalcode, admcode',
        }
        headers = {
            'X-NCP-APIGW-API-KEY-ID': NAVER_CLIENT_ID,
            'X-NCP-APIGW-API-KEY': NAVER_CLIENT_SECRET,
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('results'):
                region_info = data['results'][0]['region']
                region_name = f"{region_info['area1']['name']} {region_info['area2']['name']} {region_info['area3']['name']}"
                return region_name
        
        return None

    def recommend_activity(self, latitude, longitude):
        region_name = self.get_region_name(latitude, longitude)
        if not region_name:
            return "지역 정보를 가져올 수 없습니다"

        query = f"현재 사용자는 {region_name}에 있습니다. 활동을 추천해 주세요"
        recommendation = self.bloom_ai.query(query)

        return recommendation
