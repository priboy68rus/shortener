from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from data import add_entry, get_entries


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<int:short>")
def short(short):
	if short < len(get_entries()):
		return redirect(get_entries()[short]["link"], code=302)
	else:
		return redirect("/not_found")

@app.route("/not_found")
def not_found():
	return render_template("not_found.html")

@app.route("/new_link", methods=["POST"])
def new_link():
	link = request.form["link"]
	short = int(get_entries()[-1]["short"]) + 1
	add_entry({
		"link": link,
		"short": short
	})
	return render_template("new_link.html", short=short)

if __name__ == "__main__":
	app.run(debug=True)