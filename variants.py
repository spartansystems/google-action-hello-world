from pprint import pprint as pp
import json

yes_no_intents = [
    ("yes", "yes_intent"),
    ("yes i have", "yes_intent"),
    ("i have", "yes_intent"),
    ("i did", "yes_intent"),
    ("they are put away", "yes_intent"),
    ("i did it", "yes_intent"),
    ("i plugged them in", "yes_intent"),
    ("i put away my devices", "yes_intent"),
    ("i put my devices away", "yes_intent"),
    ("i put them away", "yes_intent"),
    ("i put them outside", "yes_intent"),
    ("i put them up", "yes_intent"),
    ("yes i did", "yes_intent"),
    ("they are put away", "yes_intent"),
    ("yes i did it", "yes_intent"),
    ("yes i plugged them in", "yes_intent"),
    ("yes i put away my devices", "yes_intent"),
    ("yes i put my devices away", "yes_intent"),
    ("yes i put them away", "yes_intent"),
    ("yes i put them outside", "yes_intent"),
    ("yes i put them up", "yes_intent"),
    ("i have done it", "yes_intent"),
    ("i have plugged them in", "yes_intent"),
    ("i have put away my devices", "yes_intent"),
    ("i have put my devices away", "yes_intent"),
    ("i have put them away", "yes_intent"),
    ("i have put them outside", "yes_intent"),
    ("i have put them up", "yes_intent"),
    ("i've done it", "yes_intent"),
    ("i've plugged them in", "yes_intent"),
    ("i've put away my devices", "yes_intent"),
    ("i've put my devices away", "yes_intent"),
    ("i've put them away", "yes_intent"),
    ("i've put them outside", "yes_intent"),
    ("i've put them up", "yes_intent"),
    ("yes i've done it", "yes_intent"),
    ("yes i've plugged them in", "yes_intent"),
    ("yes i've put away my devices", "yes_intent"),
    ("yes i've put my devices away", "yes_intent"),
    ("yes i've put them away", "yes_intent"),
    ("yes i've put them outside", "yes_intent"),
    ("yes i've put them up", "yes_intent"),
    ("yep", "yes_intent"),
    ("yep i have", "yes_intent"),
    ("yep i did it", "yes_intent"),
    ("yep i plugged them in", "yes_intent"),
    ("yep i put away my devices", "yes_intent"),
    ("yep i put my devices away", "yes_intent"),
    ("yep i put them away", "yes_intent"),
    ("yep i put them outside", "yes_intent"),
    ("yep i put them up", "yes_intent"),
    ("yep i've done it", "yes_intent"),
    ("yep i've plugged them in", "yes_intent"),
    ("yep i've put away my devices", "yes_intent"),
    ("yep i've put my devices away", "yes_intent"),
    ("yep i've put them away", "yes_intent"),
    ("yep i've put them outside", "yes_intent"),
    ("yep i've put them up", "yes_intent"),
    ("yea", "yes_intent"),
    ("yea i have", "yes_intent"),
    ("yea i did it", "yes_intent"),
    ("yea i plugged them in", "yes_intent"),
    ("yea i put away my devices", "yes_intent"),
    ("yea i put my devices away", "yes_intent"),
    ("yea i put them away", "yes_intent"),
    ("yea i put them outside", "yes_intent"),
    ("yea i put them up", "yes_intent"),
    ("yea i've done it", "yes_intent"),
    ("yea i've plugged them in", "yes_intent"),
    ("yea i've put away my devices", "yes_intent"),
    ("yea i've put my devices away", "yes_intent"),
    ("yea i've put them away", "yes_intent"),
    ("yea i've put them outside", "yes_intent"),
    ("yea i've put them up", "yes_intent"),
    ("yup", "yes_intent"),
    ("yup i have", "yes_intent"),
    ("yup i did it", "yes_intent"),
    ("yup i plugged them in", "yes_intent"),
    ("yup i put away my devices", "yes_intent"),
    ("yup i put my devices away", "yes_intent"),
    ("yup i put them away", "yes_intent"),
    ("yup i put them outside", "yes_intent"),
    ("yup i put them up", "yes_intent"),
    ("yup i've done it", "yes_intent"),
    ("yup i've plugged them in", "yes_intent"),
    ("yup i've put away my devices", "yes_intent"),
    ("yup i've put my devices away", "yes_intent"),
    ("yup i've put them away", "yes_intent"),
    ("yup i've put them outside", "yes_intent"),
    ("yup i've put them up", "yes_intent"),
    ("sure", "yes_intent"),
    ("sure i have", "yes_intent"),
    ("sure i did it", "yes_intent"),
    ("sure i plugged them in", "yes_intent"),
    ("sure i put away my devices", "yes_intent"),
    ("sure i put my devices away", "yes_intent"),
    ("sure i put them away", "yes_intent"),
    ("sure i put them outside", "yes_intent"),
    ("sure i put them up", "yes_intent"),
    ("sure i've done it", "yes_intent"),
    ("sure i've plugged them in", "yes_intent"),
    ("sure i've put away my devices", "yes_intent"),
    ("sure i've put my devices away", "yes_intent"),
    ("sure i've put them away", "yes_intent"),
    ("sure i've put them outside", "yes_intent"),
    ("sure i've put them up", "yes_intent"),
    ("ok", "yes_intent"),
    ("ok i have", "yes_intent"),
    ("ok i did it", "yes_intent"),
    ("ok i plugged them in", "yes_intent"),
    ("ok i put away my devices", "yes_intent"),
    ("ok i put my devices away", "yes_intent"),
    ("ok i put them away", "yes_intent"),
    ("ok i put them outside", "yes_intent"),
    ("ok i put them up", "yes_intent"),
    ("ok i've done it", "yes_intent"),
    ("ok i've plugged them in", "yes_intent"),
    ("ok i've put away my devices", "yes_intent"),
    ("ok i've put my devices away", "yes_intent"),
    ("ok i've put them away", "yes_intent"),
    ("ok i've put them outside", "yes_intent"),
    ("ok i've put them up", "yes_intent"),
    ("no", "no_intent"),
    ("i have not", "no_intent"),
    ("they are not put away", "no_intent"),
    ("i have not done it", "no_intent"),
    ("i have not plugged them in", "no_intent"),
    ("i have not put away my devices", "no_intent"),
    ("i have not put my devices away", "no_intent"),
    ("i have not put them away", "no_intent"),
    ("i have not put them outside", "no_intent"),
    ("i have not put them up", "no_intent"),
    ("they are not put away", "no_intent"),
    ("i have not done it", "no_intent"),
    ("i have not plugged them in", "no_intent"),
    ("i have not put away my devices", "no_intent"),
    ("i have not put my devices away", "no_intent"),
    ("i have not put them away", "no_intent"),
    ("i have not put them outside", "no_intent"),
    ("i have not put them up", "no_intent"),
    ("i've not done it", "no_intent"),
    ("i've not plugged them in", "no_intent"),
    ("i've not put away my devices", "no_intent"),
    ("i've not put my devices away", "no_intent"),
    ("i've not put them away", "no_intent"),
    ("i've not put them outside", "no_intent"),
    ("i've not put them up", "no_intent"),
    ("no i've not done it", "no_intent"),
    ("no i've not plugged them in", "no_intent"),
    ("no i've not put away my devices", "no_intent"),
    ("no i've not put my devices away", "no_intent"),
    ("no i've not put them away", "no_intent"),
    ("no i've not put them outside", "no_intent"),
    ("no i've not put them up", "no_intent"),
    ("nope", "no_intent"),
    ("nope i have not", "no_intent"),
    ("nope i've not done it", "no_intent"),
    ("nope i've not plugged them in", "no_intent"),
    ("nope i've not put away my devices", "no_intent"),
    ("nope i've not put my devices away", "no_intent"),
    ("nope i've not put them away", "no_intent"),
    ("nope i've not put them outside", "no_intent"),
    ("nope i've not put them up", "no_intent"),
    ("nah", "no_intent"),
    ("nah i have not", "no_intent"),
    ("nah i've not done it", "no_intent"),
    ("nah i've not plugged them in", "no_intent"),
    ("nah i've not put away my devices", "no_intent"),
    ("nah i've not put my devices away", "no_intent"),
    ("nah i've not put them away", "no_intent"),
    ("nah i've not put them outside", "no_intent"),
    ("nah i've not put them up", "no_intent"),
]

