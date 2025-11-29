
# Data Transactions Pipeline – Projet Démo

Ce projet est un **exemple simple de pipeline de données** que tu peux utiliser dans ton portfolio pour postuler à une **POEI Data / Cloud / IA**.

L’objectif est de montrer que tu comprends :
- la manipulation de données avec Python,
- la notion de pipeline (chargement → nettoyage → transformation → export),
- la qualité des données (tests simples, cohérence métier).

## 🧩 Contexte

On se place dans un **contexte bancaire** (proche de ton expérience QA) :

Chaque jour, un fichier CSV de transactions est généré avec les colonnes suivantes :
- `transaction_id`
- `client_id`
- `date`
- `montant`

Le pipeline :
1. charge les transactions brutes ;
2. nettoie les données (valeurs manquantes, types, montants négatifs) ;
3. calcule le **montant total par client** ;
4. sauvegarde le résultat dans un nouveau fichier CSV ;
5. effectue quelques **contrôles de qualité** de données.

## 🏗️ Structure du projet

```text
data-transactions-pipeline/
├── README.md
├── requirements.txt
├── data/
│   └── transactions_sample.csv
├── src/
│   ├── __init__.py
│   ├── pipeline.py
│   └── data_quality.py
└── tests/
    └── test_data_quality.py
```

## ▶️ Comment exécuter le projet

1. Crée un environnement virtuel (optionnel mais recommandé) :

```bash
python -m venv .venv
source .venv/bin/activate  # sous Windows : .venv\Scripts\activate
```

2. Installe les dépendances :

```bash
pip install -r requirements.txt
```

3. Lance le pipeline :

```bash
python -m src.pipeline
```

Un fichier `data/totaux_clients.csv` sera généré.

## ✅ Lancer les tests

Les tests vérifient quelques règles simples de qualité des données.

```bash
pytest
```

## 🧾 Ce que tu peux écrire sur ton CV

> **Projet perso – Pipeline de transactions bancaires (Python / Data)**
>
> - Chargement et nettoyage de données de transactions (CSV)
> - Détection de valeurs incohérentes (montants négatifs, valeurs manquantes)
> - Agrégation des montants par client et export des résultats
> - Mise en place de tests automatisés de qualité de données (pytest)

Tu peux mettre ce projet sur GitHub et ajouter le lien dans ton CV et sur ton profil LinkedIn.
