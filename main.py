import gradio as gr
from app import translate, get_languages, set_openai_api_key, get_models

with gr.Blocks() as demo:

    gr.Label("Translator")
    model_dropdown = gr.Dropdown(label="Model Selection", value="gpt-3.5-turbo", choices=get_models())
    openai_api_key_textbox = gr.Textbox(
        label="Open AI API Key", placeholder="Set your OpenAI API key (Required)", type="password"
    )
    gr.Markdown("[Get Your OpenAI API key here](https://platform.openai.com/api-keys)")

    text_textbox = gr.Textbox(label="Text to translate")
    language_dropdown = gr.Dropdown(label="Language", choices=get_languages())
    translation_textbox = gr.Textbox(label="Translation")

    gr.Interface(
        fn=translate,
        inputs=[text_textbox, language_dropdown],
        outputs=[translation_textbox],
    )

    model_dropdown.change(set_openai_api_key, inputs=[openai_api_key_textbox, model_dropdown])
    openai_api_key_textbox.change(set_openai_api_key, inputs=[openai_api_key_textbox, model_dropdown])


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
