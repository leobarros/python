from jinja2 import FileSystemLoader, Environment

loader = FileSystemLoader('templates')
env = Environment(loader=loader)
template = env.get_template('homepage.html')


file = open('output/index.html', 'w')
render = template.render(titulo="Teste com jinja", cor_fundo="#000", cor_texto="#fff", nome="Leonardo Barros")
file.write(render)
file.close()