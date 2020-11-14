from substrateutils import Kusama
from substrateutils import Polkadot

from .settings import ARBITRATOR_KEY
from .settings import KUSAMA_NODE_PROVIDER
from .settings import POLKADOT_NODE_PROVIDER

print("Kusama provider", KUSAMA_NODE_PROVIDER)
print("Polkadot provider", POLKADOT_NODE_PROVIDER)

kusama = Kusama(arbitrator_key=ARBITRATOR_KEY, node_url=KUSAMA_NODE_PROVIDER)
kusama.connect()
kusama.runtime_info()

polkadot = Polkadot(arbitrator_key=ARBITRATOR_KEY, node_url=POLKADOT_NODE_PROVIDER)
polkadot.connect()
polkadot.runtime_info()
