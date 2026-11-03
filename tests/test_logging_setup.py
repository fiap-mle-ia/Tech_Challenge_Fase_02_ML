import logging

import pytest
from pydantic import ValidationError

from propensao_compra.logging_setup import configure_logging
from propensao_compra.settings import Settings, get_settings


@pytest.fixture
def restaura_logger_raiz():
    root = logging.getLogger()
    handlers, level = root.handlers[:], root.level
    get_settings.cache_clear()
    yield root
    root.handlers[:], root.level = handlers, level
    get_settings.cache_clear()


def test_usa_o_log_level_do_ambiente(monkeypatch, restaura_logger_raiz):
    monkeypatch.setenv("LOG_LEVEL", "debug")

    configure_logging()

    assert restaura_logger_raiz.level == logging.DEBUG


def test_nivel_explicito_tem_prioridade(monkeypatch, restaura_logger_raiz):
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    configure_logging("WARNING")

    assert restaura_logger_raiz.level == logging.WARNING


def test_log_level_invalido_e_rejeitado(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "VERBOSO")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)
