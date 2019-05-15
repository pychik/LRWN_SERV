import requests
import json
import time


# fetching Jwt for admin admin
def get_jwt(ip_port, username, password):

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    # data = '{ \\ \n   "password": "admin",\\ \n   "username": "admin" \\ \n }'
    data = '{ \n   "password": ' + str(password)+', \n   "username": ' + str(username) + ' \n }'
    # print(data)
    
    try:
        response = requests.post('http://' + ip_port + '/api/internal/login', headers=headers, data=data)
        r = response.text
        
        j = r.split('"jwt":', 1)[1]
        jwt = j.split('}', 1)[0]
        jwt = jwt.replace('"', "")
        print('we got authentification key')
        
        return jwt
    except Exception as ex:
        print(ex)
# fetching AppID and AppName


def get_apps(j_token, ip_port):
    mes = 'Bearer ' + j_token
   
    headers = {
        'Accept': 'application/json',
        'Grpc-Metadata-Authorization': mes,
    }

    params = (
        ('limit', '15000'),
    )

    response = requests.get('http://' + ip_port + '/api/applications', headers=headers, params=params)
    string = response.text
    j = string  # .decode('utf-8')
    count = int(json.loads(j)['totalCount'])
    for i in range(count):
        app_id = json.loads(j)['result'][i]['id']
        app_name = json.loads(j)['result'][i]['name']
        print('app_id: ' + str(app_id) + '\nApp_Name: ' + str(app_name))
        get_dev_eui(j_token, ip_port, app_id)  # adding searching for app_id devEui func


# use it in get APP func
def get_dev_eui(j_token, ip_port, a_id):
    mes = 'Bearer ' + j_token
    headers = {
        'Accept': 'application/json',
        'Grpc-Metadata-Authorization': mes,
    }

    params = (
        ('limit', '15000'),
        ('applicationID', a_id),
    )

    response = requests.get('http://' + ip_port + '/api/devices', headers=headers, params=params)
    j = response.text
    print('Devices we got:')
    count = int(json.loads(j)['totalCount'])
    for i in range(count):
        dev_name = json.loads(j)['result'][i]['name']
        dev_eui = json.loads(j)['result'][i]['devEUI']
        last_seen = json.loads(j)['result'][i]['lastSeenAt']
        
        print(str(i+1) + '\nname: ' + str(dev_name) + '  devEUI: ' + str(dev_eui) + ' lastSeen: ' + str(last_seen))
        get_dev_addr(j_token, ip_port, dev_eui)


def get_dev_addr(j_token, ip_port, dev_eui):
    mes = 'Bearer ' + j_token
    headers = {
        'Accept': 'application/json',
        'Grpc-Metadata-Authorization': mes,
    }

    response = requests.get('http://' + ip_port + '/api/devices/'+str(dev_eui)+'/activation', headers=headers)
    j = response.text
    # dev_activation = str(json.loads(j)['deviceActivation'])
    # for el in dev_activation:
    #    print
    dev_addr = json.loads(j)['deviceActivation']['devAddr']
    apps_key = json.loads(j)['deviceActivation']['appSKey']
    nws_key = json.loads(j)['deviceActivation']['nwkSEncKey']
    print('devAddr: ' + str(dev_addr) + ' Appskey: ' + str(apps_key) + ' Nwskey: ' + str(nws_key))


if __name__ == "__main__":
    
    iport = '192.168.1.153:8080'
    login = '"admin"'
    password = '"admin"'
    while True:
        jwt = get_jwt(iport, login, password)
        get_apps(jwt, iport)
        time.sleep(3600)
    # js = '{"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJleHAiOjE1NTQ5MTE1OTUsImlzcyI6ImxvcmEtYXBwLXNlcnZlciIsIm5iZiI6MTU1NDgyNTE5NSwic3ViIjoidXNlciIsInVzZXJuYW1lIjoiYWRtaW4ifQ.sf_6kSnU2aWjzCumuIpFswXk5Lc_gM-nYWnqNno3Y2Q"}'
    # j = js.split('"jwt":',1)[1]
    # j = j.split('}',1)[0]
    # print(j)
