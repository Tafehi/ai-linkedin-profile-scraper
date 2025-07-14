
## 🔍 LinkedIn Profile Scraper AI Agent
This project is an AI-powered LinkedIn profile summarizer built using the Ollama framework, LangChain, and Streamlit. It leverages Google's Gemma model (via Ollama) or OpenAI's GPT-4o-mini for efficient and cost-effective reasoning. The agent uses Scrapin.io to fetch LinkedIn profile data and intelligently decides whether to use live scraping or cached data from GitHub Gist.

This project is an AI-powered agent that scrapes LinkedIn profiles using the `Olama framework` integrated with LangChain, leveraging Google's `Gemma` model. It uses [Scrapin.io](https://www.scrapin.io/) fetching LinkedIn profile information.

---
## 🚀 Features
. 🔍 Scrapes LinkedIn profiles using the Scrapin.io API
. 🧠 Uses Gemma (via Ollama) or GPT-4o-mini (via OpenAI)
. 🔗 Built with LangChain for agent orchestration
. 🌐 Uses Tavily API as a web search tool
. 🧠 AI agent (lookup.py) searches LinkedIn using GPT-4o-mini
. 💾 Fetches cached data from GitHub Gist for specific users (e.g., "Ehsan Tafehi") to reduce costs
. 🖥️ Interactive Streamlit UI
. 💰 Only the paid Scrapin.io API can fetch live data
. 👉 Scrapin Pricing

---

## 🛠️ Requirements
Python 3.10+
Ollama installed and running (for Gemma)
LangChain
Streamlit
A Scrapin.io API key
OpenAI API key (for GPT-4o-mini)
Tavily API key (for web search)

---

## 📦 Installation

1. **Clone the repository**

```bash
  git clone https://github.com/your-username/linkedin-agent.git
  cd linkedin-agent
```

2. **Install dependencies**

```bash
  pip install -r requirements.txt
```

3. **Set up environment variables**
Create a .env file in the root directory:

```bash
  SCRAPIN_API_KEY=your_scrapin_api_key_here
  OPENAI_API_KEY=your_openai_api_key_here
  TAVILY_API_KEY=your_tavily_api_key_here
  LLM_MODEL=gpt-4o-mini
```

## ⚙️ How It Works
The user enters a name in the Streamlit UI.
If the name is "Ehsan Tafehi", the app fetches data from a GitHub Gist to avoid API costs.
Otherwise, the AI agent (lookup.py) uses GPT-4o-mini and Tavily to search for the LinkedIn profile.
The Scrapin.io API fetches the profile data.
The data is summarized using LangChain and the selected LLM.
The result is displayed in a structured format in the Streamlit app.

## 🧠 AI Agent Logic
lookup.py: An AI agent using GPT-4o-mini to search for LinkedIn profiles.
Uses Tavily API (in tools/tavily.py) for real-time web search.
If the name is "Ehsan Tafehi", the agent bypasses search and loads data from GitHub Gist.
This logic ensures cost-efficiency and low latency.

## 🗂️ Project Structure

```bash
├── agents
│   ├── __init__.py
│   └── lookup.py               # AI agent using GPT-4o-mini + Tavily
├── app.py                      # Main Streamlit application
├── README.md
├── requirements.txt
├── tools
│   ├── __init__.py
│   └── tavily.py               # Tavily API integration
└── utils
    ├── __init__.py
    └── linkedin.py             # LinkedIn scraper logic (Scrapin.io or Gist)
```

## 📄 Notes
You must have a valid Scrapin.io account and API key.
Ensure Ollama is running locally with the Gemma model pulled.
The project defaults to GPT-4o-mini for cost and speed.
This project is for educational and research purposes. Always respect LinkedIn’s terms of service.