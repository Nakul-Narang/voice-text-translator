

from googletrans import Translator
from langdetect import detect, DetectorFactory
import speech_recognition as sr

# Ensure consistent language detection results
DetectorFactory.seed = 0

def translate_text(text: str, target_language: str) -> str:
   
    if not text.strip():
        raise ValueError("Input text cannot be empty.")
        
    translator = Translator()
    detected_language = detect(text)
    translated = translator.translate(text, src=detected_language, dest=target_language)
    return translated.text

def translate_speech(target_language: str) -> None:
    """Captures microphone input, converts speech to text, and translates it."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            print("Listening... Please speak clearly.")
            recognizer.adjust_for_ambient_noise(source, duration=1.0)
            audio = recognizer.listen(source)

        print("Processing audio...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        
        translated_text = translate_text(text, target_language)
        print(f"Translated Text: {translated_text}")
        
    except sr.UnknownValueError:
        print("Error: Audio was unintelligible. Please try again.")
    except sr.RequestError as e:
        print(f"Error: Could not reach speech recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main() -> None:
    print("=== CLI Multilingual Translation Utility ===")
    input_type = input("Choose input mode [text / speech]: ").strip().lower()
    
    if input_type not in ["text", "speech"]:
        print("Invalid input mode. Please choose either 'text' or 'speech'.")
        return

    target_language = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ").strip().lower()
    if not target_language:
        print("Target language code cannot be empty.")
        return

    if input_type == "text":
        text = input("Enter text to translate: ")
        try:
            result = translate_text(text, target_language)
            print(f"Translated Text: {result}")
        except Exception as e:
            print(f"Translation failed: {e}")
            
    elif input_type == "speech":
        translate_speech(target_language)

if __name__ == "__main__":
    main()
