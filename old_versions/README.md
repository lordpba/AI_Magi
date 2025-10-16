# 📦 Old Versions - Legacy Files

Questa cartella contiene i file delle versioni precedenti del MAGI System (v1.0).

## 📁 Contenuto

### File Legacy (v1.0)

| File | Descrizione | Data |
|------|-------------|------|
| **Main_core.py** | Script originale v1.0 | ~2024 |
| **Main_core_refactor.py** | Versione intermedia | ~2024 |
| **Gui_Magi.py** | GUI originale | ~2024 |

### Output Vecchi

| File | Descrizione |
|------|-------------|
| **Magi_response.txt** | Risposte precedenti del sistema |
| **magi_system_log.txt** | Log di sistema vecchi |

## ⚠️ Nota Importante

Questi file sono mantenuti per riferimento storico ma **non sono più utilizzati** nel sistema v2.0.

### Usa Invece:

- ✅ **Nuova versione**: `src/Main_core_002.py`
- ✅ **Interfaccia web**: `src/magi_web_interface.py`
- ✅ **Entry point**: `src/app.py`

## 📚 Differenze Principali

### v1.0 (Legacy)
- Script procedurale
- Solo CLI
- Input hardcodato
- Nessuna interfaccia web
- Configurazione manuale

### v2.0 (Attuale)
- Architettura OOP
- Interfaccia web Gradio
- Configurazione tramite .env
- Theme Evangelion custom
- Deploy ready per Hugging Face
- Multi-lingua
- Documentazione estensiva

## 🗑️ Puoi Eliminare?

Sì, puoi eliminare questa cartella se:
- ✅ Hai testato v2.0 e funziona
- ✅ Non hai bisogno dei file legacy
- ✅ Non vuoi mantenere lo storico

**Per eliminare:**
```bash
rm -rf old_versions/
```

## 🔄 Migrazione da v1.0 a v2.0

Se hai usato v1.0 e vuoi migrare:

1. **API Keys**: Copia in `.env` nella root
2. **Configurazione**: Vedi `config/.env.example`
3. **Esecuzione**: Usa `python src/app.py`
4. **Documentazione**: Leggi `docs/QUICKSTART.md`

---

<div align="center">

**🔺 MAGI System v2.0 🔺**

*Questi file legacy sono parte della storia del progetto*

</div>
