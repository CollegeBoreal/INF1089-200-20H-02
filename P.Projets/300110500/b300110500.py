# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:01:05 2020

@author: 300110500

"""



import socket 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
get_Host_name_IP()
  
# Python Program to compute 
# MAC address of host 
# using UUID module 
  
import uuid 
  
# printing the value of unique MAC 
# address using uuid and getnode() function  
print (hex(uuid.getnode())) 


