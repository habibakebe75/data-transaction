
from typing import Tuple

import pandas as pd


def filter_transactions_valides(df: pd.DataFrame) -> pd.DataFrame:
    """Filtre les transactions pour ne garder que celles qui respectent
    des règles métier simples.

    Règles:
    - montant >= 0
    - client_id non vide
    """
    df = df.copy()
    df = df.dropna(subset=["client_id"])
    df = df[df["montant"] >= 0]
    return df


def rapport_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """Retourne un DataFrame contenant les transactions considérées
    comme anormales (par ex. montant négatif)."""
    anomalies = df[df["montant"] < 0].copy()
    return anomalies
