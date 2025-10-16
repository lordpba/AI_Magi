# 🔺 MAGI System - Hugging Face Deployment Guide

## 📁 Contents

This folder contains everything needed to deploy MAGI System on Hugging Face Spaces:

- `app.py` - Main Gradio interface with API key input and token statistics
- `magi_core.py` - MAGI system core logic with stats tracking
- `requirements.txt` - Python dependencies
- `README.md` - Hugging Face Space card (this file will be displayed on your Space)

## 🚀 How to Deploy on Hugging Face

### Option 1: Direct Upload

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Choose:
   - **Space name**: `magi-system` (or your preferred name)
   - **License**: MIT
   - **SDK**: Gradio
   - **SDK version**: 5.0.0 or higher
   - **Visibility**: Public or Private
4. Click **"Create Space"**
5. Upload these files from the `HF/` folder:
   - `app.py`
   - `magi_core.py`
   - `requirements.txt`
   - `README.md`
6. Wait for the Space to build (usually 2-5 minutes)
7. Done! Your MAGI system is live 🎉

### Option 2: Git Push

```bash
# Clone your new space
git clone https://huggingface.co/spaces/YOUR_USERNAME/magi-system
cd magi-system

# Copy files from HF folder
cp ../HF/* .

# Commit and push
git add .
git commit -m "Initial MAGI System deployment"
git push
```

## 🔑 API Keys Configuration

**Important**: Users will provide their own API keys through the web interface.

No environment variables need to be configured in Hugging Face Spaces settings, as API keys are entered by users directly in the UI.

### Optional: Pre-configure SERPER_API_KEY for search

If you want to enable internet search by default:

1. Go to your Space settings
2. Add a Secret:
   - Name: `SERPER_API_KEY`
   - Value: Your Serper API key from [serper.dev](https://serper.dev)

## 📊 Features

✅ **User-provided API keys** - Secure, never stored
✅ **Token usage statistics** - See real-time token consumption
✅ **Multiple providers** - Groq (free), OpenAI, or local Ollama
✅ **Evangelion theme** - NERV/MAGI aesthetic
✅ **Three-agent analysis** - Melchior, Balthasar, Casper
✅ **Example questions** - Pre-loaded Evangelion scenarios

## 🎨 Customization

### Change the theme colors

Edit the `EVANGELION_CSS` variable in `app.py`:

```python
EVANGELION_CSS = """
/* Customize colors here */
h1, h2, h3 {
    color: #ff6f00 !important;  /* Change to your preferred color */
}
"""
```

### Add more example questions

Edit the `gr.Examples` section in `app.py`:

```python
gr.Examples(
    examples=[
        ["Your custom question 1"],
        ["Your custom question 2"],
        # Add more...
    ],
    inputs=question_input
)
```

### Change default model

Edit `get_model()` in `magi_core.py`:

```python
return LLM(
    model="groq/llama-3.1-70b-versatile",  # Change model here
    temperature=temperature
)
```

## 🔧 Troubleshooting

### Build fails

- Check that all files are uploaded
- Verify `requirements.txt` has correct package versions
- Check Space logs for specific errors

### API key errors

- Ensure users are entering valid API keys
- Check that the correct provider is selected
- Verify API key format (Groq: `gsk_...`, OpenAI: `sk-...`)

### Out of memory

- Reduce model size in `magi_core.py`
- Use `llama-3.1-8b-instant` instead of larger models
- Consider upgrading to a paid Space tier

## 📈 Usage Limits

### Free Tier (Hugging Face)
- CPU: 2 cores
- RAM: 16GB
- Storage: 50GB
- Good for moderate usage

### Groq API (Free)
- 14,400 requests/day
- 20 requests/minute
- Perfect for demos and testing

### OpenAI API (Paid)
- Pay-per-token pricing
- No rate limits with sufficient credits
- Higher quality responses

## 🎯 Best Practices

1. **Start with Groq** - It's free and fast
2. **Enable token stats** - Users can monitor usage
3. **Add rate limiting** - Prevent abuse (optional)
4. **Monitor Space logs** - Check for errors
5. **Update regularly** - Keep dependencies current

## 📞 Support

- **GitHub Issues**: [github.com/lordpba/AI_Magi/issues](https://github.com/lordpba/AI_Magi/issues)
- **Hugging Face Discussions**: Use the Discussions tab on your Space
- **Documentation**: See main repo README

## 🎉 You're Ready!

Your MAGI System is now ready to deploy on Hugging Face Spaces. Follow the steps above and you'll have a public AI system inspired by Evangelion in minutes!

**MELCHIOR-1 • BALTHASAR-2 • CASPER-3**

---

*God's in his heaven, all's right with the world* 🔺
