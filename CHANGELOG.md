# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-10-31

### Added
- ✅ **Custom data support**: Added `data` parameter to `create()` method
  - Attach custom data (dict, str, or any JSON-serializable object) to verification sessions (max 100KB)
  - Data is returned in webhook callbacks as `customData` field
  - Useful for tracking user IDs, order IDs, or any custom metadata

### Changed
- ✅ **Enhanced `create()` method**: Added missing parameters
  - `lang` - Language code ('en', 'tr')
  - `webhook_url` - Webhook URL for completion callback
  - `redirect_url` - Redirect URL after verification
  - `timeout` - Session timeout in minutes (1-15)
  - `data` - Custom data (replaces deprecated `metadata` parameter)
- 📝 Updated README with complete parameter examples
- 📝 Updated webhook examples to show `customData` field

### Example
```python
session = verifly.verification.create(
    phone='5551234567',
    methods=['sms', 'whatsapp'],
    lang='tr',
    webhook_url='https://mysite.com/webhook',
    data={'userId': '12345', 'orderId': 'ORD-789'}
)

# Webhook payload will include:
# { 'sessionId': '...', 'customData': {'userId': '12345', 'orderId': 'ORD-789'}, ... }
```

---

## [1.0.0] - 2025-10-15

### Added

- ✅ HMAC-SHA256 signature authentication for all API requests
- ✅ Verification session management (`create`, `get`, `select_method`)
- ✅ Session control (`cancel`, `abort`)
- ✅ Balance inquiry (`get_balance`)
- ✅ Webhook signature verification
- ✅ Full type hints for Python 3.6+
- ✅ Custom error classes for better error handling
- ✅ Comprehensive documentation and examples

### Features

**Verification Methods:**
- `create()` - Create verification session
- `get()` - Get session status
- `select_method()` - Select verification method
- `cancel()` - Cancel session (temporary)
- `abort()` - Abort session (permanent)
- `get_balance()` - Get account balance and transactions

**Webhook Utilities:**
- `verify()` - Verify webhook signature
- `generate_signature()` - Generate HMAC signature
- `construct_event()` - Construct verified event object

**Security:**
- HMAC-SHA256 signature for every API request
- Timestamp-based replay attack prevention
- Fixed base URL: `https://www.verifly.net`

### Configuration

```python
from verifly import Verifly

verifly = Verifly(
    api_key='your-api-key',
    secret_key='your-secret-key',  # REQUIRED for HMAC signature
    timeout=30,                     # Optional: Request timeout (seconds)
    debug=False                     # Optional: Debug logging
)
```

---

## Links

- [README](./README.md)
- [PyPI Package](https://pypi.org/project/verifly-sdk/)
