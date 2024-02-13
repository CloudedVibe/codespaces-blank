# main.py
from my_speech_recognition.listener import listen
from speech_synthesis.speaker import speak
from command_processing.processor import process_command

def main():
    try:
        while True:
            # Listen for commands
            command = listen()
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
