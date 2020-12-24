from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views.generic import View
from .utils import is_json
from .mixins import mixinserialize,httpresponse

import json
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCrudCBV(View,mixinserialize,httpresponse) :
    def get_object_by_id(self,id):
        try :
          emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp

    def get(self,request,*args,**kwargs):
       data=request.body
       if not is_json(data) :
           return self.render_to_httpresponse(json.dumps({'msg':'Please Send Valid Json Data'}),status=400)

       data=json.loads(data)
       id=data.get('id',None)
       if id is not None :
           emp=self.get_object_by_id(id)
           if emp is None :
              return self.render_to_httpresponse(json.dumps({'msg':'No Matched Record Found For Specified Id..'}),status=400)
           json_data=self.serialize_data([emp,])
           return self.render_to_httpresponse(json_data)
       qs=Employee.objects.all()
       json_data=self.serialize_data(qs)
       return self.render_to_httpresponse(json_data)

    def post(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data) :
            return  self.render_to_httpresponse(json.dumps({'msg':'Please provide valid json data..'}),status=400)
        empdata=json.loads(data)
        form=EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Data save Successfully'})
            return self.render_to_httpresponse(json_data)
        if form.errors :
            json_data=json.dumps(form.errors)
            return self.render_to_httpresponse(json_data,status=400)
    def put(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data) :
            json_data=json.dumps({'msg':'Please Provide Valid Json Data..'})
            return self.render_to_httpresponse(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)

        if id is None:
            json_data = json.dumps({'msg': 'To perform updation please provide valid id'})
            return self.render_to_httpresponse(json_data, status=400)
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'No Resource With Matched id,Not Possible to perform updation...'})
            return self.render_to_httpresponse(json_data, status=400)
        provided_data=json.loads(data)
        original_data={
                 'eno' :emp.eno,
                 'ename':emp.ename,
                 'esal' :emp.esal,
                 'eaddr' :emp.eaddr,
        }
        original_data.update(provided_data)
        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid() :
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Data Updated Successfully..'})
            return self.render_to_httpresponse(json_data, status=400)
        if form.errors :
            json_data = json.dumps(form.errors)
            return self.render_to_httpresponse(json_data, status=400)
    def delete(self,request,*args,**kwargs):
        data = request.body
        pdata=json.loads(data)
        id=pdata.get('id',None)

        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'The Requested Resource Not Available with matched id'})
                return self.render_to_httpresponse(json_data,status=400)
            status,deleted_item=emp.delete()
            if status == 1:
                json_data = json.dumps({'msg':'Resource Deleted Successfully..'})
                return self.render_to_httpresponse(json_data)
            json_data = json.dumps({'msg': 'Unable To delete please try again'})
            return self.render_to_httpresponse(json_data,status=400)
        json_data = json.dumps({'msg': 'To perform deletion id is mandatory,please provide valid id'})
        return self.render_to_httpresponse(json_data,status=400)