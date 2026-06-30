from jinja2 import Template

def preare_tmp(filename , data ):
    with open(filename, "r") as file:
        template = Template(file.read())
        output = template.render(data = data)
        return output
