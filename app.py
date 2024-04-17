import json

from flask import Flask, render_template, request, jsonify

from linkme import start_scraping

app = Flask(__name__, static_folder='static', template_folder='templates')


# @app.route('/')
# def index():
#     input_data = request.args.get('input_data', '')
#
#     response_data = None
#     if input_data:
#         json_result = start_scraping(input_data)
#
#         response_data = {
#             "summary": "Tyler Reed is a Software Engineer currently based in Tampa, Florida, United States, with experience at JPMorgan Chase & Co. and IBM.",
#             "interesting_facts": [
#                 "Tyler Reed has 337 followers and 287 connections on LinkedIn.",
#                 "Tyler Reed has worked as a Software Engineer at JPMorgan Chase & Co. and IBM."
#             ],
#             "education": [
#                 {
#                     "university": "Frostburg State University",
#                     "degree": "Master's degree in Applied Computer Science",
#                     "duration": "2016 - 2017"
#                 },
#                 {
#                     "university": "Frostburg State University",
#                     "degree": "Bachelor's degree in Computer Science",
#                     "duration": "2011 - 2016"
#                 }
#             ],
#             "activities_count": 12
#         }
#         # start_marker = "json"
#         # end_marker = "`"
#         #
#         # start_pos = json_result.find(start_marker)
#         # end_pos = json_result.find(end_marker, start_pos + len(start_marker))
#         # json_content = json_result[start_pos + len(start_marker):end_pos].strip()
#         # # Process the input data and get a response
#         # response_data = json_content
#         # print(response_data)
#
#     return render_template('index.html', input_data=input_data, response_data=jsonify(response_data))

@app.route('/')
def index():
    input_data = request.args.get('input_data', '')
    response_data = None
    if input_data:
        # Process the input data and get a response
        json_result = start_scraping(input_data)
        start_marker = "json"
        end_marker = "`"

        start_pos = json_result.find(start_marker)
        end_pos = json_result.find(end_marker, start_pos + len(start_marker))
        json_content = json_result[start_pos + len(start_marker):end_pos].strip()

        response_data = json.loads(json_content)

    return render_template('index.html', input_data=input_data, response_data=response_data)


@app.route('/api', methods=['POST'])
def api():
    input_data = request.get_json()['data']
    # Process the input data and get a response
    response_data = {
        "summary": "Tyler Reed is a Software Engineer currently based in Tampa, Florida, United States, with experience at JPMorgan Chase & Co. and IBM.",
        "interesting_facts": [
            "1234123412",
            "543212"
        ],
        "education": [
            {
                "university": "Frostburg State University",
                "degree": "Master's degree in Applied Computer Science",
                "duration": "2016 - 2017"
            },
            {
                "university": "Frostburg State University",
                "degree": "Bachelor's degree in Computer Science",
                "duration": "2011 - 2016"
            }
        ],
        "activities_count": 12
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
