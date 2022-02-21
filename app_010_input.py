from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        return render_template('data.html',form_data = request.form)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)