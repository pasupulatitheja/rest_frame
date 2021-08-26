from django.shortcuts import render
from .models import EmployeeModel
from .mixin import serializerMixin,Mixin_Json_serial
from django.views.generic import View
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from  django.utils.decorators import method_decorator
from .utilise import is_json
import json
from .forms import EmployeeForm
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmplyeeCBV(View,serializerMixin,Mixin_Json_serial):
    def get_by_id(self,id):
        try:
            emp = EmployeeModel.objects.get(emid=id)
        except EmployeeModel.DoesNotExist:
            emp = None
        return emp
    def get(self,request,*args,**kwargs):
        data = request.body
        vaild_json = is_json(data)
        if not vaild_json:
            json_data = json.dumps({"mess":"Provid valid json data"})
            return self.Http_Resopnse_code(json_data,status=400)
        p_data = json.loads(data)
        id = p_data.get('id',None)
        if id is not None:
            emp = self.get_by_id(id)
            if emp is None:
                json_data = json.dumps({"mess":"No record is avaiable"})
                return self.Http_Resopnse_code(json_data,status=400)
            json_data = self.Json_Mixin([emp,])
            return self.Http_Resopnse_code(json_data)
        qs = EmployeeModel.objects.all()
        json_data = self.Json_Mixin(qs)
        return self.Http_Resopnse_code(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        vaild_json = is_json(data)
        if not vaild_json:
            json_data = json.dumps({"meass":"provide the valid json"})
            return self.Http_Resopnse_code(json_data,status=400)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"mess":"Data is saved"})
            return self.Http_Resopnse_code(json_data,status=400)
        if form.errors:
            json_data = json.dumps(form.errors)
            return  self.Http_Resopnse_code(json_data,status=400)
    def put(self,request,*args,**kwargs):
        data = request.body
        vaild_json = is_json(data)
        if not vaild_json:
            json_data = json.dumps({"mess":"Please provide valid json"})
            return self.Http_Resopnse_code(json_data,status=400)

        p_dict = json.loads(data)
        p_id = p_dict.get('id',None)
        if p_id is None:
            json_data = json.dumps({"meass":"provide coorect id"})
            return self.Http_Resopnse_code(json_data,status=400)
        emp = self.get_by_id(p_id)
        if emp is None:
            json_data = json.dumps({"meass": "no record found"})
            return self.Http_Resopnse_code(json_data, status=400)
        provide_data = json.loads(data)
        orginal_data = {
            'emid':emp.emid,
            'ename':emp.ename,
            'esalary':emp.esalary,
            'eaddress':emp.eaddress
        }
        orginal_data.update(provide_data)
        form = EmployeeForm(orginal_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"mess":"data updated succssfully"})
            return self.Http_Resopnse_code(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.Http_Resopnse_code(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"mess":"provide the coorect json"})
            return self.Http_Resopnse_code(json_data,status=400)
        p_data = json.loads(data)
        p_dict = p_data.get('id',None)
        if p_dict is not None:
            emp = self.get_by_id(id)
            if emp is None:
                json_data = json.dumps({"mess": "No recorde is there"})
                return self.Http_Resopnse_code(json_data, status=400)
            status,delete_items = emp.delete()
            if status == 1:
                json_data = json.dumps({"mess":"delete succssfully"})
                return self.Http_Resopnse_code(json_data)
            json_data = json.dumps({"mess":"delete after some time"})
            return self.Http_Resopnse_code(json_data,status=400)
        json_data = json.dumps({"mess":"give the id it compulsory"})
        return self.Http_Resopnse_code(json_data, status=400)


