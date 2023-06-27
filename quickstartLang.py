import azure.cognitiveservices.speech as speechsdk
import time


import os
import azure.cognitiveservices.speech as speechsdk


def initialize_speech_recognizer(language):
    global speech_recognizer, speech_key, service_region
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = "a9229554d38e4986864ac9c6ed4fb954", "westus"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Set the language for speech recognition
    speech_config.speech_recognition_language = language

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    return speech_recognizer



def on_recognizing(event):
    check_cancel(event.result.text)
   

# def change_language(language):
#     speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=os.environ.get("a9229554d38e4986864ac9c6ed4fb954"), region=os.environ.get("westus"))
#     speech_translation_config.speech_recognition_language = "en-US"

#     target_language = "ar-QA"
#     speech_translation_config.add_target_language(target_language)
#     audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
#     translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)


def on_recognized(event):
    global start_time, current_speaker

    check_cancel(event.result.text)

    if start_time is None:
        start_time = time.time()
        current_speaker = "Speaker 1"
    else:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:
            current_speaker = "Speaker 2"
            start_time = None
        else:

            start_time = time.time()

    print("{}: {}".format(current_speaker, event.result.text))
    

    start_recognition()

def start_recognition(speech_recognizer):
    speech_recognizer.start_continuous_recognition()
    
def check_cancel(text):
    if "cancel" in text.lower():
        speech_recognizer.stop_continuous_recognition()
        print("Speech recognition canceled.")
    
        



        
# to change the language you are talking in:
# pip install azure-cognitiveservices-speech
# def print_languages():
#     supported_languages = ["en-US", "ar-QA"]
#     print("Available languages:")
#     for lang in supported_languages:
#         print(lang)
#     return supported_languages

# def change_language(languageslist):
    
#     global speech_recognizer
#     speech_recognizer.stop_continuous_recognition() 
#     print("Select a language by entering its code:")
#     language_code = input("Language index: ")
#     speech_recognizer = initialize_speech_recognizer(languageslist[int(language_code)])
#     print(speech_recognizer)
#     start_recognition(speech_recognizer)
#     print("Language changed.")
    

#to change the translation of the target language:




initial_language = "en-US"

# Initialize the speech recognizer with the initial language
speech_recognizer = initialize_speech_recognizer(initial_language)

start_time = None  # Tracks the start time of each speaker turn
current_speaker = None  # Tracks the current speaker


# print_supported_languages()
speech_recognizer.recognized.connect(on_recognized)
speech_recognizer.recognizing.connect(on_recognizing)
# print_supported_languages()
print("start recognition: ")
start_recognition(speech_recognizer)

# Keep the program running
while True:
    pass