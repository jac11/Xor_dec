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

    def Fainal_Stage(self) : 

        with open ('X_Payload.txt','w') as XPayload,open('X_Key.txt','w')as XKey:
             XPayload = XPayload.write(str(self.Xor_Payload))
             XKey = XKey.write(str(self.Value_Key))
        with open ('X_Payload.txt','r') as XPayload,open('X_Key.txt','r')as XKey:
             XPayload = XPayload.read()
             XKey = XKey.read()  

        def hide(Payload,key):
            Local0= "​"
            Local1 = "‌"
            key= "".join(format(ord(char),"08b") for char in str(key))
            midpoint = int((len(Payload)/2)//1)
            result = ""
            for word in list(str(key)):
                result += Local0 if word == "0" else Local1 if word == "1" else ""
            return Payload[:midpoint]+result+Payload[midpoint:] 

        with open (self.args.output,'w') as w:
            w.write(hide(XPayload ,XKey))    
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
   .33