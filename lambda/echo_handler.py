import json

def handler(event, context):
    print("EVENTO RECEBIDO:")
    print(json.dumps(event))

    if not event.get("body"):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Request body is required"})
        }

    try:
        body = json.loads(event["body"])
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON"})
        }

    message = body.get("message")

    if not message:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Field 'message' is required"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"echo": message})
    }
