#Syntax Highlighter
from tkinter import *
from pygments import lex
from pygments.lexers.python import Python3Lexer, PythonLexer, CythonLexer, DgLexer
from pygments.lexers.special import TextLexer
from pygments.lexers.html import ScamlLexer, HtmlLexer, DtdLexer, HamlLexer, XmlLexer, PugLexer
from pygments.lexers.templates import HtmlPhpLexer
from pygments.lexers.perl import Perl6Lexer
from pygments.lexers.ruby import RubyLexer
from pygments.lexers.configs import IniLexer, ApacheConfLexer
from pygments.lexers.shell import BashLexer, BatchLexer, FishShellLexer, PowerShellLexer
from pygments.lexers.diff import DiffLexer, WDiffLexer
from pygments.lexers.dotnet import CSharpLexer, FSharpLexer, VbNetLexer
from pygments.lexers.sql import MySqlLexer
from pygments.lexers.jvm import JavaLexer, KotlinLexer
from pygments.lexers.markup import MarkdownLexer, TexLexer
from pygments.lexers.bibtex import BibTeXLexer, BSTLexer
from pygments.lexers.basic import VBScriptLexer
from pygments.lexers.c_cpp import CLexer, CppLexer
from pygments.lexers.c_like import ArduinoLexer, CharmciLexer, ClayLexer, CudaLexer
from pygments.lexers.c_like import ECLexer, PikeLexer, SwigLexer, ValaLexer 
from pygments.lexers.actionscript import ActionScript3Lexer,MxmlLexer
from pygments.lexers.algebra import MathematicaLexer, MuPADLexer
from pygments.lexers.css import CssLexer, LessCssLexer, SassLexer, ScssLexer
from pygments.lexers.data import JsonLexer, YamlLexer, JsonLdLexer
from pygments.lexers.email import EmailLexer
from pygments.lexers.esoteric import BrainfuckLexer as BfLexer
from pygments.lexers.graphics import PostScriptLexer,PovrayLexer
from pygments.lexers.go import GoLexer
from pygments.lexers.j import JLexer
from pygments.lexers.javascript import CoffeeScriptLexer, DartLexer, EarlGreyLexer, JavascriptLexer
from pygments.lexers.javascript import JuttleLexer, KalLexer, LassoLexer,LiveScriptLexer, MaskLexer
from pygments.lexers.javascript import ObjectiveJLexer, TypeScriptLexer
from pygments.lexers.julia import JuliaLexer
from pygments.lexers.objective import ObjectiveCLexer, ObjectiveCppLexer, SwiftLexer, LogosLexer
from pygments.lexers.php import ZephirLexer
from pygments.lexers.scripting import AppleScriptLexer, ChaiscriptLexer, MoonScriptLexer
from pygments.lexers.ambient import AmbientTalkLexer
from pygments.lexers.apl import APLLexer
from pygments.lexers.archetype import AdlLexer, CadlLexer, OdinLexer
from pygments.lexers.asm import Dasm16Lexer, HsailLexer, LlvmLexer, NasmLexer, TasmLexer
from pygments.lexers.automation import AutoItLexer, AutohotkeyLexer
from pygments.lexers.basic import BBCBasicLexer, BlitzBasicLexer, BlitzMaxLexer
from pygments.lexers.basic import MonkeyLexer, QBasicLexer
from pygments.lexers.boa import BoaLexer
from pygments.lexers.business import ABAPLexer, CobolFreeformatLexer, CobolLexer
from pygments.lexers.business import GoodDataCLLexer, MaqlLexer
from pygments.lexers.capnproto import CapnProtoLexer
from pygments.lexers.chapel import ChapelLexer
from pygments.lexers.clean import CleanLexer
from pygments.lexers.configs import TerraformLexer, AugeasLexer, Cfengine3Lexer, DockerLexer, TOMLLexer
from pygments.lexers.console import PyPyLogLexer
from pygments.lexers.crystal import CrystalLexer
from pygments.lexers.d import CrocLexer, DLexer
from pygments.lexers.dalvik import SmaliLexer
from pygments.lexers.dotnet import BooLexer
from pygments.lexers.dsls import RslLexer, ZeekLexer, ThriftLexer, SnowballLexer, AlloyLexer, PanLexer, ProtoBufLexer, PuppetLexer
from pygments.lexers.dylan import DylanLexer, DylanLidLexer
from pygments.lexers.ecl import ECLLexer
from pygments.lexers.eiffel import EiffelLexer
from pygments.lexers.elm import ElmLexer
from pygments.lexers.erlang import ElixirLexer, ErlangLexer
from pygments.lexers.factor import FactorLexer
from pygments.lexers.fantom import FantomLexer
from pygments.lexers.felix import FelixLexer
from pygments.lexers.floscript import FloScriptLexer
from pygments.lexers.forth import ForthLexer
from pygments.lexers.fortran import FortranFixedLexer, FortranLexer
from pygments.lexers.grammar_notation import AbnfLexer, BnfLexer, JsgfLexer
from pygments.lexers.graph import CypherLexer
from pygments.lexers.haskell import AgdaLexer, LiterateIdrisLexer, LiterateHaskellLexer, LiterateCryptolLexer, LiterateAgdaLexer, KokaLexer, CryptolLexer, HaskellLexer, IdrisLexer
from pygments.lexers.haxe import HaxeLexer, HxmlLexer
from pygments.lexers.hdl import VerilogLexer, SystemVerilogLexer, VhdlLexer
from pygments.lexers.idl import IDLLexer
from pygments.lexers.igor import IgorLexer
from pygments.lexers.inferno import LimboLexer
from pygments.lexers.iolang import IoLexer
from pygments.lexers.jvm import IokeLexer, XtendLexer, ScalaLexer, SarlLexer, PigLexer, JasminLexer, AspectJLexer, GoloLexer, CeylonLexer, ClojureLexer, ClojureScriptLexer
from pygments.lexers.lisp import CPSALexer, CommonLispLexer, EmacsLispLexer, FennelLexer
from pygments.lexers.lisp import NewLispLexer, RacketLexer, SchemeLexer, ShenLexer, XtlangLexer
from pygments.lexers.make import CMakeLexer, MakefileLexer
from pygments.lexers.markup import GroffLexer, RstLexer
from pygments.lexers.matlab import ScilabLexer
from pygments.lexers.ml import OcamlLexer, OpaLexer, SMLLexer
from pygments.lexers.modeling import BugsLexer, JagsLexer, ModelicaLexer, StanLexer
from pygments.lexers.monte import MonteLexer
#from pygments.lexers.mosel import MoselLexer
from pygments.lexers.ncl import NCLLexer
from pygments.lexers.nimrod import NimrodLexer
from pygments.lexers.nit import NitLexer
from pygments.lexers.nix import NixLexer
from pygments.lexers.oberon import ComponentPascalLexer as CPascalLexer
from pygments.lexers.ooc import OocLexer
from pygments.lexers.parasail import ParaSailLexer
from pygments.lexers.parsers import TreetopLexer
from pygments.lexers.pascal import AdaLexer, DelphiLexer
from pygments.lexers.pawn import PawnLexer, SourcePawnLexer
from pygments.lexers.pony import PonyLexer
from pygments.lexers.praat import PraatLexer
from pygments.lexers.prolog import LogtalkLexer, PrologLexer
from pygments.lexers.qvt import QVToLexer
from pygments.lexers.r import RConsoleLexer, RdLexer, SLexer
from pygments.lexers.rdf import ShExCLexer, SparqlLexer, TurtleLexer
from pygments.lexers.rebol import RebolLexer, RedLexer
#from pygments.lexers.ride import RideLexer
from pygments.lexers.rnc import RNCCompactLexer as RNCCLexer
from pygments.lexers.roboconf import RoboconfGraphLexer, RoboconfInstancesLexer
from pygments.lexers.robotframework import RobotFrameworkLexer as RFLexer
from pygments.lexers.ruby import FancyLexer
from pygments.lexers.rust import RustLexer
from pygments.lexers.sas import SASLexer
from pygments.lexers.scdoc import ScdocLexer
from pygments.lexers.scripting import EasytrieveLexer, RexxLexer, HybrisLexer, MOOCodeLexer, JclLexer, LSLLexer, LuaLexer
from pygments.lexers.sgf import SmartGameFormatLexer as SGFLexer
from pygments.lexers.shell import SlurmBashLexer, TcshLexer
from pygments.lexers.slash import SlashLexer
from pygments.lexers.smalltalk import NewspeakLexer, SmalltalkLexer
from pygments.lexers.smv import NuSMVLexer
from pygments.lexers.snobol import SnobolLexer
from pygments.lexers.solidity import SolidityLexer
from pygments.lexers.sql import RqlLexer
from pygments.lexers.stata import StataLexer
from pygments.lexers.supercollider import SuperColliderLexer
from pygments.lexers.tcl import TclLexer
from pygments.lexers.teraterm import TeraTermLexer
from pygments.lexers.testing import GherkinLexer, TAPLexer
from pygments.lexers.textedit import AwkLexer, VimLexer
from pygments.lexers.textfmts import GettextLexer, IrcLogsLexer, TodotxtLexer
from pygments.lexers.theorem import CoqLexer, IsabelleLexer, LeanLexer
from pygments.lexers.trafficscript import RtsLexer
from pygments.lexers.typoscript import TypoScriptLexer
from pygments.lexers.unicon import IconLexer, UcodeLexer, UniconLexer
from pygments.lexers.urbi import UrbiscriptLexer
#from pygments.lexers.usd import UsdLexer
from pygments.lexers.varnish import VCLLexer
from pygments.lexers.verification import BoogieLexer, SilverLexer
from pygments.lexers.webmisc import CirruLexer, DuelLexer, QmlLexer, SlimLexer, XQueryLexer
from pygments.lexers.whiley import WhileyLexer
from pygments.lexers.x10 import X10Lexer
from pygments.lexers.zig import ZigLexer
havePygments = True

