

---

```markdown
# 🌍 Travelexa – Your Smart Trip Planning Assistant ✈️

**Travelexa** is an intelligent, interactive travel planning chatbot built using Streamlit and OpenAI's GPT-4o-mini. It acts as your personal trip advisor – helping you explore destinations, plan itineraries, and customize trips based on your preferences in real time.

---

## ✨ Features

- 💬 Conversational Interface – Chatbot powered by GPT-4o-mini  
- 🧠 Smart Planning – Analyzes your travel dates, people count, and interests  
- 📅 Daywise Itinerary – Generates concise, professional travel plans  
- 🌐 World Expertise – Knows destinations, events, food, and hotels worldwide  
- 🖥️ Streamlit UI – Clean, responsive web interface  
- 🔒 Secure API Handling – Uses `.env` for OpenAI API key protection  

---

## 📦 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [OpenAI GPT-4o-mini](https://openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🗂️ Project Structure

```

📁 travelexa/
├── chatbot.py           # Main Streamlit app
├── .env                 # Environment variable (API key, excluded from git)
├── .gitignore           # Prevents sensitive files from being committed

```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8 or higher
- An OpenAI API key ([get yours here](https://platform.openai.com/account/api-keys))

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

Then open your browser and visit: [http://localhost:8501](http://localhost:8501)

---

## 💬 How It Works

* The assistant, Tripzy, begins the conversation by asking your destination, travel dates, number of travelers, and preferences.
* Based on your responses, it generates a professional, concise **daywise itinerary** (within 200 words).
* The chatbot interface is powered by Streamlit for real-time interaction.

---

## 👤 Author

**Haritha K. Suresh**
B.Tech in Artificial Intelligence and Data Science
📧 [harithaksuresh6@gmail.com](mailto:harithaksuresh6@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/haritha-k-suresh-92a55b275/)

---

## 📜 License

This project is for educational and personal use only.

