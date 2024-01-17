from flask import Flask, render_template

app = Flask(__name__)




@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")

@app.route('/bootstrap-grid')
def bootstrap_grid():
    return render_template

@app.route('/name')
def name():
    return "Jiselle Frerichs"

# the homepage for your site will be at the route below
@app.route('/')
def hello_world():
    return """
    <h1>Hello World!</h1> 
    <br />
    Try these links: <br /> 
     - <a href='/home'>home</a><br />
     - <a href='/bootstrap'>bootstrap</a><br />
    """

# Rendering a html template
@app.route('/home')
def home():
    return render_template("home.html")


# Rendering a html template with the Bootstrap framework



if __name__ == '__main__':
    app.run(debug=True)