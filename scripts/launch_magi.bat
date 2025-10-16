@echo off
REM MAGI System Launcher Script for Windows
REM Quick start script for the MAGI web interface

echo ╔══════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                              ║
echo ║                           MAGI SYSTEM v2.0                                   ║
echo ║                     NERV Decision Support System                             ║
echo ║                                                                              ║
echo ║                    MELCHIOR-1 • BALTHASAR-2 • CASPER-3                      ║
echo ║                                                                              ║
echo ╚══════════════════════════════════════════════════════════════════════════════╝
echo.

REM Check if .env file exists
if not exist .env (
    echo ⚠️  WARNING: .env file not found!
    echo.
    echo Creating .env from template...
    
    if exist config\.env.example (
        copy config\.env.example .env
        echo ✓ Created .env file from config\.env.example
        echo.
        echo Please edit .env and add your API keys before continuing.
        echo You can get API keys from:
        echo   - Groq: https://console.groq.com (free^)
        echo   - OpenAI: https://platform.openai.com
        echo   - Serper: https://serper.dev (free tier available^)
        echo.
        pause
    ) else (
        echo ❌ Error: config\.env.example not found!
        echo Please create a .env file manually with your API keys.
        pause
        exit /b 1
    )
)

REM Check if virtual environment exists
if not exist venv (
    echo 📦 Virtual environment not found. Creating one...
    python -m venv venv
    echo ✓ Virtual environment created
    echo.
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if dependencies are installed
echo 📚 Checking dependencies...
python -c "import gradio" 2>nul
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -r config\requirements.txt
    echo ✓ Dependencies installed
) else (
    echo ✓ Dependencies already installed
)

echo.
echo 🚀 Launching MAGI System Web Interface...
echo.
echo The interface will open in your browser at:
echo   Local:  http://localhost:7860
echo   Public: A shareable link will be generated
echo.
echo Press Ctrl+C to stop the server
echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo.

REM Launch the web interface
python src\app.py

pause
