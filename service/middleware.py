from substrateutils import Kusama

from .settings import ARBITRATOR_KEY
from .settings import KUSAMA_NODE_PROVIDER
from .settings import POLKADOT_NODE_PROVIDER

# from substrateutils import Polkadot

print("Kusama provider", KUSAMA_NODE_PROVIDER)
print("Polkadot provider", POLKADOT_NODE_PROVIDER)

kusama = Kusama(arbitrator_key=ARBITRATOR_KEY, node_url=KUSAMA_NODE_PROVIDER)
kusama.connect()
print("Kusama runtime", kusama.runtime_info()["specVersion"])

# polkadot = Polkadot(arbitrator_key=ARBITRATOR_KEY, node_url=POLKADOT_NODE_PROVIDER)
# polkadot.connect()
# print("Polkadot runtime", polkadot.runtime_info()['specVersion'])
