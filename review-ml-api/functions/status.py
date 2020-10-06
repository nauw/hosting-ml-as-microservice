import json

print('Loading function')


def main(event, context):
    body = {
        "message": "With CI/CD in place X attempt",
        "input": event
    }

    response = {
        "headers":{
          "Content-Type":"application/json"  
        },
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response


if __name__ == "__main__":
    main('','')