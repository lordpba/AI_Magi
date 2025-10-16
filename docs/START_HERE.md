# 🔺 START HERE - MAGI System v2.0

**Benvenuto nel MAGI System!** Questa è la tua guida rapida per iniziare.

---

## 🎯 Prima Volta Qui? Leggi Questo!

### Chi Sei?

#### 🆕 Sono Nuovo - Voglio Solo Provarlo!

**→ Leggi: [`QUICKSTART.md`](QUICKSTART.md)**

In 5 minuti:
1. Installi le dipendenze
2. Configuri le API keys
3. Avvii l'interfaccia web
4. Provi il sistema MAGI!

**Quick Command:**
```bash
./launch_magi.sh  # Linux/Mac
launch_magi.bat   # Windows
```

---

#### 👨‍💻 Sono uno Developer - Voglio Capire il Codice

**→ Leggi in ordine:**
1. [`SUMMARY.md`](SUMMARY.md) - Panoramica completa del progetto
2. [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md) - Struttura file e architettura
3. [`README_v2.md`](README_v2.md) - Documentazione tecnica completa

**Poi studia il codice:**
1. `Main_core_002.py` - Core logic (300 linee)
2. `magi_web_interface.py` - Web UI (400 linee)

---

#### 🌐 Voglio Deployare Online

**→ Leggi: [`DEPLOY_GUIDE.md`](DEPLOY_GUIDE.md)**

Guida completa per:
- Hugging Face Spaces (gratuito!)
- Configurazione secrets
- Link pubblico permanente
- Troubleshooting deploy

---

#### 🤝 Voglio Contribuire al Progetto

**→ Leggi:**
1. [`README_v2.md`](README_v2.md) - Sezione "Contribuire"
2. [`CHANGELOG.md`](CHANGELOG.md) - Roadmap e feature future
3. [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md) - Per capire l'architettura

**Poi:**
1. Fork il repo
2. Crea un branch
3. Fai modifiche
4. Testa con `python test_setup.py`
5. Pull request!

---

## 📚 Mappa Completa della Documentazione

```
START_HERE.md (sei qui!)
    │
    ├─── 🚀 Quick Start
    │    └─→ QUICKSTART.md (5 minuti)
    │
    ├─── 📖 Documentazione Completa  
    │    └─→ README_v2.md (tutto quello che serve sapere)
    │
    ├─── 🗂️  Orientamento Progetto
    │    ├─→ PROJECT_STRUCTURE.md (mappa dei file)
    │    └─→ SUMMARY.md (riepilogo v2.0)
    │
    ├─── 🌐 Deploy & Sharing
    │    └─→ DEPLOY_GUIDE.md (Hugging Face Spaces)
    │
    └─── 📝 Altro
         └─→ CHANGELOG.md (storia e roadmap)
```

---

## ⚡ Super Quick Start (30 secondi)

Hai già tutto installato e configurato?

```bash
# Testa la configurazione
python test_setup.py

# Se tutto OK, lancia l'interfaccia
./launch_magi.sh
```

Visita: **http://localhost:7860**

---

## 🎮 Cosa Puoi Fare con MAGI?

Il sistema MAGI simula tre supercomputer AI che lavorano insieme:

- **MELCHIOR-1** 🔬: Analisi scientifica e logica
- **BALTHASAR-2** 🛡️: Strategia difensiva e protezione
- **CASPER-3** ⚖️: Valutazione etica e consenso

### Esempi di Domande

**In contesto Evangelion:**
- "Shinji Ikari dovrebbe pilotare l'Eva-01?"
- "Quali sono i rischi del Progetto di Complementazione?"
- "Come difendersi dal 5° Angelo Ramiel?"

**Domande generiche:**
- "È etico usare l'AI nelle decisioni militari?"
- "Quali strategie per esplorare Marte?"
- "Pro e contro dell'energia nucleare?"

---

## 🔑 Setup Veloce API Keys

### Dove Ottenerle (GRATIS!)

1. **Groq** (Consigliato - Veloce!)
   - 🔗 https://console.groq.com
   - ✅ Gratuito con limiti generosi
   - ⚡ Molto veloce

2. **Serper** (Per ricerca internet)
   - 🔗 https://serper.dev
   - ✅ 2500 query/mese gratis
   - 🔍 Necessario per ricerca online

3. **OpenAI** (Opzionale - Più potente)
   - 🔗 https://platform.openai.com
   - 💰 A pagamento (crediti)
   - 🚀 Modelli più avanzati

### Configura

```bash
# 1. Copia il template
cp .env.example .env

# 2. Edita con le tue chiavi
nano .env
# oppure
code .env
```

---

## 🛠️ Troubleshooting Rapido

### ❌ "Module not found"
```bash
pip install -r requirements.txt
```

### ❌ "API Key not found"
```bash
# Verifica che .env esista e contenga le chiavi
cat .env
```

### ❌ "Port 7860 already in use"
Modifica la porta in `magi_web_interface.py` linea ~320:
```python
app.launch(server_port=7861)  # Cambia numero
```

**Più problemi?** → [`README_v2.md`](README_v2.md) sezione Troubleshooting

---

## 📊 Struttura Progetto (Semplificata)

