from dataclasses import dataclass


@dataclass
class Node:
    start: any
    end: any


@dataclass
class NumberNode:
    value: any


@dataclass
class OperationNode:
    left: any
    op: any
    right: any
