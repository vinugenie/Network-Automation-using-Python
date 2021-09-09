import jinja2
import json
import os

temp_file = "config.j2"
param_file = "data.json"
output_dir = "output"

print("Reading the JSON File for config parameters")
config_params = json.load(open(param_file))

print("Creating Jinja environment")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."), trim_blocks=True, lstrip_blocks=True)
template = env.get_template(temp_file)

print("Creating output directory if it doesn't exist")
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

print("Rendering configuration template....")
for params in config_params:
    result = template.render(params)
    f = open(os.path.join(output_dir, params['hostname'] + "_with_ospf.cfg"), "w")
    f.write(result)
    f.close()
    print("Configuration is created")
print("Done")