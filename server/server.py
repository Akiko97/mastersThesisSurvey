from flask import Flask, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
counter = 0


@app.route('/survey-data', methods=['POST'])
def survey_data():
    global counter
    data = request.json
    # print("收到的问卷数据:", data)
    print(f'received survey data: {counter}')
    filename = f'survey_data_{counter}.json'
    with open(filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    counter += 1

    return jsonify({"message": f"Success: {filename}"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12163, debug=True)
