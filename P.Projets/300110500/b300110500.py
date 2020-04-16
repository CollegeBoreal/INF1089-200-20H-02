# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:01:05 2020

@author: 300110500

"""

# import le socket library
import socket 

# definition de la fonction et les parametres ip address et hostname
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
# Appel de la fonction definieet execution du code
get_Host_name_IP()
  
# ajout d'un UUID module  qui affichera le MAC address de lèhote(pc) 
  
import uuid 
  
# imprime la valeur unique de MAC  address 
print (hex(uuid.getnode())) 

# Ajout des informations du reseau
import subprocess
proc = subprocess.check_output("ipconfig" ).decode('utf-8')
print (proc)