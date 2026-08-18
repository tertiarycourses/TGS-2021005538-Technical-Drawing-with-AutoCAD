# Lab 5 — 2D Isometric Drawing

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 02:** Technical Drawing with AutoCAD

**Objective:** LO2 — produce 2D and 3D technical drawings using AutoCAD (A2, K2)

## Goal

Use ISODRAFT to create a 2D isometric representation of the 3D object supplied in iso-object.dwg, switching isoplanes and drawing isocircles for the round features.

## You'll produce

A flat isometric drawing of the 3D object — edges on the three isoplanes plus isocircle holes.

**Commands / tools:** ISODRAFT, isoplanes (F5), ELLIPSE Isocircle, polar tracking

## Files in this lab

- `iso-object.dwg` — AutoCAD drawing file
- `iso-object-sheet.pdf` — drawing sheet / reference (PDF)
- `iso-object.png` — reference image

## Step-by-step

1. Open the object sheet iso-object-sheet.pdf and identify its three faces

2. Turn on isometric drafting from the status bar and set the Top isoplane

   ```
   ISODRAFT → Isoplane Top (F5)
   ```

3. Draw the top face edges along the 30°/150° isometric axes with polar tracking

   ```
   L with polar 30°/150°
   ```

4. Switch to the Right and Left isoplanes and complete the vertical faces

   ```
   F5 → Right · F5 → Left
   ```

5. Add the round features as isocircles on the correct isoplane

   ```
   EL → I (Isocircle) → centre → radius
   ```

6. Compare your isometric with the 3D model in iso-object.dwg and save

   ```
   SAVEAS iso-mine.dwg
   ```

## Check your work

Each face lies on the correct isoplane (edges at 30°/90°/150°), the isocircles read as ellipses aligned to their faces, and the drawing matches the supplied object's proportions.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*