from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
#from urllib.parse import parse_qs
import json
import binascii,base64


class ThreadingMULTIServer(ThreadingMixIn, HTTPServer):
    pass
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Server working!"
        self.wfile.write(bytes(message, "utf8"))
        print('зашел пользователь на страничку')
	#return
	    
    def do_POST(self):
	#self._set_headers()
        print("принята информация")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.end_headers()
        data = self.data_string
        data = jreader.json_read(data)
        print(data)
        '''
	readings_dec = binascii.hexlify(base64.b64decode(str(readings[0]))).upper()
	print('readings data:'+ str(readings))
	print('decoded_readings: ' + str(readings_dec.decode('utf-8')))
	#self.wfile.write(bytes("Hello World".encode("UTF-8")))
	'''        
	#return
class jreader():
    def json_read(a):
        jstring = a.decode('utf-8')
        jjq_GW = json.loads(jstring)['rxInfo'][0]['gatewayID']
        jjq_App = json.loads(jstring)['applicationName']
        jjq_type = json.loads(jstring)['deviceName']
        jjq_deveui = json.loads(jstring)['devEUI']
        jjq_data = json.loads(jstring)['data']
        if jjq_type.startswith('ARDUINO'):
            jjq_data =  base64.b64decode(jjq_data).decode('utf-8')
        elif jjq_type.startwith('BAYLAN'):
            jjq_data = binascii.hexlify(base64.b64decode(jjq_data)).upper()
        elif jjq_type.startwith('ZENNER_HCA'):
            jjq_data = binascii.hexlify(base64.b64decode(jjq_data)).upper()
        elif jjq_type.startwith('ETK-m'):
            jjq_data = binascii.hexlify(base64.b64decode(jjq_data)).upper()
        concl = 'GATEWAY_ID: '+ str(jjq_GW) + '\nApplication_Name: '+ str(jjq_App) + '\nDev_Type: '+ str(jjq_type) + '\nDev_EUI: '+ str(jjq_deveui) + '\nData: '+ str(jjq_data)
        return concl


#26 01 1d 9d
#11 34 13 4f a2 84 14 9d bc d3 8c 5a 56 e9 00 32
#2f b5 fd 86 f9 85 bc 7a 2b a3 db 46 62 a3 aa 71
server = ThreadingMULTIServer(('192.168.1.104', 8009), myHandler)
server.serve_forever()

