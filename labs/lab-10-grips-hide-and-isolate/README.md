# Lab 10 — Grips, Hide and Isolate

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 04:** Organizing Objects

**Objective:** LO3/LO4 — edit and manage drawing objects directly (A4, K4)

## Goal

Use multi-functional grips on EX-7, then practise isolate, hide, select-similar and end-isolate in the denser new-office-design.dwg without losing or deleting objects.

## You'll produce

An edited EX-7 layout plus a saved office-plan view in which the targeted object class was isolated, edited and fully restored.

**Commands / tools:** Multi-functional grips, grip modes (Enter to cycle), Isolate/Hide Objects, Select Similar

## Files in this lab

- `ex7.dwg` — AutoCAD drawing file
- `ex7-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex7.png` — reference image
- `new-office-design.dwg` — AutoCAD drawing file

## Step-by-step

1. Open ex7.dwg, click an object and hover its grips to see the grip menu

2. Stretch an endpoint grip to lengthen an edge; use the midpoint grip to move the object

   ```
   click grip → drag / type distance
   ```

3. Cycle grip modes with Enter: Stretch → Move → Rotate → Scale → Mirror

   ```
   select grip → Enter to cycle
   ```

4. Copy a feature by grip-moving with the Copy option (or Ctrl held)

   ```
   grip → Move → C (Copy)
   ```

5. Open new-office-design.dwg, select one furniture object and use Select Similar

   ```
   OPEN new-office-design.dwg → select → right-click → Select Similar
   ```

6. Isolate the selection, make one grip edit, hide a second class, then restore everything

   ```
   ISOLATEOBJECTS · HIDEOBJECTS · UNISOLATEOBJECTS
   ```

## Check your work

You can stretch, move, rotate and copy with grips alone; after UNISOLATEOBJECTS, the office drawing's object count and layer visibility match the starting state except for your saved edit.
