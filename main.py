# main.py
from my_speech_recognition import listen, choose_microphone
from speech_synthesis import speak
from command_processing.processor import process_command

def main():
    try:
        mic_name, mic_index = choose_microphone()  # Let the user choose the microphone
        print(f"Selected microphone: {mic_name}")

        while True:
            # Use the selected microphone for listening
            command = listen(device=mic_index)
            print(f"Command received: {command}")

            # Process command
            response = process_command(command)
            print(f"Response: {response}")

            # Speak out the response
            speak(response)
    except KeyboardInterrupt:
        print("\nJarvis shutting down. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
