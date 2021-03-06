#-----------------------------------------------------------------------
# PyMTLError
#-----------------------------------------------------------------------
class PyMTLError( Exception ):
  pass

#-----------------------------------------------------------------------
# model components
#-----------------------------------------------------------------------

from model.Model      import Model
from model.signals    import Wire, InPort, OutPort
from model.PortBundle import PortBundle, create_PortBundles

#-----------------------------------------------------------------------
# data types
#-----------------------------------------------------------------------

from datatypes.Bits        import Bits
from datatypes.BitStruct   import BitStruct, BitStructDefinition, BitField
from datatypes.helpers     import (
    get_nbits, clog2, zext, sext, concat,
    reduce_and, reduce_or, reduce_xor
)
from datatypes.SignalValue import CreateWrappedClass

#-----------------------------------------------------------------------
# tools
#-----------------------------------------------------------------------

from tools.simulation.SimulationTool import SimulationTool
from tools.translation.verilator_sim import TranslationTool
from tools.translation.cpp_sim       import get_cpp
from tools.integration.verilog       import VerilogModel
from tools.integration.systemc       import SystemCModel

#-----------------------------------------------------------------------
# py.test decorators
#-----------------------------------------------------------------------

from pytest          import mark            as _mark
from distutils.spawn import find_executable as _find_executable
from os.path         import exists          as _exists

_has = lambda x: _find_executable( x ) != None

requires_xcc = _mark.skipif( not( _has('maven-gcc') and _has('maven-objdump') ),
                             reason='requires cross-compiler toolchain' )

requires_vmh = _mark.skipif( not _exists('../tests/build/vmh'),
                             reason='requires vmh files' )

requires_iverilog  = _mark.skipif( not( _has('iverilog') ),
                                   reason='requires iverilog' )

requires_verilator = _mark.skipif( not( _has('verilator') ),
                                   reason='requires verilator' )

#-----------------------------------------------------------------------
# pymtl namespace
#-----------------------------------------------------------------------

__all__ = [ # Model Construction
            'Model',
            'VerilogModel',
            'SystemCModel',
            # Signals
            'InPort',
            'OutPort',
            'Wire',
            'PortBundle',
            'create_PortBundles',
            # Message Types
            'Bits',
            'BitStruct',
            # Message Constructors
            'BitStructDefinition',
            'BitField',
            # Tools
            'SimulationTool',
            'TranslationTool',
            # TEMPORARY
            'get_cpp',
            'CreateWrappedClass',
            # Helper Functions
            'get_nbits',
            'clog2',
            'sext',
            'zext',
            'concat',
            'reduce_and',
            'reduce_or',
            'reduce_xor',
            # py.test decorators
            'requires_xcc',
            'requires_vmh',
            'requires_iverilog',
            'requires_verilator',
          ]

