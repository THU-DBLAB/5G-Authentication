import colorama
from colorama import Style, Fore, Back
colorama.init(autoreset=True)
"""
Step 01-1
Get the SUPI, and add sn-name, then deliver them to AMF
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.2",1))
f.listen(5)
c,addr = f.accept()
data = c.recv(1024)
SUPI = data.decode('UTF-8')
sn = "10011"
print(Back.RED+"STEP 01-1")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"| v    v     v")
print(Fore.RED+"|>UE---RAN---AMF")
print(Fore.RED+"|>"+Fore.GREEN+"[sn-name]%s" %(sn))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  RAN deliver")
print(Fore.GREEN+"[SUPI]%s\n  [sn-name]%s\n" %(SUPI, sn)+Fore.RED+"  to RAN")
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(("10.1.0.3", 1))
data11 = "%s%s" %(SUPI, sn)
t.send(data11.encode('UTF-8'))

"""
Step 11-1
Get RAND, AUTN, ngSKI, then deliver them to UE
"""
RAND = t.recv(1024)
AUTN = t.recv(1024)
ngSKI =t.recv(1024)
print("\n\n")
print(Back.CYAN+"STEP 11-1")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"| v     v     v     v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Get RAND, AUTN, ngSKI from SEAF, then deliver them to UE")
import time
c.send(RAND)
time.sleep(1)
c.send(AUTN)
time.sleep(1)
c.send(ngSKI)

"""
Step 13-1
Get RES from UE, and send it to AMF
"""
data13 = c.recv(1024)
RES = data13.decode('UTF-8')
print("\n\n")
print(Back.RED+"STEP 13-1")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"| v     v    v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  Get\n  "+Fore.GREEN+"[RES]%s" %(RES)+Fore.RED+"\n  ,and send it to AMF")
t.send(data13)