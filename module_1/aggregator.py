from .sbox44 import SBOX44
from .preprocessing import sbox_to_boolean
from .nonlinearity import nonlinearity
from .sac import sac
from .bic import bic_nl
from .linear_tests import lap
from .differential_tests import dap, du
from .algebraic_tests import algebraic_degree
from .sidechannel_tests import transparency_order, correlation_immunity

def run_all_tests():
    boolean_funcs = sbox_to_boolean(SBOX44)
    return {
        "NL": min(nonlinearity(f) for f in boolean_funcs),
        "SAC": sac(SBOX44),
        "BIC-NL": bic_nl(boolean_funcs),
        "LAP": lap(SBOX44),
        "DAP": dap(SBOX44),
        "DU": du(SBOX44),
        "AD": max(algebraic_degree(f) for f in boolean_funcs),
        "TO": transparency_order(SBOX44),
        "CI": correlation_immunity(boolean_funcs[0])
    }
