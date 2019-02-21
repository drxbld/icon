# ------------------------------------------------------------
# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Stefano Thegroove 360
# Copyright 2018 https://stefanoaddon.info
#
# Distribuito sotto i termini di GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------- -----------
# Questo file fa parte di Stefano Thegroove 360.
#
# Stefano Thegroove 360 ​​è un software gratuito: puoi ridistribuirlo e / o modificarlo
# è sotto i termini della GNU General Public License come pubblicata da
# la Free Software Foundation, o la versione 3 della licenza, o
# (a tua scelta) qualsiasi versione successiva.
#
# Stefano Thegroove 360 ​​è distribuito nella speranza che possa essere utile,
# ma SENZA ALCUNA GARANZIA; senza nemmeno la garanzia implicita di
# COMMERCIABILITÀ o IDONEITÀ PER UN PARTICOLARE SCOPO. Vedere il
# GNU General Public License per maggiori dettagli.
#
# Dovresti aver ricevuto una copia della GNU General Public License
# insieme a Stefano Thegroove 360. In caso contrario, vedi <http://www.gnu.org/licenses/>.
# ------------------------------------------------- -----------
# Client for Stefano Thegroove 360
#------------------------------------------------------------

from .base import *
from .constructors.jsmath import Math
from .constructors.jsdate import Date
from .constructors.jsobject import Object
from .constructors.jsfunction import Function
from .constructors.jsstring import String
from .constructors.jsnumber import Number
from .constructors.jsboolean import Boolean
from .constructors.jsregexp import RegExp
from .constructors.jsarray import Array
from .prototypes.jsjson import JSON
from .host.console import console
from .host.jseval import Eval
from .host.jsfunctions import parseFloat, parseInt, isFinite, isNaN

# Now we have all the necessary items to create global environment for script
__all__ = ['Js', 'PyJsComma', 'PyJsStrictEq', 'PyJsStrictNeq',
           'PyJsException', 'PyJsBshift', 'Scope', 'PyExceptionToJs',
           'JsToPyException', 'JS_BUILTINS', 'appengine', 'set_global_object',
           'JsRegExp', 'PyJsException', 'PyExceptionToJs', 'JsToPyException', 'PyJsSwitchException']


# these were defined in base.py
builtins = ('true','false','null','undefined','Infinity',
            'NaN', 'console', 'String', 'Number', 'Boolean', 'RegExp',
            'Math', 'Date', 'Object', 'Function', 'Array',
            'parseFloat', 'parseInt', 'isFinite', 'isNaN')
            #Array, Function, JSON,   Error is done later :)
            # also some built in functions like eval...

def set_global_object(obj):
    obj.IS_CHILD_SCOPE = False
    this = This({})
    this.own = obj.own
    this.prototype = obj.prototype
    PyJs.GlobalObject = this
    # make this available
    obj.register('this')
    obj.put('this', this)



scope = dict(zip(builtins, [globals()[e] for e in builtins]))
# Now add errors:
for name, error in ERRORS.items():
    scope[name] = error
#add eval
scope['eval'] = Eval
scope['JSON'] = JSON
JS_BUILTINS = dict([(k,v) for k,v in scope.items()])

