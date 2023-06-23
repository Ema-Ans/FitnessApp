
# # </code>

import azure.cognitiveservices.speech as speechsdk

speech_key = "a9229554d38e4986864ac9c6ed4fb954"
service_region = "westus"


speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the buffer size in milliseconds (e.g., 50 ms)
buffer_size_ms = 100
speech_config.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, str(buffer_size_ms))
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
def on_recognizing(event):
    print("Recognizing: {}".format(event.result.text))
    check_cancel(event.result.text)

def on_recognized(event):
    print("Recognized: {}".format(event.result.text))
    check_cancel(event.result.text)
    start_recognition()
    

def start_recognition():
    print("Say something...")
    speech_recognizer.start_continuous_recognition()

def check_cancel(text):
    if "cancel" in text.lower():
        speech_recognizer.stop_continuous_recognition()
        print("Speech recognition canceled.")
        
speech_recognizer.recognizing.connect(on_recognizing)
speech_recognizer.recognized.connect(on_recognized)

print("Say something...")

start_recognition()

# Keep the program running
while True:
    pass

