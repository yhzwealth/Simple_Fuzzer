import os

from fuzzer.PathGreyBoxFuzzer import PathGreyBoxFuzzer
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from schedule.PathPowerSchedule import PathPowerSchedule
from examples.Examples import example1, example2, example3, example4

if __name__ == "__main__":
    f_runner = FunctionCoverageRunner(example4)
    corpus_path = "corpus"

    seeds = []
    for i in os.listdir(corpus_path):
        fname = os.path.join(corpus_path, i)
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                seeds.append(f.read())

    grey_fuzzer = PathGreyBoxFuzzer(seeds=seeds, schedule=PathPowerSchedule(5))
    grey_fuzzer.runs(f_runner, run_time=60)
    print(f_runner.all_coverage)
