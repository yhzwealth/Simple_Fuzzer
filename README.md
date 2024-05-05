# PJ2 - 模糊测试（Fuzzing）
软件质量保障与测试 2023-2024春

## 项目结构
该简易模糊测丝滑项目由一个样例执行入口 main.py 以及如下五个包组成：

### examples
该包下的 Examples.py 中共有 5 个 Example Program，你可以通过模糊测试这 5 个样例程序来测试 fuzzer 工具的有效性以及工作效率

### fuzzer
该包下目前共有 3 个文件，具体体现为：
1. Fuzzer.py：该文件中的 Fuzzer 类，为所有 Fuzzers 的基类，Fuzzer 是处理输入生成以及 Schedule 调度的工具类
2. GreyBoxFuzzer.py：该文件中的 GreyBoxFuzzer 继承自 Fuzzer 类，其中编写了简易的输入选择，Mutation 调用以及覆盖率、Crashes统计的处理逻辑
3. PathGreyBoxFuzzer.py：该文件中的 PathGreyBoxFuzzer 继承自 GreyBoxFuzzer 类，目前没有编写逻辑，预期实现效果为 **根据 PathSchedule 的调度算法实现逻辑**

### runner
该包下目前共有 2 个文件，具体体现为：
1. Runner.py：该文件中的 Runner 类，为所有 Runners 的基类，Runner 是将 input 放入目标程序进行执行的工具类
2. FunctionCoverageRunner.py：该文件中的 FunctionCoverageRunner 继承自 Runner 类，其中编写了简易的函数执行以及获取执行覆盖率的处理逻辑

### schedule
该包下目前共有 2 个文件，具体体现为：
1. Schedule.py：该文件中的 Schedule 类，为所有 Schedules 的基类，Schedule 是进行 Seed 选择调度的工具类
2. PathSchedule.py：该文件中的 PathSchedule 继承自 Schedule 类，目前没有编写逻辑，预期实现效果为 **根据 inputs 经过的路径频率动态选择 Seed**

### utils
该包下目前共有 3 个文件，具体体现为：
1. Coverage.py：该文件中的 Coverage 类是统计覆盖率信息的工具类
2. Seed.py：该文件中的 Seed 类，存储了每个 Seed 的具体信息
3. Mutator.py：给文件中的 Mutator 类是具体执行 Mutate 的工具类，目前没有编写具体的 Mutation 逻辑

## 工程需求：
* 在 Mutator.py 中添加具体的变异逻辑，以达成 Fuzzing 的效果
* 完善 PathSchedule.py 以及 PathGreyBoxFuzzer.py，以完整实现 **根据 inputs 经过的路径频率动态选择 Seed**
* 添加更多可行的 Schedules 并放置于 schedule 包中

## 样例执行入口：
```python
from fuzzer.GreyBoxFuzzer import GreyBoxFuzzer
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from schedule.Schedule import Schedule
from examples.Examples import example1
from utils.Coverage import population_coverage

if __name__ == "__main__":
    # 构建相应程序的 Runner 对象
    f_runner = FunctionCoverageRunner(example1)
    
    # 构建带有初始 seeds 的 Fuzzer，并指定 schedule
    grey_fuzzer = GreyBoxFuzzer(seeds=["abcd"], schedule=Schedule())
    
    # 使用 Runner 执行 Fuzzer 中的输入，并指定运行时间(s)
    grey_fuzzer.runs(f_runner, run_time=5)
    
    # 可以使用 Coverage 中已经编写完成的函数查看本次 fuzzing 执行的覆盖率信息
    all_coverage, _ = population_coverage(list(map(lambda seed: seed.data, grey_fuzzer.population)), example1)
    print(all_coverage)
```