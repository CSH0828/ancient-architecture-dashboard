# app.py
from flask import Flask, render_template
from data import ArchitectureData

app = Flask(__name__)

@app.route('/')
def index():
    data = ArchitectureData()
    return render_template('index.html', form=data, title=data.title)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
