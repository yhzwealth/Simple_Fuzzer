from typing import Tuple, Callable, Set, Any

from runner.Runner import Runner
from utils.Coverage import Coverage, Location


class FunctionCoverageRunner(Runner):
    def __init__(self, function: Callable) -> None:
        """Initialize.  `function` is a function to be executed"""
        self._coverage = None
        self.function = function
        
    def run_function(self, inp: str) -> Any:
        with Coverage() as cov:
            try:
                result = self.function(inp)
            except Exception as exc:
                self._coverage = cov.coverage()
                raise exc

        self._coverage = cov.coverage()
        return result

    def coverage(self) -> Set[Location]:
        return self._coverage
    
    def run(self, inp: str) -> Tuple[Any, str]:
        try:
            result = self.run_function(inp)
            outcome = self.PASS
        except Exception as exc:
            result = type(exc)
            outcome = self.FAIL

        return result, outcome
