from flask import Flask
app = Flask(__name__)

@app.route('/your_flask_funtion')

def get_ses():
    print('Hello')

if __name__ == '__main__':
   app.run()