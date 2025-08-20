import json, random, time
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# ====== Hiperparametreler ======
SEED = 42
N_TRAIN = 1000   # İstenen altküme
N_VAL   = 2000   # Hızlı valid için altküme (istersen 1000 yap)
BATCH_SIZE = 64
EPOCHS = 5
LR = 1e-3

# ====== Deterministik kurulum ======
random.seed(SEED)
torch.manual_seed(SEED)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ====== Veri ======
transform = transforms.ToTensor()
data_dir = Path("data")

train_full = datasets.MNIST(root=data_dir.as_posix(), train=True, download=True, transform=transform)
val_full   = datasets.MNIST(root=data_dir.as_posix(), train=False, download=True, transform=transform)

# Rastgele permütasyon ile altküme seç
g = torch.Generator().manual_seed(SEED)
train_indices = torch.randperm(len(train_full), generator=g)[:N_TRAIN]
val_indices   = torch.randperm(len(val_full),   generator=g)[:N_VAL]

train_ds = Subset(train_full, train_indices)
val_ds   = Subset(val_full,   val_indices)

train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=BATCH_SIZE, shuffle=False)

# ====== Model ======
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28*28, 256), nn.ReLU(), nn.Dropout(0.2),
    nn.Linear(256, 128),   nn.ReLU(),
    nn.Linear(128, 10)
).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LR)

# ====== Eğitim döngüsü ======
train_losses = []
val_losses = []

def evaluate(loader):
    model.eval()
    total_loss, correct, total = 0.0, 0, 0
    with torch.no_grad():
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            logits = model(x)
            loss = criterion(logits, y)
            total_loss += loss.item() * x.size(0)
            preds = logits.argmax(dim=1)
            correct += (preds == y).sum().item()
            total += x.size(0)
    avg_loss = total_loss / total
    acc = correct / total
    return avg_loss, acc

for epoch in range(1, EPOCHS + 1):
    model.train()
    running = 0.0
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        logits = model(x)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()
        running += loss.item() * x.size(0)
    avg_train = running / len(train_ds)
    train_losses.append(avg_train)

    val_loss, val_acc = evaluate(val_loader)
    val_losses.append(val_loss)
    print(f"Epoch {epoch}/{EPOCHS} - train_loss={avg_train:.4f}  val_loss={val_loss:.4f}  val_acc={val_acc:.4f}")

# ====== Nihai metrikler ======
train_loss_last = train_losses[-1]
val_loss_last, val_acc_last = evaluate(val_loader)
train_loss_eval, train_acc_last = evaluate(train_loader)  # train acc’i de ölç

metrics = {
    "epochs": EPOCHS,
    "train_loss_last": train_loss_last,
    "train_accuracy": train_acc_last,
    "val_loss_last": val_loss_last,
    "val_accuracy": val_acc_last,
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
}

with open("mlp_metrics.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, ensure_ascii=False, indent=2)

# ====== Kayıp grafiği ======
plt.figure()
plt.plot(range(1, EPOCHS+1), train_losses, label="train_loss")
plt.plot(range(1, EPOCHS+1), val_losses,   label="val_loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("MNIST MLP - Training vs Validation Loss")
plt.legend()
plt.tight_layout()
plt.savefig("mlp_loss.png", dpi=150)
print("Kaydedildi: mlp_loss.png, mlp_metrics.json")
