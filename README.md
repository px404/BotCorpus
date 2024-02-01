# BotCorpus
Provide dataset (preferably a huge corpus of text data) upon running the code

How it works?

Think of it as a complicated if else program, and that is the easiest way to understand this.

Text Preprocessing:
The bot preprocesses the text by converting it to lowercase and tokenizing it into sentences and words. It also removes punctuation marks to simplify the text.

TF-IDF Vectorization:
It uses the Term Frequency-Inverse Document Frequency (TF-IDF) vectorization technique to convert text data into numerical vectors. TF-IDF assigns weights to words based on their importance in the document relative to the entire corpus.

Cosine Similarity:
The bot computes the cosine similarity between the TF-IDF vectors of the user's input and the sentences/questions in its corpus. Cosine similarity measures the similarity between two vectors based on the cosine of the angle between them.

Greeting Functionality:
It includes a function to recognize common greeting phrases such as "hello", "hi", etc., and responds with predefined greetings.

Conversation Loop:
The bot engages in a conversation loop where it continuously prompts the user for input until the user enters "bye" to terminate the conversation.

Random Response Selection:
In cases where the bot cannot find a suitable response based on cosine similarity, it selects a random response to maintain engagement with the user.

Lemmatization:
It employs lemmatization to reduce words to their base or dictionary form. This helps in standardizing words and reducing the vocabulary size.
