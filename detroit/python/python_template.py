import yaml
from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('./templates'))

interfaces = yaml.load(open('interfaces.yml'))
template = ENV.get_template('interfaces.j2')

interfaces_config = template.render(
    interfaces=interfaces
)

print(interfaces_config)


