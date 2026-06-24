import networkx as nx

from app.schemas.workflow import Phase, ServiceCard, WorkflowResponse
from app.services.seed_data import GOALS, SERVICES


class WorkflowGraphError(ValueError):
    pass


def build_workflow(goal_key: str, prompt_hash: str, extra_service_ids: list[str] | None = None) -> WorkflowResponse:
    goal = GOALS[goal_key]
    service_ids = list(dict.fromkeys([*goal["services"], *(extra_service_ids or [])]))
    graph = nx.DiGraph()
    graph.add_nodes_from(service_ids)
    graph.add_edges_from(goal["dependencies"])

    if not nx.is_directed_acyclic_graph(graph):
        raise WorkflowGraphError("Workflow dependencies must be a DAG")

    generations = list(nx.topological_generations(graph))
    phases = [
        Phase(
            id=f"phase-{index}",
            title=f"Phase {index}",
            services=[ServiceCard(**SERVICES[service_id]) for service_id in sorted(generation)]
        )
        for index, generation in enumerate(generations, start=1)
    ]

    return WorkflowResponse(
        goal_detected=goal["goal"],
        category=goal["category"],
        timeline=goal["timeline"],
        phases=phases,
        prompt_hash=prompt_hash,
        disclaimer="This workflow is generated from manually verified sources and predefined rules. ProcessIQ does not guarantee approval or legal compliance."
    )


def parallel_groups(goal_key: str) -> list[list[str]]:
    goal = GOALS[goal_key]
    graph = nx.DiGraph()
    graph.add_nodes_from(goal["services"])
    graph.add_edges_from(goal["dependencies"])
    depths: dict[str, int] = {}
    for node in nx.topological_sort(graph):
        depths[node] = max((depths[pred] + 1 for pred in graph.predecessors(node)), default=1)
    return [
        sorted(node for node, depth in depths.items() if depth == level)
        for level in sorted(set(depths.values()))
    ]
