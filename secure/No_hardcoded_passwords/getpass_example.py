import getpass
from nornir import InitNornir
from nornir.scrapli.tasks import send_command
from nornir.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password

def credential_task(task):
    task.run(task=send_command, command="show ip int brief")

results = nr.run(task=credential_task)
print_result(results)


#remove the password from default config or host or wherever it is.
#this script is binding the default password requests and getting the user to put it in in the terminal.
#there should be no password hardcoded anywhere.