# Lab 3 — Circles, Rectangles and Polygons

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 02:** Technical Drawing with AutoCAD

**Objective:** LO2 — produce 2D technical drawings using AutoCAD (A2, K2)

## Goal

Complete practice drawing EX-2 by adding circles (centre-radius, diameter, 2P/3P and Tan-Tan-Radius), a rectangle with chamfered/filleted corners and inscribed/circumscribed polygons.

## You'll produce

The completed EX-2 drawing with all holes, rectangles and polygons placed to the sheet dimensions.

**Commands / tools:** CIRCLE (Cen-Rad, 2P, 3P, TTR), RECTANG, POLYGON, object snaps

## Files in this lab

- `ex2.dwg` — AutoCAD drawing file
- `ex2-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex2.png` — reference image

## Step-by-step

1. Open the EX-2 sheet (ex2-drawing-sheet.pdf) and identify each hole's centre

2. Draw the main circles by centre point and radius, snapping to intersections

   ```
   C → cen point → 25
   ```

3. Add a circle by diameter and one through two points on existing geometry

   ```
   C → D → 40  ·  C → 2P
   ```

4. Draw a tangent-tangent-radius circle touching two existing circles

   ```
   C → TTR → pick 2 tangents → radius
   ```

5. Create the rectangle feature, then a hexagon inscribed in a 30-radius circle

   ```
   REC → corner → @80,50  ·  POL → 6 → I → 30
   ```

6. Verify against the solution ex2.dwg and save your drawing

   ```
   SAVEAS ex2-mine.dwg
   ```

## Check your work

Every circle's centre and radius match the sheet (use LIST), the hexagon has 6 equal sides, and your drawing overlays ex2.dwg cleanly.
