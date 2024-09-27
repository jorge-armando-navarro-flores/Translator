import gradio as gr
from app import translate, get_languages

with gr.Blocks() as demo:
    language_dropdown = gr.Dropdown(value="English", choices=get_languages())

    gr.Interface(
        fn=translate,
        inputs=["text", language_dropdown],
        outputs=["text"],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
