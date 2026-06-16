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
