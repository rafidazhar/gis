from flask import Flask, request, jsonify
import csv

app = Flask(__name__, static_folder='static', static_url_path='')

# Load valid codes from CSV
valid_codes = set()
with open('code.csv', newline='') as csvfile:
    code_reader = csv.reader(csvfile)
    for row in code_reader:
        valid_codes.add(row[0])

@app.route('/verify_code')
def verify_code():
    code = request.args.get('code')
    if code in valid_codes:
        return jsonify(valid=True)
    else:
        return jsonify(valid=False)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
