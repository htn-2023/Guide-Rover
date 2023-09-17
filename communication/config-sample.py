# rename this file to config.py and fill in the values below
OPENAI_API_KEY = "key"

TRANSCRIPT_FILE = "communication/transcriptions/transcript.txt"

COMMAND_WORD = "whisper"

PROMPT_INSTRUCTIONS = "You are trying to direct a blind man to walk. " \
    "Return the status of the decision below. " \
    "If the person specify the word 'front' or similar, give a '0' as degree. Right is '90', left is '270', and feel free to give other angle from 0 to 360 if you think it fits the description of the user." \
    "Also record down the distance in meter." \
    "Return the result in JSON format:"

PROMPT_OUTPUT_FORMAT = """
{
    "direction": "",
    "distance": "",
}
"""