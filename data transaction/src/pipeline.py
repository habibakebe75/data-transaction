
import os
from pathlib import Path

import pandas as pd

from .data_quality import (
    filter_transactions_valides,
    rapport_anomalies,
)


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def charger_transactions(path: Path) -> pd.DataFrame:
    """Charge le fichier CSV de transactions dans un DataFrame pandas."""
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable: {path}")
    df = pd.read_csv(path)
    return df


def nettoyer_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie les données de transactions.

    - supprime les lignes sans client_id
    - convertit la colonne 'montant' en float
    - supprime les lignes où le montant est manquant
    """
    df = df.copy()

    # supprimer les lignes sans client_id
    df = df.dropna(subset=["client_id"])

    # convertir le montant en numérique
    df["montant"] = pd.to_numeric(df["montant"], errors="coerce")

    # supprimer les montants manquants
    df = df.dropna(subset=["montant"])

    return df


def calculer_totaux_par_client(df: pd.DataFrame) -> pd.DataFrame:
    """Calcule le montant total par client."""
    df_grouped = (
        df.groupby("client_id", as_index=False)["montant"].sum()
        .rename(columns={"montant": "total_montant"})
    )
    return df_grouped


def sauvegarder_totaux(df_totaux: pd.DataFrame, path_sortie: Path) -> None:
    """Sauvegarde le DataFrame des totaux clients dans un fichier CSV."""
    path_sortie.parent.mkdir(parents=True, exist_ok=True)
    df_totaux.to_csv(path_sortie, index=False)


def run_pipeline() -> None:
    """Exécute le pipeline de bout en bout."""
    chemin_entree = DATA_DIR / "transactions_sample.csv"
    chemin_sortie = DATA_DIR / "totaux_clients.csv"

    print(f"Chargement des données depuis: {chemin_entree}")
    df_brut = charger_transactions(chemin_entree)

    print("Nettoyage des données...")
    df_nettoye = nettoyer_transactions(df_brut)

    print("Contrôles de qualité des données...")
    df_valides = filter_transactions_valides(df_nettoye)
    anomalies = rapport_anomalies(df_nettoye)

    print("Calcul des totaux par client...")
    df_totaux = calculer_totaux_par_client(df_valides)

    print(f"Sauvegarde des résultats dans: {chemin_sortie}")
    sauvegarder_totaux(df_totaux, chemin_sortie)

    print("\nRésumé du pipeline:")
    print(f"- Transactions brutes: {len(df_brut)}")
    print(f"- Transactions nettoyées: {len(df_nettoye)}")
    print(f"- Transactions valides (après règles métier): {len(df_valides)}")
    print(f"- Nombre d'anomalies détectées: {len(anomalies)}")


if __name__ == "__main__":
    run_pipeline()
