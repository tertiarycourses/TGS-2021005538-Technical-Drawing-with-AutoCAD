# Lab 9 — Object Properties and Layers

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 04:** Organizing Objects

**Objective:** LO3/LO4 — organise a drawing with layers and properties (A4, K4)

## Goal

Open the furniture drawing lab-table-lesson2.dwg, create a layer scheme (outline, hidden, centre, dimensions, text), assign colours/linetypes/lineweights ByLayer, and move the existing objects onto the correct layers.

## You'll produce

A layered version of the table drawing where every object's colour and linetype come ByLayer.

**Commands / tools:** LAYER (LA), Properties palette (PR), Layer Walk, MATCHPROP, freeze/thaw, lock

## Files in this lab

- `lab-table-lesson2.dwg` — AutoCAD drawing file

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

## Check your work

Turning each layer off hides exactly its objects, everything reports ByLayer in the Properties palette, and Layer Walk steps cleanly through the scheme.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*