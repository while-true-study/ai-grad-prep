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

| Day | Date | Topic | Output |
|---:|---|---|---|
| Day 01 | 2026-06-16 ~ 2026-06-17 | D2L 2.1 Data Manipulation | `d2l/02_preliminaries/02_01_data_manipulation.ipynb` |
| Day 02 | 2026-06-17 | D2L 2.2 Data Preprocessing: CSV sample creation, pandas DataFrame inspection, input/target split, missing value checks, numeric imputation, one-hot encoding, and DataFrame/Series to PyTorch Tensor conversion | `d2l/02_preliminaries/02_02_Data Preprocessing.ipynb`, `d2l/data/house_tiny.csv` |
| Day 02 | 2026-06-17 | D2L 2.3 Linear Algebra: scalars, vectors, matrices, tensors, shape/ndim/numel checks, elementwise operations, reductions by dimension, dot product, matrix-vector product, matrix-matrix product, L1/L2 norms, and Frobenius norm | `d2l/02_preliminaries/02_03_linear_algebra.ipynb` |
| Day 03 | 2026-06-17 ~ 2026-06-18 | D2L 2.4 Calculus: numerical differentiation and PyTorch autograd comparison, gradient/partial derivative/chain rule summary, a simple linear-model gradient descent update flow, and three PyTorch-style exercises with a link to the original D2L exercises | `d2l/02_preliminaries/02_04_Calculus.ipynb` |
| Day 04 | 2026-06-18 ~ 2026-06-19 | D2L 2.5 Automatic Differentiation: PyTorch autograd flow, `requires_grad`, `backward()`, `.grad`, gradient accumulation and `zero_grad()`, scalar vs vector outputs, why `y.sum().backward()` is used, `detach()`, chain rule and computation graph, `loss.backward()` vs `optimizer.step()`, and the roles of `w`, `b`, `learning_rate`, and `gradient` in parameter updates | `d2l/02_preliminaries/02_05_Automatic Differentiation.ipynb` |
| Day 05 | 2026-06-19 ~ 2026-06-20 | D2L 2.6 Probability and Statistics: probability vs statistics, coin-toss simulation, multinomial sampling, law of large numbers, sample space/event/random variable, joint and conditional probability, Bayes theorem and base rate, independence and conditional independence, expectation, variance, covariance, and aleatoric vs epistemic uncertainty | `d2l/02_preliminaries/02_06_Probability and Statistics.ipynb` |
| Day 06 | 2026-06-23 | D2L 3.1 Linear Regression: notebook scaffold with study goals, environment setup, and implementation checklist for synthetic data generation, minibatch loading, training loop, and parameter comparison | `d2l/03_linear_ne/03_01_Linear Regression.ipynb` |
| Day 07 | 2026-06-28 | D2L 3.2 Object-Oriented Design for Implementation: object-oriented training structure, D2L utility helpers, `Module`, `DataModule`, `Trainer`, `training_step`, `configure_optimizers`, dataloader flow, and the separation of data, model, loss, optimizer, and training loop responsibilities | `d2l/03_linear_ne/03_02_Object-Oriented Design for Implementation.ipynb` |
| Day 08 | 2026-07-02 | D2L 3.3 Synthetic Regression Data: synthetic feature and label generation with `y = Xw + b + noise`, train/validation split, why `w.reshape(-1, 1)` is used, manual minibatch sampling, `TensorDataset`, `DataLoader`, and batch shape checks | `d2l/03_linear_ne/03_03_Synthetic Regression Data.ipynb` |
| Day 09 | 2026-07-03 | D2L 3.4 Linear Regression Implementation from Scratch: manual parameter initialization, linear model definition, squared loss, SGD updates with `torch.no_grad()`, gradient reset, epoch training loop, validation loss checks, and learned-parameter comparison against `true_w` and `true_b` | `d2l/03_linear_ne/03_04_Linear Regression Implementation from Scratch.ipynb` |
| Day 10 | 2026-07-04 | D2L 3.5 Concise Implementation of Linear Regression: replacing manual `w`, `b`, squared loss, and SGD updates with `nn.Linear`, `nn.MSELoss`, `torch.optim.SGD`, and `DataLoader` while preserving the train loop flow of prediction, loss calculation, backpropagation, and parameter updates | `d2l/03_linear_ne/03_05_Concise Implementation of Linear Regression.ipynb` |
| Day 11 | 2026-07-05 ~ 2026-07-06 | D2L 3.6 Generalization: training error vs generalization error, validation-set estimation, IID assumptions, model complexity, underfitting and overfitting, polynomial feature construction, closed-form least-squares fitting with `torch.linalg.lstsq`, dataset-size effects, model selection, train/validation/test split roles, and simple K-fold cross-validation | `d2l/03_linear_ne/03_06_Generalization.ipynb` |
| Day 12 | 2026-07-07 ~ 2026-07-08 | D2L 3.7 Weight Decay: overfitting from high-dimensional features with limited data, weight size and model complexity, L2 penalty formulation, regularization strength `lambda`, direct weight decay implementation, train/validation loss comparison, and concise PyTorch usage with optimizer `weight_decay` | `d2l/03_linear_ne/03_07_Weight Decay.ipynb` |

Next:

- Start the next D2L section after 3.7 Weight Decay

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
