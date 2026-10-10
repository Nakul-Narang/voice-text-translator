
# Multilingual Voice and Text Translation Utility

A lightweight command-line utility for real-time text and speech translation with automatic source language detection.

Python 3.10+

## Project Overview

### Problem Addressed
Global users and engineering teams often need fast, programmatic translation for text or spoken language without using heavy web applications, complex cloud dashboards, or paid enterprise SDKs for small-scale local tasks.

### Solution and Business Value
This project provides a modular dual-mode command-line interface that accepts both typed text and live microphone input. It automatically detects the source language and translates the content in real time. The utility is designed to support:

- Localization workflows
- Accessibility enhancements
- Multilingual communication tools
- Rapid prototyping and internal productivity use cases

## Key Features

- Dual-mode input: text and live speech
- Automatic language detection
- Real-time translation
- Lightweight CLI-based workflow
- Resilient exception handling for network issues, empty inputs, and poor audio quality

## Technical Stack

- Python 3.10+
- SpeechRecognition
- Googletrans
- Langdetect

## System Requirements

### Required
- Python 3.10 or higher
- A working microphone for speech translation mode
- Internet access for translation services

### Platform Dependency
- Linux/macOS: PortAudio may be required for PyAudio installation

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/voice-text-translator.git
cd voice-text-translator
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

Run the application:

```bash
python translator.py
```

## Usage Examples

### Translate typed text

```bash
python translator.py --text "Hello, how are you?"
```

### Translate spoken input

```bash
python translator.py --speech
```

### Specify source and target languages

```bash
python translator.py --text "Bonjour" --source fr --target en
```

## Project Structure

```text
voice-text-translator/
├── translator.py
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── text_translator.py
│   ├── speech_translator.py
│   └── language_detector.py
```

## Contributing

Contributions are welcome. You can help by:

- Fixing bugs
- Improving language detection accuracy
- Enhancing error handling
- Adding documentation and examples
- Writing tests

##License

This project is licensed under the MIT License.

## Support

For questions or issues, use the GitHub Issues page for the repository.

