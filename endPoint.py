from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/question", methods=['POST'])
def endpoint():
    data = request.form
    print(data)
    locationName = str(data['location']).capitalize()
    firstName = str(data['name']).capitalize()
    secondName = str(data['nameTwo']).capitalize()
    outPut = f"""
<!DOCTYPE html>
<html>

<head>

<style>
    .story {{
        border: solid 2px;
        padding: 10px;
        border-radius: 20px;
        background-color:lightcyan;
    }}

    #theStory {{
        position: absolute;
        right: 2.5%;
        left: 2.5%;
        border: solid 2px;
        padding: 10px;
        border-radius: 20px;
        background-color:lightcyan;
        z-index: 2;
    }}

    label {{
        font-size: 1.05em;
    }}

    #whatHaveYouDone {{
        border: solid 2px;
        padding: 10px;
        border-radius: 20px;
        background-color:darkseagreen;
        position: absolute;
        bottom: 15px;
        right: 25px;
        width: 80%;
        z-index: 1;
    }}

    body {{
        background-color:lightsalmon;
    }}
</style>

    <title>Story Time</title>

</head>

<body>

    <h1>
        {locationName} night trip
    </h1>

    <div class="story">
        <p>
            {firstName} and {secondName} wanted to go to the {locationName} at night. However there were {data['job']} workers. {firstName} and {secondName} walked up beside the {data['job']} workers, slowly disipering into the bushes. Once in the darknes they started to run, {secondName} ran dirictly into a {data['forest']}. When they got to the road they saw a {data['colour']} truck speeding tawords them. To avoid the {data['colour']} truck {firstName} and {secondName} hid in the drive way to the {locationName}. When the {data['colour']} truck turned into the drive way to the {locationName} at max speed {firstName} and {secondName} dove into the bushes with a loud crunch. The {data['colour']} truck whent to a full stop, rolled down his window and asked, "People or {data['animal']}?" {firstName} replyd "People", and the truck dive said "Oh Okay", and drove away. {firstName} and {secondName} filany made it to the {locationName} and had a great time, laghing the whole time about their journy.
        </p>
    </div>
        
    <table id="whatHaveYouDone">
        <tr>
            <th class="story">
                <label>
                    Name 1: {firstName}
                </label>
            </th>
            <th class="story" colspan="2">
                <label>
                    Location: {locationName}
                </label>
            </th>
            <th class="story">
                <label>
                    Name 2: {secondName}
                </label>
            </th>
        </tr>

        <tr>
            <th class="story">
                <label>
                    Ocupation: {data['job']}
                </label>
            </th>
            <th class="story">
                <label>
                    Colour: {data['colour']}
                </label>
            </th>
            <th class="story">
                <label>
                    Animal: {data['animal']}
                </label>
            </th>
            <th class="story">
                <label>
                    Forest Object: {data['forest']}
                </label>
            </th>
        </tr>
        
    </div>

</body>

</html>
"""
    return outPut

app.run(port=5000)