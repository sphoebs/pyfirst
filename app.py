from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Wefdfdsfdsfslcome!"



@app.route("/yoursister")
def yoursister():
    return "sister!"


if __name__ == "__main__":
    app.run()

