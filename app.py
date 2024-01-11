from flask import Flask, request

app = Flask(__name__)

@app.route('/version', methods=['GET', 'POST'])
def version():
    if request.method == 'POST':
        # Обработка входящего запроса
        data = request.json
        return "Get Data: " + str(data)
    else:
        return "Get request"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)  # Указывайте тот же порт, что и в Docker Compose