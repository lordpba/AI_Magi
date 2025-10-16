"""
MAGI System - Web Interface v2.0
Neon Genesis Evangelion AI Simulation

Gradio web interface for the MAGI multi-agent system
"""

import gradio as gr
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Tuple

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Import MAGI system
from Main_core_002 import analyze_question

# Evangelion-themed CSS
EVANGELION_CSS = """
/* NERV/MAGI Theme - Evangelion Style */
.gradio-container {
    font-family: 'Courier New', monospace !important;
    background: linear-gradient(135deg, #0a0e1a 0%, #1a1f2e 100%) !important;
}

.contain {
    background: rgba(26, 31, 46, 0.95) !important;
    border: 2px solid #d32f2f !important;
    border-radius: 0px !important;
}

h1, h2, h3, h4, h5, h6, .centered-markdown {
    color: #ff6f00 !important;
    font-family: 'Courier New', monospace !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    text-shadow: 0 0 10px rgba(211, 47, 47, 0.5) !important;
    text-align: center !important;
}

.output-markdown, .gr-textbox, .gradio-markdown, .gradio-label, .gradio-status {
    text-align: center !important;
}

.tab-nav button {
    background: #1a1f2e !important;
    color: #00bcd4 !important;
    border: 1px solid #d32f2f !important;
    font-weight: bold !important;
}

.tab-nav button.selected {
    background: #d32f2f !important;
    color: white !important;
    border: 2px solid #ff6f00 !important;
}

textarea, input {
    background: #0a0e1a !important;
    color: #00ff41 !important;
    border: 1px solid #00bcd4 !important;
    font-family: 'Courier New', monospace !important;
}

.output-markdown {
    background: #0a0e1a !important;
    color: #00ff41 !important;
    border: 1px solid #d32f2f !important;
    padding: 20px !important;
    font-family: 'Courier New', monospace !important;
    text-align: center !important;
}

button {
    background: linear-gradient(135deg, #d32f2f 0%, #ff6f00 100%) !important;
    color: white !important;
    border: none !important;
    font-weight: bold !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    box-shadow: 0 0 20px rgba(211, 47, 47, 0.5) !important;
}

button:hover {
    box-shadow: 0 0 30px rgba(255, 111, 0, 0.8) !important;
}

.progress-bar {
    background: #d32f2f !important;
}

footer {
    color: #00bcd4 !important;
    text-align: center !important;
}
"""


def process_magi_query(
    question: str,
    provider: str = "Groq",
    ollama_model: str = "",
    enable_search: bool = False,
    temperature: float = 0.5
) -> Tuple[str, str]:
    """
    Process a query through the MAGI system
    
    Args:
        question: User's question
        provider: LLM provider (Groq or OpenAI)
        enable_search: Whether to enable internet search
        temperature: Model temperature
        
    Returns:
        Tuple of (result_text, status_message)
    """
    if not question or not question.strip():
        return "❌ ERROR: Please enter a question.", "⚠️ No input provided"
    
    try:
        # Convert provider name to lowercase
        provider_lower = provider.lower()
        # If Ollama, use custom model name
        if provider_lower == "ollama (local)":
            provider_lower = "ollama"
        
        # Add timestamp and header
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"""
╔══════════════════════════════════════════════════════════════════╗
║                     MAGI SYSTEM ANALYSIS                          ║
║                   Multi-Agent General Intelligence                ║
╚══════════════════════════════════════════════════════════════════╝

⏰ Timestamp: {timestamp}
❓ Question: {question}
🤖 Provider: {provider}
🌐 Search: {"Enabled" if enable_search else "Disabled"}
🌡️  Temperature: {temperature}
🦙 Ollama Model: {ollama_model if provider_lower == "ollama" else "-"}

{'='*70}
EXECUTING THREE-PERSPECTIVE ANALYSIS...
{'='*70}

"""
        # Run MAGI analysis
        result = analyze_question(
            question=question,
            provider=provider_lower,
            ollama_model=ollama_model,
            enable_search=enable_search,
            temperature=temperature
        )
        # Format output
        output = header + "\n" + result['result'] + "\n\n" + "="*70
        status = f"✅ Analysis completed successfully at {timestamp}"
        return output, status
    except Exception as e:
        error_msg = f"""
╔══════════════════════════════════════════════════════════════════╗
║                          ERROR                                    ║
╚══════════════════════════════════════════════════════════════════╝

❌ An error occurred during MAGI analysis:

{str(e)}

Please check:
- Your API keys are configured in config/.env
- You have a stable internet connection
- The question is not empty

"""
        return error_msg, f"❌ Error: {str(e)}"


