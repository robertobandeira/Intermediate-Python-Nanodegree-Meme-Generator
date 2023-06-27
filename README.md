# Overview
## Meme Generator – Instructions
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. It’s not that simple though! Your content team spent countless hours writing quotes in a variety of filetypes. You could manually copy and paste these quotes into one standard format – but you’re going to over-engineer a solution to load quotes from each file to show off your fancy new Python skills.

## What did I Build?
I used my newly learned skills to create a dynamic data-rich application to generate images with quotes. 
The application I built:
* Interacts with a variety of complex filetypes. This emulates the kind of data encountered in a data engineering role.
* Loads quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
* Loads, manipulates, and saves images.
* Accepts dynamic user input through a command-line tool and a web service. This emulates the kind of work encountered as a full stack developer.

This project gave mr a hands-on opportunity to practice what I learned in this course, such as:
* Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
* DRY (don’t repeat yourself) principles of class and method design.
* Working with modules and packages in Python.

# Using this code
There are two main ways to use this application:
* Generating a meme - you can call meme.py with 3 optional arguments image_url, body and quote. Example:
`python meme.py --body 'Testing quote out' --author 'Roberto'`
* Run this application behind a server that constitutes the backend for a Udacity-supplied frontend. To do so, run:
`python app.py`

# Modules
## Quote Engine
This powerful module implements the QuoteModel class and abstracts the different methods for consuming data from different extensions (pdf, csv, txt, docx):
* The QuoteModel encapsulates the body and author of a quote into an instance object
* The Ingestor abstracts away the Object-strategy design used in the remaining classes of the module
## Meme Engine
This module contains the class that handles the image manipulation and quote insertion to generate the memes.

# Final Result
When running this application as a server, you'll have available a website that can generate random memes (with pictures from a database and quotes from different file types), or generate your own meme by inputting a image url, quote and author. It's fun and easy to use!