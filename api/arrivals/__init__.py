import logging
import json
import os
import azure.functions as func


# build an azure funtion that returns the contents of arrivals.json file as json
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    script_dir = os.path.dirname(__file__)
    # read the arrivals.json file
    with open(os.path.join(script_dir, 'arrivals.json')) as json_file:
        data = json_file.read()
        arrivals = json.loads(data)

    # return the contents of arrivals.json file as json
    return func.HttpResponse(json.dump(arrivals), mimetype="application/json")



