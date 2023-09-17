OPENAI_API_KEY = ""
COHERE_API_KEY = ""

TRANSCRIPT_FILE = "communication/transcriptions/transcript.txt"

COMMAND_WORD = "siri"

PROMPT_INSTRUCTIONS = "You are trying to direct a blind man to walk. " \
    "Return the status of the decision below. " \
    "If the person specify the word 'front' or similar, give a '0' as degree. Right is '90' degree, back is '180', left is '270'," \
    " and feel free to give other angle from 0 to 360 if you think it fits the description of the user." \
    "For example, if the user says front-left or any similar command, you can give '315' degree." \
    "Also record down the distance in meter." \
    "Return the result in correct JSON format:"

PROMPT_OUTPUT_FORMAT = """
{
    "direction": "",
    "distance": ""
}
"""