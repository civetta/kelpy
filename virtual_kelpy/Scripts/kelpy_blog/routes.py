from kelpy_blog import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
