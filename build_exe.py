import PyInstaller.__main__
import os
import sys
from PyInstaller.utils.hooks import collect_submodules

# Get the directory of the current script
base_dir = os.path.abspath(os.path.dirname(__file__))

# Define data files
# Format: ('source', 'destination')
# On Windows, use semi-colon ';' to separate source and destination for PyInstaller
data_files = [
    (os.path.join(base_dir, 'backend', 'templates'), 'backend/templates'),
    (os.path.join(base_dir, 'backend', 'static'), 'backend/static'),
]

# Build command parts
params = [
    os.path.join(base_dir, 'backend', 'app.py'),
    '--onefile',
    '--noconsole',  # Hide the terminal window
    '--icon', os.path.join(base_dir, 'foleydraco.ico'),
    '--name', 'FoleyAI',
    '--hidden-import', 'flask_socketio',
    '--hidden-import', 'eventlet',
    '--hidden-import', 'eventlet.hubs.epolls',
    '--hidden-import', 'eventlet.hubs.kqueue',
    '--hidden-import', 'eventlet.hubs.poll',
    '--hidden-import', 'eventlet.hubs.selects',
    '--hidden-import', 'engineio.async_drivers.eventlet',
]

# Add all dns submodules to hidden imports
dns_hidden_imports = collect_submodules('dns')
for module_name in dns_hidden_imports:
    params.append('--hidden-import')
    params.append(module_name)

# Add data files
for src, dst in data_files:
    params.append(f'--add-data={src}{os.pathsep}{dst}')

# Run PyInstaller
PyInstaller.__main__.run(params)
