from django.shortcuts import render
from django.http import HttpResponse
from .models import InviteCode, Match
from users.models import User

def generate_code(request):
    if request.method == 'POST':
        creator_id = request.POST['creator_id']
        try:
            creator = User.objects.get(id=creator_id)
            invite_code = InviteCode(creator=creator)
            invite_code.save()
            return HttpResponse(f"Generated code: {invite_code.code}")
        except User.DoesNotExist:
            return HttpResponse("Invalid user ID")
    return render(request, 'match/index.html')

def verify_code(request):
    if request.method == 'POST':
        input_code = request.POST['code']
        person_B_id = request.POST['person_B_id']
        try:
            person_B = User.objects.get(id=person_B_id)
            invite_code = InviteCode.objects.get(code=input_code)
            
            if invite_code.creator and person_B:
                if person_B.gender == 'female':
                    match = Match(female=person_B, male=invite_code.creator)
                else:
                    match = Match(female=invite_code.creator, male=person_B)
                match.save()
                return HttpResponse(f"{person_B.username}님은 {invite_code.creator.username}님과 연결되었습니다")
        except InviteCode.DoesNotExist:
            return HttpResponse("Invalid code")
        except User.DoesNotExist:
            return HttpResponse("Invalid user ID")
    return render(request, 'match/index.html')
