# travel-planner-chatbot-
Here's a complete `README.md` for your project **Travelexa**, a smart travel planner chatbot built using Streamlit and OpenAI:

---

```markdown
# 🌍 Travelexa – Your Smart Trip Planning Assistant ✈️

**Travelexa** is an intelligent, interactive travel planning chatbot built using **Streamlit** and **OpenAI's GPT-4o-mini**. It acts as your personal trip advisor – helping you explore destinations, plan itineraries, and customize trips based on your preferences in real time.

---

## ✨ Features

- 💬 **Conversational Interface**: Chatbot powered by GPT-4o-mini
- 🧠 **Smart Planning**: Analyzes your travel dates, people count, and interests
- 📅 **Daywise Itinerary**: Generates detailed travel plans
- 🌐 **World Expertise**: Knowledgeable in global destinations, events, food, and hotels
- 🖥️ **Streamlit UI**: Clean and interactive frontend
- 🔒 **Secure API Handling**: Uses `.env` for API key protection

---

## 📦 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [OpenAI GPT-4o-mini](https://openai.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🗂️ Project Structure

```

📁 travelexa/
├── chatbot.py           # Main Streamlit app
├── .env                 # Environment variable (API Key)
├── .gitignore           # Ignores .env and unwanted files

```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- An OpenAI API key

### 🔐 Setup `.env` File

Create a `.env` file in the root directory:

```

OPENAI\_API\_KEY=your\_openai\_key\_here

````

### 📥 Install Dependencies

```bash
pip install streamlit openai python-dotenv
````

### ▶️ Run the App

```bash
streamlit run chatbot.py
```

Visit `http://localhost:8501` in your browser.

---

## 💬 How It Works

* The assistant, **Tripzy**, begins the conversation by asking your destination, dates, number of travelers, and preferences.
* After analyzing your responses, it creates a **professional, concise** daywise travel itinerary under 200 words.
* Everything is displayed in a sleek chat interface powered by Streamlit.

---

## 👤 Author

**Haritha K. Suresh**
B.Tech in Artificial Intelligence and Data Science
📧 [harithaksuresh6@gmail.com](mailto:harithaksuresh6@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/haritha-k-suresh-92a55b275/)

---

## 📜 License

This project is for educational and personal use only.

```

---

Would you like me to save this as a `README.md` file in your folder, ready to commit?
```
