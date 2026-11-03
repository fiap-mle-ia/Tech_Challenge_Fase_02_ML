"""Configurações vindas do ambiente (.env) e dos parâmetros do pipeline (YAML)."""

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """Variáveis de ambiente do projeto, com os mesmos nomes do `.env.example`."""

    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env", extra="ignore")

    mlflow_tracking_uri: str = "sqlite:///mlflow.db"
    mlflow_experiment_name: str = "propensao-compra"
    mlflow_registered_model_name: str = "propensao-compra-classificador"
    mlflow_champion_alias: str = "champion"
    params_path: Path = Path("configs/params.yaml")
    log_level: str = "INFO"

    def resolved_params_path(self) -> Path:
        """Caminho absoluto do arquivo de parâmetros, relativo à raiz do repositório."""
        if self.params_path.is_absolute():
            return self.params_path
        return PROJECT_ROOT / self.params_path


@lru_cache
def get_settings() -> Settings:
    """Lê o ambiente uma única vez e reaproveita o resultado."""
    return Settings()


def load_params(path: Path | None = None) -> dict[str, Any]:
    """Carrega o YAML de parâmetros (seeds, split, hiperparâmetros)."""
    params_file = path or get_settings().resolved_params_path()
    with params_file.open(encoding="utf-8") as file:
        return yaml.safe_load(file)
