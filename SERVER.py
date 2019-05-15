import base64
import binascii
# from urllib.parse import parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn


class ThreadingMULTIServer(ThreadingMixIn, HTTPServer):
    pass


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Server working!"
        self.wfile.write(bytes(message, "utf8"))
        print('зашел пользователь на страничку')
    # return

    def do_POST(self):
        # self._set_headers()
        print("PACKET RECEIVED")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        # print(self.data_string)
        self.send_response(200)
        self.end_headers()
        data = self.data_string
        data = Jreader.json_read(data)
        print(data)
        '''
    readings_dec = binascii.hexlify(base64.b64decode(str(readings[0]))).upper()
    print('readings data:'+ str(readings))
    print('decoded_readings: ' + str(readings_dec.decode('utf-8')))
    #self.wfile.write(bytes("Hello World".encode("UTF-8")))
    '''
    # return


class Jreader:
    def json_read(self):
        jstring = self.decode('utf-8')
        jjq_GW = json.loads(jstring)['rxInfo'][0]['gatewayID']
        jjq_App = json.loads(jstring)['applicationName']
        jjq_type = json.loads(jstring)['deviceName']
        jjq_deveui = json.loads(jstring)['devEUI']
        jjq_data = json.loads(jstring)['data']
        if jjq_type.startswith('ARDUINO'):
            jjq_data =  base64.b64decode(jjq_data).decode('utf-8')
        elif jjq_type.startswith('BAYLAN'):
            jjq_data = binascii.hexlify(base64.b64decode(jjq_data)).upper()
            jjq_data = jjq_data.decode('utf-8')
        elif jjq_type.startswith('ZENNER_HCA'):
            jjq_data = binascii.hexlify(base64.b64decode(jjq_data)).upper()
            jjq_data = jjq_data.decode('utf-8')
            
        elif jjq_type.startswith('ETK-m'):
            jjq_data = binascii.hexlify(base64.b64decode(jjq_data)).upper()
            jjq_data = jjq_data.decode('utf-8')
            fin = 'неизвестный пакет' + str(jjq_data)
            if jjq_data.startswith('11'):
                print('received zenner payload sp1')
                a1 = jjq_data[8:10]
                a2 = jjq_data[6:8]
                a3 = jjq_data[4:6]
                a4 = jjq_data[2:4]
                a = a1 + a2 + a3 + a4
                jjq_data = str(int(a,16)) + ' liters'
            else:
                jjq_data = fin
        concl = 'GATEWAY_ID: ' + str(jjq_GW) + '\nApplication_Name: ' + str(jjq_App) + '\nDev_Type: ' + str(jjq_type) \
                + '\nDev_EUI: ' + str(jjq_deveui) + '\nData: ' + str(jjq_data)
        return concl


# 26 01 1d 9d
# 11 34 13 4f a2 84 14 9d bc d3 8c 5a 56 e9 00 32
# 2f b5 fd 86 f9 85 bc 7a 2b a3 db 46 62 a3 aa 71
server = ThreadingMULTIServer(('192.168.1.104', 8009), MyHandler)
server.serve_forever()

