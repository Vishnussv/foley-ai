
# Foleydraco AI Deployment Guide

## 1. Quick Start (Local)
To run Foleydraco easily on this computer, just double-click the **`run_foleydraco.bat`** file in this folder.

## 2. Mobile App (Foleydraco Connection)
You can install the Foleydraco Mobile App on your phone to control this PC.

1.  **Start Foleydraco** on this PC (using `run_foleydraco.bat` or the `.exe` file in `dist`).
2.  **Find your PC's IP**:
    *   The console will show something like: `http://192.168.1.15:5000`
3.  **Open on Phone**:
    *   Open Chrome/Safari on your phone and go to that URL.
4.  **Install App**:
    *   **Android (Chrome)**: Tap the menu (⋮) -> **"Install App"** or "Add to Home Screen".
    *   **iOS (Safari)**: Tap "Share" -> **"Add to Home Screen"**.

This installs a full-screen, native-feeling app that connects directly to your PC.

## 3. Cloud Deployment (Not Recommended)
We do **not** recommend deploying the backend to a cloud server because:
*   The main features (System Volume, Brightness, App Launching) control the **machine running the code**.
*   By running it locally, you get the best of both worlds: Web Interface + Local System Control.
