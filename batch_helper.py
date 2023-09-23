# import libraries
import os
import PyPDF2
import stanza
import re
from pathlib import Path
from typing import List, Tuple, Generator
from tqdm.notebook import tqdm
from stanza.server import CoreNLPClient
from dataclasses import dataclass, asdict
import pandas as pd

def annotate_ner(ner_model_file: str, texts: List[str], tokenize_whitespace: bool = True):
    properties = {"ner.model": ner_model_file, "tokenize.whitespace": tokenize_whitespace, "ner.applyNumericClassifiers": False}
    
    annotated = []
    with CoreNLPClient(
         annotators=['tokenize','ssplit','ner'],
         properties=properties,
         timeout=30000,
         be_quiet=True,
        memory='6G') as client:
    
        for text in tqdm(texts):
            annotated.append(client.annotate(text))
    return annotated

@dataclass
class NERData:
    ner: List[str]
    tokens: List[str]
        
    # Let's use Pandas to make it pretty in a notebook
    def _repr_html_(self):
        return pd.DataFrame(asdict(self)).T._repr_html_()

def extract_ner_data(annotation) -> NERData:
    tokens = [token for sentence in annotation.sentence for token in sentence.token]
    return NERData(tokens=[t.word for t in tokens], ner=[t.coarseNER for t in tokens])


