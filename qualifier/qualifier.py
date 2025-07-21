from __future__ import annotations

from node import Node

def query_selector_all(node: Node, selector: str) -> list[Node]:
    """
    Given a node, the function will return all nodes, including children,
    that match the given selector.
    """