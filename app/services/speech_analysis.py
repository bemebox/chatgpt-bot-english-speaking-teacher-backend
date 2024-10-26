import base64
import uuid
import speech_recognition as sr
import language_tool_python
import logging
from app.utils.file_manager import save_file, delete_file
from app.utils.logger import setup_logging

# Ensure the logging is set up once at the beginning of your program
setup_logging()

def recognize_audio_from_base64(base64_audio: str) -> str:
    """
    Decode a base64-encoded audio string, save it as a .wav file, 
    and analyze its quality.

    Parameters:
    - base64_audio (str): A base64-encoded string representing the audio data.

    Returns:
    - str: The result of the audio quality analysis.

    Raises:
    - ValueError: If the provided base64 string is invalid.
    """
    # Initialize a variable to store the audio file path
    audio_file_path = None

    try:
        # Decode the base64 string into raw audio data
        audio_data = base64.b64decode(base64_audio)
        
        # Generate a unique ID for the audio file
        audio_id = str(uuid.uuid4())
        audio_file_path = f"{audio_id}.wav"
        
        # Save the decoded audio data to a file
        audio_file_path = save_file(audio_data, audio_file_path)

        # Analyze the audio for quality
        feedback_text = analyze_audio_quality(audio_file_path)
        return feedback_text  # Return the feedback if successful
    
    except ValueError as e:
        # Raise ValueError with a message if base64 decoding fails
        logging.error(f"ValueError occurred: {e}")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise
    finally:
        # Ensure the temporary audio file is deleted regardless of success or failure
        if audio_file_path:
            try:
                delete_file(audio_file_path)
            except Exception as delete_error:
                # Optionally handle errors that occur during file deletion
                logging.error(f"Failed to delete file {audio_file_path}: {delete_error}")
                pass
        

def analyze_audio_quality(audio_file_path: str) -> str:
    """
    Analyze the audio file for speech quality and provide feedback.

    Args:
        audio_file_path (str): Path to the audio file.

    Returns:
        str: Feedback on the quality of the speech.
    """
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file and recognize speech
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)  # Read the entire audio file
        try:
            # Use Google Web Speech API for recognition
            recognized_text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            raise ValueError("Could not understand audio.")
        except sr.RequestError as e:
            return ValueError(f"Could not request results from Google Speech Recognition service; {e}")

    # Analyze the recognized text for grammar and style issues
    feedback = analyze_text_quality(recognized_text)
    return feedback



def analyze_text_quality(text: str) -> str:
    """
    Analyze the recognized text for grammar and fluency.

    Args:
        text (str): The recognized text to analyze.

    Returns:
        str: Feedback and suggestions for improvement.
    """
    tool = language_tool_python.LanguageTool('en-US')

    # Check for grammar and style issues
    matches = tool.check(text)
    issues = len(matches)

    if issues == 0:
        feedback = "The speech is clear, fluent, and well-formed."
    else:
        feedback = f"There are {issues} issues with grammar and style. Here are some suggestions:\n"
        for match in matches:
            feedback += f"- {match.message} (Suggestion: {', '.join(match.replacements)})\n"

    return feedback