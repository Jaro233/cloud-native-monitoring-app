import psutil
from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_system_metrics():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        yield f"data:{cpu_percent},{memory_percent}\n\n"
        time.sleep(1)

@app.route('/metrics')
def metrics():
    return app.response_class(get_system_metrics(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
