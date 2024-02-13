import sounddevice as sd


def choose_microphone():
    devices = sd.query_devices()
    print("Available audio input devices:")
    mic_list = [device for device in devices if device['max_input_channels'] > 0]
    for i, device in enumerate(mic_list):
        print(f"{i}: {device['name']}")

    # Prompt user for microphone selection
    while True:
        try:
            device_index = int(input("Please select a microphone by entering its index: "))
            if 0 <= device_index < len(mic_list):
                return mic_list[device_index]['name'], device_index
            else:
                print("Invalid index, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
