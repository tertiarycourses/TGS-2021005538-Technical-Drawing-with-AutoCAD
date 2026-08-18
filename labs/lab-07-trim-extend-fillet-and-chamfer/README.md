# Lab 7 — Trim, Extend, Fillet and Chamfer

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 03:** Modifying Objects

**Objective:** LO2/LO3 — clean up and finish drawing geometry (A3, K3)

## Goal

Complete practice drawing EX-5 by trimming overlapping construction geometry, extending short edges to their boundaries, and finishing corners with fillets and chamfers.

## You'll produce

A clean EX-5 profile with every corner finished exactly as dimensioned on the sheet.

**Commands / tools:** TRIM (Quick/Standard), EXTEND, FILLET, CHAMFER, BREAK

## Files in this lab

- `ex5.dwg` — AutoCAD drawing file
- `ex5-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex5.png` — reference image

## Step-by-step

1. Open the EX-5 sheet (ex5-drawing-sheet.pdf) and rough out the profile with overlapping lines

2. Trim the overshoots in Quick mode — click or drag across the pieces to remove

   ```
   TR → click segments
   ```

3. Use Standard mode where you need explicit cutting edges: select boundaries, then objects

   ```
   TR → Enter (all edges) → pick
   ```

4. Extend the short edges to meet their boundary lines

   ```
   EX → pick edges to extend
   ```

5. Fillet the rounded corners at the sheet radius, and chamfer the bevelled ones

   ```
   F → R → 10 → pick 2 lines  ·  CHA → D → 5,5
   ```

6. Compare with ex5.dwg and save

   ```
   SAVEAS ex5-mine.dwg
   ```

## Check your work

No overshooting or dangling segments remain (zoom around the whole profile), and every fillet radius / chamfer distance matches the drawing sheet.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*