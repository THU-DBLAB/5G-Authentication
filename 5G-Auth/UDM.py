"""
Step 06
⑥ [SUCI or SUPI de-concealment], Authentication Method Selection and Generate AV
Key、SN-name、SQN、
以下集結成向量AV：
RAND、XRES*、KAUSF、AUTNUDM(包含SQN⊕AK, AMF, MAC)
"""
import socket
f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(("10.1.0.4",1))
f.listen(5)
c,addr = f.accept()
data6 = c.recv(1024) #SUPI[0:14], sn-name[14:19]
data6 = data6.decode('UTF-8')
SUPI = data6[0:14]
sn = data6[14:19]
print("STEP 06")
print("------------------------------------------------------------")
print("|                          v      v     v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print("|>[SUPI]%s" %(SUPI))
print("|>[sn-name]%s" %(sn))
print("------------------------------------------------------------")
if sn == "10011":
    print("  RAN's sn-name is allowed!")
    print("  Because SUPI, so use 5G-AKA to authenticate")
else:
    print("--NOT ALLOW!--")
    exit()
print("------------------------------------------------------------")
print("|      _____________________RAND____________________       |")
print("|      |                      |      |      |      |       |")
print("|      |  Key         AMF___  |  Key |      |  Key |       |")
print("|      |   |                | |   |  |      |   |  |       |")
print("|      f5__|    ______SQN___|_f1__⊥__f2     f3__⊥__f4      |")
print("|      |       |              |      |      |      |       |")
print("|      v       |              v      v      v      v       |")
print("|      AK_____xor           MAC-A   XRES    CK     IK      |")
print("|              |                                           |")
print("|              v                                           |")
print("|           SQN⊕AK                                         |")
print("------------------------------------------------------------")
#Because transfer of data = SUPI, no need to pass to SIDF
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
print("|>[Key]%s" %(Key))
print("|>[RAND1]%s" %(RAND1))
print("|>[RAND2]%s" %(RAND2))
print("|>[SQN]%s" %(SQN))
print("|>[AMF]%s" %(AMF))
print("------------------------------------------------------------")
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
print("|>RAND1")
print("|>[f1][MAC-A]%s" %(MAC_A))
print("|>[f2][XRES]%s" %(XRES))
print("|>[f3][CK]%s" %(CK))
print("|>[f4][IK]%s" %(IK))
print("|>[f5][AK]%s" %(AK))
print("------------------------------------------------------------")
print("|>[xor]%s" %(xor))
print("|>[K_ausf]%s" %(K_ausf))
print("|>[AUTN]%s" %(AUTN))
print("|>[AV]%s" %(AV))
print("------------------------------------------------------------")

"""
Step 07
⑦ Auth. Get Response
Deliver AV, SUPI to AUSF
"""
import time
print("\n\n")
print("STEP 07")
print("------------------------------------------------------------")
print("|                          v      v")
print("|>UE---RAN---AMF---SEAF---AUSF---UDM---ARPF")
print("|>[AV]%s" %(AV))
print("|>[SUPI]%s" %(SUPI))
print("------------------------------------------------------------")
print("  Deliver [AV]%s,\n  [SUPI]%s\n  to AUSF" %(AV, SUPI))
c.send(AV.encode('UTF-8')) #AV
time.sleep(2)
c.send(SUPI.encode('UTF-8')) #SUPI
time.sleep(1)
#AKMA Ref:https://www.etsi.org/deliver/etsi_ts/133500_133599/133535/16.00.00_60/ts_133535v160000p.pdf
