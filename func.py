import io
import json
import logging

from fdk import response


def handler(ctx, data: io.BytesIO=None):

    try:
        body = json.loads(data.getvalue())
        name = body.get("json_file")
        f = open(name)
        data = json.load(f)
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python function")
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": print(data.values())}),
        headers={"Content-Type": "application/json"}
    )
