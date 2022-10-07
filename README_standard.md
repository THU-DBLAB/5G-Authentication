# 5G-AKA
> 在 Virtual Box 上建立 Linux 虛擬環境，ubuntu-18.04.5-desktop-amd64.iso / ubuntu-20.04.2.0-desktop-amd64.iso，使用 Mininet 拓樸，使用 Ryu 控制傳輸，模擬 5G 認證過程。  
***
## 環境
> Mac(IOS):  Big Sur 11.1  
| Virtual Application | RAM | hard drive size |
| ---- | ---- | ---- |
| Virtual Box 6.1.16 r140961 | 8192 MB | 20.0 GB |
> Win:  Win10  
| Virtual Application | RAM | hard drive size |
| ---- | ---- | ---- |
| Virtual Box 6.1.16 r140961 | 8192 MB | 20.0 GB |
***
## Ubuntu COPY & PASTE in Virtualbox
1. 安裝元件
```bash
$ sudo apt install dkms build-essential linux-headers-generic
```
2. VirtualBox Menu > Devices > Insert Guest Additions CD images …
3. 關機
```bash
$ shutdown -f now
```
4. VirtualBox > 設定 > 一般 > 進階 > 共用剪貼簿 > 雙向
5. Success!
***
### 1. 安裝 Mininet
> 更新  
```bash
$ sudo apt-get update
```
> 升級  
```bash
$ sudo apt-get upgrade
```
> 安裝 git  
```bash
$ sudo apt-get install -y git
```
> 從 github 上下載 Mininet  
```bash
$ git clone https://github.com/mininet/mininet
```
> 安裝 Mininet  
```bash
$ sudo ./mininet/util/install.sh -n3
```
> 執行 Mininet，測試是否能運行
```bash
$ sudo mn
```
***
### 2. 安裝 Ryu
> 至根目錄  
```bash
cd ~
```
> 安裝所需 package  
```bash
$ sudo apt-get install -y libxml2-dev libxslt1-dev libffi-dev libssl-dev zlib1g-dev python3-pip python3-eventlet python3-routes python3-webob python3-paramiko gcc python3-dev
```
```bash
$ sudo pip3 install msgpack-python eventlet==0.15.2
```
```bash
$ sudo pip3 install six --upgrade
```
```bash
$ sudo pip3 install oslo.config q --upgrade
```
> 從 github 上下載 ryu
```bash
$ git clone https://github.com/faucetsdn/ryu
```
> 至 根目錄/ryu/  
```bash
$ cd ryu
```
> 執行安裝  
```bash
sudo pip3 install .
```
> 測試運行  
```bash
ryu-manager --verbose ryu.app.ofctl_rest
```
***
### 3. 下載教材
> 至 根目錄/mininet/custom/
```bash
$ cd ~/mininet/custom
```
> 從 github 上下載此教材
```bash
$ git clone https://github.com/THU-DBLAB/5G-Authentication.git
```
***
### 4. 安裝 Visual Studio Code
> 方便後續修改程式碼  
> 至[官網](https://code.visualstudio.com/)下載網頁（選.deb），並至 Ubuntu > Downloads > 安裝 code_1.56.2-1620838498_amd64.deb  
***
### 5. 小試身手1，使用python並用socket的方式連結兩個節點
> 開第一個 Terminal 使用 Ryu 控制  
```bash
$ ryu-manager ryu.app.simple_switch_13
```
> 開第二個 Terminal 使用 Mininet 拓樸  
> 先移至方才從 github 下載的教材資料夾內  
```bash
$ cd ~/mininet/custom/5G-Authentication/5G-Auth
```
> 使用教材內的 5G拓樸  
```bash
$ sudo mn --custom 5gtopo.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow13
```
> 在 mininet 輸入，測試所有節點連線是否正常  
```bash
$ pingall
```
> 開啟 UE 與 RAN 的終端機
```bash
$ xterm UE RAN
```
> 在 ~/mininet/custom/5gAuth 寫入 Client.py  
```bash
import socket
host = "10.1.0.2"
port = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    cmd = input("Please input msg: ")
    s.send(cmd.encode('UTF-8'))
    data = s.recv(1024)
    print("server send: %s" % (data.decode('UTF-8')))
```
> 在 ~/mininet/custom/5gAuth 寫入 Server.py  
```bash
import socket
bind_ip = "10.1.0.2"
bind_port = 1
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((bind_ip, bind_port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("Connected by: ", addr)
    while True:
        data = c.recv(1024)
        print("Client recv data: %s" % (data.decode('UTF-8')))
        c.send("ACK!".encode('UTF-8'))
```
> in xterm (RAN) >  
```bash
$ sudo python3 Server.py
```
> in xterm (UE) >  
```bash
$ sudo python3 Client.py
```
***
### 6. 小試身手2，使三個節點能互相連線，並接收發送訊息，封包傳輸時需進行加密動作，節點接收到後，能解密獲得原始訊息
> ദ്ദി ˉ͈̀꒳ˉ͈́ )✧  
***
### 7. 5G-AKA連線
> 第一個 Terminal 開啟 Ryu  
```bash
$ ryu-manager ryu.app.simple_switch_13
```
> 第二個 Terminal 開啟 Mininet  
```bash
$ cd ~/mininet/custom/5G-Authentication/5G-Auth/
```
```bash
$ sudo mn --custom 5gtopo.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow13
```
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSgYbSoBM_JbXdy7bcYkDwohQIFIjIqtbDj59MZfusBraDp9QMHRYxBs0KSsRuVoZgUj69fE7w=w3024-h842)
> 確認拓樸的節點皆有連線成功  
```bash
$ pingall
```
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRziisNew1xsD2H1McwG5dslOa_VKFHrUTK7t2Omgm5A9Dz-f8cPiXmFrWL56ieKr63ZnRAK0g=w3024-h1730)
> 開啟各個節點的終端機  
```bash
$ xterm UE RAN AMF AUSF UDM
```
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmS9SgpGj8KALBMgTH-qB5bv0Zal3hXZ8tSQsd_iTAlw9YhJSzTFmzybq5K0PrV7IBNCIt6Eydg=w3024-h1730)
> 在各個終端機上輸入對應的名稱  
> 在UDM終端機中輸入UDM.py、在AUSF終端機中輸入AUSF.py，依此類推  
```bash
$ sudo python3 UDM.py
```
> 依順序UDM＞AUSF＞AMF＞RAN＞UE的順序按下Enter鍵執行，即可觀察5G-AKA傳遞的步驟  
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQlMIXu3VnKXA923JjUzFR8xP2e9DYESemZEDHQTCEbJIcVwMBlMB_hd9ZOuxT8VeWF6Kef81Q=w3024-h1730)
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTQrtwzEKNZbe8CjMY8tiNabQHkkRHKNYpKYVCXNYh_5Ft7hlreRTnPyN30jN6jTjhz_eEJ3KA=w3024-h842)