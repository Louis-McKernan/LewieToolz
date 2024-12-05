import ctypes
from ctypes import wintypes

# Define the DEVMODE structure once
class DEVMODE(ctypes.Structure):
    _fields_ = [
        ("dmDeviceName", wintypes.WCHAR * 32),
        ("dmSpecVersion", wintypes.WORD),
        ("dmDriverVersion", wintypes.WORD),
        ("dmSize", wintypes.WORD),
        ("dmDriverExtra", wintypes.WORD),
        ("dmFields", wintypes.DWORD),
        ("dmPositionX", wintypes.LONG),
        ("dmPositionY", wintypes.LONG),
        ("dmDisplayOrientation", wintypes.DWORD),
        ("dmDisplayFixedOutput", wintypes.DWORD),
        ("dmColor", wintypes.SHORT),
        ("dmDuplex", wintypes.SHORT),
        ("dmYResolution", wintypes.SHORT),
        ("dmTTOption", wintypes.SHORT),
        ("dmCollate", wintypes.SHORT),
        ("dmFormName", wintypes.WCHAR * 32),
        ("dmLogPixels", wintypes.WORD),
        ("dmBitsPerPel", wintypes.DWORD),
        ("dmPelsWidth", wintypes.DWORD),
        ("dmPelsHeight", wintypes.DWORD),
        ("dmDisplayFlags", wintypes.DWORD),
        ("dmDisplayFrequency", wintypes.DWORD),
        ("dmICMMethod", wintypes.DWORD),
        ("dmICMIntent", wintypes.DWORD),
        ("dmMediaType", wintypes.DWORD),
        ("dmDitherType", wintypes.DWORD),
        ("dmReserved1", wintypes.DWORD),
        ("dmReserved2", wintypes.DWORD),
        ("dmPanningWidth", wintypes.DWORD),
        ("dmPanningHeight", wintypes.DWORD),
    ]

def get_current_resolution():
    """Retrieve the current screen resolution."""
    user32 = ctypes.windll.user32
    devmode = DEVMODE()
    devmode.dmSize = ctypes.sizeof(DEVMODE)

    # Get the current settings
    if user32.EnumDisplaySettingsW(None, -1, ctypes.byref(devmode)) == 0:
        print("Unable to fetch display settings.")
        return None

    return devmode.dmPelsWidth, devmode.dmPelsHeight

def change_screen_resolution(width, height):
    """Change the screen resolution and center it on the display."""
    user32 = ctypes.windll.user32
    devmode = DEVMODE()
    devmode.dmSize = ctypes.sizeof(DEVMODE)

    # Get the current settings
    if user32.EnumDisplaySettingsW(None, -1, ctypes.byref(devmode)) == 0:
        print("Unable to fetch display settings.")
        return

    # Update the resolution and set centering
    devmode.dmPelsWidth = width
    devmode.dmPelsHeight = height
    devmode.dmFields = 0x00080000 | 0x00100000  # DM_PELSWIDTH | DM_PELSHEIGHT
    devmode.dmDisplayFixedOutput = 2  # DMDFO_CENTER (center the resolution)

    result = user32.ChangeDisplaySettingsW(ctypes.byref(devmode), 1)  # CDS_UPDATEREGISTRY
    if result == 0:  # DISP_CHANGE_SUCCESSFUL
        print(f"Screen resolution changed to {width}x{height}, centered.")
    else:
        print("Failed to change screen resolution.")

if __name__ == "__main__":
    # Get the current resolution
    current_resolution = get_current_resolution()
    if current_resolution:
        print(f"Current resolution: {current_resolution[0]}x{current_resolution[1]}")

    # Example: Change resolution to 1280x720 and center it
    change_screen_resolution(1280, 720)
