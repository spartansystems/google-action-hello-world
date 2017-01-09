import json
import random


def google(event, context):
    body = get_request_json(event)
    print body

    intent = get_intent(body)
    raw_query = get_raw_input(body)

    go_to_sleep = """
        Go to sleep, good night and sleep tight.
        <audio src='https://s3.amazonaws.com/thrive-staging-alexa-audio/acupressure.mp3' />
        <audio src='https://s3.amazonaws.com/thrive-staging-alexa-audio/breathe.mp3' />
        <audio src='https://s3.amazonaws.com/thrive-staging-alexa-audio/gratitude.mp3' />
        <audio src='https://s3.amazonaws.com/thrive-staging-alexa-audio/mind_dump.mp3' />
        <audio src='https://s3.amazonaws.com/thrive-staging-alexa-audio/visualize.mp3' />
    """

    if "MAIN" in intent:
        response = initial_state()
    else:
        response = retry_putting_away_devices()
        if ("yes" in raw_query or
            "yea" in raw_query or
            "yup" in raw_query or
            "yep" in raw_query):
            response = tell_response(go_to_sleep)

    payload = format_response(response)
    print payload
    return payload


def get_request_json(event):
    return json.loads(event["body"])


def get_intent(body):
    return body["inputs"][0]["intent"]


def get_raw_input(body):
    return body["inputs"][0]["raw_inputs"][0]["query"]


def ask_response(message, reprompt_1, reprompt_2, no_response):
    return {
        "conversation_token": str(random.randint(0, 100)),
        "expect_user_response": True,
        "expected_inputs": [
            {
                "input_prompt": {
                    "initial_prompts": [
                        {
                            "ssml": "<speak>" + message + "</speak>",
                        }
                    ],
                    "no_input_prompts": [
                        {
                            "ssml": "<speak>" + reprompt_1 + "</speak>",
                        },
                        {
                            "ssml": "<speak>" + reprompt_2 + "</speak>",
                        },
                        {
                            "ssml": "<speak>" + no_response + "</speak>",
                        },
                    ],
                },
                "possible_intents": [
                    {"intent": "assistant.intent.action.TEXT"},
                ]
            }
        ]
    }


def tell_response(message):
    return {
        "conversation_token": str(random.randint(101, 200)),
        "expect_user_response": False,
        "final_response": {
            "speech_response": {
                "ssml": "<speak>" + message + "</speak>"
            }
        }
    }


def format_response(reply):
    return {
        "statusCode": 200,
        "headers": {
            "Google-Assistant-API-Version": "v1"
        },
        "body": json.dumps(reply)
    }


def initial_state():
    message = """
        Welcome to Thrive. To prepare your mind and body for
        sleep. First, turn off your devices and gently escort them outside
        your bedroom. Are your devices put away?
    """
    reprompt_1 = "Are your devices put away?"
    reprompt_2 = "I'm sorry, I didn't hear that. Are your devices put away?"
    no_response = "Let's try again another time"
    return ask_response(message, reprompt_1, reprompt_2, no_response)

def retry_putting_away_devices():
    message = """
        Let's finish putting away your devices.
        Please let me know when you've put your devices away.
    """
    reprompt_1 = "Are your devices put away?"
    reprompt_2 = "I'm sorry, I didn't hear that. Are your devices put away?"
    no_response = "Let's try again another time"
    return ask_response(message, reprompt_1, reprompt_2, no_response)
