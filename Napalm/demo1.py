import sys
import json
from napalm import get_network_driver
def err_report(*err_list):
    error_msg = ' '.join(str(x) for x in err_list)
    sys.exit(error_msg.rstrip("\n\r"))

# if len(sys.argv) != 3:
#     err_report("Usage: python demo1.py get_config hostname")
# hostname = sys.argv[2]

try:
    with open('hosts.json', 'r') as f:
        device_db = json.load(f)
        # json.loads - this is used when we have json data within the program
        # json.load - is used when we are dealing with json file
except (ValueError, IOError, OSError) as err:
    err_report('Could not read the host file: ', err)

for device in device_db:
    hostname = device["hostname"]
    dev_type = device["type"]
    ip = device["IP"]
    user = device["user"]
    pwd = device["password"]

    driver = get_network_driver(dev_type)
    with driver(ip, user, pwd) as dev:
        cfg = dev.get_config()
        dev.load_merge_candidate(filename='new.cfg')
        diffs = dev.compare_config()
        if diffs != "":
            print(diffs)
            yesno = input('\n Do you wish to apply the changes? [y/n] ').lower()
            if yesno == 'y' or yesno == "yes":
                print("Applying changes...")
                dev.commit_config()
            else:
                print("Discarding changes...")
                dev.discard_config()
        else:
            print("Configuration is already present on the device")
            dev.discard_config()

