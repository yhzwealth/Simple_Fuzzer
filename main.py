from fuzzer.GreyBoxFuzzer import GreyBoxFuzzer
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from schedule.Schedule import Schedule
from examples.Examples import example1
from utils.Coverage import population_coverage

if __name__ == "__main__":
    f_runner = FunctionCoverageRunner(example1)
    grey_fuzzer = GreyBoxFuzzer(seeds=["abcd"], schedule=Schedule())
    grey_fuzzer.runs(f_runner, run_time=5)
    all_coverage, _ = population_coverage(list(map(lambda seed: seed.data, grey_fuzzer.population)), example1)
    print(all_coverage)
