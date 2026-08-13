# AI Graduate School Preparation

This repository records study materials and practice code for AI graduate school preparation.

Current scope:

- D2L-based PyTorch basics
- Tensor creation, shape handling, indexing, broadcasting, and basic GPU checks
- Synthetic regression data generation and minibatch loading with PyTorch
- Linear regression training loops implemented from scratch
- Concise linear regression implementation with `nn.Linear`, `nn.MSELoss`, and `torch.optim.SGD`
- Generalization concepts including training error, validation/generalization error, IID assumptions, model complexity, underfitting, overfitting, dataset size effects, model selection, and cross-validation
- Weight decay and L2 regularization notes for controlling model complexity
- Softmax regression notes covering multiclass outputs, logits, softmax probabilities, cross-entropy loss, gradients, and PyTorch tensor shapes
- Fashion-MNIST preprocessing, visualization, and minibatch loading with torchvision
- Base classification model notes covering class prediction, accuracy, validation evaluation, and optimizer setup
- Softmax regression from-scratch implementation covering stable softmax, manual parameters, cross-entropy loss, accuracy, SGD, training and evaluation loops, learning curves, and Fashion-MNIST predictions
- Concise softmax regression implementation with `nn.Flatten`, `nn.Linear`, `nn.CrossEntropyLoss`, `torch.optim.SGD`, training and evaluation loops, learning curves, and Fashion-MNIST predictions
- Classification generalization, test-set uncertainty, model complexity, and statistical learning theory
- Distribution shift, risk correction, deployment environments, fairness, and feedback loops
- Multilayer perceptron concepts covering hidden layers, activation functions, and universal approximation
- Fashion-MNIST MLP implementations from scratch and with `nn.Sequential`
- Forward propagation, backpropagation, computational graphs, the chain rule, and intermediate-value storage
- Numerical stability, vanishing and exploding gradients, symmetry, and Xavier initialization
- Deep learning generalization, generalization gaps, overparameterization, double descent, inductive bias, early stopping, and regularization
- Small reproducible exercises suitable for a public repository

## Environment

- Python 3.11
- PyTorch with CUDA support when available

Install dependencies:

```powershell
pip install -r requirements.txt
```

For CUDA-enabled PyTorch installs, use the command recommended by the official PyTorch selector for the local CUDA version.

## Folder Structure

