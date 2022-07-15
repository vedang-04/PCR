import os
import imp

# import importlib
import scipy

DEBUG = False
from lib.networks.snake.ct_snake import get_network as get_ro

_network_factory = {
}


def get_network(cfg):
    arch = cfg.network
    heads = cfg.heads
    head_conv = cfg.head_conv
    num_layers = int(arch[arch.find('_') + 1:]) if '_' in arch else 0
    arch = arch[:arch.find('_')] if '_' in arch else arch
    network = get_ro(num_layers, heads, head_conv, down_ratio, det_dir)
    # network = get_ro(heads)
    return network


def make_network(cfg):
    module = '.'.join(['lib.networks', cfg.task])
    path = os.path.join('lib/networks', cfg.task, '__init__.py')
    if DEBUG:
        print('make-network-path:', path)
    return imp.load_source(module, path).get_network(cfg)
