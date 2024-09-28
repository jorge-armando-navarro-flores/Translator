import gradio as gr
from backend.app import get_models


def change_model_source(source):
    if source == "OpenAI":
        return (
            gr.Dropdown(
                label="Model Selection",
                value="gpt-3.5-turbo",
                choices=get_models(source),
            ),
            gr.Textbox(
                label="OpenAI API Key",
                placeholder="Set your OpenAI API key (Required)",
                type="password",
            ),
            gr.Markdown(
                "[Get Your OpenAI API key here](https://platform.openai.com/api-keys)"
            ),
        )
    elif source == "Groq":
        return (
            gr.Dropdown(
                label="Model Selection",
                value="gemma2-9b-it",
                choices=get_models(source),
            ),
            gr.Textbox(
                label="Groq API Key",
                placeholder="Set your Groq API key (Required)",
                type="password",
            ),
            gr.Markdown("[Get Your Groq API key here](https://console.groq.com/keys)"),
        )
    elif source == "MistralAI":
        return (
            gr.Dropdown(
                label="Model Selection",
                value="mistral-small-latest",
                choices=get_models(source),
            ),
            gr.Textbox(
                label="Mistral API Key",
                placeholder="Set your Mistral API key (Required)",
                type="password",
            ),
            gr.Markdown(
                "[Get Your Mistral API key here](https://console.mistral.ai/api-keys/)"
            ),
        )
    elif source == "HuggingFace":
        return (
            gr.Dropdown(
                label="Model Selection",
                value="HuggingFaceH4/zephyr-7b-beta",
                choices=get_models(source),
            ),
            gr.Textbox(
                label="HuggingFace API Key",
                placeholder="Set your HuggingFace API key (Required)",
                type="password",
            ),
            gr.Markdown(
                "[Get Your HuggingFace API key here](https://huggingface.co/settings/tokens)"
            ),
        )
