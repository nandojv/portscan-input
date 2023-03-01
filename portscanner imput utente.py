import nmap
#specificato da utente ip porte e metdo

primo_port_scanner = nmap.PortScanner()
host_scan = input("quale host scansionare? ")
host_port = input("inserisci le porte separate da virgola: ")
#host_type_scan = input ("nserisci tipo di scansione: ")

primo_port_scanner.scan(host_scan, host_port)

#ottenere sansione delle porte qundi manipolare creando un array
array_portList = host_port.split(",")
print(array_portList)
for port in array_portList:
    state = primo_port_scanner[host_scan]["tcp"][int(port)]["state"]
    print("porta: " + str(port) + "stato: " + state)

