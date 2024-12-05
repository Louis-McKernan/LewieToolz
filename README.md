# Screen Resolution and Display Configuration Tool

This project provides utilities to manage screen resolution and display configurations on Windows systems. It leverages Windows APIs for direct interaction with display settings and configurations, offering a streamlined interface for tasks such as detecting the current monitor mode, changing screen resolutions, and switching display modes.

## Features

- Detect current monitor configuration (e.g., single, extend).
- Change screen resolution programmatically.
- Switch between display modes (extend, duplicate, single, external).

## Prerequisites

- Python 3.x
- Windows Operating System
- Administrator privileges (required for some operations)

---

## Tools in This Project

### 1. **Screen Resolution Changer**
#### File: `change_resolution.py`
This tool allows you to programmatically change the screen resolution on a Windows machine using the `ChangeDisplaySettingsW` API.

#### Functions:
- `change_screen_resolution(width, height)`: Updates the screen resolution to the specified width and height.

#### Example Usage:
```python
from change_resolution import change_screen_resolution

# Set resolution to 1920x1080
change_screen_resolution(1920, 1080)
