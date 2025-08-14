#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyTorch temel operasyonları örneği
- Tensör oluşturma
- Şekil değiştirme (reshape/view/permute)
- Cihaz seçimi (CPU/GPU)
- İleri (forward) ve geri (backward) hesaplamalar (autograd)
- 2B rastgele tensörler üzerinde toplama, matris çarpımı, element-wise fonksiyonlar

Çalıştırma:
    python torch_basics.py
"""

from __future__ import annotations
import torch

def select_device() -> torch.device:
    """CUDA varsa CUDA'yı, yoksa CPU'yu seçer."""
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    return device

def tensor_basics(device: torch.device) -> None:
    print("=== Cihaz ===")
    print("PyTorch sürüm:", torch.__version__)
    print("CUDA kullanılabilir mi?:", torch.cuda.is_available())
    print("Seçilen cihaz:", device)

    # Tekrarlanabilirlik için sabit tohum
    torch.manual_seed(42)

    print("\n=== Tensör Oluşturma ===")
    # 2B rastgele tensörler
    X = torch.randn((3, 4), device=device)  # 3x4
    Y = torch.randn((3, 4), device=device)  # 3x4
    print("X.shape:", tuple(X.shape), "Y.shape:", tuple(Y.shape))
    print("X dtype:", X.dtype, "Y dtype:", Y.dtype)

    print("\n=== Toplama (element-wise) ===")
    S = X + Y
    print("S = X + Y -> shape:", tuple(S.shape))
    print("S[0, :2]:", S[0, :2].detach().cpu().numpy())

    print("\n=== Matris Çarpımı ===")
    # (3x4) @ (4x2) -> (3x2)
    W = torch.randn((4, 2), device=device)
    M = X @ W
    print("M = X @ W -> shape:", tuple(M.shape))
    print("M[0]:", M[0].detach().cpu().numpy())

    print("\n=== Element-wise Fonksiyonlar ===")
    relu_X = torch.relu(X)
    sigmoid_X = torch.sigmoid(X)
    custom = X**2 + torch.sin(X)  # örnek bir fonksiyon
    print("relu(X)[0, :2]:", relu_X[0, :2].detach().cpu().numpy())
    print("sigmoid(X)[0, :2]:", sigmoid_X[0, :2].detach().cpu().numpy())
    print("custom(X)[0, :2]:", custom[0, :2].detach().cpu().numpy())

    print("\n=== Şekil Değiştirme (reshape/view/permute) ===")
    X_flat = X.reshape(-1)          # 12 elemanlı vektör
    X_view = X.view(3, 2, 2)        # view: aynı bellek, farklı görünüm (uygun boyutlar gerekir)
    X_perm = X.permute(1, 0)        # eksenleri yer değiştir (4x3)
    print("X_flat.shape:", tuple(X_flat.shape))
    print("X_view.shape:", tuple(X_view.shape))
    print("X_perm.shape:", tuple(X_perm.shape))

def autograd_demo(device: torch.device) -> None:
    print("\n=== Autograd (Forward & Backward) ===")
    torch.manual_seed(123)

    # Giriş ve hedef
    X = torch.randn((3, 4), device=device)          # (batch=3, features=4)
    y_true = torch.randn((3, 2), device=device)     # (batch=3, outputs=2)

    # Öğrenilecek parametreler
    W = torch.randn((4, 2), device=device, requires_grad=True)
    b = torch.zeros((2,), device=device, requires_grad=True)

    # Forward: doğrusal katman
    y_pred = X @ W + b          # (3x2)
    # Basit MSE loss
    loss = torch.mean((y_pred - y_true) ** 2)

    print("y_pred.shape:", tuple(y_pred.shape))
    print("loss:", float(loss.detach().cpu()))

    # Backward: türev/grad hesaplaması
    loss.backward()

    # Grad bilgisi
    print("W.grad.shape:", tuple(W.grad.shape), "|| b.grad.shape:", tuple(b.grad.shape))
    print("||W.grad|| (Frobenius):", float(torch.norm(W.grad).detach().cpu()))
    print("||b.grad|| (L2):", float(torch.norm(b.grad).detach().cpu()))

    # Basit bir adım (SGD) örneği - no_grad ile
    lr = 0.1
    with torch.no_grad():
        W -= lr * W.grad
        b -= lr * b.grad
        # Sonraki backward için gradleri sıfırlamak iyi bir alışkanlıktır
        W.grad.zero_()
        b.grad.zero_()
    print("Bir güncelleme adımından sonra örnek: W[0, :2] =", W[0, :2].detach().cpu().numpy())

def main() -> None:
    device = select_device()
    tensor_basics(device)
    autograd_demo(device)

if __name__ == "__main__":
    main()
