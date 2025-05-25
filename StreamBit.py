import serial, threading, time, os

BAUDRATE = 115200

# Mapování příkazů na spuštění aplikací
COMMANDS = {
    'COM_': {  # Replace with what you find in Device Manager under Ports
        'a':  lambda: os.startfile("C:\\"),                      # Replace with your directory, file or program
        'b':  lambda: os.startfile("notepad.exe"),               # Replace with your directory, file or program
        'ab': lambda: os.startfile("calc.exe"),                  # Replace with your directory, file or program
        'logo': lambda: os.startfile(r"C:\Users\OEM"),           # Replace with your directory, file or program
        'p0': lambda: os.startfile(r"D:\Other\hexit.pyw"),       # Replace with your directory, file or program
        'p1': lambda: os.startfile(r"D:\Other\pdf-to-png.pyw"),  # Replace with your directory, file or program
        'p2': lambda: os.startfile(r"D:\Apps"),                  # Replace with your directory, file or program
        'shake': lambda: os.startfile(r"D:\Downloads")           # Replace with your directory, file or program
    },
    'COM_': {  # Replace with what you find in Device Manager under Ports
        'a2':  lambda: os.startfile(r"D:\Apps\Steam\steam.exe"),                        # Replace with your directory, file or program
        'b2':  lambda: os.startfile(r"D:\Apps\Thonny\thonny.exe"),                      # Replace with your directory, file or program
        'ab2': lambda: os.startfile(r"D:\Apps\Angry IP Scanner\ipscan.exe"),            # Replace with your directory, file or program
        'logo2': lambda: os.startfile(r"D:\Apps\OBS\obs-studio\bin\64bit\obs64.exe"),   # Replace with your directory, file or program
        'p02': lambda: os.startfile(r"D:\Apps\Voicemod V3\Voicemod.exe"),               # Replace with your directory, file or program
        'p12': lambda: os.startfile(r"D:\Apps\MultiMC"),                                # Replace with your directory, file or program
        'p22': lambda: os.startfile(r"D:\Apps\Steam\steamapps\common"),                 # Replace with your directory, file or program
        'shake2': lambda: os.startfile(r"D:\Downloads\Songs")                           # Replace with your directory, file or program
    }
}

def handle_microbit(port):
    try:
        ser = serial.Serial(port, BAUDRATE, timeout=1)
        print(f"[{port}] Sending handshake…")
        ser.write(b"test\n")

        # Čekáme na "OK" od micro:bitu
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line == "OK":
                print(f"[{port}] Handshake OK ✔")
                break

        print(f"[{port}] Listening for commands…")
        print("-" * 25)
        while True:
            cmd = ser.readline().decode('utf-8').strip().lower()
            if cmd in COMMANDS[port]:
                print(f"[{port}] Received '{cmd}', executing…")
                try:
                    COMMANDS[port][cmd]()
                    print(f"[{port}] Done.")
                except Exception as e:
                    print(f"[{port}] Error launching app: {e}")
                time.sleep(1)

    except serial.SerialException as e:
        print(f"[{port}] Serial error: {e}")
    except Exception as e:
        print(f"[{port}] Unexpected error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    ports = ['COM_', 'COM_']  # Replace with what you find in Device Manager under Ports
    for p in ports:
        t = threading.Thread(target=handle_microbit, args=(p,), daemon=True)
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting…")
