from flask import Flask,request, render_template, url_for
import model

app = Flask(__name__)
model.init_db()

@app.route("/", methods=["POST","GET"])
def home():
    if  request.method == 'POST':
        if request.form['action'] == 'search':
            action = request.form['action']
            todos = model.show()
            players = request.form.getlist('check')
            # item = request.form['todos[0]']
            item = model.get_score(players)
            return render_template('home.html', todos = todos, action = action, item = item)

        elif request.form['action'] == 'science':
            action = request.form['action']
            todos = model.datasci()
            return render_template('home.html',todos = todos, action = action)

    elif request.method == 'GET':
         return render_template('home.html')




if __name__ == "__main__":
	app.run(debug=True)
