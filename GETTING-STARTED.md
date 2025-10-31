# 🐍 Verifly Python SDK - Başlangıç Rehberi

## 📁 Proje Yapısı

```
verifly-python-sdk/
├── verifly/                    # Ana paket
│   ├── __init__.py            # Package initialization
│   ├── client.py              # Verifly client (ana sınıf)
│   ├── errors.py              # Error sınıfları
│   ├── resources/             # API resources
│   │   ├── __init__.py
│   │   ├── verification.py    # Verification methods
│   │   └── webhook.py         # Webhook utilities
│   └── utils/                 # Utilities
│       ├── __init__.py
│       └── request.py         # HTTP request handler + HMAC
├── examples/                   # Örnek kodlar
│   ├── basic.py               # Basit kullanım
│   └── flask_webhook.py       # Flask webhook örneği
├── setup.py                    # PyPI packaging
├── requirements.txt            # Dependencies
├── README.md                   # Dokümantasyon
├── LICENSE                     # MIT License
├── CHANGELOG.md               # Version history
├── PUBLISH.md                 # PyPI yayınlama rehberi
├── MANIFEST.in                # Package files
└── .gitignore                 # Git ignore
```

---

## 🚀 Hızlı Test

### 1. Virtual Environment Oluştur

```bash
cd verifly-python-sdk

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Dependencies Yükle

```bash
pip install -r requirements.txt
```

### 3. Development Mode Install

```bash
# Editable install (kodda değişiklik yapınca otomatik güncellenir)
pip install -e .
```

### 4. Test Et

```python
# Python interactive shell
python

>>> from verifly import Verifly
>>> verifly = Verifly(api_key='test', secret_key='test')
>>> print("✅ SDK yüklendi!")
```

---

## 🧪 Örnek Çalıştırma

### Basic Example

```bash
# API key'leri düzenle
nano examples/basic.py

# Çalıştır
python examples/basic.py
```

### Flask Webhook Example

```bash
# Flask yükle
pip install flask

# API key'leri düzenle
nano examples/flask_webhook.py

# Çalıştır
python examples/flask_webhook.py
```

---

## 📦 PyPI'a Yayınlama

### 1. Gerekli Paketleri Yükle

```bash
pip install build twine
```

### 2. Build Et

```bash
python -m build
```

### 3. TestPyPI'da Test Et (İsteğe Bağlı)

```bash
python -m twine upload --repository testpypi dist/*
```

### 4. PyPI'a Yayınla

```bash
python -m twine upload dist/*
```

Detaylı rehber için: [PUBLISH.md](PUBLISH.md)

---

## 🔧 Development

### Kod Değişiklikleri

1. Kodda değişiklik yap
2. Editable install sayesinde otomatik güncellenir
3. Test et:

```python
# Reload et
from importlib import reload
import verifly
reload(verifly)
```

### Version Güncelleme

**3 yerde güncelle:**

1. `setup.py`:
```python
version='1.0.1',
```

2. `verifly/__init__.py`:
```python
__version__ = '1.0.1'
```

3. `CHANGELOG.md`:
```markdown
## [1.0.1] - 2025-10-15
### Fixed
- Bug fix
```

---

## 🧪 Testing

### Manual Test

```python
from verifly import Verifly

verifly = Verifly(
    api_key='your-api-key',
    secret_key='your-secret-key',
    debug=True
)

# Test create
session = verifly.verification.create(
    phone='5551234567',
    methods=['sms']
)
print(session)

# Test get
status = verifly.verification.get(session['sessionId'])
print(status)

# Test balance
balance = verifly.verification.get_balance()
print(balance)
```

### Unit Tests (Gelecekte)

```bash
# pytest yükle
pip install pytest

# Tests oluştur
mkdir tests
touch tests/test_verification.py

# Çalıştır
pytest
```

---

## 📚 Dokümantasyon

### README.md Güncelleme

```bash
nano README.md
```

### Kod Dokümantasyonu

Tüm fonksiyonlar docstring ile dokümante edilmiş:

```python
def create(
    self,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    ...
) -> Dict[str, Any]:
    """
    Create verification session
    
    Args:
        phone: Phone number
        email: Email address
        
    Returns:
        Session data
        
    Example:
        session = verifly.verification.create(...)
    """
```

---

## 🔍 Debugging

### Debug Mode

```python
verifly = Verifly(
    api_key='...',
    secret_key='...',
    debug=True  # Request/response loglar
)
```

### Interactive Testing

```python
import verifly
from importlib import reload

# Kod değiştir
reload(verifly)

# Test et
v = verifly.Verifly(...)
```

---

## ✅ Pre-publish Checklist

- [ ] Tüm dosyalar oluşturuldu
- [ ] `setup.py` doğru yapılandırıldı
- [ ] Dependencies `requirements.txt`'de
- [ ] README.md güncel
- [ ] CHANGELOG.md güncel
- [ ] LICENSE mevcut
- [ ] Examples çalışıyor
- [ ] Manual test yapıldı
- [ ] Version numaraları tutarlı

---

## 🎯 Next Steps

1. ✅ Local test yap
2. ✅ Virtual env'de test et
3. ✅ Examples çalıştır
4. ✅ TestPyPI'a yükle (isteğe bağlı)
5. ✅ PyPI'a yayınla
6. ✅ `pip install verifly-sdk` ile test et
7. ✅ Dokümantasyon yayınla

---

## 📞 Destek

- Email: info@verifly.net
- Website: https://www.verifly.net
- Docs: https://www.verifly.net/docs

---

**🎉 Python SDK hazır! İyi kodlamalar!**
