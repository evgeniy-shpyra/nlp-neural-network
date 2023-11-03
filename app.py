from flask import Flask, render_template, request, jsonify 
from chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def request_error ():
  return jsonify({"error": "Bad request"}), 400

@app.post("/predict") 
def predict():
  request_data = request.get_json()
  
  if "message" not in request_data:
    return request_error()

  text = request_data["message"]
  
  if not isinstance(text, str):
    return request_error()
  
  response = get_response(text)
  message = {"answer": response}
  return jsonify(message)
  
if __name__ == "__main__":
  app.run(debug=True)