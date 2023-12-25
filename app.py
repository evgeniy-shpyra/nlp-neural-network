from flask import Flask, render_template, request, jsonify 
from chat import get_response
from flask_cors import CORS, cross_origin
from datetime import datetime

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def request_error ():
  return jsonify({"error": "Bad request"}), 400


@app.post("/predict") 

def predict():
  request_data = request.get_json()
  if "message" not in request_data or "id" not in request_data:
    return request_error()

  text = request_data["message"]
  id = request_data["id"]
  
  if not isinstance(text, str):
    return request_error() 
  
  response = get_response(text, id, True)
  message = {"answer": response, "time": datetime.now()}
  return jsonify(message)
  
  
if __name__ == "__main__":
  app.run(debug=True)