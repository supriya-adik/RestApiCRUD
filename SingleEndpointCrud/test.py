from django.test import TestCase
import requests
import json
# Create your tests here.

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resource(id=None)  :
    data={}
    if id is not None :
        data={'id':id}
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.json())
    print(resp.status_code)
# id=input('Enter the id:')
#get_resource()
def create_resource() :
    eno=int(input("Enter Eno:"))
    ename=input('Enter Ename:')
    esal=int(input('Enter Esal:'))
    eaddr=input('Enter Address:')
    new_emp={
        'eno':eno,
        'ename':ename,
        'esal':esal,
        'eaddr':eaddr
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.json())
    print(resp.status_code)
# create_resource()

def update_resource(id) :
    #ename = input('Enter Ename:')
    esal = int(input('Enter Esal:'))
    eaddr = input('Enter Address:')

    udata= {
        'id':id,
        'esal' :esal,
        'eaddr':eaddr
    }

    data=json.dumps(udata)
    print(data)
    resp=requests.put(BASE_URL+ENDPOINT,data)
    print(resp.json())
# id=(input('Enter the id to update:'))
# update_resource(5)

def delete_resource(id) :
    data={
        'id':id
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.json())
id=input('Enter the id:')
delete_resource(id)