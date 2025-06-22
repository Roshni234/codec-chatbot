import spacy
nlp = spacy.load("en_core_web_sm")

def chatbot_response(message):
    message = message.lower()
    doc = nlp(message)
    lemmas = [token.lemma_ for token in doc]

    if any(word in lemmas for word in ["order", "track", "status"]):
        return "You can track your order using the link sent to your email."

    elif any(word in lemmas for word in ["refund", "return", "money", "replace"]):
        return "Refunds are processed within 5-7 business days after we receive the returned item."

    elif any(word in lemmas for word in ["hour", "open", "time"]):
        return "We are open from 9 AM to 9 PM, Monday to Saturday."

    elif any(word in lemmas for word in ["contact", "phone", "email", "call"]):
        return "You can contact us at support@example.com or call 1800-123-456."

    elif any(word in lemmas for word in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"
    
    elif any(word in lemmas for word in ["delay", "late", "not arrive", "waiting"]):
        return "We’re sorry your order is delayed. Please check the tracking link or contact support."

    elif any(word in lemmas for word in ["cancel", "cancelled", "stop", "abort"]):
        return "To cancel your order, go to 'My Orders' and click 'Cancel'. If it's already shipped, contact support."

    elif any(word in lemmas for word in ["change", "edit", "modify"]) and any(word in lemmas for word in ["address", "delivery"]):
        return "To change your delivery address, go to your account > orders > edit address. This is possible only before shipping."

    elif any(word in lemmas for word in ["reschedule", "postpone", "new date"]):
        return "You can reschedule your delivery via the courier tracking link or by contacting our support team."

    elif any(word in lemmas for word in ["package", "damaged", "broken", "defective"]):
        return "We're sorry your package arrived damaged. Please initiate a return and upload a photo of the item.We will refund the amount"

    elif any(word in lemmas for word in ["where", "when", "status"]) and any(word in lemmas for word in ["delivery", "order"]):
        return "You can check your delivery status using the tracking number provided via email/SMS."

    elif any(word in lemmas for word in ["shipped", "dispatch", "sent"]):
        return "Most orders are shipped within 1-2 business days. You'll receive a confirmation once it's dispatched."

    else:
        return "I'm sorry, I didn't quite get that. Could you rephrase?"
