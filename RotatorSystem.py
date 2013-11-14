import socket
import xml.etree.ElementTree as ET


UDP_IP_Recieve = ''  
UDP_PORT_Recieve = 12040

TCP_IP_Send = "127.0.0.1"
TCP_Port_Send = 91

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_Recieve, UDP_PORT_Recieve))

sendTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "Program Started:"
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    tree = ET.fromstring(data)
    Heading = int(float(tree.find("goazi").text))
    print "Beam Heading at "+ str(Heading) + " Degrees"
    print "Packet Sent :AP1" + "{0:03d}".format(Heading) +";AM1;\r"
    sendTCP.connect((TCP_IP_Send, TCP_Port_Send))
    sendTCP.send("AP1" + "{0:03d}".format(Heading) +";AM1;\r")
    sendTCP.close()
