from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print str(request.data)
        return 'thanks'
    else:
        return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

def hello():
    app.run(host='0.0.0.0')