# 📁 Struttura del Progetto MAGI System

Questa è una guida completa a tutti i file del progetto e le loro funzioni.

## 🎯 File Principali per l'Utente

### Script Eseguibili

| File | Descrizione | Uso |
|------|-------------|-----|
| **`magi_web_interface.py`** | 🌐 Interfaccia web Gradio principale | `python magi_web_interface.py` |
| **`Main_core_002.py`** | 💻 Sistema MAGI refactorizzato (v2.0) | `python Main_core_002.py` (CLI) |
| **`app.py`** | 🚀 Entry point per Hugging Face Spaces | Auto-run su HF Spaces |
| **`test_setup.py`** | 🔧 Script di test configurazione | `python test_setup.py` |

### Script di Avvio

| File | Descrizione | Uso |
|------|-------------|-----|
| **`launch_magi.sh`** | 🐧 Launcher automatico (Linux/Mac) | `./launch_magi.sh` |
| **`launch_magi.bat`** | 🪟 Launcher automatico (Windows) | `launch_magi.bat` |

## 📚 Documentazione

| File | Contenuto | Per Chi |
|------|-----------|---------|
| **`README_v2.md`** | 📖 Documentazione completa v2.0 | Tutti - LEGGI PRIMA |
| **`QUICKSTART.md`** | 🚀 Guida rapida di avvio | Principianti |
| **`DEPLOY_GUIDE.md`** | 🌐 Guida deploy Hugging Face | Deploy in produzione |
| **`CHANGELOG.md`** | 📝 Storia delle modifiche | Developers |
| **`readme.md`** | 📄 README originale (v1.0) | Reference storico |
| **`PROJECT_STRUCTURE.md`** | 📁 Questo file | Orientamento progetto |

## 🔧 Configurazione

| File | Descrizione | Note |
|------|-------------|------|
| **`.env.example`** | 🔑 Template per API keys | Copia in `.env` e configura |
| **`.env`** | 🔒 API keys (non committare!) | Creato dall'utente |
| **`requirements.txt`** | 📦 Dipendenze Python | `pip install -r requirements.txt` |
| **`.gitignore`** | 🚫 File da escludere da Git | Protegge `.env` |

## 💾 Output e Log

| File | Descrizione | Generato Da |
|------|-------------|-------------|
| **`Magi_response.txt`** | 📄 Ultima analisi MAGI | Sistema MAGI |
| **`magi_system_log.txt`** | 📋 Log di sistema dettagliati | CrewAI |

## 🗂️ Versioni Legacy

| File | Descrizione | Status |
|------|-------------|--------|
| **`Main_core.py`** | 🕰️ Script originale v1.0 | Legacy - usa v2.0 |
| **`Main_core_refactor.py`** | 🔄 Versione intermedia | Legacy |
| **`Gui_Magi.py`** | 🖼️ GUI originale | Legacy - usa web interface |

## 🎨 Media

| File | Descrizione | Uso |
|------|-------------|-----|
| **`Magi.jpg`** | 🖼️ Logo/Immagine MAGI | README, documentazione |

## 🗃️ Cartelle di Sistema

| Cartella | Contenuto | Note |
|----------|-----------|------|
| **`.git/`** | Repository Git | Gestito da Git |
| **`venv/`** | Virtual environment | Creato da utente (in .gitignore) |
| **`__pycache__/`** | Cache Python | Auto-generato (in .gitignore) |

---

## 📊 Diagramma delle Dipendenze

```
┌─────────────────────────────────────────────────┐
│                USER INTERFACE                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  Web Interface           CLI                    │
│  ├─ magi_web_interface.py  ├─ Main_core_002.py │
│  └─ app.py (HF Spaces)     └─ test_setup.py    │
│                                                 │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│            CORE MAGI SYSTEM                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  Main_core_002.py                               │
│  ├─ MagiSystem Class                            │
│  │  ├─ Agent: MELCHIOR-1                        │
│  │  ├─ Agent: BALTHASAR-2                       │
│  │  └─ Agent: CASPER-3                          │
│  └─ Analysis Engine                             │
│                                                 │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│              DEPENDENCIES                       │
├─────────────────────────────────────────────────┤
│                                                 │
│  ├─ CrewAI (Multi-agent framework)              │
│  ├─ LangChain (LLM orchestration)               │
│  ├─ Gradio (Web interface)                      │
│  ├─ Groq/OpenAI (AI models)                     │
│  └─ SerperDev (Internet search)                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🚀 File di Avvio: Quale Usare?

### Per Utenti Normali

**Interfaccia Web (Consigliato):**
```bash
# Linux/Mac - Con launcher automatico
./launch_magi.sh

# Windows - Con launcher automatico  
launch_magi.bat

# Oppure direttamente
python magi_web_interface.py
```

**Linea di Comando:**
```bash
python Main_core_002.py
```

### Per Developers

**Test Configurazione:**
```bash
python test_setup.py
```

**Deploy su Hugging Face:**
```bash
# Il file app.py viene usato automaticamente
git push
```

---

## 📝 Workflow Tipico

### 1. Primo Avvio

```bash
# 1. Clone/Download del progetto
git clone https://github.com/lordpba/AI_Magi.git
cd AI_Magi

