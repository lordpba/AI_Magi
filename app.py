"""
Gradio Spaces entrypoint for MAGI System.

This file exposes a top-level variable `app` (a gradio.Blocks instance)
so that Gradio/Hugging Face Spaces can serve the UI without calling launch().
"""

from src.magi_web_interface import create_magi_interface

# Gradio/HF Spaces will look for `app` or `demo`.
app = create_magi_interface()
