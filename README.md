# AI Graduate School Preparation

This repository records study materials and practice code for AI graduate school preparation.

Current scope:

- D2L-based PyTorch basics
- Tensor creation, shape handling, indexing, broadcasting, and basic GPU checks
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
├── d2l/                 # D2L-based practice files
├── docs/                # Public repository conventions
├── requirements.txt     # Minimal Python dependency list
└── README.md
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

Next:

- Continue D2L preliminaries

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
