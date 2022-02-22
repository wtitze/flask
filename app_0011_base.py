from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def backgroundColor():
  ora = datetime.datetime.now().hour
  if ora < 12:
    return render_template("index11.html", Titolo='Welcome', Testo='Hello, world!', Colore='yellow')
  elif ora < 20:
    return render_template("index11.html", Titolo='Welcome', Testo='Hello, world!', Colore='orange')
  else:
    return render_template("index11.html", Titolo='Welcome', Testo='Hello, world!', Colore='blue')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)