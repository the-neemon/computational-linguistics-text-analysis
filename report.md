Task 3:
The shortest words are 1 letter words: ['a', 'b', 'c', 'e', 'h', 'i', 'l', 'o', 's'] appearing 21,803 times. These are of three types: real english words like 'a'(article), 'i'(pronoun) and 'o'(interjection) which appear frequently, grammar parts like 's'(possessive/plural marker) that got separated during processing and formatting leftovers like 'b', 'c', 'e', 'h', 'l' which rarely appear. The high total frequency shows these are patterns, not random errors.

Task 7: "Are word lengths optimized for efficient communication?"
Yes, the results show that word lengths are optimized for efficient communication. The data has a Pearson Correlation of -0.6448 between the word length and frequency, since the Pearson Correlation is negative this means that shorter words come more than longer words. It makes sense because naturally people use short words for things they say often to save time and effort when speaking and thinking. The shortest words 'a' and 'i' are used often and are very important in grammar, this shows that important words are short. This is true for words of all lengths, showing that this works throughout the language. This supports that human language developed to balance what we need to say with how easy it is to say, creating a system where common words are short and rare words are usually longer.

Note-
I've used the nltk tokenizer which splits contractions into different tokens so my tokenization is as follows - "it's" becomes "it" + "'s" and "don't" becomes "do" + "n't" etc.
