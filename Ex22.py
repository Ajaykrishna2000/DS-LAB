import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

sample_text = """Rama killed Ravana to save sita from Lanka. The legend of the Ramayan is the most popular Indian epic. 
A lot of movies and serials have already been shot in several languages here in India based on the Ramayana."""
tokenized = nltk.sent_tokenize(sample_text)
for i in  tokenized:
    words = nltk.word_tokenize(i)
    tagged_words=nltk.pos_tag(words)
    chunkGram=r"""VB:{}"""
    chunkParse=nltk.RegexpParser(chunkGram)
    chunked=chunkParse.parse(tagged_words)
    print(chunked)
    chunked.draw()