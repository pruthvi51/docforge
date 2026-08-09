"""
Topological Sort DAG Compiler for Pipeline Steps.
"""
from typing import List
from docforge.models.spec import ExtractionPipelineSpec

def compile_execution_order(spec: ExtractionPipelineSpec) -> List[str]:
    in_degree = {s.step_id: len(s.depends_on) for s in spec.steps}
    graph = {s.step_id: [] for s in spec.steps}
    for s in spec.steps:
        for dep in s.depends_on:
            if dep in graph:
                graph[dep].append(s.step_id)

    queue = [sid for sid, deg in in_degree.items() if deg == 0]
    order = []
    while queue:
        curr = queue.pop(0)
        order.append(curr)
        for nxt in graph[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(order) != len(spec.steps):
        raise ValueError("Cyclic dependency detected in extraction pipeline!")
    return order