extensions = (
    ('x10', X10Lexer),
    ('zig', ZigLexer),
    ('whiley', WhileyLexer),
    ('bpl', BoogieLexer),
    ('sil', 'vpr', SilverLexer),
    ('cirru', CirruLexer),
    ('duel', 'jbst', DuelLexer),
    ('qml', 'qbs', QmlLexer),
    ('slim', SlimLexer),
    ('xqy', 'xquery', 'xq', 'xql', 'xqm', XQueryLexer),
    ('vcl', VCLLexer),
    ('typoscript', TypoScriptLexer),
    ('icon', IconLexer),
    ('u', 'u1', 'u2', UcodeLexer),
    ('icn', UniconLexer),
    ('u', UrbiscriptLexer),
    ('v', CoqLexer),
    ('thy', IsabelleLexer),
    ('lean', LeanLexer),
    ('rts', RtsLexer),
    ('todotxt', TodotxtLexer),
    ('weechatlog', IrcLogsLexer),
    ('pot', 'po', GettextLexer),
    ('awk', AwkLexer),
    ('vim', 'vimrc', 'exrc', 'gvimrc', 'exrc', VimLexer),
    ('feature', GherkinLexer),
    ('tap', TAPLexer),
    ('ttl', TeraTermLexer),
    ('tcl', 'rvt', TclLexer),
    ('sc', 'scd', SuperColliderLexer),
    ('do', 'ado', StataLexer),
    ('rql', RqlLexer),
    ('ns2', NewspeakLexer),
    ('st', SmalltalkLexer),
    ('smv', NuSMVLexer),
    ('snobol', SnobolLexer),
    ('sol', SolidityLexer),
    ('sl', SlurmBashLexer),
    ('tcsh', 'csh', TcshLexer),
    ('sl', SlashLexer),
    ('ps1', 'psm1', PowerShellLexer),
    ('bat', 'cmd', BatchLexer),
    ('fish', 'load', FishShellLexer),
    ('sgf', SGFLexer),
    ('rexx', 'rex', 'rx', 'arexx', RexxLexer),
    ('moo', MOOCodeLexer),
    ('lua', 'wlua', LuaLexer),
    ('lsl', LSLLexer),
    ('ezt', 'mac', EasytrieveLexer),
    ('hy', 'hyb', HybrisLexer),
    ('jcl', JclLexer),
    ('scd', 'scdoc', ScdocLexer),
    ('robot', RFLexer),
    ('fy', 'fancypack', FancyLexer),
    ('rs', RustLexer),
    ('sas', SASLexer),
    ('graph', RoboconfGraphLexer),
    ('instances', RoboconfInstancesLexer),
    ('rnc', RNCCLexer),
    ('red', 'reds', RedLexer),
    ('r', 'r3', 'reb', RebolLexer),
    ('ttl', TurtleLexer),
    ('shex', ShExCLexer),
    ('rq', 'sparql', SparqlLexer),
    ('Rout', RConsoleLexer),
    ('Rd', RdLexer),
    ('s', 'r', 'rhistory', 'rprofile', 'renviron', SLexer),
    ('qvto', QVToLexer),
    ('dg', DgLexer),
    ('p', 'pwn', 'inc', PawnLexer),
    ('sp', SourcePawnLexer),
    ('pony', PonyLexer),
    ('praat', 'proc', 'psc', PraatLexer),
    ('lgt', 'logtalk', LogtalkLexer),
    ('ecl', 'prolog', 'pro', 'pl', PrologLexer),
    ('psi', 'psl', ParaSailLexer),
    ('treetop', 'tt', TreetopLexer),
    ('adb', 'ads', 'ada', AdaLexer),
    ('pas', 'dpr', DelphiLexer),
    ('ooc', OocLexer),
    ('x', 'xi', 'xm', 'xmi', LogosLexer),
    ('cp', 'cps', CPascalLexer),
    ('nix', NixLexer),
    ('nim', 'nimrod', NimrodLexer),
    ('nit', NitLexer),
    ('ncl', NCLLexer),
    ('bug', BugsLexer),
    ('jag', JagsLexer),
    ('mo', ModelicaLexer),
    ('stan', StanLexer),
    ('mt', MonteLexer),
    ('sci', 'sce', 'tst', ScilabLexer),
    ('ml', 'mli', 'mll', 'mly', OcamlLexer),
    ('opa', OpaLexer),
    ('sml', 'sig', 'fun', SMLLexer),
    ('xtm', XtlangLexer),
    ('cmake', CMakeLexer),
    ('mak', 'mk', MakefileLexer),
    ('man', '[1234567]', GroffLexer),
    ('rst', 'rest', RstLexer),
    ('shen', ShenLexer),
    ('lsp', 'nl', 'kif', NewLispLexer),
    ('rkt', 'rktd', 'rktl', RacketLexer),
    ('scm', 'ss', SchemeLexer),
    ('cl', 'lisp', CommonLispLexer),
    ('el', EmacsLispLexer),
    ('fnl', FennelLexer),
    ('cpsa', CPSALexer),
    ('xtend', XtendLexer),
    ('scala', ScalaLexer),
    ('sarl', SarlLexer), 
    ('pig', PigLexer),
    ('j', JasminLexer),
    ('ik', IokeLexer),
    ('aj', AspectJLexer),
    ('ceylon', CeylonLexer),
    ('clj', ClojureLexer),
    ('cljs', ClojureScriptLexer),
    ('golo', GoloLexer),
    ('io', IoLexer),
    ('b', LimboLexer),
    ('ipf', IgorLexer),
    ('pro', IDLLexer),
    ('scaml', ScamlLexer),
    ('v', VerilogLexer),
    ('sv', 'svh', SystemVerilogLexer),
    ('vhdl', 'vhd', VhdlLexer),
    ('hx', 'hxsl', HaxeLexer),
    ('hxml', HxmlLexer),
    ('kk', 'kki', KokaLexer),
    ('agda', AgdaLexer),
    ('lagda', LiterateAgdaLexer),
    ('cry', CryptolLexer),
    ('lcry', LiterateCryptolLexer),
    ('hs', HaskellLexer),
    ('lhs', LiterateHaskellLexer),
    ('idr', IdrisLexer),
    ('lidr', LiterateIdrisLexer),
    ('cyp', 'cypher', CypherLexer),
    ('pov', 'inc', PovrayLexer),
    ('flx', 'flxh', FelixLexer),
    ('flo', FloScriptLexer),
    ('frt', 'fs', ForthLexer),
    ('f', FortranFixedLexer),
    ('f03', 'f90', FortranLexer),
    ('abnf', AbnfLexer),
    ('bnf', BnfLexer),
    ('jsgf', JsgfLexer),
    ('fan', FantomLexer),
    ('factor', FactorLexer),
    ('ex', 'exs', ElixirLexer),
    ('erl', 'hrl', 'es', 'escript', ErlangLexer),
    ('e', EiffelLexer),
    ('ecl', ECLLexer),
    ('elm', ElmLexer),
    ('dylan', 'dyl', 'intr', DylanLexer),
    ('lid', 'hdp', DylanLidLexer),
    ('thrift', ThriftLexer),
    ('zeek', 'bro', ZeekLexer),
    ('sbl', SnowballLexer),
    ('rsl', RslLexer),
    ('proto', ProtoBufLexer),
    ('pp', PuppetLexer),
    ('boo', BooLexer),
    ('als', AlloyLexer),
    ('pan', PanLexer),
    ('wdiff', WDiffLexer),
    ('jsonld', JsonLdLexer),
    ('smali', SmaliLexer),
    ('pypylog', PyPyLogLexer),
    ('cr', CrystalLexer),
    ('croc', CrocLexer),
    ('d', 'di', DLexer),
    ('tf', TerraformLexer),
    ('toml', TOMLLexer),
    ('aug', AugeasLexer),
    ('cf', Cfengine3Lexer),
    ('docker', DockerLexer),
    ('capnp', CapnProtoLexer),
    ('chpl', ChapelLexer),
    ('icl', 'dcl', CleanLexer),
    ('pike', 'pmod', PikeLexer),
    ('swg', 'i', SwigLexer),
    ('vala', 'vapi', ValaLexer),
    ('boa', BoaLexer),
    ('abap', ABAPLexer),
    ('cbl', CobolFreeformatLexer),
    ('cob', 'cpy', CobolLexer),
    ('gdc', GoodDataCLLexer),
    ('maql', MaqlLexer),
    ('ci', CharmciLexer),
    ('clay', ClayLexer),
    ('cu', 'cuh', CudaLexer),
    ('ec', 'eh', ECLexer),
    ('bbc', BBCBasicLexer),
    ('bb', 'decls', BlitzBasicLexer),
    ('bmx', BlitzMaxLexer),
    ('monkey', MonkeyLexer),
    ('bas', QBasicLexer),
    ('bst', BSTLexer),
    ('apl', APLLexer),
    ('adl', 'adls', 'adlf', 'adlx', AdlLexer),
    ('cadl', CadlLexer),
    ('odin', OdinLexer),
    ('dasm', 'dasm16', Dasm16Lexer),
    ('hsail', HsailLexer),
    ('ll', LlvmLexer),
    ('asm', NasmLexer),
    ('tasm', TasmLexer),
    ('au3', AutoItLexer),
    ('ahk', 'ahkl', AutohotkeyLexer),
    ('at', AmbientTalkLexer),
    ('mu', MuPADLexer),
    ('sql', MySqlLexer),
    ('cs', CSharpLexer),
    ("diff", "patch", DiffLexer),
    ("sh", "cmd", "bashrc", "bash_profile", BashLexer),
    ("conf", "cnf", "config", ApacheConfLexer),
    ("ini", "init", IniLexer),
    ("rb", "rbw", "rake", "rbx", "duby", "gemspec", RubyLexer),
    ("pl", "pm", "nqp", "p6", "6pl", "p6l", "pl6", "6pm", "p6m", "pm6", "t", Perl6Lexer),
    ("php", "php5", HtmlPhpLexer),
    ("xml", "rss", "xsd", "wsdl", "wsf", XmlLexer),
    ("htm", "html", "xhtml", "phtml", HtmlPhpLexer),
    ("txt", "README", "text", TextLexer),
    ("py", "pyw", "sc", "sage", "tac", "pyf", "pycl", "pyc", "pyprog", PythonLexer),
    ("java", JavaLexer),
    ("kt", KotlinLexer),
    ("md", MarkdownLexer),
    ("tex", "aux", "toc", TexLexer),
    ("bib", BibTeXLexer),
    ("vbs", "VBS", VBScriptLexer),
    ("c", "h", "idc", CLexer),
    ('cpp', 'hpp', 'c++', 'h++', 'cc', 'hh', 'cxx', 'hxx', 'C', 'H', 'cp', 'CPP', CppLexer),
    ('ino', ArduinoLexer),
    ('as', ActionScript3Lexer),
    ('mxml', MxmlLexer),
    ('nb', 'cdf', 'nbp', 'ma', MathematicaLexer),
    ('css', CssLexer),
    ('less', LessCssLexer),
    ('sass', SassLexer),
    ('scss', ScssLexer),
    ('json', JsonLexer),
    ('yaml', 'yml', YamlLexer),
    ('fs', 'fsi', FSharpLexer),
    ('vb', 'bas', VbNetLexer),
    ('eml', EmailLexer),
    ('bf', 'b', BfLexer),
    ('go', GoLexer),
    ('ps', 'eps', PostScriptLexer),
    ('dtd', DtdLexer),
    ('haml', HamlLexer),
    ('pug', 'jade', PugLexer),
    ('ijs', JLexer),
    ('coffee', CoffeeScriptLexer),
    ('dart', DartLexer),
    ('eg', EarlGreyLexer),
    ('js', 'jsm', JavascriptLexer),
    ('juttle', JuttleLexer),
    ('kal', KalLexer),
    ('lasso', 'lasso[89]', LassoLexer),
    ('ls', LiveScriptLexer),
    ('mask', MaskLexer),
    ('j', ObjectiveJLexer),
    ('ts', 'tsx', TypeScriptLexer),
    ('jl', JuliaLexer),
    ('m', ObjectiveCLexer),
    ('mm', ObjectiveCppLexer),
    ('swift', SwiftLexer),
    ('zep', ZephirLexer),
    ('pyx', 'pyd', 'pxi', CythonLexer),
    ('applescript', AppleScriptLexer),
    ('chai', ChaiscriptLexer),
    ('moon', MoonScriptLexer)
)[::-1]


