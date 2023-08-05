### Third Code - Home work for Static Route###

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

user_input = int(input("Enter the number of static routes required: "))

for interface in range(0,user_input):
    destination = input("Destination: ")
    net_mask = input("Subnet Mask :")
    next_hop  = input("Next Hop :")
     
    commands =[f"ip route {destination} {net_mask} {next_hop}"]
    route_conf = ssh.send_config_set(commands)
    print(route_conf)

route_details = ssh.send_command("show ip route")
print(route_details)
route_details = ssh.send_command("show run | i ip route")
print(route_details)

