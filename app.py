from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name=request.args.get("name","World")
    return render_template('index.html', placeholder=name)
@app.route("/game", methods=["POST"])
def play_game():
    name=request.form.get("user_name")
    game=request.form.get("game")
    return render_template("game.html",name=name,game=game)

if __name__=='__main__':
    app.run(debug=True)