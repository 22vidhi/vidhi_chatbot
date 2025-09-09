"""
RA Agent module for Regulatory Affairs Automation
Provides AI-powered document generation and compliance automation for pharmaceutical regulatory affairs.
"""

from .ra_core import RAAgent, RAQuery, ra_agent, DocumentManifest
from .ra_ui import display_ra_main
from .templates.csr_template import generate_csr_template

__all__ = [
    'RAAgent',
    'RAQuery',
    'ra_agent',
    'DocumentManifest',
    'display_ra_main',
    'generate_csr_template'
]

__version__ = "1.0.0"
