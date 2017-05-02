# -*- coding: utf-8 -*-
import json


def read_phrases_from_file(file_path):
    with open(file_path, 'r') as f:
        context_data = json.loads(f.read())
    return context_data['phrases']
