from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def p1():
    return render_template('plant 1.html')

@app.route('/2')
def p2():
    return render_template('plant 2.html')

@app.route('/3')
def p3():
    return render_template('plant 3.html')

@app.route('/4')
def p4():
    return render_template('plant 4.html')




if __name__ == '__main__':
    app.run()