from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/api/meow", methods=["POST"])
def receive_cheep():
	print(request.form)
	return "Success!"

if __name__ == "__main__":
    app.run()