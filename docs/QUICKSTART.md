# 🚀 Guida Rapida di Avvio - MAGI System v2.0

## Avvio Velocissimo in 3 Passi

### 1️⃣ Installa le Dipendenze
```bash
pip install -r requirements.txt
```

### 2️⃣ Configura le API Keys
Crea un file `.env` e aggiungi le tue chiavi:
```env
GROQ_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
```

**Dove ottenere le chiavi gratuite:**
- Groq: https://console.groq.com
- Serper: https://serper.dev (2500 query/mese gratis)

### 3️⃣ Avvia l'Interfaccia Web
```bash
python magi_web_interface.py
```

L'interfaccia si aprirà automaticamente su `http://localhost:7860` e genererà anche un **link pubblico condivisibile**!

---

## 🎯 Avvio con Script Automatico

### Linux/Mac:
```bash
./launch_magi.sh
```

### Windows:
```cmd
launch_magi.bat
```

Gli script gestiranno automaticamente:
- ✓ Creazione del virtual environment
- ✓ Installazione dipendenze
- ✓ Avvio dell'interfaccia
- ✓ Controllo configurazione

---

## 🎮 Primi Passi nell'Interfaccia

1. **Seleziona il Provider AI**: 
   - Groq (consigliato - veloce e gratuito)
   - OpenAI (più potente ma a pagamento)

2. **Scegli la Lingua**:
   - Italiano
   - English
   - Japanese

3. **Inserisci la tua domanda**: 
   Esempio: "Shinji Ikari dovrebbe pilotare l'Eva-01?"

4. **Abilita la ricerca online** (opzionale):
   Per permettere ai MAGI di cercare informazioni su internet

5. **Clicca "INITIATE MAGI ANALYSIS"** e attendi il consenso!

---

## 💡 Query di Esempio

Clicca sugli esempi pre-caricati nell'interfaccia:

### In Contesto Evangelion:
- "Should Shinji Ikari pilot EVA-01?"
- "What are the ethical implications of the Human Instrumentality Project?"
- "Analyze the threat level of the 5th Angel (Ramiel)"
- "Is the use of child pilots morally acceptable?"
- "Evaluate the reliability of the Dummy Plug system"

### Domande Generiche:
- "È etico usare l'intelligenza artificiale per prendere decisioni militari?"
- "Quali sono i rischi dell'esplorazione spaziale umana?"
- "Analizza i pro e contro dell'energia nucleare"

---

## 🔧 Risoluzione Problemi Rapida

### ❌ "Module 'gradio' not found"
```bash
pip install gradio
```

### ❌ "API Key not found"
Verifica che il file `.env` esista e contenga le chiavi corrette.

### ❌ "Port 7860 already in use"
Modifica la porta in `magi_web_interface.py`:
```python
app.launch(server_port=7861)  # Cambia 7860 in 7861
```

### ❌ Errori durante la ricerca online
- Verifica la `SERPER_API_KEY`
- Oppure disabilita la ricerca nell'interfaccia

---

## 📱 Condivisione del Link Pubblico

Quando avvii l'interfaccia con `share=True` (già configurato), Gradio genera automaticamente un link pubblico tipo:

```
https://abc123.gradio.live
```

Questo link:
- ✅ È accessibile da chiunque
- ✅ Funziona anche se il tuo computer è dietro firewall/NAT
- ✅ È valido per 72 ore
- ⚠️ Condividilo solo con persone fidate (usa le tue API keys!)

---

## 🎨 Personalizzazione

### Cambiare i colori del tema:
Modifica le variabili CSS in `magi_web_interface.py`:

```python
--nerv-red: #d32f2f;        # Rosso NERV
--nerv-orange: #ff6f00;     # Arancione
--magi-blue: #0d47a1;       # Blu MAGI
--terminal-green: #00ff41;  # Verde terminale
```

### Cambiare il modello AI:
In `Main_core_002.py`:

```python
# Groq - modelli disponibili
"gemma2-9b-it"              # Default, veloce
"llama-3.1-70b-versatile"   # Più potente
"mixtral-8x7b-32768"        # Contesto molto lungo

# OpenAI - modelli disponibili  
"gpt-4o-mini"               # Default, economico
"gpt-4o"                    # Più potente
"gpt-4-turbo"               # Molto potente
```

---

## 📚 Prossimi Passi

1. ✅ Leggi la documentazione completa in `README_v2.md`
2. 🎮 Prova le query di esempio
3. 🎨 Personalizza il tema secondo i tuoi gusti
4. 🤝 Contribuisci al progetto su GitHub
5. 🌐 Condividi il link con altri fan di Evangelion!

---

## 🆘 Serve Aiuto?

- 📖 Documentazione completa: `README_v2.md`
- 🐛 Bug reports: GitHub Issues
- 💬 Discussioni: GitHub Discussions
- 📧 Contatto: GitHub profile

---

<div align="center">

### 🔺 NERV - God's in his heaven, all's right with the world 🔺

**MELCHIOR-1 • BALTHASAR-2 • CASPER-3**

*Three supercomputers. One consensus. Humanity's future.*

</div>
