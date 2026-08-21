# Lab 9 — Object Properties and Layers

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 04:** Organizing Objects

**Objective:** LO3/LO4 — organise a drawing with layers and properties (A4, K4)

## Goal

Create a standards-based layer scheme in lab-table-lesson2.dwg, then audit the supplied office-plan-ground-floor.dwg to see how a larger architectural drawing separates systems.

## You'll produce

A layered table drawing where every object is ByLayer, plus a five-layer audit of the office plan covering naming, colour, linetype, lineweight and plot state.

**Commands / tools:** LAYER (LA), Properties palette (PR), Layer Walk, MATCHPROP, freeze/thaw, lock

## Files in this lab

- `lab-table-lesson2.dwg` — AutoCAD drawing file
- `office-plan-ground-floor.dwg` — AutoCAD drawing file

## Step-by-step

1. Open lab-table-lesson2.dwg and inspect current object properties

   ```
   PR (Properties palette)
   ```

2. Create layers: A-OUTLINE, A-HIDDEN, A-CENTRE, A-DIMS, A-TEXT with colours and linetypes

   ```
   LA → New Layer → colour/linetype
   ```

3. Load the HIDDEN and CENTER linetypes and set lineweights per layer

   ```
   LA → Linetype → Load → HIDDEN, CENTER
   ```

4. Select objects by type and move them to their layers; copy formatting with MATCHPROP

   ```
   select → Layer drop-down  ·  MA
   ```

5. Practise layer states: turn off, freeze/thaw, lock and Layer Walk through the scheme

   ```
   LAYWALK · LAYFRZ · LAYLCK
   ```

6. Set every object's colour, linetype and lineweight to ByLayer and save

   ```
   SETBYLAYER → SAVEAS table-layers.dwg
   ```

7. Open office-plan-ground-floor.dwg and audit five functional layers against the same rules

   ```
   OPEN office-plan-ground-floor.dwg → LA → record name/colour/linetype/lineweight/plot
   ```

## Check your work

Turning each layer off hides exactly its objects, everything in table-layers.dwg reports ByLayer, and the office-plan audit identifies five layers with their intended functions.
