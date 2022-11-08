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
        # Return in Native DataType
        serializer = EventSerializer(event, many=True)
        json_data = JSONRenderer().render(serializer.data)  # Return in Json Format
        return HttpResponse(json_data, content_type="appication/json")

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)  # fetch Json data
        # Convert json_data to python Native Datatype
        pythondata = JSONParser().parse(stream)
        # Convert Native Data to Complex Data Type
        serializer = EventSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'mslg': 'Data Saved Successfully.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="appication/json")
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="appication/json")
