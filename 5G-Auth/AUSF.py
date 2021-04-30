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
print("STEP 04")
print("------------------------------------------------------------")
print("|                   v      v")
print("|>UE---RAN---AMF---SEAF---AUSF")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]%s" %(sn))
print("------------------------------------------------------------")
print("  Get [SUPI]%s, [sn-name]%s" %(SUPI, sn))

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
print("STEP 05")
print("------------------------------------------------------------")
print("|                          v      v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]%s" %(sn))
print("------------------------------------------------------------")
print("  Deliver [SUPI]%s, [sn-name]%s to UDM" %(SUPI, sn))

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
print("STEP 08")
print("------------------------------------------------------------")
print("|                          v      v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM")
print("|>[AV]%s" %(AV))
print("|>[SUPI]%s" %(SUPI))
print("------------------------------------------------------------")
print("|>[RAND]%s" %(RAND))
print("|>[XRES]%s" %(XRES))
print("|>[K_ausf]%s" %(K_ausf))
print("|>[AUTN]%s" %(AUTN))
print("------------------------------------------------------------")
print("  Store:\n  [XRES]%s,\n  [K_ausf]%s" %(XRES, K_ausf))
print("  Derive:\n  [HXRES]%s\n  [K_seaf]%s" %(HXRES, K_seaf))
AV = "%s%s%s%s" %(RAND, HXRES, K_seaf, AUTN)
print("  Generate new AV(RAND, HXRES, K_seaf, AUTN):\n  [AV]%s" %(AV))

"""
Step 09
⑨ Auth. Response
Deliver AV to AMF
"""
print("\n\n")
print("STEP 09")
print("------------------------------------------------------------")
print("|                   v      v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM")
print("|>[AV]%s" %(AV))
print("------------------------------------------------------------")
print("  Deliver [AV]%s to SEAF" %(AV))
c.send(AV.encode('UTF-8'))

"""
Step 16
⑯ RES Verify response
RES = XRES
"""
data16 = c.recv(1024) #RES
RES = data16.decode('UTF-8')
print("\n\n")
print("STEP 16")
print("------------------------------------------------------------")
print("|             v     v      v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print("------------------------------------------------------------")
print("|>Data in stored from UDM:\n|>  [XRES]%s" %(XRES))
print("|>Data from UE:\n|>  [RES]%s" %(RES))
print("------------------------------------------------------------")
if RES == XRES:
    print("  RES = XRES, allow!")
else:
    print("  RES != XRES, NOT ALLOW!")
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