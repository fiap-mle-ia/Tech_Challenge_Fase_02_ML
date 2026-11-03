"""Regras de Clean Code do enunciado verificadas automaticamente em todo o src/."""

import ast
from pathlib import Path

import pytest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
MAX_FUNCTION_LINES = 20


def _functions() -> list[tuple[str, ast.FunctionDef | ast.AsyncFunctionDef]]:
    found = []
    for file in sorted(SRC_DIR.rglob("*.py")):
        tree = ast.parse(file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
                found.append((f"{file.relative_to(SRC_DIR)}::{node.name}", node))
    return found


def _body_lines(node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    """Linhas do corpo da função, sem contar a assinatura e a docstring."""
    body = node.body
    if ast.get_docstring(node) is not None:
        body = body[1:]
    if not body:
        return 0
    return body[-1].end_lineno - body[0].lineno + 1


FUNCTIONS = _functions()


@pytest.mark.parametrize(("name", "node"), FUNCTIONS, ids=[name for name, _ in FUNCTIONS])
def test_funcoes_tem_no_maximo_20_linhas(name, node):
    assert _body_lines(node) <= MAX_FUNCTION_LINES, f"{name} passou de {MAX_FUNCTION_LINES} linhas"


@pytest.mark.parametrize(("name", "node"), FUNCTIONS, ids=[name for name, _ in FUNCTIONS])
def test_funcoes_tem_type_hint_de_retorno(name, node):
    assert node.returns is not None, f"{name} não declara o tipo de retorno"
