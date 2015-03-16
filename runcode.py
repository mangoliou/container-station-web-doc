from sphinx.directives import CodeBlock, Directive
import subprocess as sp
from sphinx.ext import autodoc
import os
import sys
from StringIO import StringIO
from docutils import nodes
from os.path import basename


class RuncodeDirective(CodeBlock):
    """Execute the specified python code and insert the output as codeblock
    """
    def run(self):
        cmd = self.content
        try:
            self.content = sp.check_output(' '.join(cmd), shell=True).split('\n')
        except:
            self.content = [u'Failed to run command', ' '.join(cmd)]
        return CodeBlock.run(self)


class ExecDirective(Directive):
    """Execute the specified python code and insert the output into the document"""
    has_content = True

    def run(self):
        oldStdout, sys.stdout = sys.stdout, StringIO()
        try:
            exec '\n'.join(self.content)
            return [nodes.paragraph(text = sys.stdout.getvalue())]
        except Exception:
            return [nodes.paragraph(text='error: ' + self.content)]
        finally:
            sys.stdout = oldStdout


class SimpleDocumenter(autodoc.FunctionDocumenter):
    """Document docstring only
    """
    objtype = "simple"

    # do not indent the content
    content_indent = ""

    # do not add a header to the docstring
    def add_directive_header(self, sig):
        pass


def setup(app):
    if os.environ.get('QIP') is None or len(os.environ.get('QIP')) == 0:
        os.environ['QIP'] = '127.0.0.1'
    if os.environ.get('QPORT') is None or len(os.environ.get('QPORT')) == 0:
        os.environ['QPORT'] = '9000'
    app.add_directive('runcode', RuncodeDirective)
    app.add_directive('exec', ExecDirective)
    app.add_autodocumenter(SimpleDocumenter)