def create_magi_interface():
    """Create the Gradio interface for MAGI system"""
    
    with gr.Blocks(css=EVANGELION_CSS, title="MAGI System", theme=gr.themes.Base()) as interface:
        # Header
        gr.Markdown("""
        # 🔺 MAGI SYSTEM 🔺
        ## Multi-Agent General Intelligence
        ### *Based on Neon Genesis Evangelion*
        
        ---
        
        The MAGI system consists of three AI agents, each representing a different aspect of Dr. Naoko Akagi's personality:
        - **MELCHIOR-1**: Scientific analysis (logic and data)
        - **BALTHASAR-2**: Ethical evaluation (emotions and morals)
        - **CASPER-3**: Practical assessment (social and real-world)
        
        All three perspectives are synthesized to provide comprehensive analysis.
        """, elem_classes="centered-markdown")
        # Main interface
        with gr.Row():
            with gr.Column(scale=2):
                # Input section
                question_input = gr.Textbox(
                    label="🎯 Enter Your Question",
                    placeholder="What question would you like the MAGI system to analyze?",
                    lines=3
                )
                
                # Settings
                with gr.Accordion("⚙️ Advanced Settings", open=False):
                    provider_dropdown = gr.Dropdown(
                        choices=["Groq", "OpenAI", "Ollama (local)"],
                        value="Groq",
                        label="LLM Provider",
                        info="Groq is free and fast, OpenAI requires paid API key, Ollama runs locally"
                    )
                    ollama_model_input = gr.Textbox(
                        label="Ollama Model Name (if using Ollama)",
                        placeholder="e.g. llama3, phi3, mistral, ...",
                        visible=False
                    )
                    search_checkbox = gr.Checkbox(
                        label="Enable Internet Search",
                        value=False,
                        info="Requires SERPER_API_KEY in .env file"
                    )
                    temperature_slider = gr.Slider(
                        minimum=0.0,
                        maximum=1.0,
                        value=0.5,
                        step=0.1,
                        label="Temperature",
                        info="Higher = more creative, Lower = more focused"
                    )
                
                # Action buttons
                with gr.Row():
                    analyze_btn = gr.Button("🚀 EXECUTE MAGI ANALYSIS", variant="primary", size="lg")
                    clear_btn = gr.Button("🗑️ Clear", variant="secondary")
            
            with gr.Column(scale=3):
                # Output section
                result_output = gr.Textbox(
                    label="📊 MAGI Analysis Result",
                    lines=20,
                    max_lines=30,
                    show_copy_button=True,
                    elem_classes="centered-markdown"
                )
                status_output = gr.Textbox(
                    label="ℹ️ Status",
                    lines=1,
                    interactive=False,
                    elem_classes="centered-markdown"
                )
        
        # Example questions
        gr.Examples(
            examples=[
                ["Should we deploy EVA Unit-01 against the approaching Angel despite Shinji's unstable sync ratio?"],
                ["Is it ethical to proceed with the Human Instrumentality Project to eliminate individual suffering?"],
                ["Should NERV prioritize civilian evacuation or Angel neutralization during an active attack on Tokyo-3?"],
                ["What is the acceptable risk threshold for activating a Dummy Plug system in combat operations?"],
                ["Should we collaborate with SEELE's directives or maintain autonomous control over NERV operations?"]
            ],
            inputs=question_input,
            label="💡 Example Questions"
        )
        
        # Footer
        gr.Markdown("""
        ---
        
        **MAGI System v2.0** | Powered by CrewAI & Groq  
        *"The truth lies in the synthesis of three perspectives"*  
        
        🔴 NERV Systems Division | 🟠 MAGI Supercomputer Array
        """)
        
        # Event handlers
        def update_ollama_visibility(provider):
            return gr.update(visible=(provider == "Ollama (local)"))
        provider_dropdown.change(
            fn=update_ollama_visibility,
            inputs=provider_dropdown,
            outputs=ollama_model_input
        )
        analyze_btn.click(
            fn=process_magi_query,
            inputs=[question_input, provider_dropdown, ollama_model_input, search_checkbox, temperature_slider],
            outputs=[result_output, status_output]
        )
        clear_btn.click(
            fn=lambda: ("", "", ""),
            inputs=None,
            outputs=[question_input, result_output, status_output]
        )
    
    return interface


def main():
    """Launch the MAGI web interface"""
    print("="*70)
    print("MAGI SYSTEM - WEB INTERFACE STARTING")
    print("="*70)
    print("\n🔺 Initializing NERV MAGI Supercomputer Array...")
    print("🔸 Loading: MELCHIOR-1 (Scientific)")
    print("🔸 Loading: BALTHASAR-2 (Ethical)")
    print("🔸 Loading: CASPER-3 (Practical)")
    print("\n✅ All systems operational")
    print("🌐 Launching web interface...\n")
    
    interface = create_magi_interface()
    
    # Launch with custom settings
    interface.launch(
        server_name="0.0.0.0",  # Allow external access
        server_port=7862,  # Different port to avoid conflict
        share=True,  # Create public link
        inbrowser=True,  # Open in browser automatically
        show_error=True
    )


if __name__ == "__main__":
    main()
