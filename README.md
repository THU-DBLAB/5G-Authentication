# 5G-Authentication

在 Virtual Box 上建立 Linux 虛擬環境，
ubuntu-18.04.5-desktop-amd64.iso / ubuntu-20.04.2.0-desktop-amd64.iso
使用 Mininet 拓樸，使用 Ryu 控制傳輸，模擬 5G 認證過程。

### 環境：
##### Mac(IOS):  Big Sur 11.1
App:  Virtual Box 6.1.16 r140961
Virtual Box:
RAM:  8192 MB
虛擬硬碟大小:  20.0 GB

##### Win:  Win10
App:  Virtual Box 6.1.16 r140961
Virtual Box:
RAM:  8192 MB
虛擬硬碟大小:  20.0 GB

---

### Ubuntu COPY & PASTE in virtualbox

```bash
# 安裝元件
$ sudo apt install dkms build-essential linux-headers-generic

# VirtualBox Menu > Devices > Insert Guest Additions CD images …

# 關機
$ shutdown -f now

# VirtualBox > 設定 > 一般 > 進階 > 共用剪貼簿 > 雙向

# Success!
```
---

### 下載教材

```bash
$ cd ~/mininet/custom
$ git clone https://github.com/THU-DBLAB/5G-Authentication.git
```

---

### install Visual Studio Code

##### 下載網頁（選.deb），並至 Ubuntu > Downloads > 安裝 code_1.56.2-1620838498_amd64.deb
##### https://code.visualstudio.com/

---

### Socket with python

##### 開第一個 Terminal 使用 Ryu 控制

```bash
$ ryu-manager ryu.app.simple_switch_13
```

##### 開第二個 Terminal 使用 Mininet 拓樸

```bash
$ cd ~/mininet/custom/5G-Authentication/5G-Auth
$ sudo mn --custom 5gtopo.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow13

# mininet > 
$ pingall
$ xterm UE RAN
```

##### 在 ~/mininet/custom/5gAuth 寫入 Client.py

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

##### 在 ~/mininet/custom/5gAuth 寫入 Server.py

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

##### in xterm (RAN) > 

```bash
$ sudo python3 Server.py
```

##### in xterm (UE) > 

```bash
$ sudo python3 Client.py
```

---

