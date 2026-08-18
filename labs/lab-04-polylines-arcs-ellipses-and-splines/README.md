# Lab 4 — Polylines, Arcs, Ellipses and Splines

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 02:** Technical Drawing with AutoCAD

**Objective:** LO2 — produce 2D technical drawings using AutoCAD (A2, K2)

## Goal

Draw practice drawing EX-3 combining polylines with arc segments, standalone arcs, an ellipse and a spline, plus construction lines to project feature positions between views.

## You'll produce

The completed EX-3 drawing with mixed line/arc geometry drawn as clean, connected objects.

**Commands / tools:** PLINE (Arc mode), ARC, ELLIPSE, SPLINE, XLINE, POINT/DIVIDE

## Files in this lab

- `ex3.dwg` — AutoCAD drawing file
- `ex3-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex3.png` — reference image

## Step-by-step

1. Open the EX-3 sheet (ex3-drawing-sheet.pdf) and plan the outline as one polyline

2. Draw the outline with PLINE, switching between Line and Arc segments as you go

   ```
   PL → pick → A (arc) → L (line)
   ```

3. Place construction lines to project the centres of features between views

   ```
   XL → H / V through centres
   ```

4. Add a three-point arc and a centre-start-end arc where the sheet shows open curves

   ```
   A → 3 points  ·  A → C
   ```

5. Draw the ellipse from its axis endpoints and a smooth spline through the fit points

   ```
   EL → axis ends → half-width  ·  SPL
   ```

6. Compare with ex3.dwg, purge the construction lines and save

   ```
   ERASE xlines → SAVEAS ex3-mine.dwg
   ```

## Check your work

The outline is a single polyline (one object when selected), arcs and the ellipse match the sheet dimensions, and no construction lines remain in the final drawing.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*