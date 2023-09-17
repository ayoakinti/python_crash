# from thefuzz import fuzz
from rapidfuzz import fuzz, utils
# from thefuzz import process

# print(fuzz.ratio("this is a test", "this is a test!"))

relevantText1 = '''
  Tesla's clean energy initiatives with Powerwall and solar panels
  are reshaping our relationship with energy sources. But
  I don't get the difference between a car and a horse
'''
relevantText2 = '''
  Tesla's clean energy initiatives with Powerwall and solar panels
   are reshaping our relationship with energy sources
'''
relevantText3 = "zzzzzz zzzzzz zzzzz zzzz zzzz zzzz zzz zzz zzzzzzz zzzzzzz zzzzzzzz zzzzzzzz zzzzzzz zzzzzzz zzzzzzzz zzzz z zzzz zzzzzz zzzzzz zzzzz zzzzzz zzzzz zzzzzz zzzzzz zzzz"
relevantText4 = "abcde fghijklmo pqrstuvwxyz ddeydydsksnshb djsdyeydsds dsudowdoiweoid ddisiduwoiedue didudieydhgdsc eudheuiye7yt7ed eedueudedue"
relevantText5 = "The Gigafactories, are engineering marvels that produce these innovations at an astonishing scale"
relevantText6 = "Let's talk about Tesla, epitome of innovation."
relevantText7 = "Tesla isn't just a car company;"

entireTranscript = '''
  Let's talk about Tesla, an epitome of innovation. This company isn't just about
  electric cars; it's a revolution. Their vehicles, like the Model S, X, 3, and Y,
  have redefined how we view transportation.The Autopilot feature, introduced in 2014,
  laid the foundation for autonomous driving technology. It's not just about getting
  from A to B; it's about safety and convenience.And the impact isn't limited to roads.
  Tesla's clean energy initiatives with Powerwall and solar panels are reshaping our
   relationship with energy sources.The Gigafactories, like the one in Shanghai, are
  engineering marvels that produce these innovations at an astonishing scale, bringing
  us closer to sustainable manufacturing.The Cybertruck's bold design and the Model S
  Plaid's incredible performance are testaments to their constant push for excellence.
  Tesla isn't just a car company; it's a force that's propelling us into a future where
  eco-friendly technology is a norm.In conclusion, Tesla's journey showcases how innovation,
  when driven by a vision, can transform industries and inspire a global shift
  towards a more sustainable tomorrow.
'''

# entireTranscript = '''
#   Let's talk about Tesla, an epitome of innovation. This company 
#   isn't just about electric cars; it's a revolution. Their 
#   vehicles, like the Model S, X, 3, and Y, have 
#   redefined how we view transportation.
#   The Autopilot feature, introduced in 2014, laid the 
#   foundation for autonomous driving technology. It's not 
#   just about getting from A to B; it's about safety and convenience.
#   And the impact isn't limited to roads. Tesla's clean 
#   energy initiatives with Powerwall and solar panels are 
#   reshaping our relationship with energy sources.
# '''


# print(fuzz.partial_ratio(relevantText1, entireTranscript, processor=utils.default_process), "relevantText1")
# print(fuzz.partial_ratio(relevantText2, entireTranscript, processor=utils.default_process), "relevantText2")
# print(fuzz.partial_ratio(relevantText3, entireTranscript, processor=utils.default_process), "relevantText3")
# print(fuzz.partial_ratio(relevantText4, entireTranscript, processor=utils.default_process), "relevantText4")

# print(fuzz.partial_ratio(entireTranscript, relevantText1, processor=utils.default_process), "relevantText1")
# print(fuzz.partial_ratio(entireTranscript, relevantText2, processor=utils.default_process), "relevantText2")
# print(fuzz.partial_ratio(entireTranscript, relevantText3, processor=utils.default_process), "relevantText3")
# print(fuzz.partial_ratio(entireTranscript, relevantText4, processor=utils.default_process), "relevantText4")
# print(fuzz.partial_ratio(relevantText2, entireTranscript), "relevantText2")
# print(fuzz.partial_ratio(relevantText3, entireTranscript), "relevantText3")
# print(fuzz.partial_ratio(relevantText4, entireTranscript), "relevantText4")


# print(fuzz.partial_ratio("the brown fox jumped over the lazy dog", "the brown fox jumped over the lazy dog i dont know why"), "relevantText5")
# print(fuzz.partial_ratio("the brown fox jumped", "the brown fox jumped over the lazy dog"), "relevantText6")

# print(fuzz.partial_ratio("I need to speak to you about the importance of using the fuzzy string matcher in your current approach", entireTranscript), "relevantText7")
# print(fuzz.partial_ratio("1", "dssdsdsds 2"), "relevantText8")
# print(fuzz.partial_ratio("Kurtis Pykes", "Kurtis K D Pykes"), "relevantText9")