```
AI_Magi/
│
├── 🚀 ESEGUIBILI
│   ├── magi_web_interface.py    ← Interfaccia web (START HERE!)
│   ├── Main_core_002.py          ← Sistema core (o usa CLI)
│   ├── app.py                    ← Entry point per HF Spaces
│   └── test_setup.py             ← Test configurazione
│
├── 📚 DOCUMENTAZIONE
│   ├── START_HERE.md             ← Questo file!
│   ├── QUICKSTART.md             ← Guida rapida 5 min
│   ├── README_v2.md              ← Docs completa
│   ├── DEPLOY_GUIDE.md           ← Come deployare online
│   ├── PROJECT_STRUCTURE.md      ← Mappa file dettagliata
│   ├── SUMMARY.md                ← Riepilogo v2.0
│   └── CHANGELOG.md              ← Storia modifiche
│
├── 🔧 UTILITY
│   ├── launch_magi.sh            ← Launcher Linux/Mac
│   ├── launch_magi.bat           ← Launcher Windows
│   └── show_overview.sh          ← Mostra panoramica
│
└── ⚙️  CONFIG
    ├── .env.example              ← Template API keys
    ├── .env                      ← Le TUE keys (crea questo!)
    ├── requirements.txt          ← Dipendenze Python
    └── .gitignore                ← Protezione secrets
```

---

## 🎯 Percorsi Suggeriti

### Percorso 1: "Voglio Solo Usarlo" (10 minuti)
1. ✅ Leggi `QUICKSTART.md`
2. ✅ Esegui `./launch_magi.sh`
3. ✅ Prova le query di esempio
4. ✅ Divertiti!

### Percorso 2: "Voglio Capirlo" (30 minuti)
1. ✅ Leggi `SUMMARY.md`
2. ✅ Leggi `PROJECT_STRUCTURE.md`
3. ✅ Studia `Main_core_002.py`
4. ✅ Sperimenta con modifiche

### Percorso 3: "Voglio Deployarlo" (45 minuti)
1. ✅ Leggi `DEPLOY_GUIDE.md`
2. ✅ Crea account HF Spaces
3. ✅ Configura secrets
4. ✅ Push e deploy
5. ✅ Condividi il link!

### Percorso 4: "Voglio Contribuire" (1 ora)
1. ✅ Leggi `README_v2.md` completo
2. ✅ Studia il codice
3. ✅ Controlla `CHANGELOG.md` per feature richieste
4. ✅ Fork, modifica, PR!

---

## 🌟 Features Principali v2.0

### ✨ Cosa c'è di Nuovo
- 🌐 **Interfaccia Web Gradio** con tema Evangelion
- 🔗 **Link pubblico** auto-generato (condivisibile)
- 🎨 **UI custom** con colori NERV
- 📊 **Metriche in tempo reale**
- 🌍 **Multi-lingua** (IT/EN/JP)
- 🤖 **Supporto multi-modello** (Groq/OpenAI)
- 🔍 **Ricerca internet** integrata
- 💡 **Query di esempio** pre-caricate
- 🚀 **Deploy ready** per HF Spaces
- 📚 **Documentazione completa**

---

## 💡 Tips Utili

### Per Utenti
- 💰 **Usa Groq**: È gratuito e velocissimo!
- 🔍 **Disabilita ricerca** se non hai SERPER_API_KEY
- 💡 **Prova gli esempi** prima di fare domande custom
- 🌐 **Condividi il link** con amici (dura 72h)

### Per Developers  
- 📖 **Leggi il codice** in `Main_core_002.py` - è ben commentato
- 🎨 **Personalizza CSS** in `magi_web_interface.py` 
- 🔧 **Estendi MagiSystem** class per nuove features
- ✅ **Usa test_setup.py** prima di committare

---

## 🆘 Bisogno di Aiuto?

### Risorse
- 📚 **Documentazione**: Leggi i file `.md`
- 🐛 **Bug**: Apri issue su GitHub
- 💬 **Discussioni**: GitHub Discussions
- 📧 **Contatto**: GitHub profile dell'autore

### Checklist Problemi Comuni
- [ ] Ho letto `QUICKSTART.md`?
- [ ] Ho eseguito `test_setup.py`?
- [ ] Il mio `.env` ha le API keys?
- [ ] Ho installato le dipendenze?
- [ ] Ho controllato il Troubleshooting in README?

---

## 🎉 Ready to Start?

### Comando Magico per Iniziare
```bash
# 1. Test tutto
python test_setup.py

# 2. Se OK, lancia!
./launch_magi.sh
```

### Primo Accesso
1. 🌐 Browser si apre su `http://localhost:7860`
2. 🔗 Copia il link pubblico dalla console
3. 💡 Clicca un esempio o scrivi la tua query
4. 🚀 Premi "INITIATE MAGI ANALYSIS"
5. ⏳ Attendi il consenso dei tre MAGI
6. 📊 Leggi l'analisi completa!

---

<div align="center">

# 🔺 BENVENUTO NEL MAGI SYSTEM! 🔺

### MELCHIOR-1 • BALTHASAR-2 • CASPER-3

**Three supercomputers. One consensus. Humanity's future.**

---

## Quick Links

📚 [QUICKSTART](QUICKSTART.md) | 
📖 [README](README_v2.md) | 
🌐 [DEPLOY](DEPLOY_GUIDE.md) | 
🗂️ [STRUCTURE](PROJECT_STRUCTURE.md)

---

### 🚀 Ready? Let's Go!

```bash
./launch_magi.sh
```

*God's in his heaven, all's right with the world.*

---

**MAGI System v2.0** | Created with ❤️ by Evangelion fans

*Neon Genesis Evangelion © GAINAX / khara*

</div>
