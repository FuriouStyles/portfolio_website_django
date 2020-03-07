from django.apps import AppConfig
import html
import pathlib
import os


class BoxingConfig(AppConfig):
    name = 'boxing'
    MODEL_PATH = Path("model")
    #BOXING_PRETRAINED_PATH = path
    LABEL_PATH = Path("label/")
    #pred
