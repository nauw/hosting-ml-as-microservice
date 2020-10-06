import json

print('Loading function')


def main(event, context):
    body = {
        "message": "With CI/CD in place X attempt",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response


if __name__ == "__main__":
    main('','')