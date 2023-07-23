import logging
import json
import azure.functions as func


# build an azure funtion that returns the contents of arrivals.json file as json
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # read the arrivals.json file
    with open('arrivals.json') as json_file:
        data = json_file.read()
        arrivals = json.loads(data)

    # return the contents of arrivals.json file as json
    return func.HttpResponse(arrivals, mimetype="application/json")



