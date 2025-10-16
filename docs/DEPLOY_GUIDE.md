# 🚀 Deploy MAGI System su Hugging Face Spaces

Questa guida ti spiega come deployare il MAGI System su Hugging Face Spaces per avere un'interfaccia web pubblica sempre disponibile.

## 🌟 Vantaggi di Hugging Face Spaces

- ✅ **Hosting gratuito** per progetti Gradio
- ✅ **URL pubblico permanente** (non scade dopo 72 ore)
- ✅ **SSL/HTTPS automatico**
- ✅ **Gestione secrets** per API keys
- ✅ **Integrazione con Git**
- ✅ **Community ampia**

## 📋 Prerequisiti

1. Account su [Hugging Face](https://huggingface.co/join)
2. Git installato
3. Repository MAGI System funzionante localmente

## 🎯 Guida Passo-Passo

### 1. Crea un Nuovo Space

1. Vai su https://huggingface.co/spaces
2. Clicca su **"Create new Space"**
3. Configura:
   - **Name**: `magi-system` (o quello che preferisci)
   - **License**: MIT
   - **SDK**: Gradio
   - **Hardware**: CPU basic (gratuito)
   - **Visibility**: Public o Private

### 2. Prepara i File

Crea un file `app.py` nella root del progetto (necessario per Hugging Face):

```python
# app.py - Entry point for Hugging Face Spaces
from magi_web_interface import create_interface

if __name__ == "__main__":
    app = create_interface()
    app.launch()
```

Modifica `requirements.txt` per Hugging Face (rimuovi versioni specifiche se causano problemi):

```txt
crewai
crewai-tools
langchain
langchain-openai
langchain-groq
langchain-community
gradio
python-dotenv
```

### 3. Configura Git

```bash
# Clone il tuo Space
git clone https://huggingface.co/spaces/YOUR_USERNAME/magi-system
cd magi-system

# Copia i file necessari
cp /path/to/your/Main_core_002.py .
cp /path/to/your/magi_web_interface.py .
cp /path/to/your/requirements.txt .

# Crea app.py
cat > app.py << 'EOF'
from magi_web_interface import create_interface

if __name__ == "__main__":
    app = create_interface()
    app.launch()
EOF
```

### 4. Aggiungi un README.md per lo Space

Crea un `README.md` specifico per Hugging Face:

```markdown
---
title: MAGI System
emoji: 🔺
colorFrom: red
colorTo: orange
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# 🔺 MAGI System - NERV Decision Support System

Three AI supercomputers working in consensus to analyze complex questions.

Based on the MAGI System from Neon Genesis Evangelion.

## Usage

1. Select your AI provider (Groq recommended)
2. Enter your question
3. Wait for the three MAGI units to reach consensus

⚠️ **Note**: You need to configure API keys in the Space settings.
```

### 5. Configura i Secrets (API Keys)

1. Vai alle **Settings** del tuo Space
2. Nella sezione **Repository secrets**, aggiungi:
   - `GROQ_API_KEY`: La tua chiave Groq
   - `OPENAI_API_KEY`: La tua chiave OpenAI (opzionale)
   - `SERPER_API_KEY`: La tua chiave Serper

### 6. Modifica il Codice per Hugging Face

In `magi_web_interface.py`, modifica la funzione `main()`:

```python
def main():
    """Launch the web interface"""
    
    # On Hugging Face Spaces, secrets are in environment variables
    if not os.getenv("GROQ_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        print("⚠️  WARNING: No API keys found in environment!")
        print("Please configure API keys in Space Settings > Repository secrets")
    
    app = create_interface()
    
    # For Hugging Face Spaces
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,  # Not needed on HF Spaces
        show_error=True
    )
```

### 7. Push al Repository

```bash
# Aggiungi tutti i file
git add app.py Main_core_002.py magi_web_interface.py requirements.txt README.md

# Commit
git commit -m "Initial MAGI System deployment"

# Push a Hugging Face
git push
```

### 8. Monitora il Build

1. Vai alla pagina del tuo Space
2. Guarda i **Logs** per vedere il build in progress
3. Una volta completato, l'app sarà live!

## 🔧 Risoluzione Problemi

### Build Failed - Requirements

Se il build fallisce sui requirements, prova:

```txt
# requirements.txt semplificato
crewai>=0.55.0
gradio>=4.40.0
langchain>=0.2.0
langchain-openai
langchain-groq
python-dotenv
```

### Timeout durante l'analisi

Aggiungi timeout in `Main_core_002.py`:

```python
magi_crew = Crew(
    # ... altri parametri
    max_rpm=4,
    timeout=300,  # 5 minuti max
)
```

### GPU non disponibile

Il tier gratuito usa solo CPU. Per GPU:
1. Vai in Space Settings
2. Hardware > Upgrade to GPU
3. Note: Richiede abbonamento Hugging Face PRO

## 🎨 Personalizzazione dell'URL

Puoi avere un URL custom tipo:
```
https://huggingface.co/spaces/YOUR_USERNAME/magi-nerv-system
```

Scegli il nome quando crei lo Space!

## 📊 Limitazioni Tier Gratuito

- **CPU**: Basic CPU (sufficiente per MAGI)
- **Storage**: 50GB
- **RAM**: ~16GB
- **Timeout**: 1h inattività
- **Sleep**: Lo Space va in sleep dopo 48h di inattività

Per risvegliarlo, basta visitare l'URL.

## 🔐 Sicurezza

### ⚠️ IMPORTANTE

1. **MAI** committare il file `.env`
2. Usa sempre i **Repository secrets** per le API keys
3. Se lo Space è pubblico, le tue API keys sono al sicuro (non visibili nel codice)
4. Monitora l'uso delle API per evitare abusi

### Rate Limiting

Aggiungi rate limiting per proteggere le tue API keys:

```python
import time
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, max_requests=10, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
    
    def can_make_request(self):
        now = datetime.now()
        cutoff = now - timedelta(seconds=self.time_window)
        self.requests = [req for req in self.requests if req > cutoff]
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
```

## 🌐 URL Finale

Il tuo MAGI System sarà disponibile a:
```
https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
```

Esempio:
```
https://huggingface.co/spaces/lordpba/magi-system
```

## 📱 Condivisione

Una volta deployato:
- ✅ Condividi il link con chiunque
- ✅ Embedded in altri siti
- ✅ API endpoint disponibile
- ✅ Non scade mai (finché non lo elimini)

## 🚀 Prossimi Passi

1. **Custom Domain**: Collega un tuo dominio
2. **Analytics**: Monitora l'uso con Gradio Analytics
3. **Duplicate**: Gli utenti possono duplicare il tuo Space
4. **Community**: Ricevi feedback nella sezione Discussion

## 📚 Risorse Utili

- [Hugging Face Spaces Docs](https://huggingface.co/docs/hub/spaces)
- [Gradio on Spaces](https://huggingface.co/docs/hub/spaces-sdks-gradio)
- [Managing Secrets](https://huggingface.co/docs/hub/spaces-overview#managing-secrets)

---

<div align="center">

### 🔺 Deploy your MAGI System to the world! 🔺

**Questions? Open an issue on GitHub!**

</div>
