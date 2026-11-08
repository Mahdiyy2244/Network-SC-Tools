import os
ip_list = ["192.168.1.1", "8.8.8.8", "1.1.1.1"]
for ip in ip_list:
    response = os.system(f"ping -n 1 -w 1000 {ip} > nul")
    if response == 0:
        print(f"IP {ip} is ONLINE")
    else:
        print(f"IP {ip} is OFFLINE")
