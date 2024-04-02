from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

def get_text_from_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Clearing background noise...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Waiting for your message...')
        recorded_audio = recognizer.listen(source)
        print('Done Recording...')

    try:
        print('Printing the message...')
        text = recognizer.recognize_google(recorded_audio, language='en-US')
        print('Your message: {}'.format(text))
        return text
    except sr.UnknownValueError:
        print('Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def get_text_from_audio_file(file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        print(f'Reading audio file: {file_path}')
        recorded_audio = recognizer.record(source)

    try:
        print('Printing the message...')
        text = recognizer.recognize_google(recorded_audio, language='en-US')
        print('Your message: {}'.format(text))
        return text
    except sr.UnknownValueError:
        print('Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    v = analyzer.polarity_scores(text)
    print(v)

if __name__ == "__main__":
    user_input = input("Choose input method (microphone or file): ").lower()

    if user_input == 'microphone':
        text_from_microphone = get_text_from_microphone()
        if text_from_microphone:
            analyze_sentiment(text_from_microphone)
    elif user_input == 'file':
        audio_file_path = input("Enter the path to the audio file: ")
        text_from_file = get_text_from_audio_file(audio_file_path)
        if text_from_file:
            analyze_sentiment(text_from_file)
    else:
        print("Invalid input method. Please choose 'microphone' or 'file'.")