# print(fuzz.ratio("I need to speak to you about the importance of using the fuzzy string matcher in your current approach", entireTranscript), "relevantText7a")
# print(fuzz.ratio("1", "dssdsdsds 2"), "relevantText8a")
# print(fuzz.ratio("Kurtis Pykes", "Kurtis K D Pykes"), "relevantText9a")

# print(fuzz.ratio("test", "test"), "relevantText1")
# print(fuzz.partial_ratio("test", "test"), "relevantText1a")
# print(fuzz.token_sort_ratio("test", "test"), "relevantText1b")
# print(fuzz.token_set_ratio("test", "test"), "relevantText1c")

# print(fuzz.ratio("test", "TEST", processor=lambda s: s.upper()), "relevantText1")
# print(fuzz.ratio("test", "TEST", processor=utils.default_process), "relevantText1")
# print(fuzz.partial_ratio("test", "TEST"), "relevantText1a")
# print(fuzz.token_sort_ratio("test", "TEST"), "relevantText1b")
# print(fuzz.token_set_ratio("test", "TEST"), "relevantText1c")

# print(fuzz.ratio("test", "stte"), "relevantText2")
# print(fuzz.partial_ratio("test", "stte"), "relevantText2a")
# print(fuzz.token_sort_ratio("test", "stte"), "relevantText2b")
# print(fuzz.token_set_ratio("test", "stte"), "relevantText2c")

# print(fuzz.ratio("abcd", "teast"), "relevantText3")
# print(fuzz.partial_ratio("abcd", "teast"), "relevantText3a")
# print(fuzz.token_sort_ratio("abcd", "teast"), "relevantText3b")
# print(fuzz.token_set_ratio("abcd", "teast"), "relevantText3c")
# print(fuzz.WRatio("abcd", "teast"), "relevantText3d")
# print(fuzz.QRatio("abcd", "teast"), "relevantText3e")

# print(fuzz.ratio("teast", "abcd"), "relevantText4")
# print(fuzz.partial_ratio("teast", "abcd"), "relevantText4a")
# print(fuzz.token_sort_ratio("teast", "abcd"), "relevantText4b")
# print(fuzz.token_set_ratio("teast", "abcd"), "relevantText4c")

# print(fuzz.ratio("abcd", "TEAST"), "relevantText6")
# print(fuzz.partial_ratio("abcd", "TEAST"), "relevantText6a")
# print(fuzz.token_sort_ratio("abcd", "TEAST"), "relevantText6b")
# print(fuzz.token_set_ratio("abcd", "TEAST"), "relevantText6c")
# print(fuzz.WRatio("abcd", "TEAST"), "relevantText6d")
# print(fuzz.QRatio("abcd", "TEAST"), "relevantText6e")

# print(fuzz.ratio("test slack", "stte slack"), "relevantText5")
# print(fuzz.partial_ratio("test slack", "stte slack"), "relevantText5a")


# print(utils.default_process("test twinsSSS! "), "default process test")

# print(fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
# print(fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
# print(fuzz.ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
# print(fuzz.partial_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
# print(fuzz.partial_ratio("fuzzy was a bear", "fuzzyfuzzywasabear"))
# print(fuzz.partial_ratio("fuzzyfuzzywasabear", "fuzzy was a bear"))
# print(fuzz.ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "ratio")
# print(fuzz.partial_ratio_alignment("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "partial_ratio_alignment")
print(fuzz.partial_ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "token_set_ratio")
# print(fuzz.partial_token_set_ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "partial_token_set_ratio")
# print(fuzz.token_sort_ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "token_sort_ratio")
# print(fuzz.partial_token_sort_ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "partial_token_sort_ratio")
# print(fuzz.token_ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "token_ratio")
# print(fuzz.partial_token_ratio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "partial_token_ratio")
# print(fuzz.WRatio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "WRatio")
# print(fuzz.QRatio("fuzzy was a fine man", "fuzzy was n amen ifa", processor=utils.default_process), "QRatio")

print("\n next round \n")

# print(fuzz.ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "ratio")
# print(fuzz.partial_ratio_alignment("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "partial_ratio_alignment")
print(fuzz.partial_ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "token_set_ratio")
# print(fuzz.partial_token_set_ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "partial_token_set_ratio")
# print(fuzz.token_sort_ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "token_sort_ratio")
# print(fuzz.partial_token_sort_ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "partial_token_sort_ratio")
# print(fuzz.token_ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "token_ratio")
# print(fuzz.partial_token_ratio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "partial_token_ratio")
# print(fuzz.WRatio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "WRatio")
# print(fuzz.QRatio("fuzzy was a fine man", "fuzzy was a fine man but started behaving funny after a while", processor=utils.default_process), "QRatio")

print("\n next round \n")

