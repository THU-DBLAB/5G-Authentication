from mininet.topo import Topo

class Topo1(Topo):
 def __init__(self):
  #Initialize topology
  Topo.__init__(self)

  #add Host and Switch
  #UE
  ue=self.addHost('UE',ip='10.1.0.1')
  ues=self.addSwitch('UEs',dpid='0000000000000001')
  #AMF
  amf=self.addHost('AMF',ip='10.1.0.2')
  amfs=self.addSwitch('AMFs',dpid='0000000000000002')
  #AUSF
  ausf=self.addHost('AUSF',ip='10.1.0.3')
  ausfs=self.addSwitch('AUSFs',dpid='0000000000000003')
  #UDM
  udm=self.addHost('UDM',ip='10.1.0.4')
  udms=self.addSwitch('UDMs',dpid='0000000000000004')

  #add Links
  self.addLink(ue,ues,port1=1,port2=2)
  self.addLink(ues,amfs,port1=1,port2=3)
  self.addLink(amfs,amf,port1=2,port2=1)
  self.addLink(amfs,ausfs,port1=1,port2=3)
  self.addLink(ausfs,ausf,port1=2,port2=1)
  self.addLink(ausfs,udms,port1=1,port2=3)
  self.addLink(udms,udm,port1=2,port2=1)

topos={'mytopo':(lambda:Topo1())}