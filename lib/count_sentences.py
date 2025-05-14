#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ''
        else:
            self._value = new_value
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        if not self.value:
            return 0
            
        # Replace all sentence-ending punctuation with periods for consistent splitting
        temp = self.value.replace('?', '.').replace('!', '.')
        # Split on periods and filter out empty strings
        sentences = [s for s in temp.split('.') if s.strip()]
        return len(sentences)                    
    

