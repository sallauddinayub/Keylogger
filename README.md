# Keylogger
# Keylogger with GUI

A Python-based keylogger with a GUI interface developed using `Tkinter` and `pynput`. This project captures keystrokes and logs them to a local file, with the data displayed in real-time on the GUI.

## Features
- **Key Capture**: Monitors all keystrokes entered on the system.
- **Real-time Display**: Captures and shows the keystrokes in the GUI window.
- **Threading**: Ensures smooth and responsive operation without freezing the interface.
- **File Logging**: Stores captured keystrokes in a local file with timestamps.
- **System Persistence**: Optionally, auto-starts on system boot for continuous monitoring (for educational/ethical research use).

## Requirements
- Python 3.x
- `Tkinter` (usually comes pre-installed with Python)
- `pynput` (for capturing keystrokes)

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/keylogger.git
    cd keylogger
    ```

2. Install required libraries:
    ```bash
    pip install pynput
    ```

## Usage
1. Run the script:
    ```bash
    python gulogger.py
    ```

2. The GUI will display the keystrokes in real-time.
3. Press **Start** to begin logging keystrokes and **Stop** to end logging.
4. Logs will be stored in a text file named `keystrokes.log`.

## Ethical Use
This project is for **educational** purposes only. Please ensure you have proper authorization before using this tool on any device. Unauthorized usage may breach privacy laws and ethical standards.

## License
This project is open-source and distributed under the MIT License.

