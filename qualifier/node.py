from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Node:
    tag: str
    attributes: dict[str, str] = field(default_factory=dict)
    children: list[Node] = field(default_factory=list)
    text: str = ""
