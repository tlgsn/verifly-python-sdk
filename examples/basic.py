"""
Basic Verifly SDK Usage Example
"""

from verifly import Verifly, AuthenticationError, InsufficientBalanceError

# Initialize client
verifly = Verifly(
    api_key='your-api-key',
    secret_key='your-secret-key',
    debug=True  # Enable debug logging
)

def main():
    try:
        # 1. Create verification session
        print("Creating verification session...")
        session = verifly.verification.create(
            phone='5551234567',
            methods=['sms', 'whatsapp']
        )
        
        print(f"✅ Session created!")
        print(f"  Session ID: {session['sessionId']}")
        print(f"  Iframe URL: {session['iframeUrl']}")
        print(f"  Status: {session['status']}")
        
        session_id = session['sessionId']
        
        # 2. Get session status
        print(f"\nGetting session status...")
        status = verifly.verification.get(session_id)
        print(f"  Status: {status['status']}")
        
        # 3. Get balance
        print(f"\nChecking account balance...")
        balance = verifly.verification.get_balance()
        print(f"  Balance: {balance['balance']} {balance['currency']}")
        print(f"  Recent transactions: {len(balance['recentTransactions'])}")
        
    except AuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("Check your API key and secret key")
        
    except InsufficientBalanceError as e:
        print(f"❌ Insufficient balance: {e}")
        print(f"Balance data: {e.balance_data}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
