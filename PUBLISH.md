# PyPI Yayınlama Rehberi

## 🚀 Hızlı Başlangıç

```bash
# 1. Gerekli paketleri yükle
pip install twine build

# 2. Package oluştur
python -m build

# 3. PyPI'a yükle
python -m twine upload dist/*
```

---

## 📦 Adım Adım Yayınlama

### 1. Gerekli Paketleri Yükle

```bash
pip install --upgrade pip
pip install --upgrade build twine
```

### 2. PyPI Hesabı Oluştur

https://pypi.org/account/register/

### 3. API Token Oluştur

1. PyPI'da login ol
2. Account Settings → API tokens
3. "Add API token" tıkla
4. Token'ı kopyala ve sakla

### 4. `.pypirc` Dosyası Oluştur

Windows: `C:\Users\<username>\.pypirc`
Linux/Mac: `~/.pypirc`

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # API token buraya
```

### 5. Package Build Et

```bash
# Eski build'leri temizle
rm -rf build/ dist/ *.egg-info/

# Yeni build oluştur
python -m build
```

Bu komut şunları oluşturur:
- `dist/verifly-sdk-1.0.0.tar.gz` (source distribution)
- `dist/verifly_sdk-1.0.0-py3-none-any.whl` (wheel)

### 6. TestPyPI'da Test Et (İsteğe Bağlı)

```bash
# TestPyPI'a yükle
python -m twine upload --repository testpypi dist/*

# TestPyPI'dan yükle ve test et
pip install --index-url https://test.pypi.org/simple/ verifly-sdk
```

### 7. PyPI'a Yayınla

```bash
python -m twine upload dist/*
```

### 8. Doğrula

```bash
# PyPI'dan yükle
pip install verifly-sdk

# Test et
python -c "from verifly import Verifly; print('OK')"
```

---

## 🔄 Version Güncelleme

### 1. Version'ı Artır

**setup.py:**
```python
version='1.0.1',  # 1.0.0 -> 1.0.1
```

**verifly/__init__.py:**
```python
__version__ = '1.0.1'
```

**CHANGELOG.md:**
```markdown
## [1.0.1] - 2025-10-15

### Fixed
- Bug fix açıklaması
```

### 2. Build ve Yayınla

```bash
# Eski build'leri temizle
rm -rf build/ dist/ *.egg-info/

# Yeni build
python -m build

# Yayınla
python -m twine upload dist/*
```

---

## 🛡️ Güvenlik

### API Token Güvenliği

❌ **YAPMAYIN:**
```bash
# Token'ı command line'da kullanma
twine upload -u __token__ -p pypi-AgEI... dist/*
```

✅ **YAPIN:**
```bash
# .pypirc dosyası kullan
twine upload dist/*
```

### .gitignore

```gitignore
# PyPI credentials
.pypirc

# Build artifacts
build/
dist/
*.egg-info/
```

---

## 📊 Version Semantics

```
MAJOR.MINOR.PATCH
1.0.0
```

- **MAJOR**: Breaking changes (1.0.0 → 2.0.0)
- **MINOR**: New features (1.0.0 → 1.1.0)
- **PATCH**: Bug fixes (1.0.0 → 1.0.1)

---

## ✅ Pre-publish Checklist

- [ ] Version numarası güncellendi (`setup.py`, `__init__.py`)
- [ ] CHANGELOG.md güncellendi
- [ ] README.md güncel
- [ ] requirements.txt güncel
- [ ] Tests çalıştırıldı (varsa)
- [ ] Eski build'ler temizlendi
- [ ] `.pypirc` dosyası oluşturuldu
- [ ] TestPyPI'da test edildi (isteğe bağlı)

---

## 🔧 Sorun Giderme

### "File already exists"

```bash
# Version numarasını artır
# setup.py'de version='1.0.1' yap
```

### "Invalid distribution"

```bash
# setup.py'yi kontrol et
python setup.py check

# Metadata kontrol
python -m twine check dist/*
```

### "Authentication failed"

```bash
# .pypirc dosyasını kontrol et
# API token'ı yenile
```

---

## 📚 Kaynaklar

- PyPI: https://pypi.org/
- TestPyPI: https://test.pypi.org/
- Packaging Guide: https://packaging.python.org/
- Twine Docs: https://twine.readthedocs.io/

---

## 🎯 Quick Reference

```bash
# Build
python -m build

# Upload
python -m twine upload dist/*

# Check
python -m twine check dist/*

# Version
python setup.py --version
```

---

**✨ İlk yayın için başarılar!**
