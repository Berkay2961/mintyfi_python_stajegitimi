import torch
from torchvision import models, transforms
from PIL import Image
from transformers import AutoTokenizer, AutoModel

# --- RESNET18 ---
resnet = models.resnet18(pretrained=True)
resnet.eval()

# örnek resim (siyah 224x224)
img = Image.new("RGB", (224, 224), (0, 0, 0))
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(img).unsqueeze(0)  # [1,3,224,224]

with torch.no_grad():
    out_resnet = resnet(input_tensor)

print("✅ ResNet18 çıkış boyutu:", out_resnet.shape)

# --- DISTILBERT ---
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")

inputs = tokenizer("Hello transfer learning!", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

print("✅ DistilBERT last_hidden_state:", outputs.last_hidden_state.shape)
print("✅ DistilBERT pooler_output yok, CLS token kullanılır:", outputs.last_hidden_state[:,0,:].shape)
