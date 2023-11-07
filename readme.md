
# OpenAI Text-to-Speech Script

## A python script to generate open AI's text-to-speech audio files.

This Python script uses the OpenAI API to generate speech from text. It allows you to specify the input text, voice, and model for speech generation. Additionally, you can provide the input text from a text file.

## Prerequisites

Before using this script, make sure you have the following:

1. Python 3.7 or later installed on your system.
2. An OpenAI account with API access credentials. You can sign up for an account and get your API key from the [OpenAI website](https://beta.openai.com/).

## Installation

1. Clone this repository or download the script.

2. Install the required dependencies using [Pipenv](https://pipenv.pypa.io/en/latest/):

   ```bash
   pipenv install

3. set your OpenAI API key as an environment variable:

    ```bash
        export OPENAI_API_KEY=your_api_key_here
    ```

## Usage

You can use the script to generate speech with the following options:

--text-file: Specify the path to a text file containing the input text.

--voice: (Optional) Choose a voice for speech generation (default: onyx). Available voices are (alloy, echo, fable, onyx, nova, and shimmer)

--model: (Optional) Specify the model for speech generation (default: tts-1-hd). 'tts-1' is cheaper and lower quality.

--output-file: (Optional) Specify the path to save the generated audio file.

--format: (Optional) Specify the format of the generated audio file (default: mp3). Available formats are (mp3, opus, flac, and aac).

**Note:** The input text shouldn't exceed **4096** characters. Split the input text into smaller chunks if necessary.

### Example Usages:

Generate speech from text:

```bash
pipenv run python your_script.py "Your text input"
```

Generate speech from text file with a custom voice and model:

```bash
pipenv run python your_script.py --text-file "input.txt" --voice "custom_voice" --model "custom_model"
```