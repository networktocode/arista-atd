import yaml
from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('./templates'))

interfaces = yaml.load(open('interfaces.yml'))
template = ENV.get_template('interfaces.j2')

interfaces_config = template.render(
    interfaces=interfaces
)

destination_file = 'interfaces.cfg'

print('#'* 50)
print('Generating Configuration')

with open(destination_file, 'w') as f:
    f.write(interfaces_config)

print('#' * 50)
print('Configuration output to {}'.format(destination_file))