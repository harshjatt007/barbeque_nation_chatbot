def get_response(user_message: str) -> str:
    if "book" in user_message.lower():
        return "Sure, I can help you with a booking. Could you tell me the city and date?"
    elif "cancel" in user_message.lower():
        return "Okay, please provide your booking ID for cancellation."
    elif "faq" in user_message.lower() or "menu" in user_message.lower():
        return "You can find our menu on the official website, or ask me a specific question."
    else:
        return "Sorry, I didn't understand that. Could you please rephrase?"