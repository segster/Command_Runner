import requests
from modules_and_classes import Restaurant

response = requests.get("https://gitlab.com/api/v4/users/segster/projects")
print(response.json)
print(type(response.json()))


from netmiko import ConnectHandler, redispatch
from netmiko.ssh_exception import NetMikoTimeoutException, NetmikoAuthenticationException
from openpyxl import Workbook
from openpyxl import load_workbook
from getpass import getpass