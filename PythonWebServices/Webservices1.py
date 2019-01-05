import requests
import json
import jsonpath

baseURL = "https://reqres.in"
resource = "/api/users?page=2"

response = requests.get(baseURL+resource)
print(response)
print(response.content)
print(response.headers)
print(response.headers.get("Content-Type"))
print(response.headers.get("Date"))
print(response.headers.get("Content-Type"))
print(response.headers.get("Server"))
print(response.cookies)
print(response.encoding)
print(response.elapsed)
json_response=json.loads(response.text)
first_name=jsonpath.jsonpath(json_response,"data[0].first_name")
print(first_name[0])
first_names=jsonpath.jsonpath(json_response,"data[:].first_name")

for name in first_names:
    print(name)

for i in range(0,3):
    fname = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print((fname[0]))
