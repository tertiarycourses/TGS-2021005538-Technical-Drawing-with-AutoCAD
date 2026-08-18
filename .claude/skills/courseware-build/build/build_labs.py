#!/usr/bin/env python3
"""Generate the per-lab folders: labs/lab-NN-<slug>/ each containing
  README.md            — the Markdown instruction (single source: data_domainN.py)
  lab-NN-<slug>.docx   — formatted instruction sheet (converted to PDF by the orchestrator)
  *.dwg / *.pdf / *.png — the AutoCAD data files for that lab (copied from labs/_assets)
plus the labs/README.md index. Also removes any stale flat lab-*.md files.
"""
import os, sys, shutil, glob
from docx import Document
from docx.shared import Pt, RGBColor, Inches

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from labslug import lab_dirname
ACT = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs")
ASSETS = os.path.join(LABS, "_assets")
TOPICS = {t["num"]: t for t in C.TOPICS}

BRAND = RGBColor(0x1F, 0x6F, 0xEB); GREY = RGBColor(0x55, 0x5B, 0x66)

def write_md(act, folder, files):
    t = TOPICS[act["topic"]]
    L = []
    L.append(f"# Lab {act['num']} — {act['title']}")
    L.append("")
    L.append(f"**Course:** {C.TITLE} ({C.COURSE_CODE}) · **Topic {t['code']}:** {t['title']}")
    L.append("")
    L.append(f"**Objective:** {act['objective']}")
    L.append("")
    L.append("## Goal")
    L.append("")
    L.append(act["desc"])
    L.append("")
    L.append("## You'll produce")
    L.append("")
    L.append(act["build"])
    L.append("")
    L.append(f"**Commands / tools:** {act['services']}")
    L.append("")
    if files:
        L.append("## Files in this lab")
        L.append("")
        for f in files:
            note = {"dwg": "AutoCAD drawing file", "pdf": "drawing sheet / reference (PDF)",
                    "png": "reference image", "jpg": "reference image"}.get(f.rsplit(".", 1)[-1].lower(), "data file")
            L.append(f"- `{f}` — {note}")
        L.append("")
    L.append("## Step-by-step")
    L.append("")
    for i, (instr, cmd) in enumerate(act["steps"], 1):
        L.append(f"{i}. {instr}")
        if cmd:
            L.append("")
            L.append("   ```")
            L.append(f"   {cmd}")
            L.append("   ```")
        L.append("")
    L.append("## Check your work")
    L.append("")
    L.append(act["test"])
    L.append("")
    L.append("---")
    L.append(f"*© 2026 {C.ORG} ({C.UEN}) · {C.TITLE} · {C.COURSE_CODE}*")
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write("\n".join(L))

def write_docx(act, folder, files):
    t = TOPICS[act["topic"]]
    doc = Document()
    n = doc.styles["Normal"]; n.font.name = "Arial"; n.font.size = Pt(11)
    h = doc.add_heading(f"Lab {act['num']} — {act['title']}", level=0)
    for r in h.runs: r.font.color.rgb = BRAND
    p = doc.add_paragraph()
    r = p.add_run(f"{C.TITLE} ({C.COURSE_CODE})  ·  Topic {t['code']}: {t['title']}")
    r.font.size = Pt(10); r.font.color.rgb = GREY
    p = doc.add_paragraph(); r = p.add_run(f"{C.ORG}  ·  {C.UEN}  ·  Version {C.VERSION} · {C.VERSION_DATE}")
    r.font.size = Pt(9); r.font.color.rgb = GREY

    doc.add_heading("Objective", level=1); doc.add_paragraph(act["objective"])
    doc.add_heading("Goal", level=1); doc.add_paragraph(act["desc"])
    doc.add_heading("You'll produce", level=1)
    doc.add_paragraph(act["build"])
    p = doc.add_paragraph(); r = p.add_run("Commands / tools: "); r.bold = True
    p.add_run(act["services"])
    if files:
        doc.add_heading("Files in this lab", level=1)
        for f in files:
            doc.add_paragraph(f, style="List Bullet")
    doc.add_heading("Step-by-step", level=1)
    for i, (instr, cmd) in enumerate(act["steps"], 1):
        p = doc.add_paragraph(style="List Number"); p.add_run(instr)
        if cmd:
            cp = doc.add_paragraph(); r = cp.add_run("     " + cmd)
            r.font.name = "Consolas"; r.font.size = Pt(9.5); r.font.color.rgb = RGBColor(0x0B, 0x30, 0x60)
    doc.add_heading("Check your work", level=1)
    doc.add_paragraph(act["test"])
    p = doc.add_paragraph(); r = p.add_run(f"© 2026 {C.ORG} ({C.UEN})")
    r.font.size = Pt(8.5); r.font.color.rgb = GREY
    out = os.path.join(folder, f"lab-{act['num']:02d}-instructions.docx")
    doc.save(out)
    return out

