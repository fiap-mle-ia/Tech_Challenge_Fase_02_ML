from pathlib import Path

from propensao_compra.settings import PROJECT_ROOT, Settings, load_params


def test_params_tem_seed_e_alvo():
    params = load_params(PROJECT_ROOT / "configs" / "params.yaml")

    assert params["seed"] == 42
    assert params["data"]["target"] == "Revenue"


def test_settings_le_variaveis_de_ambiente(monkeypatch):
    monkeypatch.setenv("MLFLOW_EXPERIMENT_NAME", "experimento-teste")

    settings = Settings(_env_file=None)

    assert settings.mlflow_experiment_name == "experimento-teste"


def test_caminho_relativo_e_resolvido_a_partir_da_raiz():
    settings = Settings(_env_file=None, params_path=Path("configs/params.yaml"))

    assert settings.resolved_params_path() == PROJECT_ROOT / "configs" / "params.yaml"
