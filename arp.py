import scapy.all as scapy
import subprocess
print ("""\033[1;32m

 █████╗ ██████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗   ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║   ██╔══██╗██║ ██╔╝
███████║██████╔╝██████╔╝ ╚███╔╝ ███████╗██║     ███████║██╔██╗ ██║   ██████╔╝█████╔╝ 
██╔══██║██╔══██╗██╔═══╝  ██╔██╗ ╚════██║██║     ██╔══██║██║╚██╗██║   ██╔══██╗██╔═██╗ 
██║  ██║██║  ██║██║     ██╔╝ ██╗███████║╚██████╗██║  ██║██║ ╚████║██╗██║  ██║██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                     
""")
print ("""\u001b[34m                                           ARP Spoof Monitoring, Detection and Prevetion Tool
                                                     Deployed By - Kshitij Pawar
                                                     Contact - zeusthunder69420@protonmail.ch
       """)                                              
print ("""\u001b[37m Enter the interface Name :
""")
interfac = input(">> ")
print ("""
Which Connection are you connected to : """)
print("""
 1. Wired
 2. Wireless """)
conn = input (">> ")
import time, sys
def loading():
    print ("""\u001b[36mMonitoring ......
Detecting .....""")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
    
loading()

def extract_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_rb = broadcast/arp_request
    ans_list = scapy.srp(arp_rb, timeout=1, verbose = False) [0]
    return ans_list[0][1].hwsrc
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=proc_packt)
    
def proc_packt(packet):
    if packet.haslayer(scapy.ARP):
        try:
            og_mac = extract_mac(packet[scapy.ARP].psrc)
            recieved_mac = packet[scapy.ARP].hwsrc

            if og_mac != recieved_mac:
                print ("\u001b[31m Under Attack")
                def loading():
                    print ("""\u001b[32mMitigating Attack""")
                    for i in range(0, 100):
                        time.sleep(0.1)
                        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
                        sys.stdout.flush()
                        print
                loading()
                if conn == 1:
                    subprocess.call("""netsh interface set interface "Ethernet 2" admin=disable""", shell=True)
                else:
                    subprocess.call("""netsh interface set interface "Wi-fi" admin=disable""", shell=True)
        except IndexError:
                pass

sniff(interfac)
