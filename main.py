from pathlib import Path
import argparse
from openai import OpenAI

MAX_INPUT_LENGTH = 4096  # Maximum allowed input length

def main(input_text, voice="onyx", model="tts-1-hd", output_file="speech.mp3", response_format="mp3"):
    if len(input_text) > MAX_INPUT_LENGTH:
        print("Error: The input text exceeds the maximum allowed character limit (4096).")
        return

    client = OpenAI()
    
    speech_file_path = Path(__file__).parent / output_file
    
    print("Generating speech. Please wait...")

    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=input_text,
        response_format=response_format
    )
    
    response.stream_to_file(speech_file_path)

    print(f"Speech generated and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate speech from text using OpenAI")
    parser.add_argument("input", nargs="?", help="Text input for speech generation (use as positional argument if --text-file is not provided)")
    parser.add_argument("--text-file", help="Path to a text file with input text")
    parser.add_argument("--voice", default="onyx", help="Voice for speech generation (default: onyx)")
    parser.add_argument("--model", default="tts-1-hd", help="Model for speech generation (default: tts-1-hd)")
    parser.add_argument("--output-file", default="speech.mp3", help="Output filename (default: speech.mp3)")
    parser.add_argument("--format", default="mp3", help="Response format (default: mp3)")

    args = parser.parse_args()
    
    if args.text_file:
        with open(args.text_file, 'r') as file:
            input_text = file.read()
    elif args.input:
        input_text = args.input
    else:
        print("Please provide a text file using the --text-file argument or specify the input text as a positional argument.")
        exit(1)

    if len(input_text) > MAX_INPUT_LENGTH:
        print("Error: The input text exceeds the maximum allowed character limit (4096).")
    else:
        main(input_text, args.voice, args.model, args.output_file, args.format)
