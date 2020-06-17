"""
Type specifications for API endpoints
"""

balance = [{"name": "address", "type": str, "required": True}]

nonce = [{"name": "address", "type": str, "required": True}]

transfer_payload = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
]

escrow_address = [
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "threshold", "type": int, "required": False},
]

escrow_payloads = [
    {"name": "seller_address", "type": str, "required": True},
    {"name": "escrow_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
]

publish = [
    {"name": "type", "type": str, "required": True},
    {"name": "params", "type": list, "required": True},
]

broadcast = [
    {"name": "type", "type": str, "required": True},
    {"name": "transaction", "type": str, "required": True},
]

approve_as_multi_payload = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
]

release_escrow = [
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
    {"name": "timepoint", "type": tuple, "required": True},
]

cancellation = [
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
    {"name": "timepoint", "type": tuple, "required": True},
]

dispute = [
    {"name": "victor", "type": str, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
    {"name": "welfare_value", "type": tuple, "required": False},
]

is_transaction_success = [
    {"name": "transaction_type", "type": str, "required": True},
    {"name": "events", "type": list, "required": True},
]

diagnose = [{"name": "escrow_address", "type": str, "required": True}]
