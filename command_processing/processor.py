def process_command(command):
    if command is None:
        return "I didn't catch that. Could you please repeat?"
    # Simple command processing logic
    elif "how are you" in command.lower():
        return "I'm doing well, thank you!"
    elif "weather" in command.lower():
        return "It looks sunny outside."
    # Add more commands and responses here
    else:
        return "I'm not sure how to respond to that."
