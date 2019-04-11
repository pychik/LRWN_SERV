import requests
import json

# fetching Jwt for admin admin
def get_jwt(IP_PORT,login,password):

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    #data = '{ \\ \n   "password": "admin",\\ \n   "username": "admin" \\ \n }'
    data = '{ \n   "password": ' + str(password)+', \n   "username": ' + str(login) + ' \n }'
    #print(data)
    



    try:
        response = requests.post('http://'+IP_PORT+'/api/internal/login', headers=headers, data=data)
        r = response.text
        
        
        j = r.split('"jwt":',1)[1]
        jwt = j.split('}',1)[0]
        jwt = jwt.replace('"', "")
        print('we got authentification key')
        
        return(jwt)
    except Exception as ex:
        print(ex)
# fetching AppID and AppName
def get_APPs(j_token,IP_PORT):
    MES = 'Bearer ' + j_token
   
    headers = {
        'Accept': 'application/json',
        'Grpc-Metadata-Authorization': MES,
    }

    params = (
        ('limit', '15000'),
    )

    response = requests.get('http://' + IP_PORT + '/api/applications', headers=headers, params=params)
    string = response.text
    j = string#.decode('utf-8')
    count = int(json.loads(j)['totalCount'])
    for i in range(count):
        App_ID = json.loads(j)['result'][i]['id']
        App_Name = json.loads(j)['result'][i]['name']
        print('App_ID: ' + str(App_ID) + '\nApp_Name: ' + str(App_Name))
        get_devEUI(j_token,IP_PORT, App_ID)#adding searching for app_id devEui func
##use it in get APP func        
def get_devEUI(j_token,IP_PORT,A_ID):
    MES = 'Bearer ' + j_token
    headers = {
    'Accept': 'application/json',
    'Grpc-Metadata-Authorization': MES,
    }

    params = (
        ('limit', '15000'),
        ('applicationID', A_ID),
    )

    response = requests.get('http://' + IP_PORT + '/api/devices', headers=headers, params=params)
    j = response.text
    print('Devices we got:')
    count = int(json.loads(j)['totalCount'])
    for i in range(count):
        devName = json.loads(j)['result'][i]['name']
        devEUI = json.loads(j)['result'][i]['devEUI']
        lastSeen = json.loads(j)['result'][i]['lastSeenAt']
        
        print(str(i+1) + '\nname: ' + str(devName) + '  devEUI: ' + str(devEUI) + ' lastSeen: ' + str(lastSeen))
        devaddr = get_devAddr(j_token,IP_PORT,devEUI)

def get_devAddr(j_token,IP_PORT,devEUI):
    MES = 'Bearer ' + j_token
    headers = {
    'Accept': 'application/json',
    'Grpc-Metadata-Authorization': MES,
    }

    response = requests.get('http://' +IP_PORT +'/api/devices/'+str(devEUI)+'/activation', headers=headers)
    j = response.text
    #devActiv = str(json.loads(j)['deviceActivation'])
    #for el in devActiv:
    #    prin
    devAddr = json.loads(j)['deviceActivation']['devAddr']
    Appskey = json.loads(j)['deviceActivation']['appSKey']
    Nwskey = json.loads(j)['deviceActivation']['nwkSEncKey']
    print('devAddr: '+ str(devAddr) + ' Appskey: ' + str(Appskey) + ' Nwskey: ' + str(Nwskey))

   
iport = '192.168.1.153:8080'
login = '"admin"'
password = '"admin"'
jwt = get_jwt(iport,login,password)
get_APPs(jwt,iport)
#js = '{"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJleHAiOjE1NTQ5MTE1OTUsImlzcyI6ImxvcmEtYXBwLXNlcnZlciIsIm5iZiI6MTU1NDgyNTE5NSwic3ViIjoidXNlciIsInVzZXJuYW1lIjoiYWRtaW4ifQ.sf_6kSnU2aWjzCumuIpFswXk5Lc_gM-nYWnqNno3Y2Q"}'
#j = js.split('"jwt":',1)[1]
#j = j.split('}',1)[0]
#print(j)
