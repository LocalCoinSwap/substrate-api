"""
Type specifications for API endpoints
"""

balance = [{"name": "address", "type": str, "required": True}]

nonce = [{"name": "address", "type": str, "required": True}]

multi_balance = [{"name": "addresses", "type": dict, "required": True}]

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
    {"name": "params", "type": str, "required": True, "action": "append"},
]

publish_approve_as_multi = [
    {"name": "seller_address", "type": str, "required": True},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "signed_approve_as_multi", "type": str, "required": True},
    {"name": "approve_as_multi_nonce", "type": int, "required": True},
    {"name": "trade_value", "type": int, "required": True},
]

broadcast = [
    {"name": "type", "type": str, "required": True},
    {"name": "transaction", "type": str, "required": True},
]

approve_as_multi_payload = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
    {"name": "other_trader", "type": str, "required": True},
]

as_multi_payload = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
    {"name": "other_trader", "type": str, "required": True},
    {"name": "timepoint", "type": str, "required": False, "action": "append"},
    {"name": "store_call", "type": bool, "required": False},
    {"name": "max_weight", "type": int, "required": False},
]

as_multi_storage = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": str, "required": True},
]

release_escrow = [
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "timepoint", "type": str, "required": True, "action": "append"},
]

cancellation = [
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "timepoint", "type": str, "required": True, "action": "append"},
]

dispute = [
    {"name": "victor", "type": str, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "welfare_value", "type": str, "required": False},
]

is_transaction_success = [
    {"name": "transaction_type", "type": str, "required": True},
    {"name": "events", "type": list, "required": True},
]

diagnose = [{"name": "escrow_address", "type": str, "required": True}]

fee_return_tx = [
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
]

welfare_tx = [
    {"name": "buyer_address", "type": str, "required": True},
]
