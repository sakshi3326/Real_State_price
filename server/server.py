from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/hello')
def hello():
    if request.method == 'POST':
         return "hii"
   


if __name__ == "__main__":
    print("server starts for home price prediction")
    app.run()