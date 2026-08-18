# Lab 15 — Hatching and Detail Finishing

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 05:** Design Documentation

**Objective:** LO5 — produce design specification using AutoCAD (A5, K5)

## Goal

Apply section hatching to the closed areas of a section view — pattern, scale and angle — use gradient fills for presentation, and control hatch boundaries and islands.

## You'll produce

A section view with correct ANSI/ISO hatch patterns and a presentation-filled elevation.

**Commands / tools:** HATCH (pattern/scale/angle), gradient fills, boundary/island detection, HATCHEDIT

## Files in this lab

- `ex3.dwg` — AutoCAD drawing file
- `ex3-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `landscaping-rev1.dwg` — AutoCAD drawing file
- `landscaping-rev2.dwg` — AutoCAD drawing file

## Step-by-step

1. Open a drawing with closed profiles (reuse ex3-mine.dwg) and identify the cut areas

2. Hatch the main section area with ANSI31 at a scale that reads clearly

   ```
   H → Pattern ANSI31 → pick point
   ```

3. Set different angles for adjacent parts so the section reads unambiguously

   ```
   H → Angle 90 → pick point
   ```

4. Control islands: hatch around text and holes using island detection

   ```
   H → Settings → Island detection
   ```

5. Apply a two-colour gradient fill to the elevation face for presentation

   ```
   GRADIENT → colours → pick area
   ```

6. Edit an existing hatch's pattern and scale, then save

   ```
   HATCHEDIT → new scale
   ```

## Check your work

Hatches stay inside their boundaries (no bleed), adjacent parts hatch at different angles, and text/holes remain unhatched islands.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*