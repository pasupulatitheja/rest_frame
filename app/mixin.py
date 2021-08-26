import json
from django.core.serializers import serialize
from django.http import HttpResponse


class serializerMixin(object):
    def Http_Resopnse_code(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)

class Mixin_Json_serial(object):
    def Json_Mixin(self,qs):
        json_data = serialize('json',qs)
        p_dict = json.loads(json_data)
        final_list = []
        for x in p_dict:
            data = x['fields']
            final_list.append(data)
        json_data = json.dumps(final_list)
        return json_data

