
from rest_framework.response import Response
from rest_framework.decorators import api_view

from cui_sahiwal.models import Lecutues
from cui_sahiwal.serializer import LectureSerializer

import pandas as pd
# Create your views here.

@api_view(['GET'])
def create(request):

    # lectures=Lecutues.objects.all()
    # seri = LectureSerializer(lectures,many=True)

    header=['section','subject','slot','day','teacher','room']
    dataset=pd.read_csv("assets/timetable.csv")
    dataset.columns=header


    for i in dataset['section']:
        lecture=Lecutues(key=i)
        # lecture.key=i
        lecture.save()
        print("{} is saved".format(i))

    return Response({"status":"Everything working"}) 


@api_view(['GET'])
def get(request):
    lectures=Lecutues.objects.all()
    seri = LectureSerializer(lectures,many=True)
    
    print(seri.data)
    return Response(seri.data)
