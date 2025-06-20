# -*- coding: utf-8 -*-
"""ner_processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oGsrQ00a1_166cX1Fc89PNZx4P2x5vxu
"""

#### `ner_processing.py`

```python
from navec import Navec
from slovnet import NER

def extract_entities(text):
    navec = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
    ner_model = NER.load('slovnet_ner_news_v1.tar')
    ner_model.navec(navec)

    markup = ner_model(text)
    entities = []
    for span in markup.spans:
        entity_type = span.type
        start = span.start
        stop = span.stop
        entity_text = markup.text[start:stop]
        entities.append(f"{entity_type}\t{entity_text}\n")
    return entities