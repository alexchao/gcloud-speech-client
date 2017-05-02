# -*- coding: utf-8 -*-
import json
import sys
import time


from google.cloud import speech


POLL_DELAY = 3
JSON_INDENT_SIZE = 2


# TODO(#3): consolidate operation arguments into a config object
def start_operation(gcs_uri, sample_rate, hint_phrases):
    """Start an asychronous speech-to-text operation.

    Arguments:
        gcs_uri -- gs://bucket-name/file-name.flac
        sample_rate -- e.g. 44100
        hint_phrases -- list of speech context hints as strings

    Return the started `Operation`
    """
    client = speech.Client()
    # TODO: allow user to specify encoding
    sample = client.sample(
        source_uri=gcs_uri,
        encoding=speech.Encoding.FLAC,
        sample_rate_hertz=sample_rate)
    # TODO: allow user to specify language
    operation = sample.long_running_recognize(
        'en-US',
        speech_contexts=hint_phrases)
    sys.stdout.write('Started job: {n}\n'.format(n=operation.name))
    return operation


def wait_for_results(operation):
    """Poll an operation for results and show progress.

    Return result set.
    """
    while not operation.complete:
        time.sleep(POLL_DELAY)
        operation.poll()
        sys.stdout.write('\rProgress: {p}%'.format(
            p=operation.metadata.progress_percent))
        sys.stdout.flush()

    sys.stdout.write('\rProgress: Done\n')
    sys.stdout.flush()

    return operation.results


def _result_as_json(r):
    alts = [
        {'transcript': a.transcript, 'confidence': a.confidence}
        for a in r.alternatives
    ]
    return {'alternatives': alts}


def _format_results(results):
    results_json = {}
    results_json['results'] = [_result_as_json(r) for r in results]
    return results_json


def write_results_to_file(file_path, results, operation_name):
    """Write result set out to given file path as JSON."""
    results_json = _format_results(results)
    results_json['name'] = operation_name
    with open(file_path, 'w') as f:
        f.write(json.dumps(results_json, indent=JSON_INDENT_SIZE))
