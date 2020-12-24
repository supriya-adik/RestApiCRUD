import  json
from django.core.serializers import serialize
from django.http import  HttpResponse
class mixinserialize(object) :
    def serialize_data(self,data):
         json_data=serialize('json',data) #convert into json data
         p_dict=json.loads(json_data)
         final_list=[]
         for empdata in p_dict :
             final_list.append(empdata['fields'])
             json_data=json.dumps(final_list)
             return  json_data
class httpresponse(object) :
    def render_to_httpresponse(self,data,status=200):
        return HttpResponse(data,content_type='application/json',status=status)