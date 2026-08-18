"""Shared lab-folder naming: every artifact refers to labs/<lab_dirname(act)>/."""
import re

def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s

def lab_dirname(act):
    return f"lab-{act['num']:02d}-{slugify(act['title'])}"