# print(fuzz.ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "ratio")
# print(fuzz.partial_ratio_alignment("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "partial_ratio_alignment")
print(fuzz.partial_ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "token_set_ratio")
# print(fuzz.partial_token_set_ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "partial_token_set_ratio")
# print(fuzz.token_sort_ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "token_sort_ratio")
# print(fuzz.partial_token_sort_ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "partial_token_sort_ratio")
# print(fuzz.token_ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "token_ratio")
# print(fuzz.partial_token_ratio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "partial_token_ratio")
# print(fuzz.WRatio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "WRatio")
# print(fuzz.QRatio("fuzzy was a fine man", "fuzzy was b bbbb bb", processor=utils.default_process), "QRatio")

print("\n next round \n")

# print(fuzz.ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "ratio")
# print(fuzz.partial_ratio_alignment("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "partial_ratio_alignment")
print(fuzz.partial_ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbccdjdsjds dsdsdjsjd jsdjsjdsj", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbccdjdsjds dsdsdjsjd jsdjsjdsj", processor=utils.default_process), "token_set_ratio")
# print(fuzz.partial_token_set_ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "partial_token_set_ratio")
# print(fuzz.token_sort_ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "token_sort_ratio")
# print(fuzz.partial_token_sort_ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "partial_token_sort_ratio")
# print(fuzz.token_ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "token_ratio")
# print(fuzz.partial_token_ratio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "partial_token_ratio")
# print(fuzz.WRatio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "WRatio")
# print(fuzz.QRatio("fuzzy was a fine man", "fuzzy was b bbbb bbbcc", processor=utils.default_process), "QRatio")

print("\n next round \n")

# print(fuzz.ratio("bring", "gnirb", processor=utils.default_process), "ratio")
# print(fuzz.partial_ratio_alignment("bring", "gnirb", processor=utils.default_process), "partial_ratio_alignment")
print(fuzz.partial_ratio("bring", "gnirb ring", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("bring", "gnirb ring", processor=utils.default_process), "token_set_ratio")
# print(fuzz.partial_token_set_ratio("bring", "gnirb", processor=utils.default_process), "partial_token_set_ratio")
# print(fuzz.token_sort_ratio("bring", "gnirb", processor=utils.default_process), "token_sort_ratio")
# print(fuzz.partial_token_sort_ratio("bring", "gnirb", processor=utils.default_process), "partial_token_sort_ratio")
# print(fuzz.token_ratio("bring", "gnirb", processor=utils.default_process), "token_ratio")
# print(fuzz.partial_token_ratio("bring", "gnirb", processor=utils.default_process), "partial_token_ratio")
# print(fuzz.WRatio("bring", "gnirb", processor=utils.default_process), "WRatio")
# print(fuzz.QRatio("bring", "gnirb", processor=utils.default_process), "QRatio")

print("\n next round \n")

print(fuzz.partial_ratio("test mic", "tests mic", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("test mic", "tests mic", processor=utils.default_process), "token_set_ratio")

print("\n next round \n")

print(fuzz.partial_ratio("test mic", "tests mic", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("test mic", "tests mic", processor=utils.default_process), "token_set_ratio")

print("\n next round \n")

print(fuzz.partial_ratio(relevantText1, entireTranscript, processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio(relevantText1, entireTranscript, processor=utils.default_process), "token_set_ratio")

print("\n next round \n")

print(fuzz.partial_ratio(relevantText2, entireTranscript, processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio(relevantText2, entireTranscript, processor=utils.default_process), "token_set_ratio")

print("\n next round \n")

print(fuzz.partial_ratio(relevantText3, entireTranscript, processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio(relevantText3, entireTranscript, processor=utils.default_process), "token_set_ratio")

print("\n next round \n")

print(fuzz.partial_ratio(relevantText4, entireTranscript, processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio(relevantText4, entireTranscript, processor=utils.default_process), "token_set_ratio")

print("\n next round \n")

print(fuzz.partial_ratio("test", "Ich sage ganz viel, aber das einzige Wort, das gefleckt ist, kommt auf gar keinen Fall hier vor.", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("test", "Ich sage ganz viel, aber das einzige Wort, das gefleckt ist, kommt auf gar keinen Fall hier vor.", processor=utils.default_process), "token_set_ratio")

print("\n next round \n")

print(fuzz.partial_ratio("REALLY REALLY IMPORTANT THAT I DISCUSS WITH YOU TODAY I WOULD BE IN GRAFING BY TOMORROW AND WOULD LOVE TO GET YOUR INPUT AND FEEDBACK", "This item is relevant for text much.", processor=utils.default_process), "partial_ratio")
print(fuzz.token_set_ratio("REALLY REALLY IMPORTANT THAT I DISCUSS WITH YOU TODAY I WOULD BE IN GRAFING BY TOMORROW AND WOULD LOVE TO GET YOUR INPUT AND FEEDBACK", "This item is relevant for text much.", processor=utils.default_process), "token_set_ratio")