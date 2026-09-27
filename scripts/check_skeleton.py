#!/usr/bin/env python3
"""Check that required skeleton paths exist. Stdlib only."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'rules/AGENTS.md',
    'rules/ARCHITECTURE.md',
    'rules/SOURCE_POLICY.md',
    'rules/NAMING.md',
    'rules/CONTRIBUTING.md',
    'caps/skills/router/SKILL.md',
    'caps/skills/retro/SKILL.md',
    'caps/skills/audit/SKILL.md',
    'kernel/README.md',
    'layers/action/README.md',
    'layers/context/README.md',
    'layers/orchestration/README.md',
    'caps/hooks/README.md',
    'caps/tools/README.md',
    'caps/plugins/README.md',
    'models/providers/README.md',
    'protocols/mcp/README.md',
    'interop/README.md',
    'evals/README.md',
    'observability/README.md',
    'governance/README.md',
    'sandbox/README.md',
    'src/kernel/protocols.py',
    'src/shared/types/mahea.d.ts',
    'docs/AUDIT.md',
    'docs/harness-fusion.md',
    'docs/future-trends.md',
    'stock/README.md',
    'stock/INDEX.md',
]

FORBIDDEN = ['template']


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    present_forbidden = [p for p in FORBIDDEN if (ROOT / p).exists()]
    if missing:
        print('MISSING:')
        for p in missing:
            print(' ', p)
    if present_forbidden:
        print('FORBIDDEN_PRESENT:')
        for p in present_forbidden:
            print(' ', p)
    if missing or present_forbidden:
        return 1
    print('OK: skeleton paths look good')
    return 0


if __name__ == '__main__':
    sys.exit(main())
