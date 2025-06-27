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


## Run it
```bash
python calculator.py
python Tod.py
python News_scrapper.py
python App.py