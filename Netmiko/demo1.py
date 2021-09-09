from netmiko import ConnectHandler
import re

device = ConnectHandler(device_type='cisco_xe', ip='192.168.124.11', username='admin', password='admin')
output = device.send_command("show run")

# print(output)

# cfg = ["interface lo1", "ip address 192.168.11.11 255.255.255.255"]
# device.send_config_set(cfg)

# output1 = device.send_command("show ip interface brief")
# print(output1)

device.disconnect()

ospf = r"^router ospf \d+$"
bgp = r"^router bgp \d+$"

is_ospf_enabled = True if re.search(ospf, output, re.MULTILINE) else False
is_bgp_enabled = True if re.search(bgp, output, re.MULTILINE) else False

print("protocols enabled on the router:\n")

if is_ospf_enabled:
    print("OSPF is enabled on the router.")
# else:
#     print("OSPF is not enabled on the router.")
if is_bgp_enabled:
    print("BGP is enabled on the router.")

intf_description = re.finditer(r"^(interface (?P<intf_name>\S+))\n"
                        r"( .*\n)*"
                        r"( description (?P<intf_desc>.*))\n"
                        r"( ip address (?P<ip_address>\S+) (?P<subnet_mask>\S+))\n",
                        output, re.MULTILINE)

for intf_part in intf_description:
    print("=> interface '%s' \n   description : %s \n   IP Address : %s %s \n\n" % (intf_part.group("intf_name"),
                                                                  intf_part.group("intf_desc"), intf_part.group("ip_address"),
                                                            intf_part.group("subnet_mask")))