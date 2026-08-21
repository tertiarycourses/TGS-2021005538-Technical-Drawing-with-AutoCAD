# Lab 15 — Hatching and Detail Finishing

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 05:** Design Documentation

**Objective:** LO5 — produce design specification using AutoCAD (A5, K5)

## Goal

Apply section hatching with controlled boundaries and islands, then compare two supplied landscaping revisions and mark the changed area with a revision cloud and note.

## You'll produce

A correctly hatched section view plus a documented landscaping revision showing the changed geometry, revision cloud and concise change note.

**Commands / tools:** HATCH, gradient fills, boundary/island detection, HATCHEDIT, DWG Compare, REVCLOUD, MLEADER

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

7. Compare landscaping-rev1.dwg with landscaping-rev2.dwg and isolate the changed geometry

   ```
   COMPARE → landscaping-rev2.dwg
   ```

8. Cloud the change and add a concise multileader note before saving the review copy

   ```
   REVCLOUD → MLEADER → SAVEAS landscaping-review.dwg
   ```

## Check your work

Hatches do not bleed, adjacent parts use distinct angles, islands remain clear, and the landscaping review identifies every revision with one cloud and one readable note.
