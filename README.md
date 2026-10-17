# WSQ Technical Drawing with AutoCAD

**Course Code:** TGS-2021005538
**Skills Framework TSC:** Technical Drawing (DSN-TDR-3005-1.11), Proficiency Level 3
**Provider:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)
**Register:** [WSQ Technical Drawing with AutoCAD](https://www.tertiarycourses.com.sg/wsq-technical-drawing-with-autocad.html)

| Course detail | Information |
|---|---|
| Course code | `TGS-2021005538` |
| Programme | WSQ (SkillsFuture Singapore) |
| Duration | 2 days, 16 hours (including 2-hour assessment) |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wsq-technical-drawing-with-autocad.html) |
| Funding | Up to 70% WSQ course fee funding for eligible learners (50% baseline for Singapore Citizens/PRs aged 21+; 70% for Singapore Citizens aged 40+ under MCES or SME-sponsored learners). Eligibility and terms apply - see the course page. |
| Provider | Tertiary Infotech Academy Pte Ltd |

A 2-day (16-hour) instructor-led WSQ course on producing professional technical drawings with Autodesk AutoCAD — from first drawing setup to a plotted, submission-ready sheet with dimensions, part lists and title blocks.

## Learning Outcomes

- **LO1** — Read and visualize AutoCAD technical drawings
- **LO2** — Produce 2D and 3D technical drawings using AutoCAD
- **LO3** — Create part lists using AutoCAD
- **LO4** — Create AutoCAD design documentation
- **LO5** — Produce design specification using AutoCAD

## Course Structure

| Topic | Title | TSC mapping | Labs |
|---|---|---|---|
| 01 | Getting Started with AutoCAD | A1 · K1 | Lab 1 |
| 02 | Technical Drawing with AutoCAD | A2 · K2 | Labs 2–5 |
| 03 | Modifying Objects | A3 · K3 | Labs 6–8 |
| 04 | Organizing Objects | A4 · K4 | Labs 9–12 |
| 05 | Design Documentation | A5 · K5 | Labs 13–16 |

Final assessment (Day 2): Written Assessment (SAQ, 60 min) + Practical Performance (90 min), open book.

## Repository Layout

```
courseware/                  Generated artifacts (single-source pipeline)
  WSQ Technical Drawing with AutoCAD-v13.pptx/.pdf   Concept-led slide deck (116 slides)
  LP-WSQ Technical Drawing with AutoCAD.docx/.pdf    Lesson Plan (2-day schedule)
  LG-WSQ Technical Drawing with AutoCAD.docx/.pdf    Learner Guide
LG-WSQ Technical Drawing with AutoCAD.md             Learner Guide (Markdown mirror)
labs/                        16 hands-on labs — one folder per lab:
  lab-01-… to lab-16-…         README.md + lab-NN-instructions.pdf + AutoCAD .dwg data files
  _assets/                     Shared staging copies of the lab data files
.claude/                     Courseware toolchain (skills, commands, build scripts)
```

## The 16 Hands-On Labs

Each lab folder contains the Markdown instructions (`README.md`), a printable PDF instruction sheet, and the AutoCAD DWG data files for that lab. See [labs/README.md](labs/README.md) for the full index.

1. Setting Up a New Drawing
2. Creating Lines and Coordinates
3. Circles, Rectangles and Polygons
4. Polylines, Arcs, Ellipses and Splines
5. 2D Isometric Drawing
6. Move, Copy, Rotate and Offset
7. Trim, Extend, Fillet and Chamfer
8. Mirror, Stretch, Scale and Arrays
9. Object Properties and Layers
10. Grips, Hide and Isolate
11. Blocks, Attributes and Part Lists
12. External References and PDF Import
13. Text and Text Styles
14. Dimensions, Multileaders and Part-List Tables
15. Hatching and Detail Finishing
16. Layouts, Viewports and Plotting

Lab drawing exercises adapt practice files from
[DCS-training/AutocadSelfLearn](https://github.com/DCS-training/AutocadSelfLearn),
[PacktPublishing/60-AutoCAD-2D-3D-Drawings-and-Practical-Projects](https://github.com/PacktPublishing/60-AutoCAD-2D-3D-Drawings-and-Practical-Projects),
[PacktPublishing/Mastering-AutoCAD](https://github.com/PacktPublishing/Mastering-AutoCAD) and
[RichaSavant/AutoCAD-2021](https://github.com/RichaSavant/AutoCAD-2021) under their respective licences.

The local `reference/` folder may contain additional trainer-owned or third-party source material.
It is reviewed for instructional ideas only and is never copied into the public learner package
unless redistribution rights are documented.

## Rebuilding the Courseware

All artifacts are generated from one content module (`course_data.py` + `data_domain1..5.py` + `data_concepts.py`) so the deck, Lesson Plan, Learner Guide and labs never drift apart:

```bash
bash .claude/skills/courseware-build/build/build_courseware.sh   # PPT + LP + LG (+ PDFs, TOC)
python3 .claude/skills/courseware-build/build/build_labs.py      # regenerate the 16 lab folders
python3 .claude/skills/courseware-build/build/render_lab_markdown_pdfs.py --root labs
                                                               # pagination-safe README PDFs
```

Requires Python 3 with `python-pptx`, `python-docx`, `Pillow`, and LibreOffice (`soffice`) for PDF rendering. The legacy-deck screenshot assets used by a rebuild live in the local (untracked) `reference/` folder.

## Requirements for Learners

- AutoCAD 2021 or later (free trial or education licence) on Windows or Mac
- A mouse with a scroll wheel
- The `labs/` folder of this repository

## Support

- Email: enquiry@tertiaryinfotech.com · Tel: +65 6100 0613
- LMS: https://lms-tms.tertiaryinfotech.com

---
© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). Course materials for enrolled learners and trainers.
