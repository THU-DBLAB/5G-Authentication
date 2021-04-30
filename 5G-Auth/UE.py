"""
Step 01
① Registration Request
UE send registration request to AUSF and ARPF, include SUCI or 5G-GUTI.
"""
import socket
#link to RAN's host
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(("10.1.0.2", 1))
#deliver [SUPI]46697123456789 to AMF
#SUPI = IMSI(國際移動使用者辨識碼 in SIM卡), 466 = TW(MCC), 97 = Taiwan Mobile(MNC), 123456789 = identifer num(MSIN)
SUPI = "46697123456789"
t.send(SUPI.encode('UTF-8'))
print("STEP 01") #
print("------------------------------------------------------------")
print("| v")
print("|>UE---RAN---AMF")
print("|>[SUPI]%s" %(SUPI))
print("------------------------------------------------------------")
print("  UE deliver [SUPI]%s to AMF" %(SUPI))
print("  , and pass by RAN, then get the [sn-name]10011 from RAN")
data1 = t.recv(1024)
print("  UE get [MSG]%s" %(data1.decode('UTF-8')))
print("  Connect success!")

"""
Step 12
⑫ Calculate Auth. Response (RES*)
將UE本身的 Key, 與得到的 RAND, AUTN 傳給 USIM 並進行驗證 MAC = XMAC
USIM 自行生成 RES
手機從 RES 推導出 RES*
CK || IK 推導出 K_ausf
K_ausf 推導出 K_seaf
傳遞：RES*
"""
#USIM
Key = "1000000000000001"
SQN = "010101"
SQN = str(int(SQN) + 1).zfill(6) #Each time authentication connect, add 1
#Get data from SEAF
data121 = t.recv(1024) #RAND
RAND = data121.decode('UTF-8')
data122 = t.recv(1024) #AUTN
AUTN = data122.decode('UTF-8')
data123 = t.recv(1024) #ngKSI
ngKSI = data123.decode('UTF-8')
print("\n\n")
print("STEP 12")
print("------------------------------------------------------------")
print("| v     v     v     v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print("|>[RAND]%s" %(RAND))
print("|>[AUTN]%s" %(AUTN))
print("|>[ngKSI]%s" %(ngKSI))
print("------------------------------------------------------------")
print("|>[USIM]: Key, SQN")
print("|>[Key]%s" %(Key))
print("|>[SQN]%s" %(SQN))
xor = AUTN[0:8]
AMF = AUTN[8:10]
MAC_A = AUTN[10:]
print("------------------------------------------------------------")
print("|>[AUTN]: xor, AMF, MAC-A")
print("|>[xor]%s" %(xor))
print("|>[AMF]%s" %(AMF))
print("|>[MAC-A]%s" %(MAC_A))
#Calculation in UE
import ex
XMAC_A = ex.f1(Key, RAND, AMF, SQN)
RES = ex.f2(Key, RAND)
CK = ex.f3(Key, RAND)
IK = ex.f4(Key, RAND)
AK = ex.f5(Key, RAND)
print("------------------------------------------------------------")
print("|      _____________________RAND____________________       |")
print("|      |                      |      |      |      |       |")
print("|      |  Key         AMF___  |  Key |      |  Key |       |")
print("|      |   |                | |   |  |      |   |  |       |")
print("|      f5__|    ______SQN___|_f1__⊥__f2     f3__⊥__f4      |")
print("|      |       |              |      |      |      |       |")
print("|      v       |              v      v      v      v       |")
print("|      AK_____xor          XMAC-A   RES     CK     IK      |")
print("|              |                                           |")
print("|              v                                           |")
print("|           SQN⊕AK                                         |")
print("------------------------------------------------------------")
print("|>[f1][XMAC-A]%s" %(XMAC_A))
print("|>[f2][RES]%s" %(RES))
print("|>[f3][CK]%s" %(CK))
print("|>[f4][IK]%s" %(IK))
print("|>[f5][AK]%s" %(AK))
print("------------------------------------------------------------")
if XMAC_A == MAC_A: #data in USIM = data from UDM
    print("  XMAC = MAC, allow!")
else:
    print("  XMAC != MAC , NOT ALLOW!")
    exit()

"""
Step 13
⑬ Auth. Response
Deliver RES to SEAF near by AMF
"""
t.send(RES.encode('UTF-8'))
print("\n\n")
print("STEP 13")
print("------------------------------------------------------------")
print("| v     v     v     v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print("|>[RES]%s" %(RES))
print("------------------------------------------------------------")
print("  Deliver [RES]%s to AMF" %(RES))