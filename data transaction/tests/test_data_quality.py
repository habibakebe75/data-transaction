
import pandas as pd

from src.data_quality import filter_transactions_valides, rapport_anomalies


def test_filter_transactions_valides():
    df = pd.DataFrame(
        {
            "client_id": ["CL001", "CL002", None],
            "montant": [10.0, -5.0, 20.0],
        }
    )

    df_valides = filter_transactions_valides(df)

    # On ne garde que la première ligne: client_id non nul et montant >= 0
    assert len(df_valides) == 1
    assert df_valides.iloc[0]["client_id"] == "CL001"
    assert df_valides.iloc[0]["montant"] == 10.0


def test_rapport_anomalies():
    df = pd.DataFrame(
        {
            "client_id": ["CL001", "CL002", "CL003"],
            "montant": [10.0, -5.0, -1.0],
        }
    )

    anomalies = rapport_anomalies(df)

    # On doit trouver deux anomalies (montants négatifs)
    assert len(anomalies) == 2
    assert set(anomalies["client_id"]) == {"CL002", "CL003"}
