import requests
import json

def get_jwt(a):

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    #data = '{ \\ \n   "password": "admin",\\ \n   "username": "admin" \\ \n }'
    data = '{ \n   "password": "admin", \n   "username": "admin" \n }'
    



    try:
        response = requests.post('http://'+a+'/api/internal/login', headers=headers, data=data)
        r = response.text
        print(r)
        j = r.split('"jwt":',1)[1]
        jwt = j.split('}',1)[0]
        jwt = jwt.replace('"', "'")
        print(jwt)
        return(jwt)
    except Exception as ex:
        print(ex)
def get_APPs():


    headers = {
        'Accept': 'application/json',
        'Grpc-Metadata-Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJleHAiOjE1NTQ5MTIwMjMsImlzcyI6ImxvcmEtYXBwLXNlcnZlciIsIm5iZiI6MTU1NDgyNTYyMywic3ViIjoidXNlciIsInVzZXJuYW1lIjoiYWRtaW4ifQ.CXRCTKiWpgRZpHjybJIZdiSsHegud96F_Yv8pUQ4Lys',
}

    response = requests.get('http://192.168.1.153:8080/api/gateways', headers=headers)
    print(response.text)


   
iport = '192.168.1.153:8080'
jwt = get_jwt(iport)
get_APPs()
#js = '{"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJleHAiOjE1NTQ5MTE1OTUsImlzcyI6ImxvcmEtYXBwLXNlcnZlciIsIm5iZiI6MTU1NDgyNTE5NSwic3ViIjoidXNlciIsInVzZXJuYW1lIjoiYWRtaW4ifQ.sf_6kSnU2aWjzCumuIpFswXk5Lc_gM-nYWnqNno3Y2Q"}'
#j = js.split('"jwt":',1)[1]
#j = j.split('}',1)[0]
#print(j)
