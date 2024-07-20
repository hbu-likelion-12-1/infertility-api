from enum import Enum


# 난임 진단 시기
class InferPeriod(Enum):
    LESS_THAN_6 = "LESS_THAN_6"
    BETWEEN_6_12 = "BETWEEN_6_12"
    BETWEEN_12_24 = "BETWEEN_12_24"
    MORE_2 = "MORE_2"


# 난임 치료 상황
class InferCareStatus(Enum):
    INSPECT = "INSPECT"
    OVULATION = "OVULATION"
    ARTIFICIAL = "ARTIFICIAL"
    IN_VITRO = "IN_VITRO"
    SUSPEND = "SUSPEND"


# 난임의 주된 원인
class InferCause(Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    BIDIRECT = "BIDIRECT"
    UNKNOWN = "UNKNOWN"


# 난임 치료로 인한 경제적 부담 정도
class InferCost(Enum):
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
    LOW = "LOW"
    SUPER_LOW = "SUPER_LOW"


# 가족, 주변으로부터 지지 정도
class InferSupport(Enum):
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
    LOW = "LOW"
    SUPER_LOW = "SUPER_LOW"


# 직장 내 난임 이해도
class WorkplaceComprehension(Enum):
    VERY_HIGH = "VERY_HIGH"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
    LOW = "LOW"
    SUPER_LOW = "SUPER_LOW"
    NEVERMIND = "NEVERMIND"


# 부부 간 난임 의사소통
class InferCommunication(Enum):
    EVERYDAY = "EVERYDAY"
    WEEK_2_3 = "WEEK_2_3"
    WEEK_ONE = "WEEK_ONE"
    MONTH = "MONTH"
    NEVERMIND = "NEVERMIND"


# 감정 상태
class Emotion(Enum):
    NICE = "NICE"
    GOOD = "GOOD"
    NORMAL = "NORMAL"
    BAD = "BAD"
    WORST = "WORST"
