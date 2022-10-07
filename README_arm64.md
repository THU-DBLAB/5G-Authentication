# NEW LOG: 2022-09-28
## INTRODUCTION & OVERVIEW
### 1. Ubuntu 2022 & apple m1 (arm64)
| Virtual Application | Ubuntu Version |
| ---- | ---- |
| [UTM](https://mac.getutm.app) | [Ubuntu Server 22.04.1 LTS](https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.1-live-server-arm64.iso?_ga=2.232931869.2065210953.1664353438-201900941.1664353438) |
> *Ubuntu Server will be installed and upgraded to desktop version after steps.*
### 2. Setup UTM & Ubuntu Server 22.04.1 LTS
> Create a new virtualization at UTM and installs Ubuntu 22.04.1 LTS by selecting ubuntu-22.04.1-live-server-arm64.iso.  
> When setups over, you need to quit the ISO and reboot Ubuntu.  
> Enter your ID, password and installs GUI of Ubuntu as the follow:  
```bash
$ sudo apt-get install ubuntu-desktop
```
> Reboot the virtual system.
```bash
$ sudo reboot
```
### 3. Setup Anaconda
> The python version is 3.10 in Ubuntu 22, but Ryu has to run less than or equal to python 3.9 version, so you can setup Anaconda to choose the python 3.9 version of enviroment.  
> Download: [Anaconda, ARM64](https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-aarch64.sh)  
> Go to the folder where you download and executes process as follow:  
```bash
$ bash Anaconda3-2022.05-Linux-aarch64.sh
```
```bash
$ source ~/anaconda3/bin/activate root
```
```bash
$ anaconda-navigator
```
### 4. Optional
1. Chrome:
> Because this kernel can't run chrome, so chooses the chromium installing.  
```bash
$ sudo apt install --assume-yes chromium-browser
```
2. Visual Studio Code:
> [VScode.deb](https://az764295.vo.msecnd.net/stable/74b1f979648cc44d385a2286793c226e611f59e7/code_1.71.2-1663189619_arm64.deb "ARM64"), then choose the ARM64.  
> Setup it!
***
## Detail of Building Steps
### 01. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTQmF-H9mNQh0D9kDSP5W9HDL3l2IpIqtmlQF-SAXhVIKvCe_25AvDyMVvMBExxeRN5woE33DY=w3024-h1564)
> UTM＞建立新虛擬機  
### 02. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmS9Vw5INKP5647WlpTSJJkwhy7TD19RShBGt-mJC9RfM6Agcwmb0iQcmp482VXAAzIo86jzhe0=w3024-h1730)
> 虛擬化  
### 03. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRIaqX6grI_OGXRoAcOYonV2hrujimlgW_aJ_34T0UgVETdueWixVxwE5pvrzFQ8sbUbEkC3Oc=w3024-h1730)
> Linux  
### 04. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSntFMgQUcjFvK_KLn0R-0kL0HiPrg9nVo5HdQDV4-1vxfY02ROPQKhAf9Qw_p_PIU1sdTtvH8=w3024-h1176)
> 瀏覽  
> ＊點選「下載Ubuntu Server for ARM」可以連結至Ubuntu官網下載ARM架構的Ubuntu，附上連結https://ubuntu.com/download/server/arm  
### 05. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQD2mo5sW6G5l-ji7e-COFSqex_kBHzzCMl_2hJ2b1d-kN7VV0RnDFEAoA3mRDkDill8hlSIv8=w3024-h1730)
> 選擇從Ubuntu官網下載的Ubuntu-22.04.1-live-server-arm64.iso＞下一步  
### 06. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmT924VW3sH-PXNCIg3nxaaOyeqz8ykMdL_XHaqlSNyfwHZbyDHN9WsiQ-x2gEctTXkfDehVRjg=w3024-h1730)
> 我選擇 4096 MB、4 CPU核心數＞下一步＞40GB＞下一步  
> ＊隨使用者電腦硬件自行調整  
### 07. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSo2dTfYfW0J8kaq0O4kMpdcxu-N1T16GcPsrtPfaNLY0oo5Qt0_3WzGQOoIG7dS4sXyOAPKTE=w3024-h1730)
> 下一步  
### 08. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSyvUsLkOjf0Y8wFS35fqcc0W0_I_dCsk8CPsriK4dxBcR6PpC5pDL4zvclpGHxgsIIXLOVbUE=w3024-h1730)
> 名稱隨自己喜歡做調整＞儲存  
### 09. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQO_i27H5yWTAr-zFNYlq8W3XFNYpZAGGufhTUkFRBYE67hhbFeBHL4vP3fEoCad6C16tHivmo=w3024-h1730)
> 點選播放按鈕運行  
### 10. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRjUjrC9hWZg020leZugvg7H7xxKcNHPoYBPJIOxHQSmO1Cc9c8y1-ufhzKrEKMJ8d8YV4BYhY=w3024-h1730)
> Try or Install Ubuntu Server  
### 11. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQbLnIWlYqINSbCP4Dv10sC5QyZai9livDirX5sj0pbVvPMQNdcI8o9DXjE0rUPENUpF5I2RcY=w3024-h842)
> English＞Enter/Done   
### 12. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSw02YtUmy9ctwy5uE4BEG0I86pevxad7p3ZV215LMM9IDl6P5OtWq1yQEjniYO6dQ14g1EqiQ=w3024-h1730)
> (X) Ubuntu Server＞Enter/Done  
### 13. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmS6TCDGZixgn36hzMEBN1wo3Fcf01cXwcm-ouv2TE5Jn_-v2O3TlKrU0MylWHI0_TIvbXFZo9Y=w3024-h842)
> Continue  
### 14. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTtceeE3NBnUMsPABNLAnQdOvCJANeIy4N0Krb0PG71jgRmnjKbPZZyC192xpqml_xlWzHQNYE=w3024-h1730)
> 自行設定內容＞Enter/Done  
### 15. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmT0B7cCKnJ-rWFvDIVDKUwUeTwak55Sbgl4u2QBHj4Ou3TCawk3v3KGud2aEWvmUQF-n6y9NHY=w3024-h1730)
> 等待執行完畢
### 16. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQowdjXcUb9yUZdJFSMydG9Tc8xVK8dfL6Y9rnfe6niIDUsbJjPiNVe80zJKWjcx2mYjy0M0qE=w3024-h842)
> Reboot Now  
### 17. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRDqaSzcP869w-_PyYrkbTHFJ8FH54CACPHSylhSXWrgRXGoaDP8X6-Q1efRueE7w2gQZIs33U=w3024-h1730)
> 之後視窗會變為黑畫面＞選擇此視窗右上方數來第二個icon「Drive image options」＞選擇CD/DVD (ISO)＞退出  
### 18. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmR4KMpuUDARZ1uueUIEx-Tb-seX9U_oLyORCYZImSz8BtvTypl2rgmECnwS6mtqQ9rAOayJcz8=w3024-h842)
> 選擇左上方第三個icon「Restarts the VM」  
### 19. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSS6yCyXISyokG4B5lNTJIr2gdGyqU1lvs3xQOnTEzVudiwGG5tZYk4vgGVD_vWfeyQr3eKzDk=w3024-h842)
> 輸入使用者名稱與密碼  
### 20. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTSIdh5v0xniVs4xA6kFg0zllaxDF-HAtAuspBxtusYcR26oUXtIFKBbyt9DTxAhcZJq1YVvXE=w3024-h1730)
```bash
$ sudo apt-get install ubuntu-desktop
```
> ＊安裝UI介面  
### 21. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSmab5g7s5aYk5fTOhvzpoeffO5QBGj8E4l3X1NHyTWKTO0S8QdqTeWGl8pjozmaK93HMonjPo=w3024-h1730)
> Enter/OK  
### 22. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQZOcmfYIPnsEXC6ZvfSKQAJpOYhnWLw0ki4Uj2990kRKTUQA4cJKR-isiujuSiHuOTKlbhvyQ=w3024-h1730)
```bash
$ sudo reboot
```
### 23. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTWCBykEf-ULBvn7ieFWqarMy6o08_FLAd2S5oNbfc0V8qEAGxEPjNTCrIEtCkeH9bxwDhEvrw=w3024-h1730)
> 輸入密碼  
### 24. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmShs5RwqGDfPbWsmmbsr9RcKLP9h-NCxvDLgK8OJHgs2hCedWhZCzbaO-Uk_C31Apr7p937W4g=w3024-h1730)
```bash
$ sudo apt-get update
```
```bash
$ sudo apt-get upgrade
```
> ＊更新並升級系統  
### 25. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSg6SVDLAcHA0n3V55k5vJJk8W-TQBf71H8Gp5XrgDSnLdYyl4-55x2HwikqXLuL3kGda7VCac=w3024-h842)
```bash
$ sudo apt-get install --assume-yes chromium-browser
```
> ＊安裝Chromium瀏覽器  
### 26. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQ9xDPgAorINapLmCiHstinvZkG6lTt_P_4sBtqQktdETTKFsf3CzwTeOAWbS321iGQ5LLHWxw=w3024-h1730)
> 好了會重新登入Ubuntu＞Enter/OK  
### 27. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSPZDy_EqPZXekXdPU-yoWfG8DWBWVIFtED2Ilus-Qc5NmDgyyU_dfq1iukb8hVpj9qBqvUtaM=w3024-h1730)
```bash
$ sudo passwd root
```
> ＞輸入想要的root密碼＞再次輸入想要的root密碼  
> ＊建制root密碼  
### 28. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQH8efATmCJhwTxtMSNmjJoIbJngjQSBMwq0DPSt3XCDE743z8D3kWm1yNMwhe-mI6MkL7dpEw=w3024-h842)
> 至Anaconda官網下載Linux ARM 64的版本（鼠標位置）＞右鍵＞save link as ...＞內建位置（Downloads）  
> ＊由於內建安裝的python為3.10.6版本，導致接下來運行的作業環境安裝不了，我使用Anaconda來建制python3.9的環境  
### 29. 
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmT5TYEFFiUA8TftY_-WHvn8MWjl3kFKE1hvmNmvqzL6W-8BqSKFd8poljCOBxQymOI9-qb84vA=w3024-h842)
> 在Downloads開啟Terminal  
### 30.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSYKyx1jqsVgB3ZV0SF0wq2pIk4PzQIDvKbiERAb1cLup1hfqaTPiheYhXbfxIciTMIy-zGSX8=w3024-h1730)
```bash
$ bash Anaconda3-2022.05-Linux-aarch64.sh
```
> ＞Enter＞yes  
### 31.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmS6gv7A21-711O_hlq1KdXAVA8PI3924uA702QFA1lOoo73vn6gV4cCvdwFf7d27Cq7uDHDcrQ=w3024-h1730)
```bash
$ sudo apt update
```
```bash
$ sudo apt upgrade
```
### 32.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTQPsgo9fvr-wKQAXiHmU9pnY_gLVHKH5uP6Nb2JsaUbiTpPI0OKy_nF1R_YRzpyDqj1YSASig=w3024-h1730)
```bash
$ source ~/anaconda3/bin/activate root
```
> ＊使用root執行  
```bash
$ anaconda-navigator
```
> ＊執行Anaconda，若需要更新則更新它，Lunch Navigator  
### 33.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTXVn12BQIEBsMMtFOlhYJzSJsP9dwFdnn9RG9gWVh1jFdz7I9eAdtaf8Gz3fOsEtesGzg6YCY=w3024-h1730)
> 選擇鼠標位置Environments  
### 34.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTy6bASkh0UAJRufMRg6OTgINAAqIo4H9dBxvMq9mEEmPVHhIIUhu4hV7kinSJa-0Bzv2_X4lo=w3024-h842)
> Open Terminal  
### 35.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQUMZlS4rlVAcp1Ac4Gu0IhZE1ivO7UzHKl-XCuY-pUX_mkkNTWLRFure637Vl9kI-cOMoNHcc=w3024-h842)
> 確認一下python的版本，為我們所需要的3.9  
### 36.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQYDdSgTlaxEgYOY1kaSU2xC1ReXCbaK1WtjR1w2iuipxH0490vc0MVV8ZTnqdb7H2goxu6yA0=w3024-h1730)
```bash
$ sudo apt-get update
```
```bash
$ sudo apt-get upgrade
```
```bash
$ sudo apt-get install -y git
```
```bash
$ git clone https://github.com/mininet/mininet
```
```bash
$ sudo ./mininet/util/install.sh -n3
```
```bash
$ sudo apt-get install openvswitch-switch
```
```bash
$ sudo mn
```
> ＊安裝Mininet，目的為建立拓樸，確認是否能使用，如圖所示  
### 37.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQTeXmGJ-9sN3afmMxaWmhbVKnC2zDWxWtaN2PvLhYKEvtGgWTqKoqb3DbhY4wRY2hMwFiqD_E=w3024-h842)
```bash
$ exit
```
> ＊退出mininet，接下來為安裝Ryu準備  
```bash
$ sudo apt-get install -y libxml2-dev libxslt1-dev libffi-dev libssl-dev zlib1g-dev python3-pip python3-eventlet python3-routes python3-webob python3-paramiko gcc python3-dev
```
```bash
$ pip3 install msgpack-python eventlet==0.15.2
```
```bash
$ pip3 install six --upgrade
```
```bash
$ pip3 install oslo.config q --upgrade
```
### 38.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQRhF1RPIWPAAGW9IL59rTKM2JC0jzdfMcehG4RtDFI7vpkEsWeM4DsxbWyZFRVqJrbK4F37Lg=w3024-h842)
```bash
$ cd ~
```
```bash
$ git clone https://github.com/faucetsdn/ryu
```
```bash
$ cd ryu
```
```bash
$ pip3 install .
```
```bash
$ ryu-manager --verbose ryu.app.ofctl_rest
```
> ＊安裝Ryu，並且試運行  
### 39.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTZgInV9mZVIXH6t_G9-SAZc-QpBh8ROAR2t9Ub7aTZdqBSC4YyXnSxJ1nItOxo2k8jF2Xkh0g=w3024-h1730)
```bash
$ cd ~/mininet/custom
```
```bash
$ git clone https://github.com/N9daily/5G-Authentication.git
```
> ＊下載我所製作的5G-AKA package，包含5G-AKA所用到的function：UE、RAN、AMF、SEAF、AUSF、UDM，及5G拓樸與加解密ex.py（可以在其中試需求修改加解密辦法）  
### 40.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRwXqb1CD5B0aooyePm4LQxTfXI1kDdqNIrqtYrXax98N3NwCtJi_uY9fBUxgH2aC3gDNWEWTg=w3024-h842)
> 使用Anaconda開啟兩個Terminal  
```bash
$ ryu-manager ryu.app.simple_switch_13
```
> ＊第一個使用Ryu控制器  
```bash
$ cd ~/mininet/custom/5G-Authentication/5G-Auth/
```
```bash
$ sudo mn --custom 5gtopo.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow13
```
> ＊第二個使用Mininet拓樸  
### 41.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSgYbSoBM_JbXdy7bcYkDwohQIFIjIqtbDj59MZfusBraDp9QMHRYxBs0KSsRuVoZgUj69fE7w=w3024-h842)
```bash
$ pingall
```
> ＊確認拓樸的節點皆有連線成功  
### 42.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRziisNew1xsD2H1McwG5dslOa_VKFHrUTK7t2Omgm5A9Dz-f8cPiXmFrWL56ieKr63ZnRAK0g=w3024-h1730)
```bash
$ xterm UE RAN AMF AUSF UDM
```
> ＊開啟各個節點的終端機  
### 43.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmS9SgpGj8KALBMgTH-qB5bv0Zal3hXZ8tSQsd_iTAlw9YhJSzTFmzybq5K0PrV7IBNCIt6Eydg=w3024-h1730)
> 在各個終端機上輸入對應的名稱  
```bash
$ sudo python3 UDM.py
```
> ＊在UDM終端機中輸入UDM.py、在AUSF終端機中輸入AUSF.py，依此類推  
### 44.
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQlMIXu3VnKXA923JjUzFR8xP2e9DYESemZEDHQTCEbJIcVwMBlMB_hd9ZOuxT8VeWF6Kef81Q=w3024-h1730)
![avatar](https://lh3.googleusercontent.com/drive-viewer/AJc5JmTQrtwzEKNZbe8CjMY8tiNabQHkkRHKNYpKYVCXNYh_5Ft7hlreRTnPyN30jN6jTjhz_eEJ3KA=w3024-h842)
> 依順序UDM＞AUSF＞AMF＞RAN＞UE的順序按下Enter鍵執行，即可觀察5G-AKA傳遞的步驟  