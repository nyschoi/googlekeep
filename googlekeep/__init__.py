from flask import Flask


def create_app():
    print(f'create_app() is called.')

    app = Flask(__name__)  # app

    @app.route('/')
    def index():
        return f'hello flask!!!'

    '''
    routeing practice
    '''
    from flask import jsonify, redirect, url_for
    from markupsafe import escape

    @app.route('/test/name/<string:name>')
    def name(name):
        return f"name is + {name} and type is {escape(type(name))}"

    @app.route('/test/id/<int:id>')
    def id(id):
        return f"id is {id} and type is {escape(type(id))}"

    @app.route('/test/path/<path:subpath>')
    def path(subpath):
        return subpath

    @app.route('/test/json')
    def json():
        return jsonify({'greeting': 'everyone'})

    @app.route('/test/redirect/<path:subpath>')
    def redirect_url(subpath):
        return redirect(subpath)

    @app.route('/test/urlfor/<path:subpath>')
    def urlfor(subpath):
        return redirect(url_for('path', subpath=subpath))

    return app
