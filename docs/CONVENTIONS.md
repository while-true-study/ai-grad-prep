# Repository Conventions

## Repository Purpose

This repository records AI graduate school preparation work. The current focus starts with D2L-based PyTorch basics and small reproducible learning exercises.

## Public-Safe Files

- Public study notes and learning summaries.
- Source code, notebooks, and scripts without secrets or personal data.
- Small examples that are public, redistributable, and documented.
- Configuration examples such as `.env.example`.
- Repository documentation such as this file.

## Local-Only Files

- Local notes and private planning documents under `docs/private/` or `docs/local/`.
- `.env`, `.env.*`, API keys, tokens, credentials, passwords, and private keys.
- Personal contact information, account IDs, addresses, or private profile data.
- Local experiments, scratch files, and temporary outputs under `local/`, `private/`, `secrets/`, `tmp/`, or `temp/`.
- Personal application strategy documents, lab-specific private notes, or unpublished planning notes.

## Notebook Rules

- Keep notebooks reproducible from top to bottom.
- Clear unnecessary outputs before committing, especially errors, absolute paths, environment dumps, or large printed tensors.
- Do not store credentials, tokens, private file paths, or personal data in notebook cells or outputs.
- Prefer short markdown notes that explain the goal, source material, and result of each exercise.
- If a notebook depends on local data, document the expected local path pattern without committing the data.

## Data and Model Artifact Rules

- Keep raw/private datasets under `data/raw/` or `data/private/`; do not commit them.
- Commit only small public sample data when redistribution is allowed and the source is documented.
- Do not commit large model files, checkpoints, or exports such as `*.pt`, `*.pth`, `*.ckpt`, and `*.onnx`.
- Store generated private outputs under `outputs/private/`, `tmp/`, or `temp/`.

## Commit Message Rules

Use Conventional Commits:

- `chore: initialize repository conventions`
- `docs: add study roadmap`
- `feat(d2l): add tensor basics practice`
- `refactor: organize training scripts`
- `fix: correct cuda check snippet`

Use a scope when it helps identify the study area or package, for example `feat(d2l): ...`.

## Branch Rules

- Keep `main` stable and safe for public push.
- Use short feature branches for study units or cleanup work, for example `study/d2l-tensors`.
- Do not force-push shared branches.
- Rebase or merge only after checking staged files and sensitive content.

## Pre-Push Checklist

- Run `git status --short`.
- Review staged changes with `git diff --cached`.
- Search for sensitive content:
  `rg -n "api[_-]?key|secret|token|password|passwd|authorization|bearer|client_secret|private_key|AKIA|BEGIN RSA|BEGIN OPENSSH|010-" .`
- Check notebooks for unnecessary outputs, absolute paths, credentials, or private data.
- Confirm `.gitignore` excludes local environments, private data, temporary outputs, local/private docs, and model artifacts.
- Do not commit raw/private data, credentials, personal contact information, or large checkpoint files.
