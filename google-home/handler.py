import json


def google(event, context):
    msg = """You can ask for a power down by saying, help me power down.
        Would you like to power down now?"""
    reply = {
        "conversation_token": "42",
        "expect_user_response": True,
        "expected_inputs": [
            {
                "input_prompt": {
                    "initial_prompts": [
                        {
                            "text_to_speech": msg,
                        }
                    ],
                    "no_input_prompts": [
                        {"text_to_speech": "Do you want to power down?"},
                        {"text_to_speech": "Do you want to power down again?"},
                        {"text_to_speech": "Really, Do you want to power down?"},
                    ],
                },
                "possible_intents": [
                    {"intent": "com.brianz.YesNoIntent"},
                ]
            }
        ]
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Google-Assistant-API-Version": "v1"
        },
        "body": json.dumps(reply)
    }
    print event
    print response
    return response


def age(event, context):
    body = json.loads(event['body'])
    name = body['inputs'][0]['arguments'][0]['text_value']
    speech = "Hello %s, nice to meet you" % (name, )

    reply = {
      "conversation_token": "42",
        "expect_user_response": False,

        "final_response": {
          "speech_response": {
              "text_to_speech": speech,
          }
        }
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Google-Assistant-API-Version": "v1"
        },
        "body": json.dumps(reply)
    }

    print event
    print response
    return response
