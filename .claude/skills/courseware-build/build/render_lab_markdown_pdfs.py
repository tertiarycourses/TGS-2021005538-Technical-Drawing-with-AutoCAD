#!/usr/bin/env python3
"""Render lab Markdown PDFs with course-specific pagination safeguards.

The shared courseware renderer supplies the visual design. This wrapper keeps
headings with their first paragraph and numbered actions with their command
panel so a page boundary cannot separate an instruction from its evidence.
"""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path


def load_shared_renderer():
    configured = os.environ.get("COURSEWARE_MARKDOWN_RENDERER")
    source = Path(configured).expanduser() if configured else (
        Path.home()
        / ".agents/skills/courseware-build/scripts/render_activity_markdown_pdfs.py"
    )
    if not source.is_file():
        raise SystemExit(
            "Shared Markdown PDF renderer not found. Set "
            "COURSEWARE_MARKDOWN_RENDERER to render_activity_markdown_pdfs.py."
        )
    spec = importlib.util.spec_from_file_location("courseware_markdown_renderer", source)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot load shared renderer: {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


renderer = load_shared_renderer()
shared_styles = renderer.styles


def pagination_safe_styles():
    styles = shared_styles()
    for name in ("h2", "h3", "h4", "number"):
        styles[name].keepWithNext = 1
    return styles


renderer.styles = pagination_safe_styles


if __name__ == "__main__":
    raise SystemExit(renderer.main())
