from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("indextemplates.html", Ora=datetime.datetime.utcnow())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/comments')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

@app.route('/commentsif')
def commentsif():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('commentsif.html', comments=comments)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)