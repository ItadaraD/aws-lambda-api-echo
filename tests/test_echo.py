import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.echo_handler import handler

import json


def test_echo_success():
    event = {
        "body": json.dumps({
            "message": "Olá Echo Noir"
        })
    }

    response = handler(event, None)

    assert response["statusCode"] == 200

    body = json.loads(response["body"])
    assert body["message"] == "Olá Echo Noir"
