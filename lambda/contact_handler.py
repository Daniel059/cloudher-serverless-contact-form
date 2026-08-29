import json


def lambda_handler(event, context):

    print("Received event:")
    print(json.dumps(event))

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "success": True,
            "message": "Your message was received successfully!"
        })
    }