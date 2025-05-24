import serial
import threading
import time
import os

BAUDRATE = 115200

# Mapping commands to application launches
COMMANDS = {
    'COM_': {   # Set your port here (find it in Device Manager under Ports)
        'a':  lambda: os.startfile("C:\\"),         # Replace with a directory, program, etc.
        'b':  lambda: os.startfile("notepad.exe"), # Replace with a directory, program, etc.
        'ab': lambda: os.startfile("calc.exe")     # Replace with a directory, program, etc.
    },
    'COM_': {   # Set your second port here (find it in Device Manager under Ports)
        'a2':  lambda: os.startfile(r" "),  # Replace with a directory, program, etc.
        'b2':  lambda: os.startfile(r" "),  # Replace with a directory, program, etc.
        'ab2': lambda: os.startfile(r" ")   # Replace with a directory, program, etc.
    }
}

def handle_microbit(port):
    try:
        ser = serial.Serial(port, BAUDRATE, timeout=1)
        print(f"[{port}] Sending handshake…")
        ser.write(b"test\n")

        # Wait for "OK" response from micro:bit
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
    ports = ['COM_', 'COM_']  # Set your ports here (find them in Device Manager under Ports)
    for p in ports:
        t = threading.Thread(target=handle_microbit, args=(p,), daemon=True)
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting…")
