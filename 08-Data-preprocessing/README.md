# 08 — Příprava dat pro strojové učení / Data preparation for machine learning

## Česky

Cvičení navazuje na přednášku 08. Sestavte celý řetězec pro klasifikaci
syntetických provozních záznamů: kontrola kvality → dělení dat → doplnění hodnot
→ škálování a kódování → model → výběr podle validace → závěrečný test → nová data.

- [Zadání hlavního cvičení](data-preprocessing-cz.ipynb)
- [Zadání rozšíření: dělení dat](data-splitting-cz.ipynb)

Studentské notebooky obsahují zadání, rozbalovací nápovědy a krátké
spustitelné ukázky na ilustračních datech. Vlastní řešení pište do připravených
prázdných kódových buněk. Ukázky používají proměnné s předponou `demo_`
a spouštějí se v pořadí. Notebooky s řešením se uchovávají lokálně a nejsou verzované.

Předpokládá se práce s proměnnými, seznamy, jednoduchým výběrem sloupců,
`fit`, `predict` a rozdělením na trénovací, validační a testovací data.
V hlavním cvičení porovnáte škálování a variantu bez škálování; volitelně
přidáte PCA před výběrem modelu. V rozšíření vyberte jednu úlohu: stratifikaci
kategorií a intervalů, oddělení celých zařízení nebo chronologickou validaci.

Pevně známá oprava zápisu a odstranění přesných duplicit předchází dělení.
Mediány, škály, kategorie i komponenty se odhadují z trénovacích dat uvnitř
řetězce. Varianty se vybírají podle validace. Test se otevře po uzavření
volby; nová data používají stejný naučený řetězec.

### Spuštění

Otevřete notebook v Jupyteru s prostředím, které obsahuje `numpy`, `pandas`,
`matplotlib` a `scikit-learn`. Pracovní adresář je složka tohoto cvičení;
při spuštění z kořene repozitáře začínají relativní cesty k datům složkou
`08-Data-preprocessing/`. Notebooky řešení podporují oba pracovní adresáře.
Data jsou v `data/` a při výpočtu se nic nestahuje. Po dokončení vlastního
řešení restartujte kernel a spusťte všechny buňky v pořadí.

Případnou instalaci proveďte v používaném prostředí:

```bash
python -m pip install jupyter numpy pandas matplotlib "scikit-learn>=1.2"
```

Význam dat a známé vady popisuje [dokumentace dat](data/README.md).
`prepare_data.py` obnoví vstupní CSV; při běžném řešení se nespouští.
Původní [demonstrační notebook](data_preprocessing.ipynb) je starší materiál.

## English

The lab follows lecture 08. Build a complete classification workflow
on synthetic operating records: quality checks → data split → imputation →
scaling and encoding → model → validation-based selection → final test → new data.

- [Main assignment](data-preprocessing-en.ipynb)
- [Data-splitting assignment](data-splitting-en.ipynb)

Student notebooks contain assignments, expandable hints and short runnable
examples using illustrative data. Write your solution in the empty code cells
provided. Examples use variables prefixed with `demo_` and run in order.
Solution notebooks are kept locally and excluded from version control.

Prerequisites are variables, lists, simple column selection, `fit`, `predict`,
and training/validation/test data. The main task compares scaling with an
unscaled variant; optional PCA is evaluated before model selection. Choose
one extension task: category/bin stratification, whole-device separation,
or chronological validation.

Fixed spelling corrections and exact duplicate removal precede splitting.
Imputation statistics, scales, categories and components are learned from
training data within the pipeline. Validation chooses the configuration.
The test set is opened after selection is frozen; new data use the same
fitted pipeline.

### Running the notebooks

Open the notebook in Jupyter with `numpy`, `pandas`, `matplotlib` and
`scikit-learn` installed. Use the lab folder as the working directory;
from the repository root, prefix relative data paths with
`08-Data-preprocessing/`. Solution notebooks support both directories.
All datasets are local. Once your solution is complete, restart the kernel
and run all cells in order. The installation command above is sufficient
for this lab.

See the [data description](data/README.md) for provenance and known defects.
`prepare_data.py` reproduces the input CSV files and is not run during normal
work on the assignments. The [original demonstration](data_preprocessing.ipynb)
is retained as older material.

## Reference documentation / Dokumentace

- [Pipelines and column transformations](https://scikit-learn.org/stable/modules/compose.html)
- [One-hot encoding and unknown categories](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
- [Data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)
- [Group and temporal cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
