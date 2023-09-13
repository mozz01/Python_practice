"""
Takes (str out, str word) input, 
task: return a new string where 'word' is placed in the center of 'out'
Note: 'out' is always 4 characters long
"""
def make_out_word(out, word):
  return out[:2] + word + out[2:]

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(make_out_word('<<>>', 'Yay') == '<<Yay>>')
  print(make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>')
  print(make_out_word('[[]]', 'word') == '[[word]]')
  