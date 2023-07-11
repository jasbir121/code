from tkinter import *
import tkinter as tk
import nltk
from tkinter import scrolledtext
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from nltk.sentiment import SentimentIntensityAnalyzer

# Create the Tkinter window
root = Tk()
root.title("NLP Toolkit")
root.geometry("644x788")

# Function to perform tokenization
def tokenize_text():
    text = input_text.get("1.0", tk.END).strip()
    tokens = word_tokenize(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, tokens)

# Function to perform stemming
def stem_text():
    text = input_text.get("1.0", tk.END).strip()
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in word_tokenize(text)]
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, stemmed_words)

# Function to perform lemmatization
def lemmatize_text():
    text = input_text.get("1.0", tk.END).strip()
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in word_tokenize(text)]
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, lemmatized_words)

# Function to perform POS tagging
def pos_tag_text():
    text = input_text.get("1.0", tk.END).strip()
    pos_tags = pos_tag(word_tokenize(text))
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, pos_tags)

# Function to perform sentiment analysis
def analyze_sentiment():
    text = input_text.get("1.0", tk.END).strip()
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, sentiment_scores)
f1 = Frame(root, borderwidth=2, bg="black", relief=SUNKEN)
f1.pack()
l = Label(f1, text="INPUT: ")
l.pack()
# Input text area
input_text = scrolledtext.ScrolledText(root, height=15, width=75)
input_text.pack(padx=2,pady=2)


# Tokenization button
tokenize_button = tk.Button(root, text="Tokenize", command=tokenize_text,fg="blue")
tokenize_button.pack(padx=2,pady=2)
# Stemming button
stem_button = tk.Button(root, text="Stem", command=stem_text,fg="blue")
stem_button.pack(padx=2,pady=2)

# Lemmatization button
lemmatize_button = tk.Button(root, text="Lemmatize", command=lemmatize_text,fg="blue")
lemmatize_button.pack(padx=2,pady=2)

# POS tagging button
pos_tag_button = tk.Button(root, text="POS Tag", command=pos_tag_text,fg="blue")
pos_tag_button.pack(padx=2,pady=2)

# Sentiment analysis button
sentiment_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment,fg="blue")
sentiment_button.pack(padx=1,pady=1)
f2 = Frame(root, borderwidth=2, bg="black", relief=SUNKEN)
f2.pack(padx=1,pady=1)
l = Label(f2, text="OUTPUT: ")
l.pack()

# Output text area
output_text = scrolledtext.ScrolledText(root, height=15, width=75)
output_text.pack(padx=2,pady=2)

# Start the Tkinter event loop
root.mainloop()
