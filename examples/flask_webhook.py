"""
Flask Webhook Example
"""

from flask import Flask, request, jsonify
from verifly import Verifly

app = Flask(__name__)

# Initialize Verifly
verifly = Verifly(
    api_key='your-api-key',
    secret_key='your-secret-key'
)

@app.route('/webhook/verifly', methods=['POST'])
def verifly_webhook():
    """Handle Verifly webhook"""
    
    # Get headers
    signature = request.headers.get('X-Signature')
    timestamp = request.headers.get('X-Timestamp')
    
    if not signature or not timestamp:
        return jsonify({'error': 'Missing signature headers'}), 400
    
    # Get payload
    payload = request.get_json()
    
    # Verify signature
    try:
        event = verifly.webhook.construct_event(payload, signature, timestamp)
    except ValueError as e:
        print(f"❌ Invalid webhook signature: {e}")
        return jsonify({'error': 'Invalid signature'}), 401
    
    # Process webhook event
    event_type = event.get('event')
    data = event.get('data', {})
    
    print(f"✅ Webhook received: {event_type}")
    
    if event_type == 'verification.completed':
        session_id = data.get('sessionId')
        method = data.get('method')
        print(f"  Session {session_id} verified via {method}")
        
        # Your business logic here
        # e.g., update user record, grant access, etc.
        
    elif event_type == 'verification.failed':
        session_id = data.get('sessionId')
        reason = data.get('reason')
        print(f"  Session {session_id} failed: {reason}")
        
    elif event_type == 'verification.expired':
        session_id = data.get('sessionId')
        print(f"  Session {session_id} expired")
    
    return jsonify({'success': True})

@app.route('/verify/create', methods=['POST'])
def create_verification():
    """Create verification session"""
    
    try:
        data = request.get_json()
        
        session = verifly.verification.create(
            phone=data.get('phone'),
            email=data.get('email'),
            methods=data.get('methods', ['sms', 'whatsapp'])
        )
        
        return jsonify({
            'success': True,
            'data': session
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/verify/status/<session_id>', methods=['GET'])
def get_verification_status(session_id):
    """Get verification status"""
    
    try:
        status = verifly.verification.get(session_id)
        
        return jsonify({
            'success': True,
            'data': status
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=3000)
