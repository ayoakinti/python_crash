import re

def stripMatchAndCombineText (self, text):
  print(text, "regular text")
  strippedText = self.strip(text)
  print(strippedText, "strippedText")
#   strippedText.match(/[a-zA-ZÜÖÄßäöÜÖÄß]+/g)
  matchedText = re.findall(r'/[a-zA-ZÜÖÄßäöÜÖÄß]+/g', strippedText)
  print(matchedText, "matchedText")
#   return matchedText.join(" ")

def strip (html):
  print(html, "html")
  html = re.sub('/<style([\s\S]*?)<\/style>/gi', "", html)
  html = re.sub('/<script([\s\S]*?)<\/script>/gi', "", html)
  html = re.sub('/<\/div>/ig', "\n", html)
  html = re.sub('/<\/li>/ig', "\n", html)
  html = re.sub('/<li>/ig', "  *  ", html)
  html = re.sub('/<\/ul>/ig', "\n", html)
  html = re.sub("/<\/p>/ig", "\n", html)
  html = re.sub('/<br\s*[\/]?>/gi', "\n", html)
  html = re.sub('/<[^>]+>/ig', "", html)

  replaceString1 = "<toreplace3>"
  replaceString2 = "<toreplace2>"

  html = re.sub('/(\n\n\n)+/ig', replaceString1, html)
  html = re.sub('/(\n\n)/ig', replaceString2, html)
  html = re.sub('/<toreplace3>/ig', "\n\n", html)
  html = re.sub('/<toreplace2>/ig', "\n", html)

  return html

print(strip("<p>Hello World</p>"))

txt = "The rain in Spain"
txt = re.sub("\s", "", txt)
print(txt)


from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

print(strip_tags("<p>Hello World</p>"))