# Adobe Blocker

Adobe Blocker is a free, open-source Python desktop application designed to help you manage access to Adobe domains by modifying your Windows hosts file. The application provides a simple GUI that toggles between blocking and unblocking Adobe servers using a central, online block list that is updated for everyone.

## Features

- **Simple Toggle GUI:**  
  A small main window with a single button that toggles between "Block" and "Unblock". The button resizes and changes color based on its state (red for "Block", green for "Unblock").

- **Centralized Block List:**  
  The application fetches the Adobe block list from an online source (e.g., a GitHub repository) so that any updates are reflected for all users.

- **Automatic Hosts File Management:**  
  Automatically writes or removes the block list contents in the Windows hosts file. The app detects the current state of the hosts file to display the correct button text.

- **Modern UI Theme:**  
  Uses the Sun-Valley ttk theme for a modern look and feel in your tkinter GUI.

## Prerequisites

- **Python 3.x**  
- **Administrative Privileges:**  
  The application needs to be run as an administrator on Windows to modify the hosts file.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/AdobeBlocker.git
   cd AdobeBlocker
   ```

2. **Install Dependencies:**

   Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
AdobeBlocker/              ← Project root folder
├── AdobeBlocker/          ← Python package folder
│   ├── __init__.py
│   ├── config.py
│   ├── gui.py
│   ├── main.py
│   ├── utils.py
│   └── widgets.py
├── data/                  ← Local fallback for Adobe block list
│   └── adobe_block_list.txt
├── img/                   ← Application icons (Adobe.ico)
│   └── Adobe.ico
├── LICENSE
├── README.md
└── requirements.txt
```

## Usage

1. **Run as Administrator:**  
   On Windows, right-click your command prompt or terminal and choose "Run as administrator."

2. **Launch the Application:**

   From the project root, run:

   ```bash
   python -m AdobeBlocker.main
   ```

3. **Toggle Blocking:**  
   Click the button to switch between "Block" and "Unblock". The application will update the Windows hosts file accordingly.

## Configuration

- **Hosts File Path:**  
  The path to your Windows hosts file is defined in `config.py`.

- **Online Block List URL:**  
  Update the `BLOCK_LIST_URL` in `utils.py` with the raw URL from your public repository hosting the Adobe block list.

- **Local Fallback:**  
  In case the online fetch fails, the application falls back to the local block list located in `data/adobe_block_list.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Made by **S0up12**
