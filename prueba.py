from jinja2 import Template

# Definir una plantilla
template_str = "Hola {{ nombre }}!"

# Crear un objeto de plantilla
template = Template(template_str)

# Renderizar la plantilla con datos específicos
resultado = template.render(nombre="Pacooo")

print(resultado)  # Esto imprimirá: Hola Juan!
