from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='dist', static_url_path='/survey')

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
    counter += 1

    return jsonify({"message": f"Success: {filename}"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12163, debug=True)
