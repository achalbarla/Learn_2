import socket
def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print ("Port: %s => service name: %s" %(port,socket.getservbyport(port, protocolname)))
        print ("Port: %s => service name: %s" %(53,socket.getservbyport(53, 'udp')))
        print ("Port: %s => service name: %s" % (21, socket.getservbyport(21, 'tcp')))
        print ("Port: %s => service name: %s" % (21, socket.getservbyport(22, 'tcp')))
        print ("Port: %s => service name: %s" % (21, socket.getservbyport(110, 'tcp')))

if __name__ == '__main__':
    find_service_name()