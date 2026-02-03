from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []
total = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global expenses, total

    if request.method == "POST":
        date = request.form["date"]
        name = request.form["name"]
        amount = float(request.form["amount"])


        expenses.append({
            "date": date,
            "name": name,
            "amount": amount
        })

        total += amount

    return render_template("index.html", expenses=expenses, total=total)

@app.route("/reset", methods=["POST"])
def reset():
    global expenses, total
    expenses = []
    total = 0
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

