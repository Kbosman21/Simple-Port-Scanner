import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port is closed")
    else:
        print("Port is open") 


portScanner(port)

