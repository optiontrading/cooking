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
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import spacy

# Use a pipeline as a high-level helper
# from transformers import pipeline

# ner 1
# pipe = pipeline("token-classification", model="edwardjross/xlm-roberta-base-finetuned-recipe-all")

# ner 2
# load the model and test set. Again, change the paths as required
# nlp = spacy.load('/home/himani/cooking/notebooks/TASTEset/output_eff/model-best')

def ner_mode_4(ingredient_str):

    # load model
    model_name = 'gk'
    model_file = f'/home/himani/cooking/notebooks/{model_name}.model.ser.gz'
    ner_prop_filename = f'/home/himani/cooking/notebooks/{model_name}.model.props'

    annotations = annotate_ner(model_file,
        [ingredient_str])

    tokens = [token for sentence in annotations[0].sentence for token in sentence.token]

    # for t in tokens:
        # print(t.coarseNER, ':', t.word)

    ner = [t.word for t in tokens if t.coarseNER == 'NAME']

    ner = ', '.join(ner)
    # print(ner)
    return ner

def ner_mode_3(ingredient_str):

    # load model
    model_name = 'ar'
    model_file = f'/home/himani/cooking/notebooks/{model_name}.model.ser.gz'
    ner_prop_filename = f'/home/himani/cooking/notebooks/{model_name}.model.props'

    annotations = annotate_ner(model_file,
        [ingredient_str])

    tokens = [token for sentence in annotations[0].sentence for token in sentence.token]

    # for t in tokens:
        # print(t.coarseNER, ':', t.word)

    ner = [t.word for t in tokens if t.coarseNER == 'NAME']

    ner = ', '.join(ner)
    # print(ner)
    return ner

# load ner model and return ingredient name
def ner_mode_2(ingredient_str):
    ner = []

    ner = [tok.text for tok in nlp(ingredient_str) if tok.ent_type_ == 'FOOD']

    # sample_sent = '3/4 cup all purpose flour'
    # for tok in nlp(sample_sent):
        # print(tok.ent_type_, tok.text)
    # tok.ent_type_ for tok in recipe

    ner = ', '.join(ner)
    # print(ner)
    return ner


# load ner model and return ingredient name
def ner_mode_1(ingredient_str):
    ner = []
    # print(ingredient_str)
    # pipe = pipeline("token-classification", model="edwardjross/xlm-roberta-base-finetuned-recipe-all")
    results = pipe(ingredient_str, grouped_entities=True)
    ner = [entity['word'] for entity in results if entity['entity_group'] == 'NAME']
    # for entity in results:
        # print(entity['entity_group'], ' : ', entity['word'])
        # ner.append(entity['entity_group'])

    ner = ', '.join(ner)
    # print(ner)
    return ner

# helper function to filter recipe based on minimum number of ingredients
def sort_recipes_based_on_ingredients(filtered_data):
    # todo : first use NER model to find ingredients present
    # todo : then sort the list based on minimum number of ingredients
    # filtered_data = [_['ingredients'] for _ in filtered_data]

    return filtered_data

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


