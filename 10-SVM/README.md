# 10 — Metoda podpůrných vektorů / Support vector machines

## Česky

Cvičení navazuje na přednášku 10 a má dvě části (90 minut):

1. **Edukační část (asi 35 min):** [vizualizace SVM](svm-visual-cz.ipynb).
   Metody z přednášky na malých syntetických datech: perceptron a maximální okraj na příkladu z přednášky, měkký okraj a parametr C,
   ztráta pantu, polynomiální a RBF jádro s parametrem γ, škálování, regrese s ε-trubicí a extrapolace, jednotřídní SVM a parametr ν,
   požehnání a prokletí dimenzionality (Coverova věta, náhodné třídy a polynomiální jádro).
   Kód se nečte ani nemění: je sbalený a každá metoda má nad grafem ovládací prvky Jupyteru. Studenti mění nastavení a odpovídají na úkol.
2. **Praktická část (asi 50 min):** [SVM pro diagnostiku čerpadel](svm-practice-cz.ipynb).
   Provozní záznamy čerpadel: lineární model a jádra → **samostatné ladění C a γ** mřížkou s křížovou validací (včetně rozšíření mřížky)
   → **práh podle ceny chyb** → závěrečný test → jednotřídní SVM bez označených poruch → regrese charakteristiky čerpadla s ε-trubicí
   a extrapolací. Kroky 1–3 jsou připravené, ostatní píšete sami; kroky 8 a 9 jsou rozšiřující.

Notebook praktické části obsahuje zadání, rozbalovací nápovědy a krátké spustitelné ukázky na ilustračních datech s předponou `demo_`.
Vzorové řešení s výstupy a poznámkami: [CZ](svm-practice-solution-cz.ipynb) / [EN](svm-practice-solution-en.ipynb).

Ladí se podle ROC AUC (nezávisí na prahu); práh se pak volí zvlášť podle nákladů 10·FN + 1·FP. Test se otevře až po zmrazení
parametrů i prahu. Předpokládá se znalost `Pipeline` a křížové validace z cvičení 08 a 09.

### Spuštění

Otevřete notebook v Jupyteru (JupyterLab nebo Notebook 7) s prostředím, které obsahuje `numpy`, `pandas`, `matplotlib`,
`scikit-learn` a `ipywidgets` (ovládání edukační části). V edukační části zvolte *Run → Run All Cells*; ovládání funguje jen se spuštěným kernelem.
Data jsou v `data/`; bez místní kopie (např. v Google Colab) praktická část vytvoří stejnou tabulku stejným generátorem, nic se nestahuje.

```bash
python -m pip install jupyter ipywidgets numpy pandas matplotlib "scikit-learn>=1.4"
```

Význam dat popisuje [dokumentace dat](data/README.md). `prepare_data.py` obnoví `data/pumps.csv`.

## English

The lab follows lecture 10 and has two parts (90 minutes):

1. **Educational part (about 35 min):** [SVM visualisation](svm-visual-en.ipynb).
   The lecture methods on small synthetic data: the perceptron and the maximum margin on the lecture example, the soft margin and parameter C,
   the hinge loss, polynomial and RBF kernels with parameter γ, scaling, regression with the ε-tube and extrapolation, the one-class SVM and parameter ν,
   the blessing and curse of dimensionality (Cover's theorem, random classes and a polynomial kernel).
   The code is not read or changed: it is collapsed and every method has Jupyter controls above its plot. Students change the settings and answer a task.
2. **Practical part (about 50 min):** [SVM for pump diagnostics](svm-practice-en.ipynb).
   Operating records of pumps: a linear model and kernels → **independent tuning of C and γ** with a cross-validated grid (including extending the grid)
   → **threshold by the cost of errors** → final test → one-class SVM without labelled faults → regression of the pump curve with the ε-tube
   and extrapolation. Steps 1–3 are prepared; you write the rest; steps 8 and 9 are an extension.

The practical notebook contains assignments, expandable hints and short runnable examples using illustrative data prefixed with `demo_`.
Worked solution with outputs and notes: [CZ](svm-practice-solution-cz.ipynb) / [EN](svm-practice-solution-en.ipynb).

Tuning uses ROC AUC (independent of the threshold); the threshold is then chosen separately by the cost 10·FN + 1·FP. The test set is opened
only after the parameters and the threshold are frozen. `Pipeline` and cross-validation from labs 08 and 09 are assumed.

### Running the notebooks

Open the notebook in Jupyter (JupyterLab or Notebook 7) with `numpy`, `pandas`, `matplotlib`, `scikit-learn` and `ipywidgets` installed.
In the educational part choose *Run → Run All Cells*; the controls work only with a running kernel. The data are in `data/`; without
a local copy (e.g. in Google Colab) the practical part creates the same table with the same generator, nothing is downloaded.

See the [data description](data/README.md). `prepare_data.py` reproduces `data/pumps.csv`.

## Reference documentation / Dokumentace

- [Support vector machines](https://scikit-learn.org/stable/modules/svm.html)
- [Novelty and outlier detection (one-class SVM)](https://scikit-learn.org/stable/modules/outlier_detection.html)
- [Tuning the hyper-parameters (grid search)](https://scikit-learn.org/stable/modules/grid_search.html)
