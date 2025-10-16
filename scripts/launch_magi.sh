#!/bin/bash

# MAGI System Launcher Script
# Quick start script for the MAGI web interface

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                              ║"
echo "║                           MAGI SYSTEM v2.0                                   ║"
echo "║                     NERV Decision Support System                             ║"
echo "║                                                                              ║"
echo "║                    MELCHIOR-1 • BALTHASAR-2 • CASPER-3                      ║"
echo "║                                                                              ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  WARNING: .env file not found!"
    echo ""
    echo "Creating .env from template..."
    
    if [ -f config/.env.example ]; then
        cp config/.env.example .env
        echo "✓ Created .env file from config/.env.example"
        echo ""
        echo "Please edit .env and add your API keys before continuing."
        echo "You can get API keys from:"
        echo "  - Groq: https://console.groq.com (free)"
        echo "  - OpenAI: https://platform.openai.com"
        echo "  - Serper: https://serper.dev (free tier available)"
        echo ""
        read -p "Press Enter after you've added your API keys..."
    else
        echo "❌ Error: config/.env.example not found!"
        echo "Please create a .env file manually with your API keys."
        exit 1
    fi
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Virtual environment not found. Creating one..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
echo "📚 Checking dependencies..."
if ! python -c "import gradio" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r config/requirements.txt
    echo "✓ Dependencies installed"
else
    echo "✓ Dependencies already installed"
fi

echo ""
echo "🚀 Launching MAGI System Web Interface..."
echo ""
echo "The interface will open in your browser at:"
echo "  Local:  http://localhost:7860"
echo "  Public: A shareable link will be generated"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "════════════════════════════════════════════════════════════════════════════════"
echo ""

# Launch the web interface
python src/app.py
