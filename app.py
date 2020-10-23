from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/bad')
def bad():
   temp;
   return "Bad"

   
@app.route('/status')
def status():
   return jsonify({
      'status': 'up'
   })
if __name__ == "__main__":
    app.run(debug=True, port=3000,host='0.0.0.0')