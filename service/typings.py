"""
Type specifications for API endpoints
"""

balance = [{"name": "address", "type": str, "required": True}]

nonce = [{"name": "address", "type": str, "required": True}]

multi_balance = [{"name": "addresses", "type": dict, "required": True}]

transfer_payload = [
    {"name": "currency", "type": str, "required": False},
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
]

escrow_address = [
    {"name": "currency", "type": str, "required": False},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "threshold", "type": int, "required": False},
]

escrow_payloads = [
    {"name": "currency", "type": str, "required": False},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "escrow_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
]

publish = [
    {"name": "currency", "type": str, "required": False},
    {"name": "type", "type": str, "required": True},
    {"name": "params", "type": str, "required": True, "action": "append"},
]

publish_approve_as_multi = [
    {"name": "currency", "type": str, "required": False},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "signed_approve_as_multi", "type": str, "required": True},
    {"name": "approve_as_multi_nonce", "type": int, "required": True},
    {"name": "trade_value", "type": int, "required": True},
]

publish_as_multi = [
    {"name": "currency", "type": str, "required": False},
    {"name": "from_address", "type": str, "required": True},
    {"name": "signature", "type": str, "required": True},
    {"name": "nonce", "type": int, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "other_signatory", "type": str, "required": True},
    {"name": "max_weight", "type": int, "required": False},
    {"name": "timepoint", "type": str, "required": True, "action": "append"},
]

broadcast = [
    {"name": "currency", "type": str, "required": False},
    {"name": "type", "type": str, "required": True},
    {"name": "transaction", "type": str, "required": True},
]

approve_as_multi_payload = [
    {"name": "currency", "type": str, "required": False},
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
    {"name": "other_trader", "type": str, "required": True},
]

as_multi_payload = [
    {"name": "currency", "type": str, "required": False},
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
    {"name": "other_trader", "type": str, "required": True},
    {"name": "timepoint", "type": str, "required": False, "action": "append"},
    {"name": "store_call", "type": bool, "required": False},
    {"name": "max_weight", "type": int, "required": False},
]

as_multi_storage = [
    {"name": "currency", "type": str, "required": False},
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": str, "required": True},
]

release_escrow = [
    {"name": "currency", "type": str, "required": False},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "timepoint", "type": str, "required": True, "action": "append"},
]

cancellation = [
    {"name": "currency", "type": str, "required": False},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "timepoint", "type": str, "required": True, "action": "append"},
]

dispute = [
    {"name": "currency", "type": str, "required": False},
    {"name": "victor", "type": str, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "welfare_value", "type": str, "required": False},
]

is_transaction_success = [
    {"name": "currency", "type": str, "required": False},
    {"name": "transaction_type", "type": str, "required": True},
    {"name": "events", "type": list, "required": True},
]

diagnose = [
    {"name": "currency", "type": str, "required": False},
    {"name": "escrow_address", "type": str, "required": True},
]

fee_return_tx = [
    {"name": "currency", "type": str, "required": False},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
]

welfare_tx = [
    {"name": "currency", "type": str, "required": False},
    {"name": "buyer_address", "type": str, "required": True},
]
