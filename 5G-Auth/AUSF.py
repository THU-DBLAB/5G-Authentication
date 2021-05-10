import colorama
from colorama import Style, Fore, Back
colorama.init(autoreset=True)
"""
Step 04
④
Get [SUPI]46697123456789, [SN-name]10011
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.3",1))
f.listen(5)
c,addr = f.accept()
data4 = c.recv(1024) #SUPI[0:14], sn-name[14:19]
data4 = data4.decode('UTF-8')
SUPI = data4[0:14]
sn = data4[14:19]
print(Back.RED+"STEP 04")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|                   v      v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF")
print(Fore.RED+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.RED+"|>"+Fore.GREEN+"[sn-name]%s" %(sn))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  Get [SUPI]%s, [sn-name]%s" %(SUPI, sn))

"""
Step 05
⑤ Auth. Get Request
Deiver SUCI or SUPI, SN-name to UDM
"""
#link to UDM's host
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(("10.1.0.4", 1))
data5 = "%s%s" %(SUPI, sn)
t.send(data5.encode('UTF-8'))
print("\n\n")
print(Back.CYAN+"STEP 05")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|                          v      v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF---UDM")
print(Fore.CYAN+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.CYAN+"|>"+Fore.GREEN+"[sn-name]%s" %(sn))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Deliver [SUPI]%s, [sn-name]%s to UDM" %(SUPI, sn))

"""
Step 08
⑧ Store XRES and Calculate HXRES
留存：XRES*、K_ausf
XRES* hashed into HXRES*
K_ausf推導出K_seaf
用HXRES與K_seaf替換掉原先內容，生成新AV：RAND、HXRES、K_seaf、AUTN
"""
data81 = t.recv(1024) #AV
AV = data81.decode('UTF-8')
data82 = t.recv(1024) #SUPI
SUPI = data82.decode('UTF-8')
RAND = AV[0:16]
XRES = AV[16:24]
K_ausf = AV[24:88]
AUTN = AV[88:]
import ex
HXRES = ex.sha256(XRES)
K_seaf = ex.KDF(sn, K_ausf)
print("\n\n")
print(Back.RED+"STEP 08")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|                          v      v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF---UDM")
print(Fore.RED+"|>"+Fore.GREEN+"[AV]%s" %(AV))
print(Fore.RED+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|>"+Fore.GREEN+"[RAND]%s" %(RAND))
print(Fore.RED+"|>"+Fore.GREEN+"[XRES]%s" %(XRES))
print(Fore.RED+"|>"+Fore.GREEN+"[K_ausf]%s" %(K_ausf))
print(Fore.RED+"|>"+Fore.GREEN+"[AUTN]%s" %(AUTN))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  Store:\n  [XRES]%s,\n  [K_ausf]%s" %(XRES, K_ausf))
print(Fore.RED+"  Derive:\n  [HXRES]%s\n  [K_seaf]%s" %(HXRES, K_seaf))
AV = "%s%s%s%s" %(RAND, HXRES, K_seaf, AUTN)
print(Fore.RED+"  Generate new AV(RAND, HXRES, K_seaf, AUTN):\n  [AV]%s" %(AV))

"""
Step 09
⑨ Auth. Response
Deliver AV to AMF
"""
print("\n\n")
print(Back.CYAN+"STEP 09")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|                   v      v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF---UDM")
print(Fore.CYAN+"|>"+Fore.GREEN+"[AV]%s" %(AV))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Deliver [AV]%s to SEAF" %(AV))
c.send(AV.encode('UTF-8'))

"""
Step 16
⑯ RES Verify response
RES = XRES
"""
data16 = c.recv(1024) #RES
RES = data16.decode('UTF-8')
print("\n\n")
print(Back.RED+"STEP 16")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|             v     v      v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|>Data in stored from UDM:\n|>  "+Fore.GREEN+"[XRES]%s" %(XRES))
print(Fore.RED+"|>Data from UE:\n|>  "+Fore.GREEN+"[RES]%s" %(RES))
print(Fore.RED+"------------------------------------------------------------")
if RES == XRES:
    print(Fore.RED+"  RES = XRES, allow!")
else:
    print(Fore.RED+"  RES != XRES, NOT ALLOW!")
    exit()

"""
Step 17
⑰ Auth. Response
Deliver Result, [SUPI], K_seaf to SEAF
"""
import time
result = "ALLOW"
c.send(result.encode('UTF-8')) #Result
time.sleep(1)
c.send(data82) #SUPI
time.sleep(1)
c.send(K_seaf.encode('UTF-8')) #K_seaf
print("\n\n")
print(Back.CYAN+"STEP 16")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|             v     v      v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|>"+Fore.GREEN+"[Result]%s" %(result))
print(Fore.CYAN+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.CYAN+"|>"+Fore.GREEN+"[K_seaf]%s" %(K_seaf))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Deliver\n  [Result]%s,\n  [SUPI]%s,\n  [K_seaf]%s\n  to SEAF" %(result, SUPI, K_seaf))