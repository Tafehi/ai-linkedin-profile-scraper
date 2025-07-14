# LinkedIn Profile Scraper AI Agent

This project is an AI-powered agent that scrapes LinkedIn profiles using the [Olama framework integrated with LangChain, leveraging Google's **Gemma** model. It uses [Scrapin.io](https://www.scrapinr fetching LinkedIn profile information.

---

## 🚀 Features

- 🔍 Scrapes LinkedIn profiles using Scrapin.io API
- 🧠 Uses **Gemma** model from Google via **Ollama**
- 🔗 Built with **LangChain** for agent orchestration
- 🔐 Requires a valid Scrapin.io API key

---

## 🛠️ Requirements

- Python 3.10+
- Ollama installed and running
- LangChain
- A [Scrapin.io](https://www.scrapin---

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
```

⚙️ How It Works
The agent receives a LinkedIn profile URL.
It uses the Scrapin.io API to fetch profile data.
The data is processed and analyzed using the Gemma model via Ollama.
LangChain orchestrates the flow between components.


📄 Notes
You must have a valid Scrapin.io account and API key.
Ensure Ollama is running locally with the Gemma model pulled and ready.
This project is for educational and research purposes. Always respect LinkedIn's terms of service.

📬 Contact
For questions or contributions, feel free to open an issue or pull request.