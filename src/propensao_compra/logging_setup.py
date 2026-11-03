"""Configuração única do logging do projeto, com o nível vindo do LOG_LEVEL do .env."""

import logging

from propensao_compra.settings import LogLevel, get_settings

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def configure_logging(level: LogLevel | None = None) -> None:
    """Configura o logger raiz; sem `level`, usa o LOG_LEVEL do ambiente.

    Deve ser chamada uma vez, no ponto de entrada de cada comando (ex.: estágios do DVC).
    """
    logging.basicConfig(level=level or get_settings().log_level, format=LOG_FORMAT, force=True)
