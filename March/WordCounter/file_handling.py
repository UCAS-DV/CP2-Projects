from time_handling import get_timestamp

def count_words():
    with open('March/WordCounter/text.txt', 'r') as text_file:
        text = text_file.read()
        word_count = len(text.split())
        
        return word_count
    
def add_timestamp():

    with open('March/WordCounter/text.txt', 'a') as text_file:
        text_file.write(f'\n{count_words()} Words - {get_timestamp()}')