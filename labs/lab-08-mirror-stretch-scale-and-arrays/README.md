# Lab 8 — Mirror, Stretch, Scale and Arrays

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 03:** Modifying Objects

**Objective:** LO2/LO3 — reproduce patterned and symmetric geometry (A3, K3)

## Goal

Produce practice drawing EX-6 with mirror, stretch, scale and arrays, then inspect the supplied sawblade drawing to reverse-engineer a production polar-array pattern.

## You'll produce

The completed EX-6 drawing plus a verified sawblade polar array with the correct centre, item count, fill angle and associative state.

**Commands / tools:** MIRROR, STRETCH (crossing window), SCALE (Reference), ARRAYRECT, ARRAYPOLAR

## Files in this lab

- `ex6.dwg` — AutoCAD drawing file
- `ex6-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex6.png` — reference image
- `sawblade.dwg` — AutoCAD drawing file

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

4. Distribute the bolt holes around the centre with an associative polar array

   ```
   AR → PO → centre → items → 360 → Associative: Yes
   ```

5. Stretch the slot to its dimensioned length with a crossing window, scale a feature with Reference

   ```
   S → crossing → base → distance  ·  SC → R
   ```

6. Open sawblade.dwg, select its tooth array and record centre, item count, fill angle and associativity

   ```
   OPEN sawblade.dwg → select array → PR
   ```

7. Verify against ex6.dwg and save

   ```
   SAVEAS ex6-mine.dwg
   ```

## Check your work

The two halves are symmetric, array counts and spacings match the sheet, the slot length is correct, and you can explain the four defining properties of the sawblade polar array.
