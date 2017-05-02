# -*- coding: utf-8 -*-
import argparse

from recognize_async import start_operation
from recognize_async import wait_for_results
from recognize_async import write_results_to_file
from speech_context import read_phrases_from_file


DEFAULT_SAMPLE_RATE = 44100


def start(uri, path, sample_rate, context_file):
    hint_phrases = []
    if context_file:
        hint_phrases = read_phrases_from_file(context_file)
    operation = start_operation(uri, sample_rate, hint_phrases)
    results = wait_for_results(operation)
    write_results_to_file(path, results, operation.name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # TODO: add other args (encoding, language, etc.)
    parser.add_argument('uri', help='GCS URI for audio file')
    parser.add_argument('path', help='Output file path')
    parser.add_argument(
        '--sample-rate',
        dest='sample_rate',
        type=int,
        default=DEFAULT_SAMPLE_RATE,
        help='Sample rate of supplied audio data (defaults to {})'.format(DEFAULT_SAMPLE_RATE))
    parser.add_argument(
        '--speech-context',
        dest='speech_context',
        type=str,
        default=None,
        help='File path to JSON file containing hints: { "phrases": [...] }')
    args = parser.parse_args()
    start(args.uri, args.path, args.sample_rate, args.speech_context)
