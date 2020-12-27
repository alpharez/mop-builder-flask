import sys
import yaml
from jinja2 import Environment, FileSystemLoader

env=Environment(loader=FileSystemLoader('.'))
template=env.get_template(sys.argv[1])

with open(sys.argv[2], 'r') as datafile:
    context = yaml.load(datafile)

rendered_template=template.render(**context)
print(rendered_template)
