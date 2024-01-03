from flask import Flask, request, send_from_directory, jsonify
import json
import os

app = Flask(__name__, static_folder='dist', static_url_path='/survey')
counter = 0

@app.route('/survey')
@app.route('/survey/<path:path>')
def survey(path='index.html'):
    return send_from_directory(app.static_folder, path)

@app.route('/survey-data', methods=['POST'])
def survey_data():
    global counter
    data = request.json
    # print("收到的问卷数据:", data)
    print(f'received survey data: {counter}')
    filename = f'survey_data_{counter}.json'
    with open(filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    with open('counter', 'w') as file:
        file.write(str(counter))
    counter += 1

    return jsonify({"message": f"Success: {filename}"}), 200


if __name__ == '__main__':
    try:
        with open('counter', 'r') as file:
            line = file.readline()
            try:
                counter = int(line)
                counter += 1
            except ValueError:
                counter = 0
    except FileNotFoundError:
        counter = 0

    app.run(host='0.0.0.0', port=12163, debug=True)
