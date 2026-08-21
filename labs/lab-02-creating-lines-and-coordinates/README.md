# Lab 2 — Creating Lines and Coordinates

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 02:** Technical Drawing with AutoCAD

**Objective:** LO2 — produce 2D technical drawings using AutoCAD (A2, K2)

## Goal

Draw the outline of practice drawing EX-1 using the LINE and PLINE commands with absolute, relative and polar coordinate entry, working from its dimensioned drawing sheet.

## You'll produce

The completed EX-1 profile drawn to size, matching the supplied solution DWG.

**Commands / tools:** LINE, PLINE, coordinate entry (@dx,dy · @dist<angle), ORTHO, dynamic input

## Files in this lab

- `ex1.dwg` — AutoCAD drawing file
- `ex1-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex1.png` — reference image

## Step-by-step

1. Open the EX-1 drawing sheet (ex1-drawing-sheet.pdf) and study the dimensions

2. Start a new acadiso drawing and draw the first edge with absolute coordinates

   ```
   L → 0,0 → 100,0
   ```

3. Continue the profile with relative coordinates for each dimensioned edge

   ```
   @0,50  ·  @-30,0  ·  @20<135
   ```

4. Use ortho (F8) and polar tracking (F10) for the horizontal and vertical segments

   ```
   F8 · F10
   ```

5. Close the profile back to the start point and check it forms one closed loop

   ```
   C (Close)
   ```

6. Compare your result against the solution file ex1.dwg, then save

   ```
   OPEN ex1.dwg → SAVEAS ex1-mine.dwg
   ```

## Check your work

Your outline closes exactly (LIST shows the final vertex at 0,0) and overlays the solution ex1.dwg with no visible deviation.
