import colorama
from colorama import Style, Fore, Back
colorama.init(autoreset=True)
"""
Step 06
⑥ [SUCI or SUPI de-concealment], Authentication Method Selection and Generate AV
Key、SN-name、SQN、
以下集結成向量AV：
RAND、XRES*、KAUSF、AUTNUDM(包含SQN⊕AK, AMF, MAC)
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.5",1))
f.listen(5)
c,addr = f.accept()
data6 = c.recv(1024) #SUPI[0:14], sn-name[14:19]
data6 = data6.decode('UTF-8')
SUPI = data6[0:14]
sn = data6[14:19]
print(Back.RED+"STEP 06")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|                          v      v     v")
print(Fore.RED+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"  Get\n"+Fore.GREEN+"  [SUPI]%s" %(SUPI))
print(Fore.GREEN+"  [sn-name]%s" %(sn))
if sn == "10011":
    print(Fore.RED+"  RAN's sn-name is allowed!")
    print(Fore.RED+"  Because SUPI, so use 5G-AKA to authenticate")
    print(Fore.RED+"  Because SUPI, no need to pass to SIDF")
else:
    print(Fore.RED+"--NOT ALLOW!--")
    exit()
print(Fore.RED+"------------------------------------------------------------")
print(Fore.YELLOW+"|      _____________________RAND____________________       |")
print(Fore.YELLOW+"|      |                      |      |      |      |       |")
print(Fore.YELLOW+"|      |   K          AMF___  |   K  |      |   K  |       |")
print(Fore.YELLOW+"|      |   |                | |   |  |      |   |  |       |")
print(Fore.YELLOW+"|      f5__|    ______SQN___|_f1__⊥__f2     f3__⊥__f4      |")
print(Fore.YELLOW+"|      |       |              |      |      |      |       |")
print(Fore.YELLOW+"|      v       |              v      v      v      v       |")
print(Fore.YELLOW+"|      AK_____xor           MAC-A   XRES    CK     IK      |")
print(Fore.YELLOW+"|              |                                           |")
print(Fore.YELLOW+"|              v                                           |")
print(Fore.YELLOW+"|           SQN⊕AK                                         |")
print(Fore.RED+"------------------------------------------------------------")
#Check [SUPI]46697123456789 in ARPF, which Key = 1000000000000001
#Key, a 128-bit subscriber key that is an input to the functions f1, f1*, f2, f3, f4, f5 and f5*.
Key = "1000000000000001"
#RAND, a 128-bit random challenge that is an input to the functions f1, f1*, f2, f3, f4, f5 and f5*.
import random
RAND1 = random.randint(0, 9999999999999999)
RAND1 = "%s" %(RAND1)
RAND1 = RAND1.zfill(16)
RAND2 = random.randint(0, 9999999999999999)
RAND2 = "%s" %(RAND2)
RAND2 = RAND2.zfill(16)
#SQN, a 48-bit sequence number that is an input to either of the functions f1 and f1*.  (For f1* this input is more precisely called SQNMS.)
SQN = "010101"
SQN = str(int(SQN) + 1).zfill(6) #Each time authentication connect, add 1
#AMF, a 16-bit authentication management field that is an input to the functions f1 and f1*.
#AMF, Authentication Management Field. Usage is operator dependent. Bit 0 is “AMF Separation Bit” and is used to in EPS. Bits 1 to 7 are reserved for future standardization use. Bits 8 to 15 are open for proprietary use.
AMF = "10"
print(Fore.RED+"|>"+Fore.GREEN+"[Key]%s" %(Key))
print(Fore.RED+"|>"+Fore.GREEN+"[RAND1]%s" %(RAND1))
print(Fore.RED+"|>"+Fore.GREEN+"[RAND2]%s" %(RAND2))
print(Fore.RED+"|>"+Fore.GREEN+"[SQN]%s" %(SQN))
print(Fore.RED+"|>"+Fore.GREEN+"[AMF]%s" %(AMF))
print(Fore.RED+"------------------------------------------------------------")
import ex
#MAC-A, a 64-bit network authentication code that is the output of the function f1.
MAC_A = ex.f1(Key, RAND1, AMF, SQN)
#RES, a 64-bit signed response that is the output of the function f2.
XRES = ex.f2(Key, RAND1)
#CK, a 128-bit confidentiality key that is the output of the function f3.
CK = ex.f3(Key, RAND1)
#IK, a 128-bit integrity key that is the output of the function f4.
IK = ex.f4(Key, RAND1)
#AK, a 48-bit anonymity key that is the output of either of the functions f5 and f5*.
AK = ex.f5(Key, RAND1)
xor = str(int(SQN)^int(AK)).zfill(8)
K_ausf = ex.KDF("%s%s" %(CK, IK), "%s%s" %(sn, xor))
AUTN = "%s%s%s" %(xor, AMF, MAC_A)
AV = "%s%s%s%s" %(RAND1, XRES, K_ausf, AUTN)
print(Fore.RED+"|>RAND1")
print(Fore.RED+"|>"+Fore.GREEN+"[f1][MAC-A]%s" %(MAC_A))
print(Fore.RED+"|>"+Fore.GREEN+"[f2][XRES]%s" %(XRES))
print(Fore.RED+"|>"+Fore.GREEN+"[f3][CK]%s" %(CK))
print(Fore.RED+"|>"+Fore.GREEN+"[f4][IK]%s" %(IK))
print(Fore.RED+"|>"+Fore.GREEN+"[f5][AK]%s" %(AK))
print(Fore.RED+"------------------------------------------------------------")
print(Fore.RED+"|>"+Fore.GREEN+"[xor]%s" %(xor))
print(Fore.RED+"|>"+Fore.GREEN+"[K_ausf]%s" %(K_ausf))
print(Fore.RED+"|>"+Fore.GREEN+"[AUTN]%s" %(AUTN))
print(Fore.RED+"|>"+Fore.GREEN+"[AV]%s" %(AV))
print(Fore.RED+"------------------------------------------------------------")

"""
Step 07
⑦ Auth. Get Response
Deliver AV, SUPI to AUSF
"""
import time
print("\n\n")
print(Back.CYAN+"STEP 07")
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"|                          v      v")
print(Fore.CYAN+"|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print(Fore.CYAN+"|>"+Fore.GREEN+"[AV]%s" %(AV))
print(Fore.CYAN+"|>"+Fore.GREEN+"[SUPI]%s" %(SUPI))
print(Fore.CYAN+"------------------------------------------------------------")
print(Fore.CYAN+"  Deliver\n"+Fore.GREEN+"  [AV]%s\n  [SUPI]%s" %(AV, SUPI))
print(Fore.CYAN+"  to AUSF")
c.send(AV.encode('UTF-8')) #AV
time.sleep(1)
c.send(SUPI.encode('UTF-8')) #SUPI
time.sleep(1)
#AKMA Ref:https://www.etsi.org/deliver/etsi_ts/133500_133599/133535/16.00.00_60/ts_133535v160000p.pdf