# 2. Setup configurazione
cp .env.example .env
# Edita .env con le tue API keys

# 3. Test setup
python test_setup.py

# 4. Avvia interfaccia
./launch_magi.sh  # o launch_magi.bat su Windows
```

### 2. Uso Quotidiano

```bash
# Basta lanciare l'interfaccia
./launch_magi.sh
```

### 3. Aggiornamento

```bash
# Pull ultime modifiche
git pull

# Aggiorna dipendenze
pip install --upgrade -r requirements.txt

# Testa
python test_setup.py

# Avvia
./launch_magi.sh
```

---

## 🔍 Come Trovare Cosa

### Cerchi...?

| Cosa | Dove guardare |
|------|---------------|
| 📖 **Come iniziare** | `QUICKSTART.md` |
| 🔧 **Come configurare** | `README_v2.md` + `.env.example` |
| 🌐 **Come deployare** | `DEPLOY_GUIDE.md` |
| 🐛 **Come debuggare** | `test_setup.py` + `README_v2.md` (Troubleshooting) |
| 💻 **Come usare CLI** | `Main_core_002.py` + esempi in `README_v2.md` |
| 🎨 **Come personalizzare UI** | `magi_web_interface.py` (sezione CSS) |
| 📝 **Storia modifiche** | `CHANGELOG.md` |
| 🤝 **Come contribuire** | `README_v2.md` (sezione Contribuire) |

---

## 🗂️ File NON Committare su Git

Questi file sono esclusi dal versioning (vedi `.gitignore`):

```
❌ .env                    # Contiene API keys sensibili
❌ venv/                   # Virtual environment locale
❌ __pycache__/            # Cache Python
❌ *.pyc                   # Bytecode compilato
❌ Magi_response.txt       # Output analisi
❌ magi_system_log.txt     # Log di sistema
❌ .idea/                  # Config IDE
❌ .vscode/                # Config VSCode
```

---

## 📦 Dimensioni Approssimative

| Tipo | Dimensione |
|------|------------|
| **Codice sorgente** | ~150 KB |
| **Documentazione** | ~100 KB |
| **Dipendenze** (`venv/`) | ~500 MB |
| **Totale progetto** (senza venv) | ~250 KB |

---

## 🎯 File Essenziali per Deploy

### Deploy Minimale (Hugging Face)

File necessari:
```
✅ app.py
✅ Main_core_002.py
✅ magi_web_interface.py
✅ requirements.txt
✅ README.md (per HF)
```

File opzionali ma consigliati:
```
📄 .env (secrets su HF)
📄 .gitignore
📄 Magi.jpg (per README)
```

---

## 🔄 Flow dei Dati

```
┌──────────────┐
│ User Query   │
└──────┬───────┘
       │
       ▼
┌──────────────────────┐
│ magi_web_interface   │  ← Interfaccia Gradio
│ (Frontend)           │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Main_core_002.py     │  ← Core Logic
│ MagiSystem class     │
└──────┬───────────────┘
       │
       ├──────────────┐
       │              │
       ▼              ▼
┌──────────┐  ┌──────────────┐
│ CrewAI   │  │ Search Tools │
│ Agents   │  │ (Serper)     │
└──────┬───┘  └──────┬───────┘
       │              │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ AI Models    │
       │ (Groq/OpenAI)│
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ Response     │
       │ + Metrics    │
       └──────────────┘
```

---

## 🎓 Per Imparare il Codice

### Ordine di Lettura Consigliato

1. **`QUICKSTART.md`** - Panoramica veloce
2. **`README_v2.md`** - Documentazione completa
3. **`Main_core_002.py`** - Core logic (300 linee)
4. **`magi_web_interface.py`** - UI layer (400 linee)
5. **`test_setup.py`** - Testing e validazione
6. **`CHANGELOG.md`** - Storia e decisioni di design

### Complessità del Codice

| File | Linee | Difficoltà | Note |
|------|-------|------------|------|
| `Main_core_002.py` | ~300 | ⭐⭐⭐ | OOP, CrewAI |
| `magi_web_interface.py` | ~400 | ⭐⭐ | Gradio, CSS |
| `test_setup.py` | ~200 | ⭐ | Script semplice |
| `app.py` | ~50 | ⭐ | Entry point |

---

## 💡 Tips

### Per Utenti
- 📖 Leggi `QUICKSTART.md` prima
- 🎯 Usa gli script launcher per facilità
- 🧪 Esegui `test_setup.py` se hai problemi
- 🌐 L'interfaccia web è più user-friendly della CLI

### Per Developers
- 📚 Studia `Main_core_002.py` per capire la logica
- 🎨 Modifica `magi_web_interface.py` per UI
- 🔧 Estendi la classe `MagiSystem` per nuove features
- 📝 Aggiorna `CHANGELOG.md` per ogni modifica

### Per Contributors
- 🍴 Fork prima di modificare
- 🌿 Usa branch per features
- ✅ Testa con `test_setup.py`
- 📄 Documenta le modifiche

---

<div align="center">

## 🔺 MAGI System File Structure 🔺

**Una guida completa per navigare il progetto**

*"Understanding the system is the first step to mastering it"*

</div>
