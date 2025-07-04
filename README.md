# Task 1
# Calculator App 🔢
# CLI (Command Line Interface )
A simple Python-based calculator app that runs in the terminal.

## Features
- Addition
- Subtraction
- Multiplication
- Division
- Loops until user exits


# Task 2: CLI To-Do List Application (Python)

This is a simple **console-based To-Do List manager** built using Python.  
It allows users to **add**, **view**, and **remove** tasks — and it **saves them persistently** using a local text file (`tasks.txt`) stored inside the project folder.

---

# Objective

> Build a persistent, terminal-based task manager using Python lists and file I/O.

---

# 🔧 Tools Used

- **Python 3.x**
- **VS Code / Terminal**

---

# 🚀 Features

- 📝 View current tasks
- ➕ Add new tasks
- ❌ Remove tasks by number
- 💾 Persistent task saving via `tasks.txt`
- 📂 All data stored safely inside the `task2/` folder

---

# Task 3: Web Scraper for News Headlines

- Scrapes headlines from a news site using `requests` and `BeautifulSoup`.
- Stores the result in `headlines.txt`.

> Files: `news_scraper.py`, `headlines.txt`,'requirements.txt'

# ⚙️ Tools & Tech

- 🐍 Python 3
- 🌐 Requests (to fetch HTML)
- 🍲 BeautifulSoup (for parsing HTML)
- 📄 Plain `.txt` file (to save headlines)
## 🧠 How It Works

1. Sends a GET request to a news website.
2. Parses the HTML content using BeautifulSoup.
3. Extracts text from all `<h2>` or `<h3>` tags.
4. Saves the headlines to a local text file `headlines.txt`.

# Task 4 – Flask REST API

This project is part of my internship tasks. Task 4 focuses on building a simple REST API using **Flask** that supports basic CRUD (Create, Read, Update, Delete) operations for managing user data.

---

## 🚀 Features

- ✅ Create a new user (POST `/users`)
- ✅ Retrieve all users (GET `/users`)
- ✅ Retrieve a single user by username (GET `/users/<Kunal>`)
- ✅ Update an existing user (PUT `/users/<RAJ>`)
- ✅ Delete a user (DELETE `/users/<Kunal>`)

---

# 🧠 Tools and Tech

- 💻 Python 3
- 🌐 Flask
- 📮 Postman (for testing)

# Task 5: Sales Data Analysis

- Analyzed a dummy sales dataset using Pandas and Matplotlib
- Created visualizations (bar & pie charts) for products and regions
- Colab notebook and CSV included
- 📁 Folder: `task5/`
- 📄 Files: `Task_5_Sales_Analysis.ipynb`, `sales.csv`

# 🚀 Task 6: Flask Portfolio Website

**Objective:**  
Create a responsive personal portfolio website using Flask to showcase skills, projects, and contact information.

**Key Features:**
- Homepage with name, bio, projects, skills
- Contact form (saves data to CSV)
- Resume download
- Font Awesome icons + dark UI
- Deployed-ready (Render/HF)

**Tech Stack:**  
Flask, HTML, CSS, Python, Font Awesome, GitHub

# Task 7: Image Resizer Tool

### 📌 Objective:
Resize and convert images in batch using Python. This tool helps automate the process of image preprocessing by resizing all images in a given folder.

---

### 🧰 Tools & Libraries:
- 🐍 Python
- 🖼️ [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

# Task 8: Build a Rule-Based Chatbot using if-else

## 📝 Objective:
To build a simple chatbot using basic Python logic with `if-elif-else` statements. The bot should be able to respond to user queries based on predefined rules.

---

# 🛠️ Tools & Technologies:
- Language: **Python**
- Libraries Used: `datetime` (for time responses)

---

## 📁 Deliverables:
- A Python script that:
  - Takes user input
  - Processes it using conditional statements
  - Returns a predefined text-based response

---

## 💬 Chatbot Capabilities:
| Feature         | Description                                               |
|----------------|-----------------------------------------------------------|
| 👋 Greetings     | Responds to "hello", "hi", "hey"                         |
| 🕒 Time Check    | Returns current system time                              |
| 🌦️ Weather      | Informs user about lack of real-time data access         |
| 🍽️ Food Query    | Responds to "pav bhaji" with a fun fact                 |
| 😊 Emotions      | Handles "sad", "happy" with support messages            |
| 💤 Boredom       | Gives suggestions when user feels bored                 |
| 😂 Joke Feature  | Tells a joke on demand                                   |
| 👋 Exit          | Responds to "bye", "goodbye", "exit"                    |


## Run it
```bash
python calculator.py
python Tod.py
python News_scrapper.py
python App.py
python resizer.py
python chatbot.py