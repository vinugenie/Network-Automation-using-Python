from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
res = nr.run(napalm_get, getters=['get_facts'])

print_result(res)