```text
.
|-- d2l/                 # D2L-based practice files
|-- docs/                # Public repository conventions
|-- requirements.txt     # Minimal Python dependency list
`-- README.md
```

## Study Log Format

Each study file should make the learning target clear:

- Topic and source section, for example `D2L 2.3 Tensor Basics`
- Short runnable code examples
- Notes on environment assumptions such as CPU/CUDA availability
- Outputs only when they are small, useful, and safe to publish

## Study Log

### Chapter 2 — Preliminaries

| Day | Date | Section | Key topics | Material |
|---:|---|---|---|---|
| 01 | Jun 16–17 | 2.1 Data Manipulation | tensors, indexing, broadcasting | [Notebook](d2l/02_preliminaries/02_01_data_manipulation.ipynb) |
| 02 | Jun 17 | 2.2 Data Preprocessing | missing values, one-hot encoding, tensor conversion | [Notebook](<d2l/02_preliminaries/02_02_Data Preprocessing.ipynb>) · [Data](d2l/data/house_tiny.csv) |
| 02 | Jun 17 | 2.3 Linear Algebra | reductions, matrix products, norms | [Notebook](d2l/02_preliminaries/02_03_linear_algebra.ipynb) |
| 03 | Jun 17–18 | 2.4 Calculus | derivatives, chain rule, gradient descent | [Notebook](d2l/02_preliminaries/02_04_Calculus.ipynb) |
| 04 | Jun 18–19 | 2.5 Automatic Differentiation | autograd, gradients, computation graphs | [Notebook](<d2l/02_preliminaries/02_05_Automatic Differentiation.ipynb>) |
| 05 | Jun 19–20 | 2.6 Probability and Statistics | distributions, Bayes, expectation, uncertainty | [Notebook](<d2l/02_preliminaries/02_06_Probability and Statistics.ipynb>) |

### Chapter 3 — Linear Neural Networks for Regression

| Day | Date | Section | Key topics | Material |
|---:|---|---|---|---|
| 06 | Jun 23 | 3.1 Linear Regression | study scaffold and implementation plan | [Notebook](<d2l/03_linear_ne/03_01_Linear Regression.ipynb>) |
| 07 | Jun 28 | 3.2 Object-Oriented Design | modules, data modules, trainer structure | [Notebook](<d2l/03_linear_ne/03_02_Object-Oriented Design for Implementation.ipynb>) |
| 08 | Jul 2 | 3.3 Synthetic Regression Data | synthetic data, minibatches, `DataLoader` | [Notebook](<d2l/03_linear_ne/03_03_Synthetic Regression Data.ipynb>) |
| 09 | Jul 3 | 3.4 Linear Regression from Scratch | parameters, squared loss, manual SGD | [Notebook](<d2l/03_linear_ne/03_04_Linear Regression Implementation from Scratch.ipynb>) |
| 10 | Jul 4 | 3.5 Concise Linear Regression | `nn.Linear`, MSE loss, optimizer | [Notebook](<d2l/03_linear_ne/03_05_Concise Implementation of Linear Regression.ipynb>) |
| 11 | Jul 5–6 | 3.6 Generalization | overfitting, model selection, cross-validation | [Notebook](d2l/03_linear_ne/03_06_Generalization.ipynb) |
| 12 | Jul 7–8 | 3.7 Weight Decay | L2 regularization, model complexity | [Notebook](<d2l/03_linear_ne/03_07_Weight Decay.ipynb>) |

### Chapter 4 — Linear Neural Networks for Classification

| Day | Date | Section | Key topics | Material |
|---:|---|---|---|---|
| 13 | Jul 12–22 | 4.1 Softmax Regression | logits, softmax, cross-entropy | [Notebook](<d2l/04_linear_neural_networks_for_classification/04_01_Softmax Regression.ipynb>) |
| 14 | Jul 22–24 | 4.2 Image Classification Dataset | Fashion-MNIST, preprocessing, minibatches | [Notebook](<d2l/04_linear_neural_networks_for_classification/04_02_The Image Classification Dataset.ipynb>) |
| 15 | Jul 25 | 4.3 Base Classification Model | prediction, accuracy, validation | [Notebook](<d2l/04_linear_neural_networks_for_classification/04_03_The Base Classification Model.ipynb>) |
| 16 | Jul 27–28 | 4.4 Softmax Regression from Scratch | stable softmax, manual SGD, evaluation | [Notebook](<d2l/04_linear_neural_networks_for_classification/04_04_Softmax Regression Implementation from Scratch.ipynb>) |
| 17 | Jul 28–29 | 4.5 Concise Softmax Regression | PyTorch layers, training loop, predictions | [Notebook](<d2l/04_linear_neural_networks_for_classification/04_05_Concise Implementation of Softmax Regression.ipynb>) |
| 18 | Jul 29 | 4.6 Generalization in Classification | test uncertainty, model complexity, VC dimension | [Notebook](<d2l/04_linear_neural_networks_for_classification/04_06_Generalization in Classification.ipynb>) |
| 19 | Jul 30 | 4.7 Environment and Distribution Shift | shift types, risk correction, feedback loops | [Notebook](<d2l/04_linear_neural_networks_for_classification/04_07_Environment and Distribution Shift.ipynb>) |

### Chapter 5 — Multilayer Perceptrons

| Day | Date | Section | Key topics | Material |
|---:|---|---|---|---|
| 20 | Aug 1–7 | 5.1 Multilayer Perceptrons | hidden layers, activation functions, universal approximation | [Notebook](<d2l/05_Multilayer Perceptrons/05_01_Multilayer Perceptrons.ipynb>) |
| 21 | Aug 8–11 | 5.2 Implementation of Multilayer Perceptrons | manual parameters, ReLU, training loop, `nn.Sequential` | [Notebook](<d2l/05_Multilayer Perceptrons/05_02_Implementation of Multilayer Perceptrons.ipynb>) |
| 22 | Aug 11 | 5.3 Forward Propagation, Backward Propagation, and Computational Graphs | forward propagation, backpropagation, computational graphs, chain rule | [Notebook](<d2l/05_Multilayer Perceptrons/05_03_Forward Propagation, Backward Propagation, and Computational Graphs.ipynb>) |
| 23 | Aug 12–13 | 5.4 Numerical Stability and Initialization | vanishing gradients, exploding gradients, symmetry, Xavier initialization | [Notebook](<d2l/05_Multilayer Perceptrons/05_04_Numerical Stability and Initialization.ipynb>) |
| 24 | Aug 13 | 5.5 Generalization in Deep Learning | generalization gap, overparameterization, double descent, inductive bias, early stopping | [Notebook](<d2l/05_Multilayer Perceptrons/05_05_Generalization in Deep Learning.ipynb>) |

Next:

- Start D2L 5.6 Dropout

## Public Repository Safety

Do not commit credentials, API keys, tokens, private datasets, personal contact information, local-only paths, large checkpoints, or raw experiment outputs.

Repository rules are documented in [docs/CONVENTIONS.md](docs/CONVENTIONS.md). Keep private or local-only materials out of Git-tracked files.

Before pushing:

- Run `git status --short`.
- Review staged changes with `git diff --cached`.
- Search for sensitive content with `rg`.
- Clear unnecessary notebook outputs before committing.
- Keep local notes and private documentation outside Git-tracked files.

Commit messages follow Conventional Commits, for example:

- `chore: initialize repository conventions`
- `docs: add study roadmap`
- `feat(d2l): add tensor basics practice`
- `refactor: organize training scripts`
- `fix: correct cuda check snippet`
