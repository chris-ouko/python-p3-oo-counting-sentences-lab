#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if type(value) == str:
      self._value=value
    else:
      print('The value must be a string.')

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False

  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
  

  def count_sentences(self):
    value = self.value
    for punctuation in ['?', '!']:
      value = value.replace(punctuation, ".")

    sentences = [string for string in value.split('.') if string]
    return len(sentences)

  value = property(get_value, set_value)