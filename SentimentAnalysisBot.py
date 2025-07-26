#textblob is a library which provides a lot of functionality to work with text and sentiment

from textblob import  TextBlob
from dataclasses import  dataclass

@dataclass
class Mood:
    emoji :str
    sentiment: float

def get_mood(input_text: str,*,sensitivity:float)-> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold :float= sensitivity
    hostile_threshold : float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('🤗',polarity) #good mood
    elif polarity <= hostile_threshold:
        return Mood('😠',polarity) #angry mood
    else:
        return Mood('🙂',polarity)

def run_bot():
    print('Enter some text to do sentiment analysis: ')

    while True:
        user_input:str = input('You : ')
        mood: Mood = get_mood(user_input,sensitivity=0.3)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')

        if user_input.lower() == "exit" or user_input.lower() == 'bye':
            print('Have a good day!')
            break


if __name__ == '__main__':
    run_bot()