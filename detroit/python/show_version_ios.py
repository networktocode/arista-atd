from netmiko import ConnectHandler

platform = 'cisco_ios'
host = 'csr1'
username = 'ntc'
password = 'ntc123'

device = ConnectHandler(
    device_type=platform,
    ip=host,
    username=username,
    password=password
)

response = device.send_command('show version')

print(response)


