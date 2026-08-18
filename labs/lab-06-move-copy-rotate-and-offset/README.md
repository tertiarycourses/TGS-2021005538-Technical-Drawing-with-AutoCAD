# Lab 6 — Move, Copy, Rotate and Offset

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 03:** Modifying Objects

**Objective:** LO2/LO3 — modify 2D drawings efficiently to build up a design (A3, K3)

## Goal

Build practice drawing EX-4 by drawing one feature and then positioning the rest with MOVE, COPY (multiple), ROTATE with reference angle and OFFSET for the parallel profiles.

## You'll produce

The completed EX-4 drawing produced with modify commands rather than re-drawing each feature.

**Commands / tools:** MOVE, COPY (Multiple/Array), ROTATE (Reference), OFFSET

## Files in this lab

- `ex4.dwg` — AutoCAD drawing file
- `ex4-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex4.png` — reference image

## Step-by-step

1. Open the EX-4 sheet (ex4-drawing-sheet.pdf) and spot the repeated features

2. Draw the base profile, then offset it to create the parallel inner/outer edges

   ```
   O → distance → pick side
   ```

3. Draw one hole feature and copy it to every dimensioned centre

   ```
   CO → base point → second points
   ```

4. Move a mis-placed feature precisely from its centre to the correct intersection

   ```
   M → base → destination
   ```

5. Rotate the angled feature about its base point, using Reference to match the sheet angle

   ```
   RO → base → R → ref angle → new angle
   ```

6. Check against ex4.dwg and save your version

   ```
   SAVEAS ex4-mine.dwg
   ```

## Check your work

Feature spacings measure correct with DIST, offsets are at the specified distances, and the rotated feature sits at exactly the sheet's angle.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*