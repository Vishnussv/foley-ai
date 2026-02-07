# Foley AI Assistant - Hologram Edition

This is a Python-based AI assistant with a React-powered "Hologram" interface, created by **Vishnu SSV**.

## Features
- **Voice Activation**: Click "🎙️ VOICE COMMAND" to start listening.
- **Hologram UI**: Animated Arc Reactor interface that reacts to status (Listening, Processing, Speaking).
- **Identity**: Identifies as **Foley**, your high-tech companion.
- **Creator**: Proudly developed by **Vishnu SSV**.
- **Commands**:
  - "Time" / "Date"
  - "Search Wikipedia for [topic]"
  - "Open Google" / "Open YouTube"
  - "Set volume to [0-100]"
  - "Set brightness to [0-100]"
  - "Take screenshot"
  - "Mission Log": "Add [task] to log" or "Show mission log"
  - "Protocols": "Activate Stealth Protocol", "Combat Protocol", etc.

## Setup
The project uses a standard Python virtual environment. Ensure all dependencies are installed via `pip install -r requirements.txt`.

## Running the Application
1. Run the **`run_foleydraco.bat`** file in the root directory.
2. The application will automatically kill old instances and start the server.
3. Access the Hologram Interface at: [http://localhost:5000](http://localhost:5000)

## Mobile Integration
- Click the **📱 MOBILE** button in the HUD.
- Scan the QR code with your phone.
- Use the **⬇ INSTALL APP** button on your mobile browser to add Foley to your home screen.

## Architecture
- **Backend**: Flask + Flask-SocketIO (handling speech, vision, & system ops).
- **Frontend**: React (via CDN) + Modern CSS3 Animations + MediaPipe Hands.
- **AI Core**: Neural Engine with customized system protocols.
