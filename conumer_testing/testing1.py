import json
import requests
Base_URL = "http://127.0.0.1:8000/"
End_Point = 'api/'

# def get_resource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#             'id':id
#         }
#     resp = requests.get(Base_URL+End_Point,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
# get_resource(20)


# def create_resourcs():
#     new_emp = {
#         'emid' : 1,
#         'ename' : 'ravi',
#         'esalary' : 30000,
#         'eaddress' : 'hydrabd'
#     }
#     resp = requests.post(Base_URL+End_Point,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
# create_resourcs()

def updat_resourse(id):
    new_emp = {
        'id':id,
        'eaddress':'rajamandry'

    }
    resp = requests.put(Base_URL+End_Point,data=json.dumps(new_emp))
    print(resp.json())
    print(resp.status_code)

updat_resourse()