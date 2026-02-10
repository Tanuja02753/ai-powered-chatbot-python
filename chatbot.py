import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?"]],
    [r"what is your name ?", ["I am an AI Chatbot"]],
    [r"how can you help ?", ["I answer your questions"]],
    [r"bye", ["Goodbye!"]]
]

chatbot = Chat(pairs, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)
