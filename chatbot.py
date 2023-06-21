from http.client import responses
import re

from requests import Response
from ChatterBot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot('Ronny')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

def chatbot(text):
  # Prepare the input by removing special characters and converting to lowercase
  text = re.sub(r'[^\w\s]', '', text)
  text = text.lower()
  
  # Define some possible responses
  responses = {
    "hello": "Hello! How are you?",
    "hi": "Hi there! How are you?",
    "how are you": "I'm doing well, thank you. How are you?",
    "i'm good": "That's great to hear!",
    "what's your name": "My name is Chatbot. What's yours?",
    "my name is": "Nice to meet you, [name]. How can I help you today?",
    "goodbye": "Goodbye! Have a great day."
  }
  
  # Find the matching response
  for key in responses:
    if text.find(key) != -1:
      return responses[key]
      
  # Return a default response if no matches were found
  return "I'm sorry, I don't understand what you're saying."

response = chatbot("Hi there!")
print(responses)  # Output: "Hi there! How are you?"
  
response = chatbot.get_response('What is your Number')
print(responses)
 
response = chatbot.get_response('Who are you?')
print(responses)
  
  
  
  
