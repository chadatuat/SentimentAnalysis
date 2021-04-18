#overall intent of this program is to allow a user to enter a single category to pull tweets from
# 100 tweets will be analyzed for sentiment and categorized
#
# ALPHA BUILD: My Twitter API account is not yet approved.  I'm limited to anlyzing text input.

from textblob import TextBlob
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
input_text = simpledialog.askstring(title="Sentiment Analyzer", prompt="Enter a tweet:")

if len(input_text) > 0:
    testimonial = TextBlob(input_text)
    print(testimonial.sentiment)
    print(testimonial.sentiment.polarity)
