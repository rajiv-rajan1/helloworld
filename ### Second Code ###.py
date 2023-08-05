### Second Code ###

from netmiko import ConnectHandler
from getpass import getpass

username = input ("Enter your Username :")
password = getpass(" Enter your Password :")

routers = {
    "R1":"192.168.1.10",
    "R2":"192.168.1.11",
    "R3":"192.168.1.13",
}

print (routers)
user_choice = input("Which router :")
print(f"Selected router {routers[user_choice]}")

device = {
    "ip": routers[user_choice],
    "device_type":"cisco_ios",
    "username":username,
    "password":password,
}

ssh = ConnectHandler(**device)
print(f"Connection Established with {routers[user_choice]}")

user_input = int(input("Enter the number of interfaces required"))

for interface in range(0,user_input):
    int_name = input("Interface Name :")
    int_ip  = input("Enter IP address :")
    int_mask = input("Enter Mask :")
    
    commands =[f"interface {int_name}",f"ip address {int_ip} {int_mask}","no shut"]
    int_conf = ssh.send_config_set(commands)

int_details = ssh.send_command("show ip int brief")
print(int_details)
