import torch

print("torch version:", torch.__version__)
print("cuda version:", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())

device = "cuda" if torch.cuda.is_available() else "cpu"
print("device:", device)

if torch.cuda.is_available():
    print("gpu:", torch.cuda.get_device_name(0))

print("\n--- arange ---")
x = torch.arange(12)
print(x)
print("shape:", x.shape)
print("numel:", x.numel())

print("\n--- reshape ---")
X = x.reshape(3, 4)
print(X)

print("\n--- zeros / ones / randn ---")
print(torch.zeros((2, 3, 4)))
print(torch.ones((2, 3, 4)))
print(torch.randn(3, 4))

print("\n--- tensor operations ---")
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2.0, 2, 2, 2])
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x / y:", x / y)
print("x ** y:", x ** y)

print("\n--- concat ---")
X = torch.arange(12, dtype=torch.float32).reshape(3, 4)
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(torch.cat((X, Y), dim=0))
print(torch.cat((X, Y), dim=1))

print("\n--- comparison / sum ---")
print(X == Y)
print(X.sum())

print("\n--- broadcasting ---")
a = torch.arange(3).reshape(3, 1)
b = torch.arange(2).reshape(1, 2)
print(a + b)

print("\n--- indexing ---")
print(X[-1])
print(X[1:3])

print("\n--- GPU tensor ---")
X_gpu = X.to(device)
print(X_gpu.device)

print("\n--- GPU matrix multiplication ---")
A = torch.randn(3000, 3000, device=device)
B = torch.randn(3000, 3000, device=device)
C = A @ B
print(C.shape)
print("done")