phrases = [
    "meditation",
    "meditate",
    "visualization",
    "visualize",
    "breathing",
    "breath",
    "gratitude",
    "mind dump",
    "acupressure",
    "music",
    "random",
    "pick one"
]

variations = [
    "",
    "begin ",
    "begin a ",
    "for ",
    "for a ",
    "give ",
    "give me ",
    "give me a ",
    "please give ",
    "please give me ",
    "please give me a ",
    "need ",
    "i need ",
    "please i need ",
    "need a ",
    "i need a ",
    "please i need a ",
    "want ",
    "i want ",
    "please i want ",
    "want a ",
    "i want a ",
    "please i want a ",
    "like ",
    "like to ",
    "i would like to ",
    "please i would like to ",
    "start ",
    "start a ",
    "start me a ",
    "please start ",
    "please start a ",
    "please start me a ",
    "guide ",
    "guide me ",
    "guide me through ",
    "guide me through a ",
    "please guide ",
    "please guide me ",
    "please guide me through ",
    "please guide me through a ",
    "help ",
    "help me ",
    "help me with ",
    "help me with a ",
    "please help ",
    "please help me ",
    "please help me with ",
    "please help me with a ",
    "play ",
    "play a ",
    "play me ",
    "play me a ",
    "please play ",
    "please play a ",
    "please play me ",
    "please play me a ",
    "walk ",
    "walk me through ",
    "walk me through a ",
    "please walk ",
    "please walk me through ",
    "please walk me through a ",
    "i want you to walk ",
    "i want you to walk me through ",
    "i want you to walk me through a ",
]

entities_collection = []
intents_collection = []

for phrase, intent in yes_no_intents:
    entities_collection.append({
        "text": phrase,
        "intent": intent,
        "entities": []
    })
    intents_collection.append({
        "text": phrase,
        "intent": intent,
    })

for variant in variations:
    for phrase in phrases:
        entity_output = {
            "text": variant + phrase,
            "intent": "choose_path",
            "entities": [
                {
                    "start": len(variant),
                    "end": len(variant) + len(phrase),
                    "value": phrase,
                    "entity": "path"
                }
            ]
        }
        intent_output = {
            "text": variant + phrase,
            "intent": "choose_path",
        }
        entities_collection.append(entity_output)
        intents_collection.append(intent_output)

final = {
    "rasa_nlu_data": {
        "entity_examples": entities_collection,
        "intent_examples": intents_collection,
    }
}

# pp(entities_collection)
print json.dumps(final, indent=2)