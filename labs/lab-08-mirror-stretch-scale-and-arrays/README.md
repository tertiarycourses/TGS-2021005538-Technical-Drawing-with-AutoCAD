# Lab 8 — Mirror, Stretch, Scale and Arrays

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 03:** Modifying Objects

**Objective:** LO2/LO3 — reproduce patterned and symmetric geometry (A3, K3)

## Goal

Produce practice drawing EX-6 by drawing half of the symmetric design and mirroring it, then distributing the hole pattern with rectangular and polar arrays, and adjusting sizes with STRETCH and SCALE.

## You'll produce

The completed EX-6 drawing with its symmetric outline and evenly arrayed hole pattern.

**Commands / tools:** MIRROR, STRETCH (crossing window), SCALE (Reference), ARRAYRECT, ARRAYPOLAR

## Files in this lab

- `ex6.dwg` — AutoCAD drawing file
- `ex6-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex6.png` — reference image

## Step-by-step

1. Open the EX-6 sheet (ex6-drawing-sheet.pdf) and find its axis of symmetry

2. Draw one half of the outline, then mirror it across the centreline

   ```
   MI → select → axis pt1 → pt2 → N
   ```

3. Array one hole into the rectangular pattern (rows, columns, spacing from the sheet)

   ```
   AR → R → rows/cols/spacing
   ```

4. Distribute the bolt holes around the centre with a polar array

   ```
   AR → PO → centre → items → 360
   ```

5. Stretch the slot to its dimensioned length with a crossing window, scale a feature with Reference

   ```
   S → crossing → base → distance  ·  SC → R
   ```

6. Verify against ex6.dwg and save

   ```
   SAVEAS ex6-mine.dwg
   ```

## Check your work

The two halves are perfectly symmetric about the centreline, array counts and spacings match the sheet, and the stretched slot measures the dimensioned length.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*