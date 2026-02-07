import os
import win32com.client

def create_taskbar_shortcut():
    # Get the desktop path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    path = os.path.join(desktop, "Foley AI.lnk")
    
    # Foley system paths
    target_bat = r"c:\Users\User\.gemini\antigravity\scratch\jarvis_assistant\run_foleydraco.bat"
    workdir = r"c:\Users\User\.gemini\antigravity\scratch\jarvis_assistant"
    icon = r"c:\Users\User\.gemini\antigravity\scratch\jarvis_assistant\foleydraco.ico"

    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    
    # Using cmd.exe as target makes pinning batch files easier on Windows
    shortcut.Targetpath = "C:\\Windows\\System32\\cmd.exe"
    shortcut.Arguments = f'/c "{target_bat}"'
    shortcut.WorkingDirectory = workdir
    shortcut.IconLocation = icon
    shortcut.Description = "Launch Foley AI System"
    shortcut.save()

    print(f"--- SHORTCUT GENERATED ---")
    print(f"Location: {path}")
    print(f"--- INSTRUCTIONS ---")
    print("1. Go to your Desktop.")
    print("2. Right-click the 'Foley AI' icon.")
    print("3. Select 'Pin to taskbar'.")

if __name__ == "__main__":
    create_taskbar_shortcut()
