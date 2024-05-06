from fuzzer.GreyBoxFuzzer import GreyBoxFuzzer
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from schedule.Schedule import Schedule
from examples.Examples import example1, example2, example3
from utils.Coverage import population_coverage

if __name__ == "__main__":
    f_runner = FunctionCoverageRunner(example1)
    grey_fuzzer = GreyBoxFuzzer(seeds=["-11"], schedule=Schedule())
    grey_fuzzer.runs(f_runner, run_time=5)
    print(f_runner.all_coverage)
