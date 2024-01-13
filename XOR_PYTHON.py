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

        if self.args.Payload:
            with open (self.args.Payload,'r') as payload:
                if self.args.P_base64:
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
        with open(self.args.output,'w') as XP_load:
             XP_load1 = 'shell = '+str(self.Xor_Payload)+'\n'+'Key = '+str(self.Value_Key)+'\n'+\
             "de_code = bytes([ Z ^ C for Z , C in zip(shell , Key)])"+'\n'+'import base64\n'+\
             'de_set = base64.b64decode(de_code).decode("utf-8")'+'\n'+'exec(de_set)'
             XP_load.write("import base64\nexec(base64.b64decode("+str(base64.b64encode((XP_load1.encode())))+'))')
    def argparse_command(self):

        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")       
        parser.add_argument("-P","--Payload" , metavar='' , action=None ,help ="Specify the Payload to be encrypted") 
        parser.add_argument("-B","--Key_base64" , action='store_true' ,default=False,help ="Use base64 encoding key value for encryption")  
        parser.add_argument("-b","--P_base64" , action='store_true' ,default=False,help ="Use base64 encoding for the Payload Before decryption")      
        parser.add_argument("-O","--output" , metavar='' , action=None ,required=True,help ="Specify the output file for the encrypted Payload") 
        
        self.args = parser.parse_args()        
        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()         
            exit()    
if __name__=='__main__':
   Xor_class()      
