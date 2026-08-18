"""Topic 4 — Organizing Objects (A4, K4): hands-on activities."""

DOMAIN4 = [
    dict(
        num=9, topic=4,
        title="Object Properties and Layers",
        objective="LO3/LO4 — organise a drawing with layers and properties (A4, K4)",
        desc="Open the furniture drawing lab-table-lesson2.dwg, create a layer scheme "
             "(outline, hidden, centre, dimensions, text), assign colours/linetypes/lineweights ByLayer, "
             "and move the existing objects onto the correct layers.",
        build="A layered version of the table drawing where every object's colour and linetype come ByLayer.",
        services="LAYER (LA), Properties palette (PR), Layer Walk, MATCHPROP, freeze/thaw, lock",
        dwg="lab-table-lesson2.dwg",
        steps=[
            ("Open lab-table-lesson2.dwg and inspect current object properties", "PR (Properties palette)"),
            ("Create layers: A-OUTLINE, A-HIDDEN, A-CENTRE, A-DIMS, A-TEXT with colours and linetypes", "LA → New Layer → colour/linetype"),
            ("Load the HIDDEN and CENTER linetypes and set lineweights per layer", "LA → Linetype → Load → HIDDEN, CENTER"),
            ("Select objects by type and move them to their layers; copy formatting with MATCHPROP", "select → Layer drop-down  ·  MA"),
            ("Practise layer states: turn off, freeze/thaw, lock and Layer Walk through the scheme", "LAYWALK · LAYFRZ · LAYLCK"),
            ("Set every object's colour, linetype and lineweight to ByLayer and save", "SETBYLAYER → SAVEAS table-layers.dwg"),
        ],
        test="Turning each layer off hides exactly its objects, everything reports ByLayer in the "
             "Properties palette, and Layer Walk steps cleanly through the scheme.",
    ),
    dict(
        num=10, topic=4,
        title="Grips, Hide and Isolate",
        objective="LO3/LO4 — edit and manage drawing objects directly (A4, K4)",
        desc="Use multi-functional grips on practice drawing EX-7 to stretch, move, copy and rotate "
             "features without commands, and manage a busy view with Isolate and Hide Selected Objects.",
        build="An edited EX-7 layout adjusted entirely with grips, plus fluent use of isolate/hide/end-isolate.",
        services="Multi-functional grips, grip modes (Enter to cycle), Isolate/Hide Objects, Select Similar",
        dwg="ex7.dwg",
        img="ex7.png",
        steps=[
            ("Open ex7.dwg, click an object and hover its grips to see the grip menu", ""),
            ("Stretch an endpoint grip to lengthen an edge; use the midpoint grip to move the object", "click grip → drag / type distance"),
            ("Cycle grip modes with Enter: Stretch → Move → Rotate → Scale → Mirror", "select grip → Enter to cycle"),
            ("Copy a feature by grip-moving with the Copy option (or Ctrl held)", "grip → Move → C (Copy)"),
            ("Right-click a feature: Isolate Objects → Isolate Selected, edit it, then End Isolation", "ISOLATEOBJECTS · UNISOLATEOBJECTS"),
            ("Use Select Similar to grab all matching objects and hide them temporarily", "select → right-click → Select Similar → Hide"),
        ],
        test="You can stretch/move/rotate/copy with grips alone (no typed commands), and isolate then "
             "restore any subset of the drawing without losing objects.",
    ),
    dict(
        num=11, topic=4,
        title="Blocks, Attributes and Part Lists",
        objective="LO3 — create part lists using AutoCAD (A4, K4)",
        desc="Define a reusable part-tag block with attributes (part number, description, quantity) in "
             "the title-block drawing, insert it against each component, and prepare the attribute data "
             "that will feed the part list.",
        build="A BALLOON block with PART_NO / DESC / QTY attributes, inserted and filled in for each part.",
        services="BLOCK, ATTDEF, INSERT, ATTEDIT, groups, DATAEXTRACTION (preview)",
        dwg="title-block.dwg",
        steps=[
            ("Open title-block.dwg and draw the balloon symbol (circle + leader stub)", "C → radius 5"),
            ("Define attributes PART_NO, DESC and QTY with prompts and default values", "ATTDEF → tag/prompt/default"),
            ("Create the block BALLOON from the circle plus its attribute definitions", "B → name BALLOON → select objects"),
            ("Insert the balloon against each component and fill in the attribute values", "I → BALLOON → answer prompts"),
            ("Double-click a balloon to edit its attributes; group related parts together", "ATTEDIT / EATTEDIT · GROUP"),
            ("Preview extracting the attribute data — this becomes the part list in Lab 14", "DATAEXTRACTION"),
        ],
        test="Each inserted balloon prompts for and displays its own part number, description and "
             "quantity, and Data Extraction lists one row per balloon with the values you entered.",
    ),
    dict(
        num=12, topic=4,
        title="External References and PDF Import",
        objective="LO4 — assemble drawings from shared reference content (A4, K4)",
        desc="Attach the title-block drawing as an external reference under the table drawing, observe "
             "how xref updates flow through, then attach a PDF as an underlay and import PDF geometry.",
        build="A host drawing with a live xref title block and a PDF underlay ready for tracing.",
        services="XREF/ATTACH, External References palette, PDFATTACH, PDFIMPORT",
        dwg="title-block.dwg",
        steps=[
            ("Open your layered table drawing from Lab 9 as the host drawing", "OPEN table-layers.dwg"),
            ("Attach title-block.dwg as an Xref at 0,0, scale 1", "XATTACH → title-block.dwg"),
            ("Open the External References palette and note the xref's status and path", "XR (External References)"),
            ("Edit the title block in its own file, save, and reload the xref in the host", "XR → right-click → Reload"),
            ("Attach the supplied drawing-sheet PDF as an underlay and snap to its geometry", "PDFATTACH → ex1-drawing-sheet.pdf"),
            ("Import the PDF's vector geometry into the drawing and inspect the created objects", "PDFIMPORT → select underlay area"),
        ],
        test="Changing the title block file and reloading updates the host without copying geometry, "
             "and PDFIMPORT produces editable AutoCAD objects from the underlay.",
    ),
]
