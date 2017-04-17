# -*- coding: utf-8 -*-
import argparse

from recognize_async import start_operation
from recognize_async import wait_for_results
from recognize_async import write_results_to_file


def start(uri, path):
    operation = start_operation(uri, 44100)
    results = wait_for_results(operation)
    write_results_to_file(path, results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # TODO: add other args (sample rate, encoding, language, etc.)
    parser.add_argument('uri', help='GCS URI for audio file')
    parser.add_argument('path', help='Output file path')
    args = parser.parse_args()
    start(args.uri, args.path)
