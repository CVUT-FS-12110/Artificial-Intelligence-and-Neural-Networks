# 09 — Perceptron a jeden neuron / The perceptron and one neuron

## Česky

Cvičení navazuje na přednášku 09 a má dvě části (90 minut):

1. **Edukační část (asi 35 min):** [vizualizace perceptronu](perceptron-visual-cz.ipynb).
   Metody z přednášky na malých syntetických datech: perceptronové pravidlo na příkladu z přednášky,
   konvergence a mez (R/γ)², neoddělitelná data a kapsový algoritmus, škálování vstupů,
   gradientní sestup a rychlost učení, logistický neuron a logaritmická ztráta, matice záměn a práh,
   ROC, přesnost–úplnost a cena chyb, metriky regrese a XOR. Kód se nečte ani nemění: je sbalený
   a každá metoda má nad grafem ovládací prvky Jupyteru (posuvníky, nabídky, zaškrtávací pole).
   Studenti mění nastavení a odpovídají na úkol.
2. **Praktická část (asi 50 min):** [od perceptronu k vyladěnému klasifikátoru](perceptron-practice-cz.ipynb).
   Klasifikace vadných výlisků: referenční model → perceptron → logistický neuron, křivky ROC a PR →
   **samostatné ladění** (ruční varianty na validaci, mřížka s křížovou validací přes škálování, součinové
   příznaky, ztrátu, rychlost učení a regularizaci) → **práh podle ceny chyb** → závěrečný test.
   Kroky 1–3 jsou připravené, ostatní píšete sami.

Notebook praktické části obsahuje zadání, rozbalovací nápovědy a krátké spustitelné ukázky na ilustračních
datech s předponou `demo_`. Vlastní řešení pište do připravených prázdných kódových buněk.
Vzorové řešení s výstupy a poznámkami: [CZ](perceptron-practice-solution-cz.ipynb) / [EN](perceptron-practice-solution-en.ipynb).

Předpokládá se znalost `Pipeline`, `fit`, `predict` a rozdělení na trénovací, validační a testovací data
z cvičení 08. Ladí se podle ROC AUC (nezávisí na prahu); práh se pak volí zvlášť podle ceny
C = 10·FN + 1·FP. Test se otevře až po zmrazení parametrů i prahu.

### Spuštění

Otevřete notebook v Jupyteru (JupyterLab nebo Notebook 7) s prostředím, které obsahuje `numpy`, `pandas`, `scipy`,
`matplotlib`, `scikit-learn` a `ipywidgets` (ovládání edukační části).
V edukační části zvolte *Run → Run All Cells*; ovládání funguje jen se spuštěným kernelem. Pracovní adresář je složka tohoto cvičení; praktická část
funguje i z kořene repozitáře. Data jsou v `data/`; bez místní kopie (např. v Google Colab) je praktická část stáhne z GitHubu repozitáře. Edukační část
data ze složky nepotřebuje. Po dokončení vlastního řešení restartujte kernel a spusťte všechny buňky v pořadí.

```bash
python -m pip install jupyter ipywidgets numpy pandas scipy matplotlib "scikit-learn>=1.4"
```

Význam dat popisuje [dokumentace dat](data/README.md). `prepare_data.py` obnoví `data/parts.csv`;
při běžném řešení se nespouští.

## English

The lab follows lecture 09 and has two parts (90 minutes):

1. **Educational part (about 35 min):** [perceptron visualisation](perceptron-visual-en.ipynb).
   The lecture methods on small synthetic data: the perceptron rule on the lecture example,
   convergence and the bound (R/γ)², non-separable data and the pocket algorithm, input scaling,
   gradient descent and the learning rate, the logistic neuron and log loss, the confusion matrix and the threshold,
   ROC, precision–recall and the cost of errors, regression metrics and XOR. The code is not read or changed: it is collapsed,
   and every method has Jupyter controls (sliders, menus, check boxes) above its plot.
   Students change the settings and answer a task.
2. **Practical part (about 50 min):** [from the perceptron to a tuned classifier](perceptron-practice-en.ipynb).
   Classification of defective moulded parts: reference model → perceptron → logistic neuron, ROC and PR curves →
   **independent tuning** (manual variants on validation, a grid with cross-validation over scaling, product
   features, loss, learning rate and regularisation) → **threshold by the cost of errors** → final test.
   Steps 1–3 are prepared; you write the rest.

The practical notebook contains assignments, expandable hints and short runnable examples using illustrative
data prefixed with `demo_`. Write your solution in the empty code cells provided.
Worked solution with outputs and notes: [CZ](perceptron-practice-solution-cz.ipynb) / [EN](perceptron-practice-solution-en.ipynb).

Prerequisites are `Pipeline`, `fit`, `predict` and training/validation/test data from lab 08.
Tuning uses ROC AUC (independent of the threshold); the threshold is then chosen separately by the cost
C = 10·FN + 1·FP. The test set is opened only after both the parameters and the threshold are frozen.

### Running the notebooks

Open the notebook in Jupyter (JupyterLab or Notebook 7) with `numpy`, `pandas`, `scipy`, `matplotlib`,
`scikit-learn` and `ipywidgets` (controls of the educational part) installed.
In the educational part choose *Run → Run All Cells*; the controls work only with a running kernel. Use the lab folder as the working directory; the practical part
also works from the repository root. The data are in `data/`; without a local copy (e.g. in Google Colab) the practical part downloads them from the repository on GitHub. The educational part
needs no files from the folder. Once your solution is complete, restart the kernel and run all cells in order.
The installation command above is sufficient for this lab.

See the [data description](data/README.md). `prepare_data.py` reproduces `data/parts.csv`
and is not run during normal work on the assignments.

## Reference documentation / Dokumentace

- [Perceptron](https://scikit-learn.org/stable/modules/linear_model.html#perceptron)
- [Stochastic gradient descent (SGDClassifier, SGDRegressor)](https://scikit-learn.org/stable/modules/sgd.html)
- [Classification metrics, ROC and precision–recall](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
- [Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html)
- [Regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)
