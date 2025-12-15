import json


def handler(event, context):
    print("EVENTO RECEBIDO:")
    print(json.dumps(event))

    if "body" not in event or event["body"] is None:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Request body is required"
            })
        }

    body = json.loads(event["body"])

    if "message" not in body:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Field 'message' is required"
            })
        }

    message = body["message"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message
        })
    }

