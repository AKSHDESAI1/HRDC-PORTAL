from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from App.models import Event
from .Serializers import EventSerializer
from rest_framework.renderers import JSONRenderer
import io

@csrf_exempt
def Event_api(request):
    if request.method == 'GET':
        event = Event.objects.all()  # Complex DataType
        serializer = EventSerializer(event, many=True)  # Return in Native DataType
        json_data = JSONRenderer().render(serializer.data)  # Return in Json Format
        return HttpResponse(json_data, content_type="appication/json")
    
    if request.method == "POST":
        json_data = request.body  
        stream = io.BytesIO(json_data) # fetch Json data
        pythondata = JSONParser().parse(stream) #Convert json_data to python Native Datatype
        serializer = EventSerializer(data = pythondata) #Convert Native Data to Complex Data Type
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Saved Successfully.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="appication/json")
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="appication/json")
