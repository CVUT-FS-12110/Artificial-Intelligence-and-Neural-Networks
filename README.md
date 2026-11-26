# Artificial-Intelligence-and-Neural-Networks
Artificial Intelligence and Neural Networks Labs

### [00 - Python Introduction](00-Python-Introduction%2FPython-Introduction.ipynb)
Basic introduction to the Python Programming Language 
### [01 - AI Introduction](01-AI-Introduction)
Basic introduction to AI, examples of three Machine Learning tasks - 
[Regression](01-AI-Introduction%2FRegression.ipynb), 
[Classification](01-AI-Introduction%2FClassification.ipynb) and
[Clustering](01-AI-Introduction%2FClustering.ipynb).

### [01 - State space search](01-State-space-search)
Uninformed and informed search: [Towers of Hanoi (BFS/DFS)](01-State-space-search%2FTowersOfHanoi.ipynb),
[Dijkstra and A*](01-State-space-search%2FShortest_Path.ipynb), [tic-tac-toe](01-State-space-search%2Ftic-tac-toe.ipynb).

### [02 - TSP, P vs NP and A*](02-TSP-A)
Each notebook comes in an English (`_en`) and a Czech (`_cz`) version; the code is identical, comments and text differ.
Code is commented line by line for readers without a programming background.

1. Travelling salesman problem ([EN](02-TSP-A%2FTravelling_salesman_problem_en.ipynb) / [CZ](02-TSP-A%2FTravelling_salesman_problem_cz.ipynb)) - brute force, extrapolation to the age of the Universe, Held-Karp, heuristics (greedy, MST, Christofides), 2-opt exercise;
2. P vs NP ([EN](02-TSP-A%2FP_vs_NP_en.ipynb) / [CZ](02-TSP-A%2FP_vs_NP_cz.ipynb)) - growth classes overview, easy to verify vs. hard to solve: subset sum, Euler vs Hamilton, shortest vs longest path, 3-colouring exercise;
3. A* search from games to industry ([EN](02-TSP-A%2FA_star_search_en.ipynb) / [CZ](02-TSP-A%2FA_star_search_cz.ipynb)) - tile maps, 8-puzzle, warehouse order picking (A* + TSP), road navigation, diagonal-movement exercise.

### [05 - Machine Learning Introduction](05-ML-Introduction)
Basics of machine learning - data and a short pandas introduction, principles (train/validation/test, underfitting and overfitting), tasks (regression, classification, clustering) and evaluation -
lab notebook ([EN](05-ML-Introduction%2FML_Introduction_EN.ipynb) / [CZ](05-ML-Introduction%2FML_Introduction_CZ.ipynb)) and
in-class independent work with editable experiments ([EN](05-ML-Introduction%2FIndependent_Work_EN.ipynb) / [CZ](05-ML-Introduction%2FIndependent_Work_CZ.ipynb)).

### [06 - Decision Trees](06-Decision-Trees)
Decision and regression trees in a single lab ([EN](06-Decision-Trees%2FDecision_Trees_Single_Lab_EN.ipynb)) - Gini and entropy, choosing and searching splits by hand, a regression tree, a general recursive tree checked against scikit-learn, metrics and manual tuning on real data, cross-validation, grid search and pruning, bagging and gradient boosting by hand, a comparison of ensembles with logistic regression.

### [07 - k-means Introduction](07-Clustering-intro)
Introduction to k-means clustering algorithm - notebook
[tutorial](07-Clustering-intro%2Fk_means.ipynb), 

### [08 - Data Preparation for Machine Learning](08-Data-preprocessing)
Complete preprocessing and classification with local synthetic data,
validation-based selection and a final test. Student notebooks contain
assignments, hints, runnable examples and empty cells for independent work;
worked solutions are kept locally and excluded from version control.

- Main assignment: [CZ](08-Data-preprocessing/data-preprocessing-cz.ipynb) /
  [EN](08-Data-preprocessing/data-preprocessing-en.ipynb).
- Category, group and time-series splitting assignment:
  [CZ](08-Data-preprocessing/data-splitting-cz.ipynb) /
  [EN](08-Data-preprocessing/data-splitting-en.ipynb).

### [09 - The Perceptron and One Neuron](09-Perceptron)
Perceptron rule, linear and logistic neuron, classification and regression metrics.
Each part comes in Czech and English.

- Educational part with interactive visualisations (Jupyter controls): [CZ](09-Perceptron/perceptron-visual-cz.ipynb) /
  [EN](09-Perceptron/perceptron-visual-en.ipynb).
- Practical part with independent tuning and a cost-based threshold: [CZ](09-Perceptron/perceptron-practice-cz.ipynb) /
  [EN](09-Perceptron/perceptron-practice-en.ipynb).
- Worked solution of the practical part: [CZ](09-Perceptron/perceptron-practice-solution-cz.ipynb) /
  [EN](09-Perceptron/perceptron-practice-solution-en.ipynb).

### [10 - Support Vector Machines](10-SVM)
Maximum margin, soft margin and C, kernels and γ, scaling, ε-tube regression and one-class SVM.
Each part comes in Czech and English.

- Educational part with interactive visualisations (Jupyter controls): [CZ](10-SVM/svm-visual-cz.ipynb) /
  [EN](10-SVM/svm-visual-en.ipynb).
- Practical part (pump diagnostics: kernels, tuning C and γ, cost-based threshold, one-class SVM, pump-curve regression): [CZ](10-SVM/svm-practice-cz.ipynb) /
  [EN](10-SVM/svm-practice-en.ipynb).
- Worked solution of the practical part: [CZ](10-SVM/svm-practice-solution-cz.ipynb) /
  [EN](10-SVM/svm-practice-solution-en.ipynb).

See also: [Lecture slides](https://docs.google.com/presentation/d/1mFdYh_nIXf68r9mZ0f5pa6WEtTBiMGAh/edit?usp=sharing&ouid=110257199797152894121&rtpof=true&sd=true)
