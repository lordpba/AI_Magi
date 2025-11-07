

# 🔺 MAGI System v2.0

![MAGI GUI Example](example_gui.png)

<div align="center">
<img src="Magi.jpg" alt="MAGI System GUI" width="600"/>
</div>

---

## 🧬 What is MAGI?

**MAGI System** is a multi-agent AI inspired by the legendary supercomputers of Neon Genesis Evangelion. Three distinct AI personalities—Melchior (logic), Balthasar (ethics), Casper (practicality)—analyze every question from different angles, then synthesize their answers for a true "consensus of minds". 

> *"The truth lies in the synthesis of three perspectives."*

MAGI is the digital soul of NERV: scientific, ethical, and pragmatic. Now you can ask it anything—just like Gendo Ikari.

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r config/requirements.txt

# 2. Install LiteLLM (required for LLM provider support)
pip install litellm

# 3. Configure API keys
cp config/.env.example config/.env
# Edit config/.env with your keys

# 4. Launch web interface
python src/magi_web_interface.py
```

Open [http://localhost:7862](http://localhost:7862) in your browser.

---

## 🛠️ Requirements

- Python 3.8+
- API Key (Groq recommended)

---

## 🔑 API Keys

- [Groq](https://console.groq.com) (recommended)
- [Serper](https://serper.dev) (optional, for search)
- [OpenAI](https://platform.openai.com) (optional)

Copy `config/.env.example` to `config/.env` and add your keys.

---

## 💻 Usage

### Web Interface
```bash
python src/magi_web_interface.py
```

### Command Line
```bash
python src/Main_core_002.py
```

---

## 🧠 How MAGI Works

1. **Ask a question** (Evangelion, AI, ethics, anything!)
2. **Choose your LLM provider** (Groq, OpenAI, or local Ollama)
3. **MAGI splits your question** into three perspectives:
	- 🔬 Melchior: Scientific/logical
	- 🛡️ Balthasar: Ethical/emotional
	- ⚖️ Casper: Practical/social
4. **Synthesis**: The system merges all three analyses for a complete answer.

---

## 🦙 Local Ollama Support

Want to run MAGI with local models? Install [Ollama](https://ollama.com/) and download your favorite model (e.g. `llama3`, `phi3`, `mistral`). Select "Ollama (local)" in the interface and enter the model name.

---

## 📜 License & Credits

Fan-made project for educational purposes.

**Neon Genesis Evangelion** © GAINAX / khara

Code: MIT License

Powered by CrewAI & Gradio

---

<div align="center">
<b>MELCHIOR-1 • BALTHASAR-2 • CASPER-3</b><br>
<b>NERV - God's in his heaven, all's right with the world</b>
</div>
