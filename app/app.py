from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World from Flask Main Page"

@app.route("/help")
def helppage():
    return "<b><font color=blue>This is Help Page v2!!!</font></b>"


@app.route("/user")
def usermain_page():
    return "User's Main Page"


@app.route("/user/<username>")
def show_user_page(username):
    return "Hello " + username.upper()


@app.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "SubPath is: " + subpath


@app.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
    return "Kvadrat ot: " + str(x) + " = " + str(x*x)


@app.route("/htmlpage")
def show_html_page():
    myfile = open("mypage.html", mode='r')
    page   = myfile.read()
    myfile.close()
    return page


#--------Main------------------
if __name__ == "__main__":
#    application.debug = True
#    application.env   = "Working Hard"
    app.run()
#------------------------------
