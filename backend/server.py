from flask import Flask

app = Flask(__name__)

# Landing page API route
@app.route("/")
def page_test():
    return "Hello welcome to my page"

if __name__ == "__main__":
    app.run(debug=True)

    