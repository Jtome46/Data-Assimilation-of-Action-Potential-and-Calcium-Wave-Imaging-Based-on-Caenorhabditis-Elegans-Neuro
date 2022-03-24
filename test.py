from owmeta_core.command import OWM
conn = OWM().connect()

# Make the context
from owmeta_core.context import Context
ctx = conn(Context)(ident='http://openworm.org/data')

# Grab the representation of the neuronal network
from owmeta.worm import Worm
net = ctx.stored(Worm).query().neuron_network()

# Grab a specific neuron
from owmeta.neuron import Neuron
aval = ctx.stored(Neuron).query(name='AVAL')

# Get the neuron's type
print(aval.type.one())

# Count how many connections come from AVAL
print(aval.connection.count('pre'))

print(len(set(net.neuron_names())))

print(sorted(net.neuron_names()))
