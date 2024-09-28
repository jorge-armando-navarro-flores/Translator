import gradio as gr
from app import translate, get_languages, set_openai_api_key, get_models


def change_model_source(source):
    if source == "OpenAI":
        return (
            gr.Dropdown(
                label="Model Selection",
                value="gpt-3.5-turbo",
                choices=get_models(source),
            ),
            gr.Textbox(
                value="",
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
                value="",
                label="Groq API Key",
                placeholder="Set your Groq API key (Required)",
                type="password",
            ),
            gr.Markdown(
                "[Get Your Groq API key here](https://console.groq.com/keys)"
            ),
        )
    elif source == "MistralAI":
        return (
            gr.Dropdown(
                label="Model Selection",
                value="mistral-small-latest",
                choices=get_models(source),
            ),
            gr.Textbox(
                value="",
                label="Mistral API Key",
                placeholder="Set your Mistral API key (Required)",
                type="password",
            ),
            gr.Markdown(
                "[Get Your Mistral API key here](https://console.mistral.ai/api-keys/)"
            ),
        )


with gr.Blocks() as demo:

    gr.Label("Translator")
    radio = gr.Radio(value="OpenAI", choices=["OpenAI", "Groq", "MistralAI"], label="Model Source")
    model_dropdown = gr.Dropdown(
        label="Model Selection", value="gpt-3.5-turbo", choices=get_models("OpenAI")
    )
    openai_api_key_textbox = gr.Textbox(
        value="",
        label="Open AI API Key",
        placeholder="Set your OpenAI API key (Required)",
        type="password",
    )
    api_key_link_dropdown = gr.Markdown(
        "[Get Your OpenAI API key here](https://platform.openai.com/api-keys)"
    )

    text_textbox = gr.Textbox(label="Text to translate")
    language_dropdown = gr.Dropdown(label="Language", choices=get_languages())
    translation_textbox = gr.Textbox(label="Translation")

    gr.Interface(
        fn=translate,
        inputs=[text_textbox, language_dropdown],
        outputs=[translation_textbox],
    )
    gr.Markdown(
        "If you liked this space, please give me a star on GitHub 😉: [Github repo](https://github.com/jorge-armando-navarro-flores/Translator)"
    )

    model_dropdown.change(
        set_openai_api_key, inputs=[openai_api_key_textbox, model_dropdown, radio]
    )
    openai_api_key_textbox.change(
        set_openai_api_key, inputs=[openai_api_key_textbox, model_dropdown, radio]
    )
    radio.change(
        set_openai_api_key, inputs=[openai_api_key_textbox, model_dropdown, radio]
    )
    radio.change(
        change_model_source,
        inputs=[radio],
        outputs=[model_dropdown, openai_api_key_textbox, api_key_link_dropdown],
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
