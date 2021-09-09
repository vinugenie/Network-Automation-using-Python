import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

params = yaml.load(open('data.yaml'), Loader=yaml.FullLoader)

env = Environment(loader=FileSystemLoader(searchpath="."), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('config.j2')

cfg = template.render(params)

with ConnectHandler(ip="192.168.124.11", device_type="cisco_ios", username="admin", password="admin") as ch:
    config_set = cfg.split("\n")
    output = ch.send_config_set(config_set)
    print(output)

