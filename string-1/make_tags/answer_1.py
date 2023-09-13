"""
Takes (str tag, str word) input, 
task: Return HTML-like tags using the parameters tag and word
      '<' + tag + '>' + word + '</' + tag + '>'
"""
def make_tags(tag, word):
  return f"<{tag}>{word}</{tag}>"

if __name__ == "__main__":
  # Testing with different inputs and expected results
  print(make_tags('i', 'Yay') == '<i>Yay</i>')
  print(make_tags('i', 'Hello') == '<i>Hello</i>')
  print(make_tags('cite', 'Yay') == '<cite>Yay</cite>')
  print(make_tags('i', '') == '<i></i>')
  print(make_tags('body', 'Heart') == '<body>Heart</body>')
  print(make_tags('p', 'Hello World') == '<p>Hello World</p>')
  