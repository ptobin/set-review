from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/video/<name>')
def video(name):
  # get signed url


  return render_template("video.html", name=name)

@app.route('/deliver')
def deliver():
  return render_template("deliver.html")

@app.route('/detect')
def detect():
  return render_template("detect.html")

@app.route('/intro')
def intro():
  return render_template("intro.html")

@app.route('/config')
def config():
  return render_template("config.html")

@app.route('/demo')
def demo():
  return render_template("main.html")


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template("intro.html")
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
