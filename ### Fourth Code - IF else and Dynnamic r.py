### Fourth Code - IF else and Dynnamic routing ###

from netmiko import ConnectHandler
from getpass import getpass
import string
import os 

os.system("cls")
username = input ("Enter your Username :")
password = getpass("Enter your Password :")
routers = {
    "R1":"192.168.1.8",
    "R3":"192.168.1.9",
    "R2":"192.168.1.10",
}
print (routers)
user_choice = input("Which router :")
user_choice = user_choice.upper()
print(f"Selected router {routers[user_choice]}")

device = {
    "ip": routers[user_choice],
    "device_type":"cisco_ios",
    "username":username,
    "password":password,
}
ssh = ConnectHandler(**device)
print(f"Connection Established with {routers[user_choice]}")

print("Router configuration Utility")
user_input = (int(input("which router protocol: \n1 Static\n2 EIGRP\n3 OSPF\n Please make a choice(1|2|3)")))

if user_input == 1:
    print("Static routing")
    user_input1 = int(input("Number of routes : "))
    for static in range(0, user_input1):
        nw = input("Network : ")
        mask = input("Mask : ")
        nh = input ("Next-hop : ")
        static_route = [f"ip route {nw} {mask} {nh}"]
        static_config = ssh.send_config_set(static_route)
        print(static_config)
elif user_input == 2:
    print ("EIGRP")
    as_num = input("Enter AS Number : ")
    num_nws = int(input("Enter # of Networks : "))
    for eigrp in range ( 0, num_nws):
        nw_id = input("Enter the network : ")
        wc_mask = input("Enter Wildcard Mask : ")
        commands = [f"router eigrp {as_num}", f"network {nw_id} {wc_mask}"]
        eigrp_config = ssh.send_config_set(commands)
        print(eigrp_config)
        show_eigrp = ssh.send_command("show ip protocols")
        print(show_eigrp)
        show_run_eigrp= ssh.send_command("show run | sec eigrp")
        print(show_run_eigrp)
elif user_input == 3:
        print ("Chosen OSPF")
        process_num = input("Enter Process Number : ")
        num_nws = int(input("Enter # of Networks : "))
        area_num = input("Enter Enter Area for above network: ")
        area_type = int(input ("Enter if this aera is 1 for NSSA|2 for Stub|3 for Totally Stub : "))
        if area_type == 1:
             actual_area_type = "nssa"
        elif area_type == 2:
             actual_area_type = "stub"
        else:
            actual_area_type = "stub no-summary"
        for ospf in range ( 0, num_nws):
            nw_id2 = input("Enter the network : ")
            wc_mask = input("Enter Wildcard Mask : ")
            commands = [f"router ospf {process_num}", f"network {nw_id2} {wc_mask} area {area_num}", f"area {area_num} {actual_area_type}"]
            ospf_config = ssh.send_config_set(commands)
            print(ospf_config)
            show_ospf = ssh.send_command("show ip protocols")
            print(show_ospf)
            show_run_ospf = ssh.send_command("show run | sec ospf")
            print(show_run_ospf)
else: 
    print("check your input and restart")