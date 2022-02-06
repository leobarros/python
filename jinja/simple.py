import jinja2

model = "Olá {{ nome }}. Seu e-mail é: {{ email }} e seu estado é {{ estado }}"

usuarios = [
    ["leonardo@fszefs.com", 'Leonardo Barros', 'Rio de Janeiro'],
    ["juzefa@fdsafag.com", "Juzefa Soares", "São Paulo"],
    ["josealdoftavares@gddes.com", "Jose Tavares", "Rio Grande do Sul"],
]

template = jinja2.Template(model)

for dados in usuarios:
    print(template.render(nome=dados[1], email=dados[0], estado=dados[2]))