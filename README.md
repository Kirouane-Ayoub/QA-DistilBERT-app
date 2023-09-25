# QA-DistilBERT-app

## Overview
+ **Model Name**: QA-DistilBERT-base-squad
+ **Task**: Question Answering (QA)
+ **Dataset**: squad_v2
+ **Model Type**: DistilBERT-based model

## Model Description
**QA-DistilBERT-base-squad** is a fine-tuned version of the DistilBERT model, which is a smaller and faster variant of BERT while preserving much of BERT's performance. It has been fine-tuned for the task of Question Answering (QA) on the squad_v2 dataset.

## Dataset
+ **Name**: squad_v2
+ **Description**: The squad_v2 dataset combines 100,000 questions from SQuAD1.1 with over 50,000 unanswerable questions written adversarially to resemble answerable ones. This dataset challenges models not only to answer questions correctly when possible but also to recognize when no answer is supported by the paragraph.

## Usage
**QA-DistilBERT-base-squad** can be used for a wide range of question answering tasks. It is suitable for extracting answers from passages of text given a question. Users can input a passage and a question, and the model will generate an answer.

## Limitations

Like all language models, QA-DistilBERT-base-squad may generate incorrect answers if the training data contains inaccuracies or ambiguities.
The model's performance may vary depending on the complexity and domain of the questions.

## Ethical Considerations
When using QA-DistilBERT-base-squad for question answering tasks, it is essential to be aware of potential biases in the training data and to ensure that the model does not produce harmful or biased answers.

## Get started 

```python
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("question-answering", model="ayoubkirouane/QA-DistilBERT-base-squad")
context = """
The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica,Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud),also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America.This basin encompasses 7,000,000 square kilometres 
(2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations.The majority of the forest is contained within Brazil, with 60% of the rainforest, 
followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain "Amazonas" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world,with an estimated 390 billion individual trees divided into 16,000 species.
"""
question = "Which name is also used to describe the Amazon rainforest in English?"
result = pipe(question=question, context=context)
print(result)
```

## gradio APP : 


```
pip -r requirements.txt
python app.py
```

+ You can check the demo from here : **https://huggingface.co/spaces/ayoubkirouane/QA-DistilBERT-base-squad**
![Screenshot at 2023-09-25 17-59-39](https://github.com/Kirouane-Ayoub/QA-DistilBERT-app/assets/99510125/273b071d-ade6-4dea-9eed-cb8bd51f0eec)

+ Created By **Kirouane AYoub** 