class IPyText(object):
    """Python highlighter mixin"""

    def __init__(self, baseclass, widget, text=''):
        self.baseclass = baseclass
        self.widget = widget
        self._widgetkeys = ('text',)
        self.baseclass.delete(self, '1.0', END)  # initial text
        self.baseclass.insert(self, END, text)
        self.bind("<KeyRelease>", self._update)
        #self.config(font='Courier 14', tabs=40)
        self.font_family, self.font_size = self.widget.family, self.widget.size
        self._config_tags()
        self._update()  # first time

    def _config_tags(self):
        self.tag_configure("Token.Comment.Single", foreground="#aaaaaa") #grey
        self.tag_configure("Token.Comment.Multiline", foreground="#aaaaaa") #grey
        self.tag_configure("Token.Comment.Preproc", foreground='#42a5f5') #blue
        self.tag_configure("Token,Comment.Special", foreground='#ee2400') #red
        self.tag_configure("Token.Comment.Hashbang", foreground="#aaaaaa") #grey
        self.tag_configure("Token.Keyword", foreground='#ee2400') #red
        self.tag_configure("Token.Keyword.Constant", foreground='#42a5f5') #blue
        self.tag_configure("Token.Keyword.Declaration", foreground='#42a5f5') #blue
        self.tag_configure("Token.Keyword.Namespace", foreground='#ee2400') #red
        self.tag_configure("Token.Name", foreground='#444444') #blue
        self.tag_configure("Token.Name.Builtin", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Class", foreground='#7f00ff') #violet
        self.tag_configure("Token.Name.Function", foreground='#7f50af') #violet
        self.tag_configure("Token.Name.Function.Magic", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Variable.Magic", foreground='#42a5f5') #blue
        self.tag_configure("Token.Literal.String.Affix", foreground='#ee2400') #red
        self.tag_configure("Token.Literal.String.Escape", foreground='#7f00ff') #red
        self.tag_configure("Token.Literal.String", foreground='#008000') #green
        self.tag_configure("Token.Operator", foreground='#ee2400') #red
        self.tag_configure("Token.Operator.Word", foreground='#ee2400') #red
        self.tag_configure("Token.Punctuation", foreground='#888888') #dark grey
        self.tag_configure("Token.Name.Tag", foreground='#ee2400') #red
        self.tag_configure("Token.Name.Variable", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Variable.Class", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Variable.Global", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Variable.Instance", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Label", foreground='#ee2400') #red
        self.tag_configure("Token.Name.Builtin.Pseudo", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Constant", foreground='#42a5f5') #blue
        self.tag_configure("Token.Name.Entity", foreground='#7f00ff') #violet
        self.tag_configure("Token.Name.Exception", foreground='#ee2400') #red
        self.tag_configure("Token.Name.Decorator", foreground='#7f00ff') #violet
        self.tag_configure("Token.Name.Attribute", foreground='#ff8c00') #orange
        self.tag_configure("Token.Name.Namespace", foreground='#42a5f5') #blue
        self.tag_configure("Token.Keyword.Pseudo", foreground='#7f00ff') #violet
        self.tag_configure("Token.Keyword.Reserved", foreground='#ee2400') #red
        self.tag_configure("Token.Keyword.Type", foreground='#42a5f5') #blue
        
        # Numbers
        for suffix in ("Float", "Bin", "Hex", "Integer", "Integer.Long", "Oct"):
            tag = "Token.Literal.Number.%s" % suffix
            self.tag_configure(tag, foreground='#42a5f5')
        # Strings
        
        for suffix in ('Single', 'Double', 'Char', 'Doc', 'Other', 'Backtick', 'Symbol', 'Interpol', 'Regex', "Heredoc", "Delimeter"):
            tag = "Token.Literal.String.%s" % suffix
            self.tag_configure(tag, foreground='#008000') #blue

    def _update(self, *event):
        self._config_tags()
        if not havePygments:
            return
        self.mark_set("range_start", "1.0")
        data = self.get("1.0", "end-1c")
        for token, content in lex(data, self.widget.lexer()):
            self.mark_set("range_end", "range_start + %dc" % len(content))
            self.tag_add(str(token), "range_start", "range_end")
            self.mark_set("range_start", "range_end")

    def __setitem__(self, key, val):
        if key in self._widgetkeys:
            self.__setattr__('_' + key, val)
            if key == 'text':
                if not val:
                    val = ''
                self.baseclass.delete(self, '1.0', END)
                self.baseclass.insert(self, END, val)
            self._update()
        else:
            self.baseclass.__setitem__(self, key, val)

    def __getitem__(self, key):
        if key in self._widgetkeys:
            if key == 'text':
                return self.baseclass.get(self, '1.0', END)
            return getattr(self, '_' + key)
        else:
            return self.baseclass.__getitem__(self, key)

    def config(self, **kw):
        """Standard Tk config method"""
        for key in kw:
            if key == 'text':
                self.baseclass.delete(self, '1.0', END)
                self.baseclass.insert(self, END, kw[key])
                kw.pop(key, False)
            elif key in self._widgetkeys:
                self.__setattr__('_' + key, kw[key])
                kw.pop(key, False)
        self._update()
        self.baseclass.config(self, **kw)
