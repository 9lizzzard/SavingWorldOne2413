from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
  data = None
  nums = [1, 2, 3, 4, 5]
  with open("intro.txt", "r") as file:
    msg = file.read()
  if request.method == "POST":
    data = request.form["your_name"]
    with open("secret.txt", "a") as file:
      file.write(data + "\n")
  return render_template("index.html", your_name=data, nums=nums, intro=msg)


app.run(host='0.0.0.0', port=81)