# staged asset files for each lab (in labs/_assets)
FILES = {
    1:  ["lab01-table.dwg", "reading-practice.dwg", "workspaces.dwg", "drafting-settings.dwg"],
    2:  ["ex1.dwg", "ex1-drawing-sheet.pdf", "ex1.png"],
    3:  ["ex2.dwg", "ex2-drawing-sheet.pdf", "ex2.png"],
    4:  ["ex3.dwg", "ex3-drawing-sheet.pdf", "ex3.png"],
    5:  ["iso-object.dwg", "iso-object-sheet.pdf", "iso-object.png"],
    6:  ["ex4.dwg", "ex4-drawing-sheet.pdf", "ex4.png"],
    7:  ["ex5.dwg", "ex5-drawing-sheet.pdf", "ex5.png"],
    8:  ["ex6.dwg", "ex6-drawing-sheet.pdf", "ex6.png", "sawblade.dwg"],
    9:  ["lab-table-lesson2.dwg", "office-plan-ground-floor.dwg"],
    10: ["ex7.dwg", "ex7-drawing-sheet.pdf", "ex7.png", "new-office-design.dwg"],
    11: ["title-block.dwg", "architecture-library.dwg", "new-office-dynamic-blocks.dwg"],
    12: ["title-block.dwg", "ex1-drawing-sheet.pdf", "new-office-layout-with-xref.dwg"],
    13: ["lab-table-lesson2.dwg", "title-block.dwg"],
    14: ["ex8.dwg", "ex8-drawing-sheet.pdf", "ex8.png"],
    15: ["ex3.dwg", "ex3-drawing-sheet.pdf", "landscaping-rev1.dwg", "landscaping-rev2.dwg"],
    16: ["title-block.dwg", "new-office-layout.dwg"],
}

def main():
    # clear stale flat files/folders (keep _assets staging)
    for p in glob.glob(os.path.join(LABS, "lab-*")):
        if os.path.isdir(p): shutil.rmtree(p)
        else: os.remove(p)
    index = [f"# {C.TITLE} — Hands-On Labs", "",
             f"16 labs across the 5 course topics. Each lab folder contains the Markdown "
             f"instructions (README.md), a printable PDF instruction sheet, and the AutoCAD "
             f"DWG data files for that lab.", ""]
    for t in C.TOPICS:
        index.append(f"## Topic {t['code']} — {t['title']}")
        index.append("")
        for act in [a for a in ACT if a["topic"] == t["num"]]:
            d = lab_dirname(act)
            folder = os.path.join(LABS, d)
            os.makedirs(folder, exist_ok=True)
            files = FILES.get(act["num"], [])
            for f in files:
                src = os.path.join(ASSETS, f)
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(folder, f))
                else:
                    print("WARN missing asset:", f)
            write_md(act, folder, files)
            write_docx(act, folder, files)
            index.append(f"- [Lab {act['num']:02d} — {act['title']}]({d}/README.md)")
        index.append("")
    with open(os.path.join(LABS, "README.md"), "w") as f:
        f.write("\n".join(index))
    print(f"Built {len(ACT)} lab folders under labs/")

if __name__ == "__main__":
    main()
