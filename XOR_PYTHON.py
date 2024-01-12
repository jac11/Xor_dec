#!/usr/bin/evn/python

import secrets
import argparse
import base64
import sys
import os

class Xor_class:

    def __init__(self):

        self.argparse_command()
        self.Gen_Key()
        self.Xor_Process()
        self.Fainal_Stage()

    def Gen_Key(self):  

        if self.args.message:
            with open (self.args.message,'r') as payload:
                if self.args.Mes_base64:
                    payload = payload.read()
                    payload = base64.b64encode(payload.encode())
                else:
                     payload = bytes(payload.read().encode())   
        Value_Key =  secrets.token_bytes(len(payload))
        if self.args.Key_base64:
           Value_Key = base64.b64encode(Value_Key)
        self.payload = payload
        self.Value_Key = Value_Key

    def Xor_Process(self):

        if self.args.Key_base64: 
            self.Value_Key = base64.b64decode(self.Value_Key)  
        self.Xor_Payload = bytes([ I  ^ L for I , L in zip(self.payload ,self.Value_Key) ])
        #print(self.Xor_Payload)
        #print()
        #print(self.Value_Key)
    def Fainal_Stage(self) : 

        with open ('X_Payload.txt','wb') as XPayload,open('X_Key.txt','wb')as XKey:
             XPayload = XPayload.write(self.Xor_Payload)
             XKey = XKey.write(self.Value_Key)
        with open ('X_Payload.txt','rb') as XPayload,open('X_Key.txt','rb')as XKey:
             XPayload = XPayload.read()
             XKey = XKey.read()  

        def hide(Payload,key):
            Local0= "​"
            Local1 = "‌"
            key= "".join(format(ord(char),"08b") for char in str(key))
            midpoint = int((len(Payload)/2)//1)
            result = ""
            for word in list(str(key)):
                result += Local0.encode() if word.encode() == "0" else Local1.encode() if word.encode()== "1" else ""
            result  = bytes(result.encode())  
            return bytes(Payload[:midpoint])+result+bytes(Payload[midpoint:])
          
        with open (self.args.output+'.py','w') as w:
            w.write('Shell = '.replace('\n',''))
        with open (self.args.output+'.py','ab') as w:    
            w.write(hide(XPayload ,XKey))
        with open (self.args.output+'.py','a') as w:     	
            w.write('\n'+'local0 = ""\n'+'local1 = ""\n'+'result = ""\n'+\
            'for i in list(str(Shell)):\n'+'   '+'if i == local0 :\n'+\
            '      result += "0"\n'+'   elif i == local1:'+'\n    result += "1"\n'+\
            'result = "".join([chr(int(result[i:i+8],2)) for i in range(0,len(result),8)])'+'\n'+\
            'de_code = bytes([ Z ^ C for Z , C in zip(Shell , result)])\n'+'import base64\n'+\
            'de_set = base64.b64decode(de_code).decode("utf-8")')
        os.remove('X_Payload.txt')
        os.remove('X_Key.txt')  

    def argparse_command(self):

        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")       
        parser.add_argument("-M","--message" , metavar='' , action=None ,help ="wordlist of passwords") 
        parser.add_argument("-B","--Key_base64" , action='store_true' ,default=False,help ="set color display off")  
        parser.add_argument("-b","--Mes_base64" , action='store_true' ,default=False,help ="set color display off")      
        parser.add_argument("-O","--output" , metavar='' , action=None ,required=True,help ="read the hash from file input") 
        
        self.args = parser.parse_args()        
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()         
            exit()    
if __name__=='__main__':
   Xor_class()      
