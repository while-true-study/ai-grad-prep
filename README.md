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
- Dropout regularization covering random activation masking, inverted dropout scaling, training and evaluation modes, and PyTorch implementation
- Kaggle house-price regression covering mixed-type preprocessing, log-target prediction, K-fold cross-validation, ensembling, and submission generation
- PyTorch layers and modules covering custom `nn.Module` classes, `forward`, module composition, shared layers, buffers, and control flow
- PyTorch parameter management covering parameter inspection, gradients, named parameters, optimizers, and parameter sharing
- PyTorch parameter initialization covering default initialization, custom initializers, Xavier initialization, and direct parameter updates
- PyTorch lazy initialization covering deferred shape inference, `nn.LazyLinear`, first-forward initialization, and dummy-input dry runs
- PyTorch custom layers covering parameter-free modules, trainable `nn.Parameter` values, custom forward computation, and autograd integration
- PyTorch file I/O covering tensor serialization, `state_dict`, parameter restoration, evaluation mode, and checkpoint verification
- Convolutional neural network foundations covering spatial structure, translation equivariance, locality, weight sharing, channels, filters, and `nn.Conv2d` parameter shapes
- Image convolution notes covering 2D cross-correlation, output shapes, feature maps, edge detection, learnable kernels, and receptive fields
- Convolution padding and stride notes covering output-size calculations, spatial-size preservation, odd-sized kernels, downsampling, and PyTorch `nn.Conv2d` settings
- Multiple input and output channel notes covering channel-wise cross-correlation, filter banks, convolution weight shapes, feature maps, and 1×1 convolution
- Pooling notes covering max and average pooling, window size, stride, output-size calculations, channel-wise operation, and `nn.MaxPool2d`
- LeNet convolutional neural network implementation covering convolution and average-pooling stages, feature-map shape tracking, flattening, fully connected classification, Fashion-MNIST training, and evaluation
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
| 25 | Aug 15 | 5.6 Dropout | activation masking, inverted dropout, training and evaluation modes, regularization | [Notebook](<d2l/05_Multilayer Perceptrons/05_06_Dropout.ipynb>) |
| 26 | Aug 15 | 5.7 Predicting House Prices on Kaggle | preprocessing, log-price regression, K-fold validation, ensemble prediction | [Notebook](<d2l/05_Multilayer Perceptrons/05_07_Predicting House Prices on Kaggle.ipynb>) · [Data](<d2l/05_Multilayer Perceptrons/data>) · [Submission](<d2l/05_Multilayer Perceptrons/submission.csv>) |

### Chapter 6 — Builders' Guide

| Day | Date | Section | Key topics | Material |
|---:|---|---|---|---|
| 27 | Aug 16–17 | 6.1 Layers and Modules | `nn.Module`, `forward`, custom sequential modules, control flow, buffers, nested modules | [Notebook](<d2l/06_Builders’ Guide/06_01_Layers and Modules.ipynb>) |
| 28 | Aug 17 | 6.2 Parameter Management | parameter access, `state_dict`, gradients, named parameters, optimizers, parameter sharing | [Notebook](<d2l/06_Builders’ Guide/06_02_Parameter Management.ipynb>) |
| 29 | Aug 19 | 6.3 Parameter Initialization | default initialization, custom initializers, Xavier initialization, direct parameter updates | [Notebook](<d2l/06_Builders’ Guide/06_03_Parameter Initialization.ipynb>) |
| 30 | Aug 20 | 6.4 Lazy Initialization | deferred shape inference, `nn.LazyLinear`, first-forward initialization, dummy-input dry runs | [Notebook](<d2l/06_Builders’ Guide/06_04_Lazy Initialization.ipynb>) |
| 31 | Aug 20 | 6.5 Custom Layers | parameter-free modules, trainable parameters, custom forward computation, autograd integration | [Notebook](<d2l/06_Builders’ Guide/06_05_Custom Layers.ipynb>) |
| 32 | Aug 21 | 6.6 File I/O | tensor serialization, `state_dict`, parameter restoration, evaluation mode, checkpoint verification | [Notebook](<d2l/06_Builders’ Guide/06_06_File I,O.ipynb>) |
| 33 | Aug 21 | 6.7 GPUs | CUDA availability, device selection, tensor and model placement, multi-GPU indexing, transfer overhead | [Notebook](<d2l/06_Builders’ Guide/06_07_GPUs.ipynb>) |

### Chapter 7 — Convolutional Neural Networks

| Day | Date | Section | Key topics | Material |
|---:|---|---|---|---|
| 34 | Aug 22–24 | 7.1 From Fully Connected Layers to Convolutions | spatial structure, translation equivariance, locality, weight sharing, channels, filters, `nn.Conv2d` | [Notebook](<d2l/07_Convolutional Neural Networks/07_01_From Fully Connected Layers to Convolutions.ipynb>) |
| 35 | Aug 24 | 7.2 Convolutions for Images | 2D cross-correlation, output shapes, feature maps, edge detection, kernel learning, receptive fields | [Notebook](<d2l/07_Convolutional Neural Networks/07_02_Convolutions for Images.ipynb>) |
| 36 | Aug 25 | 7.3 Padding and Stride | padding, stride, output-size calculations, spatial-size preservation, downsampling, `nn.Conv2d` | [Notebook](<d2l/07_Convolutional Neural Networks/07_03_Padding and Stride.ipynb>) |
| 37 | Aug 26 | 7.4 Multiple Input and Multiple Output Channels | channel-wise cross-correlation, multiple filters, weight shapes, feature maps, 1×1 convolution | [Notebook](<d2l/07_Convolutional Neural Networks/07_04_Multiple Input and Multiple Output Channels.ipynb>) |
| 38 | Aug 26 | 7.5 Pooling | max pooling, average pooling, window size, stride, output-size calculations, channel-wise operation, `nn.MaxPool2d` | [Notebook](<d2l/07_Convolutional Neural Networks/07_05_Pooling.ipynb>) |
| 39 | Aug 26 | 7.6 Convolutional Neural Networks (LeNet) | LeNet architecture, convolutions, average pooling, feature-map shapes, fully connected layers, Fashion-MNIST training and evaluation | [Notebook](<d2l/07_Convolutional Neural Networks/07_06_Convolutional Neural Networks (LeNet).ipynb>) |

Next:

- Continue to D2L 7.7, AlexNet

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
