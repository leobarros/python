import db
from converters import RegexConverter, ListConverter
from flask import Flask, abort, url_for

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
app.url_map.converters['list'] = ListConverter

@app.route('/')
def index():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            f"<li><a href='{url_for('user',username=username)}'>{user['name']}</a></li>"
        )
        html.append('</ul>')
    return '\n'.join(html)

@app.route('/user/<list:usernames>/', endpoint='user')
def profile(usernames):
    html = ""
    for username in set(usernames):
        user = db.users.get(username)

        if user:
            html += f"""
                <h1>{user['name']}</h1>
                <img src="{user['image']}" /><br/>
                telefone: {user['tel']} <br/>
                <a href="{url_for('index')}">Voltar</a>
                <hr />
            """
    return html or abort(404, "User not found")

@app.route('/user/<username>/<int:quote_id>/')
def quote(username, quote_id):
    user = db.users.get(username, {})
    quote = user.get('quotes').get(int(quote_id))

    if user and quote:
        return f"""
            <h1>{user['name']}</h1>
            <img src="{user['image']}" /><br/>
            <p><q>{quote}</q></p>
            <hr />
        """
    else:
        return abort(404, "User or quote not found")

@app.route('/file/<path:filename>/')
def filepath(filename):
    return f"Argument received: {filename}"

@app.route('/reg/<regex("a.*"):name>/')
def reg(name):
    return f"Argument started with letter a: {name}"

@app.route('/reg/<regex("b.*"):name>/')
def reg_b(name):
    return f"Argument started with letter b: {name}"

# app.add_url_rule('/user/<username>/', view_func=profile, endpoint='user')
        
app.run(use_reloader=True)