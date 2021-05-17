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

### Socket with python

##### 在 ~/mininet/custom/5gAuth 寫入 Client.py

```bash
import socket
host = “10.1.0.2"
port = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    cmd = raw_input("Please input msg:")
    s.send(cmd)
    data = s.recv(1024)
    print(“server send: %s" % (data))
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
    print(“Connected by: ”, addr)
    while True:
        data = c.recv(1024)
        print(“Client recv data: %s" % (data))
        client.send(“ACK!")
```

---

