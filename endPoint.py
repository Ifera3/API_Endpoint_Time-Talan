from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/question", methods=['POST'])
def endpoint():
    data = request.form
    print(data)
    #outPut = f"<h1>hello, {data['name']}<h1>"
    outPut = f"""
<!DOCTYPE html>
<html>

<head>

    <title>Story Time</title>

</head>

<body>

    <h1>
        {data['location']} trip
    </h1>

    <p>
        Hello {data['name']}
    </p>

</body>

</html>
"""
    return outPut

app.run(port=5000)