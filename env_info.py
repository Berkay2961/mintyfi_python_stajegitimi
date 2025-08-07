import sys
import torch
import platform
import pkg_resources

def get_pkg_versions():
    packages = ['numpy', 'pandas', 'scikit-learn', 'matplotlib', 'torch']
    return {pkg: pkg_resources.get_distribution(pkg).version for pkg in packages}

print("Python Sürümü:", sys.version)
print("İşletim Sistemi:", platform.system(), platform.release())
print("CUDA Desteği:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "Yok")
print("Yüklü Kütüphaneler:")
for pkg, ver in get_pkg_versions().items():
    print(f"  {pkg}: {ver}")
