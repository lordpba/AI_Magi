# 🔺 MAGI System v2.0 - NERV Decision Support System

![MAGI System](https://github.com/lordpba/AI_Magi/assets/40633120/5fb8c5db-4295-4944-9034-73dd0785cd50)

**Three supercomputers. One consensus. Humanity's future.**

Una simulazione avanzata del Sistema MAGI da Neon Genesis Evangelion, ora con interfaccia web moderna e codice aggiornato per il 2025.

## 🌟 Novità nella versione 2.0

### ✨ Nuove Funzionalità
- 🎨 **Interfaccia Web con Gradio** - UI moderna con tema Evangelion
- 🌐 **Link Pubblico** - Condividi il sistema MAGI con un link pubblico
- 🔄 **Codice Refactorizzato** - Architettura orientata agli oggetti
- 📊 **Metriche in Tempo Reale** - Visualizzazione dei token e performance
- 🎭 **Tema Evangelion Completo** - CSS personalizzato con colori NERV
- 🌍 **Supporto Multi-lingua** - Italiano, Inglese, Giapponese
- 🔍 **Ricerca Online Opzionale** - Attiva/disattiva la ricerca internet

### 🤖 Le Tre Unità MAGI

#### MELCHIOR-1 🔬
**Ruolo**: Analisi Scientifica e Ragionamento Logico  
**Persona**: Dr. Naoko Akagi come scienziata  
**Funzione**: Analizza dati tecnici, identifica pattern, fornisce conclusioni basate su evidenze empiriche

#### BALTHASAR-2 🛡️
**Ruolo**: Coordinamento Difesa Strategica  
**Persona**: Dr. Naoko Akagi come madre  
**Funzione**: Formula strategie di difesa, valuta minacce, garantisce la sicurezza con focus protettivo

#### CASPER-3 ⚖️
**Ruolo**: Valutazione Etica  
**Persona**: Dr. Naoko Akagi come donna  
**Funzione**: Media tra logica ed emozione, valuta implicazioni etiche, assicura decisioni bilanciate

## 🚀 Installazione Rapida

### 1. Clone il Repository
```bash
git clone https://github.com/lordpba/AI_Magi.git
cd AI_Magi
```

### 2. Crea Ambiente Virtuale (Raccomandato)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oppure
venv\Scripts\activate  # Windows
```

### 3. Installa le Dipendenze
```bash
pip install -r requirements.txt
```

### 4. Configura le API Keys

Crea un file `.env` nella root del progetto:

```env
# API Key per Groq (consigliato - veloce e gratuito)
GROQ_API_KEY=your_groq_api_key_here

# API Key per OpenAI (opzionale)
OPENAI_API_KEY=your_openai_api_key_here

# API Key per Serper (ricerca internet)
SERPER_API_KEY=your_serper_api_key_here
```

#### 🔑 Dove Ottenere le API Keys

- **Groq**: [https://console.groq.com](https://console.groq.com) - Gratuito e veloce!
- **OpenAI**: [https://platform.openai.com](https://platform.openai.com) - Richiede credito
- **Serper**: [https://serper.dev](https://serper.dev) - 2500 query gratuite/mese

## 💻 Utilizzo

### Interfaccia Web (Consigliato) 🌐

Lancia l'interfaccia web con un semplice comando:

```bash
python magi_web_interface.py
```

L'interfaccia si aprirà automaticamente nel browser con:
- 🌐 **URL locale**: `http://localhost:7860`
- 🔗 **Link pubblico**: Generato automaticamente (condivisibile per 72 ore)

#### Caratteristiche dell'Interfaccia:
- ✨ Tema scuro ispirato a Evangelion
- 🎨 Colori NERV (rosso, arancione, blu)
- 📊 Visualizzazione in tempo reale dell'analisi
- 💡 Query di esempio pre-caricate
- 📈 Metriche di sistema dettagliate
- 🔍 Toggle per ricerca online

### Interfaccia a Linea di Comando (CLI) 💻

Per l'uso tradizionale da terminale:

```bash
python Main_core_002.py
```

#### Esempio di utilizzo CLI:
```python
from Main_core_002 import MagiSystem

# Inizializza il sistema
magi = MagiSystem(model_provider="groq", language="Italian")

# Analizza una domanda
analysis = magi.analyze_question(
    question="Shinji Ikari dovrebbe pilotare l'Eva-01?",
    enable_search=True
)

# Salva i risultati
magi.save_analysis(analysis)

print(analysis['result'])
```

## 📚 Esempi di Query

### Domande in Contesto Evangelion:

1. **Decisioni Piloti**:
   - "Shinji Ikari dovrebbe pilotare l'Eva-01?"
   - "È etico utilizzare piloti minorenni per gli Eva?"

2. **Analisi Strategica**:
   - "Valuta il livello di minaccia del 5° Angelo (Ramiel)"
   - "Quale strategia adottare contro un Angelo che si adatta?"

3. **Questioni Etiche**:
   - "Quali sono le implicazioni etiche del Progetto di Complementazione Umana?"
   - "Il sistema Dummy Plug è moralmente accettabile?"

4. **Analisi Tecnica**:
   - "Analizza l'affidabilità del sistema di sincronizzazione Eva"
   - "Valuta i rischi della riattivazione dell'Eva-00"

### Domande Generiche:

Il sistema può analizzare qualsiasi tipo di questione complessa:
- Decisioni tecniche
- Strategie aziendali
- Dilemmi etici
- Analisi di rischio
- Valutazioni scientifiche

## 🏗️ Architettura del Sistema

### Struttura del Progetto
```
AI_Magi/
├── Main_core.py              # Versione originale (legacy)
├── Main_core_002.py          # ✨ Versione refactorizzata 2.0
├── Main_core_refactor.py     # Versione intermedia
├── magi_web_interface.py     # 🌐 Interfaccia web Gradio
├── Gui_Magi.py               # GUI originale
├── requirements.txt          # Dipendenze aggiornate
├── readme.md                 # Documentazione originale
├── README_v2.md              # 📖 Questa documentazione
├── .env                      # API keys (da creare)
├── Magi_response.txt         # Output delle analisi
└── magi_system_log.txt       # Log di sistema
```

### Flusso di Lavoro

```
┌─────────────────┐
│  User Query     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  MAGI System    │
│  Initialization │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌─────────────────────────────────────────┐
│                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────┐  │
│  │MELCHIOR-1│  │BALTHASAR-2│  │CASPER-3│
│  │  🔬      │  │   🛡️     │  │  ⚖️   │
│  │Scientific│  │ Strategic │  │Ethical│
│  │ Analysis │  │  Defense  │  │Review │
│  └────┬─────┘  └─────┬─────┘  └───┬──┘  │
│       │              │            │     │
│       └──────────────┴────────────┘     │
│                      │                  │
│                      ▼                  │
│              ┌───────────────┐          │
│              │   CONSENSUS   │          │
│              └───────────────┘          │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│  Final Report   │
│  + Metrics      │
└─────────────────┘
```

## 🔧 Configurazione Avanzata

### Selezione del Modello

```python
# Usa Groq (veloce, gratuito)
magi = MagiSystem(model_provider="groq", model_name="gemma2-9b-it")

# Usa OpenAI (più avanzato)
magi = MagiSystem(model_provider="openai", model_name="gpt-4o-mini")

# Alternative per Groq
model_name="llama-3.1-70b-versatile"  # Più potente
model_name="mixtral-8x7b-32768"       # Contesto lungo
```

### Personalizzazione dell'Interfaccia

Modifica le variabili CSS in `magi_web_interface.py`:

```python
:root {
    --nerv-red: #d32f2f;      # Colore primario NERV
    --nerv-orange: #ff6f00;   # Colore secondario
    --magi-blue: #0d47a1;     # Colore MAGI
    --terminal-green: #00ff41; # Colore output
}
```

## 📊 Metriche e Performance

Il sistema fornisce metriche dettagliate:
- **Token Usage**: Token totali, prompt, completion
- **Response Time**: Tempo di elaborazione per ogni unità MAGI
- **Success Rate**: Tasso di successo delle richieste
- **Search Results**: Numero di fonti consultate

## 🐛 Troubleshooting

### Errore: "Import could not be resolved"
```bash
# Reinstalla le dipendenze
pip install --upgrade -r requirements.txt
```

### Errore: "API Key not found"
```bash
# Verifica che il file .env esista e contenga le chiavi
cat .env
```

### Interfaccia Web non si apre
```bash
# Verifica che la porta 7860 sia libera
lsof -i :7860  # Linux/Mac
netstat -ano | findstr :7860  # Windows

# Cambia porta se necessario
app.launch(server_port=7861)
```

### Errore durante la ricerca online
- Verifica la `SERPER_API_KEY` nel file `.env`
- Oppure disabilita la ricerca nell'interfaccia
- Controlla la connessione internet

## 🌐 Deploy Pubblico

### Hugging Face Spaces (Gratuito)

1. Crea account su [Hugging Face](https://huggingface.co)
2. Crea nuovo Space con Gradio
3. Carica i file del progetto
4. Aggiungi le API keys nei Secrets

### Altri Provider

- **Replit**: Deploy con un click
- **Railway**: Deploy automatico da GitHub
- **Render**: Free tier disponibile
- **Fly.io**: Deploy containerizzato

## 🤝 Contribuire

Questo è un progetto fan-made in continua evoluzione!

### Come Contribuire:
1. Fork il repository
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

### Idee per Contributi:
- 🎨 Miglioramenti UI/UX
- 🌍 Traduzioni aggiuntive
- 🤖 Supporto per altri modelli AI
- 📊 Nuove visualizzazioni dati
- 🎭 Easter eggs da Evangelion
- 📱 App mobile
- 🔊 Effetti sonori da Evangelion

## 📜 Lore di Evangelion

### Il Sistema MAGI

Nel mondo di Neon Genesis Evangelion, il Sistema MAGI è un trio di supercomputer organici sviluppati dalla Dr. Naoko Akagi presso la NERV. Ogni computer rappresenta un diverso aspetto della personalità della dottoressa:

- **CASPER** rappresenta lei come donna
- **MELCHIOR** rappresenta lei come scienziata
- **BALTHASAR** rappresenta lei come madre

Il sistema utilizza un processo decisionale basato sul consenso: una decisione viene presa solo quando almeno due dei tre computer concordano. Questo assicura che le decisioni siano bilanciate tra logica, strategia ed etica.

### Decisioni Prese dal MAGI nella Serie

- Attivazione degli Eva Units
- Strategie contro gli Angeli
- Protocolli di sicurezza NERV
- Autorizzazioni per esperimenti
- Gestione del Progetto di Complementazione

## 📄 Licenza

Questo progetto è un'opera fan-made creata per scopi educativi e di intrattenimento.

**Neon Genesis Evangelion** © GAINAX / khara

Il codice di questo progetto è rilasciato sotto licenza MIT - vedi il file LICENSE per i dettagli.

## 🙏 Ringraziamenti

- **Hideaki Anno** e **GAINAX/khara** per Neon Genesis Evangelion
- **CrewAI** per il framework multi-agente
- **Gradio** per l'interfaccia web
- La community di fan di Evangelion

## 📞 Contatti e Supporto

- **GitHub Issues**: Per bug e feature requests
- **Discussions**: Per domande e discussioni
- **Original Creator**: [@lordpba](https://github.com/lordpba)

---

<div align="center">

**⚠️ QUESTO È UN PROGETTO FAN-MADE ⚠️**

*Creato con ❤️ da fan di Evangelion per fan di Evangelion*

### 🔺 NERV - God's in his heaven, all's right with the world 🔺

</div>
