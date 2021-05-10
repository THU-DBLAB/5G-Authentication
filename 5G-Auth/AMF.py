import colorama
from colorama import Style, Fore, Back
colorama.init(autoreset=True)
"""
Step 02
②
RAN get [SUPI]46697123456789, and send back [MSG]200ACK!
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.2",1))
f.listen(5)
c,addr = f.accept()
data = c.recv(1024)
SUPI = data.decode('UTF-8')
sn = "10011" #get from RAN
c.send("200ACK!".encode('UTF-8'))
print(Back.RED+"STEP 02")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|             v     v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF")
print(Fore.RED+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.RED+"|>"+Fore.GREEN+"[sn-name]10011") #get from RAN
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  RAN get [SUPI]%s" %(SUPI))
print(Fore.RED+"  Take [SUPI]%s to SEAF near by AMF" %(data.decode('UTF-8')))
print(Fore.RED+"  Send back 200ACK! to UE")

"""
Step 03
③ Auth. Request
SUCI or SUPI, SN-name
[SN-name]00001
"""
#link to AUSF's host
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(("10.1.0.3", 1))
data3 = "%s%s" %(SUPI, sn)
t.send(data3.encode('UTF-8'))
print("\n\n")
print(Back.CYAN+"STEP 03")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|                   v      v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF")
print(Fore.CYAN+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.CYAN+"|>"+Fore.GREEN+"[sn-name]%s" %(sn))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Delivor [SUPI]%s, [sn-name]%s to AUSF" %(SUPI, sn))

"""
Step 10
⑩
Store HXRES and K_seaf
"""
data10 = t.recv(1024) #AV
AV = data10.decode('UTF-8')
RAND = AV[0:16]
HXRES = AV[16:80]
K_seaf = AV[80:144]
AUTN = AV[144:]
print("\n\n")
print(Back.RED+"STEP 10")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|                   v      v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF")
print(Fore.RED+"|>"+Fore.GREEN+"[AV]%s" %(AV))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|>"+Fore.GREEN+"[RAND]%s" %(RAND))
print(Fore.RED+"|>"+Fore.GREEN+"[HXRES]%s" %(HXRES))
print(Fore.RED+"|>"+Fore.GREEN+"[K_seaf]%s" %(K_seaf))
print(Fore.RED+"|>"+Fore.GREEN+"[AUTN]%s" %(AUTN))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  Store:\n  [HXRES]%s,\n  [K_seaf]%s" %(HXRES, K_seaf))

"""
Step 11
⑪ Auth. Request
Deliver RAND, AUTN, ngSKI to UE
"""
import time
c.send(RAND.encode('UTF-8'))
time.sleep(1)
c.send(AUTN.encode('UTF-8'))
time.sleep(1)
#ngSKI = 000[0]0000 -> KSI_amf -> native security context
#ngSKI = 000[1]0000 -> KSI_asme -> mapped security context
#000[0] ~ 110[0] -> possible values for the NAS key set identifier
#111[0] -> no key is available
#What's means after [0]?
ngSKI = "00000000"
c.send(ngSKI.encode('UTF-8'))
"""ABBA (Anti-Bidding-down Between Architectures) parameter. This parameter allows the 5G system to enforce that a UE cannot access the network using older mechanisms that have had vulnerabilities associated with them."""
print("\n\n")
print(Back.CYAN+"STEP 11")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"| v     v     v     v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF")
print(Fore.CYAN+"|>"+Fore.GREEN+"[RAND]%s" %(RAND))
print(Fore.CYAN+"|>"+Fore.GREEN+"[HXRES]%s" %(HXRES))
print(Fore.CYAN+"|>"+Fore.GREEN+"[K_seaf]%s" %(K_seaf))
print(Fore.CYAN+"|>"+Fore.GREEN+"[AUTN]%s" %(AUTN))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Deliver RAND, AUTN, ngSKI to UE\n  [RAND]%s\n  [AUTN]%s\n  [ngSKI]%s" %(RAND, AUTN, ngSKI))

"""
Step 14
⑭ Calculate HRES* and compare to HXRES*
"""
data14 = c.recv(1024) #RES
RES = data14.decode('UTF-8')
import ex
HRES = ex.sha256(RES)
print("\n\n")
print(Back.RED+"STEP 14")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"| v     v     v     v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.RED+"|>"+Fore.GREEN+"[RES]%s" %(RES))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|>Caculate: RES -> HRES")
print(Fore.RED+"|>"+Fore.GREEN+"[HRES]%s" %(HRES))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  Compare: HRES from UE =? HXRES from AUSF")
if HRES == HXRES:
    print(Fore.RED+"  HRES = HXRES, allow!")
else:
    print(Fore.RED+"  HRES != HXRES , NOT ALLOW!")
    exit()

"""
Step 15
⑮ Auth. Request
Deliver RES to AUSF
"""
t.send(data14) #RES
print("\n\n")
print(Back.CYAN+"STEP 15")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|             v     v      v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.CYAN+"|>"+Fore.GREEN+"[RES]%s" %(RES))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Deliver [RES]%s to AUSF" %(RES))

"""
Step Final
AV 內的 K_seaf 成為錨點 Key
K_seaf 推導出 K_amf
將 ngKSI 和 K_amf 發給 AMF 使用
"""
dataf1 = t.recv(1024)
result = dataf1.decode('UTF-8')
dataf2 = t.recv(1024)
SUPI = dataf2.decode('UTF-8')
dataf3 = t.recv(1024)
print("\n\n")
print(Back.RED+"FINAL")
print(Fore.RED+"------------------------------------------------------------")
if result == "ALLOW" and dataf3.decode('UTF-8') == K_seaf:
    print(Fore.GREEN+"Link between AMF and AUSF is ALLOW")
else:
    print(Fore.GREEN+"Link between AMF and AUSF isn't ALLOW")
    exit()