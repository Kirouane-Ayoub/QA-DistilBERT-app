import gradio as gr
from transformers import pipeline

# Load the question answering pipeline with your fine-tuned model
qa_pipe = pipeline("question-answering", model="ayoubkirouane/QA-DistilBERT-base-squad")

def answer_question(context, question):
    result = qa_pipe(question=question, context=context)
    return result['answer']

# Create a Gradio interface
iface = gr.Interface(
    fn=answer_question,
    inputs=["text", "text"],
    outputs="text",
    title="Question Answering with QA-DistilBERT-base-squad",
    description="Provide a context and a question to get an answer.",
)

# Launch the Gradio app
iface.launch(share=True)
