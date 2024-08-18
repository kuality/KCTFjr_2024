from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return "/calc?calc=1-1"

@app.route('/calc')
def calc():
    calculate = request.args.get('calc', '1+1')

    if calculate.lower().find("flag") != -1:
        return "no hack!"

    return render_template_string('''{{ %s }}'''% calculate)


app.run(host = '0.0.0.0')