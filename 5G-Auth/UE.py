import colorama
from colorama import Style, Fore, Back
colorama.init(autoreset=True)
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
print(Back.RED+"STEP 01")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"| v")
print(Fore.RED+"|>UE---RAN---AMF")
print(Fore.RED+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  UE deliver [SUPI]%s to AMF" %(SUPI))
print(Fore.RED+"  , and pass by RAN, then get the [sn-name]10011 from RAN")
data1 = t.recv(1024)
print(Fore.RED+"  UE get [MSG]%s" %(data1.decode('UTF-8')))
print(Fore.RED+"  Connect success!")

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
print(Back.CYAN+"STEP 12")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"| v     v     v     v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.CYAN+"|>"+Fore.GREEN+"[RAND]%s" %(RAND))
print(Fore.CYAN+"|>"+Fore.GREEN+"[AUTN]%s" %(AUTN))
print(Fore.CYAN+"|>"+Fore.GREEN+"[ngKSI]%s" %(ngKSI))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|>"+Fore.GREEN+"[USIM]: Key, SQN")
print(Fore.CYAN+"|>"+Fore.GREEN+"[Key]%s" %(Key))
print(Fore.CYAN+"|>"+Fore.GREEN+"[SQN]%s" %(SQN))
xor = AUTN[0:8]
AMF = AUTN[8:10]
MAC_A = AUTN[10:]
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|>"+Fore.GREEN+"[AUTN]: xor, AMF, MAC-A")
print(Fore.CYAN+"|>"+Fore.GREEN+"[xor]%s" %(xor))
print(Fore.CYAN+"|>"+Fore.GREEN+"[AMF]%s" %(AMF))
print(Fore.CYAN+"|>"+Fore.GREEN+"[MAC-A]%s" %(MAC_A))
#Calculation in UE
import ex
XMAC_A = ex.f1(Key, RAND, AMF, SQN)
RES = ex.f2(Key, RAND)
CK = ex.f3(Key, RAND)
IK = ex.f4(Key, RAND)
AK = ex.f5(Key, RAND)
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.YELLOW+"|      _____________________RAND____________________       |")
print(Fore.YELLOW+"|      |                      |      |      |      |       |")
print(Fore.YELLOW+"|      |   K          AMF___  |   K  |      |   K  |       |")
print(Fore.YELLOW+"|      |   |                | |   |  |      |   |  |       |")
print(Fore.YELLOW+"|      f5__|    ______SQN___|_f1__⊥__f2     f3__⊥__f4      |")
print(Fore.YELLOW+"|      |       |              |      |      |      |       |")
print(Fore.YELLOW+"|      v       |              v      v      v      v       |")
print(Fore.YELLOW+"|      AK_____xor          XMAC-A   RES     CK     IK      |")
print(Fore.YELLOW+"|              |                                           |")
print(Fore.YELLOW+"|             v                                           |")
print(Fore.YELLOW+"|           SQN⊕AK                                         |")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|>"+Fore.GREEN+"[f1][XMAC-A]%s" %(XMAC_A))
print(Fore.CYAN+"|>"+Fore.GREEN+"[f2][RES]%s" %(RES))
print(Fore.CYAN+"|>"+Fore.GREEN+"[f3][CK]%s" %(CK))
print(Fore.CYAN+"|>"+Fore.GREEN+"[f4][IK]%s" %(IK))
print(Fore.CYAN+"|>"+Fore.GREEN+"[f5][AK]%s" %(AK))
print(Fore.CYAN+"------------------------------------------------------------")
if XMAC_A == MAC_A: #data in USIM = data from UDM
    print(Fore.CYAN+"  XMAC = MAC, allow!")
else:
    print(Fore.CYAN+"  XMAC != MAC , NOT ALLOW!")
    exit()

"""
Step 13
⑬ Auth. Response
Deliver RES to SEAF near by AMF
"""
t.send(RES.encode('UTF-8'))
print("\n\n")
print(Back.RED+"STEP 13")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"| v     v     v     v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.RED+"|>"+Fore.GREEN+"[RES]%s" %(RES))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  Deliver [RES]%s to AMF" %(RES))