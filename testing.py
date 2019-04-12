'''
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJleHAiOjE1NTUxNzYwNzQsImlzcyI6ImxvcmEtYXBwLXNlcnZlciIsIm5iZiI6MTU1NTA4OTY3NCwic3ViIjoidXNlciIsInVzZXJuYW1lIjoiYWRtaW4ifQ.FDGxDQ9Wr3wtTfLF_PqgF3Dn7Fs9B8w3FGePm2GS5TY"
}

#######
{
  "totalCount": "4",
  "result": [
    {
      "devEUI": "1f7b29ecad59282a",
      "name": "ARDUINO_Chehova",
      "applicationID": "1",
      "description": "Dragino board with arduino pcb",
      "deviceProfileID": "628c0fa3-fd0e-4589-9a33-c5bd54be9854",
      "deviceProfileName": "arduino",
      "deviceStatusBattery": 255,
      "deviceStatusMargin": 256,
      "deviceStatusExternalPowerSource": false,
      "deviceStatusBatteryLevelUnavailable": true,
      "deviceStatusBatteryLevel": 0,
      "lastSeenAt": "2019-04-09T09:29:56.791753Z"
    },
    {
      "devEUI": "a3efd2c497460ebd",
      "name": "BAYLAN_METER",
      "applicationID": "1",
      "description": "TEST_METER",
      "deviceProfileID": "b94215e4-d67a-44ec-b3d2-92bbb592aae6",
      "deviceProfileName": "BAYLAN",
      "deviceStatusBattery": 255,
      "deviceStatusMargin": 256,
      "deviceStatusExternalPowerSource": false,
      "deviceStatusBatteryLevelUnavailable": true,
      "deviceStatusBatteryLevel": 0,
      "lastSeenAt": "2019-04-03T08:18:25.872057Z"
    },
    {
      "devEUI": "04b6480455082110",
      "name": "ETK-m-ZK",
      "applicationID": "1",
      "description": "zenner- белценнер etk",
      "deviceProfileID": "488dcfba-5ee2-461b-97af-746f3939b627",
      "deviceProfileName": "ETK-m-ZK",
      "deviceStatusBattery": 255,
      "deviceStatusMargin": 256,
      "deviceStatusExternalPowerSource": false,
      "deviceStatusBatteryLevelUnavailable": true,
      "deviceStatusBatteryLevel": 0,
      "lastSeenAt": "2019-04-12T00:51:29.762213Z"
    },
    {
      "devEUI": "04b648fd89990701",
      "name": "ZENNER_HCA",
      "applicationID": "1",
      "description": "Zenner LoRaWaN heat cost allocator",
      "deviceProfileID": "964841d5-1c96-4c90-bcf4-87abe2693621",
      "deviceProfileName": "ZENNER_HCA",
      "deviceStatusBattery": 255,
      "deviceStatusMargin": 256,
      "deviceStatusExternalPowerSource": false,
      "deviceStatusBatteryLevelUnavailable": true,
      "deviceStatusBatteryLevel": 0,
      "lastSeenAt": "2019-04-10T22:35:43.019305Z"
    }
  ]
}
########
{
  "deviceActivation": {
    "devEUI": "04b648fd89990701",
    "devAddr": "0049fc11",
    "appSKey": "f9f53301aa9a846a778bafac7a813ce7",
    "nwkSEncKey": "9569641637ffb412ba7d0952d7d06c8b",
    "sNwkSIntKey": "9569641637ffb412ba7d0952d7d06c8b",
    "fNwkSIntKey": "9569641637ffb412ba7d0952d7d06c8b",
    "fCntUp": 1,
    "nFCntDown": 1,
    "aFCntDown": 0
  }
}
'''

string = '1192010000'

fin = 'неизвестный пакет' + str(string)
if string.startswith('11'):
    print('recieved zenner payload sp1')
    a1 = string[8:10]
    a2 = string[6:8]
    a3 = string[4:6]
    a4 = string[2:4]
    a = a1 + a2 + a3 + a4
    fin = int(a,16)
print(fin)
#mes = 'Bearer '
#MES = 'Bearer ' + string
#print(MES)
