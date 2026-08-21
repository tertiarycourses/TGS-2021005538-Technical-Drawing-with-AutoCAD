"""Topic 4 — Organizing Objects (A4, K4): hands-on activities."""

DOMAIN4 = [
    dict(
        num=9, topic=4,
        title="Object Properties and Layers",
        objective="LO3/LO4 — organise a drawing with layers and properties (A4, K4)",
        desc="Create a standards-based layer scheme in lab-table-lesson2.dwg, then audit the supplied "
             "office-plan-ground-floor.dwg to see how a larger architectural drawing separates systems.",
        build="A layered table drawing where every object is ByLayer, plus a five-layer audit of the "
              "office plan covering naming, colour, linetype, lineweight and plot state.",
        services="LAYER (LA), Properties palette (PR), Layer Walk, MATCHPROP, freeze/thaw, lock",
        dwg="lab-table-lesson2.dwg",
        steps=[
            ("Open lab-table-lesson2.dwg and inspect current object properties", "PR (Properties palette)"),
            ("Create layers: A-OUTLINE, A-HIDDEN, A-CENTRE, A-DIMS, A-TEXT with colours and linetypes", "LA → New Layer → colour/linetype"),
            ("Load the HIDDEN and CENTER linetypes and set lineweights per layer", "LA → Linetype → Load → HIDDEN, CENTER"),
            ("Select objects by type and move them to their layers; copy formatting with MATCHPROP", "select → Layer drop-down  ·  MA"),
            ("Practise layer states: turn off, freeze/thaw, lock and Layer Walk through the scheme", "LAYWALK · LAYFRZ · LAYLCK"),
            ("Set every object's colour, linetype and lineweight to ByLayer and save", "SETBYLAYER → SAVEAS table-layers.dwg"),
            ("Open office-plan-ground-floor.dwg and audit five functional layers against the same rules", "OPEN office-plan-ground-floor.dwg → LA → record name/colour/linetype/lineweight/plot"),
        ],
        test="Turning each layer off hides exactly its objects, everything in table-layers.dwg reports "
             "ByLayer, and the office-plan audit identifies five layers with their intended functions.",
    ),
    dict(
        num=10, topic=4,
        title="Grips, Hide and Isolate",
        objective="LO3/LO4 — edit and manage drawing objects directly (A4, K4)",
        desc="Use multi-functional grips on EX-7, then practise isolate, hide, select-similar and end-isolate "
             "in the denser new-office-design.dwg without losing or deleting objects.",
        build="An edited EX-7 layout plus a saved office-plan view in which the targeted object class was "
              "isolated, edited and fully restored.",
        services="Multi-functional grips, grip modes (Enter to cycle), Isolate/Hide Objects, Select Similar",
        dwg="ex7.dwg",
        img="ex7.png",
        steps=[
            ("Open ex7.dwg, click an object and hover its grips to see the grip menu", ""),
            ("Stretch an endpoint grip to lengthen an edge; use the midpoint grip to move the object", "click grip → drag / type distance"),
            ("Cycle grip modes with Enter: Stretch → Move → Rotate → Scale → Mirror", "select grip → Enter to cycle"),
            ("Copy a feature by grip-moving with the Copy option (or Ctrl held)", "grip → Move → C (Copy)"),
            ("Open new-office-design.dwg, select one furniture object and use Select Similar", "OPEN new-office-design.dwg → select → right-click → Select Similar"),
            ("Isolate the selection, make one grip edit, hide a second class, then restore everything", "ISOLATEOBJECTS · HIDEOBJECTS · UNISOLATEOBJECTS"),
        ],
        test="You can stretch, move, rotate and copy with grips alone; after UNISOLATEOBJECTS, the office "
             "drawing's object count and layer visibility match the starting state except for your saved edit.",
    ),
    dict(
        num=11, topic=4,
        title="Blocks, Attributes and Part Lists",
        objective="LO3 — create part lists using AutoCAD (A4, K4)",
        desc="Inspect a reusable block library and a drawing containing dynamic blocks, then define a "
             "part-tag block with attributes and prepare its data for the part list.",
        build="A BALLOON block with PART_NO / DESC / QTY attributes, plus evidence that one library block "
              "and one dynamic-block state can be inserted and edited correctly.",
        services="BLOCK, WBLOCK, DesignCenter, ATTDEF, INSERT, ATTEDIT, dynamic-block grips, DATAEXTRACTION",
        dwg="title-block.dwg",
        steps=[
            ("Open architecture-library.dwg in DesignCenter and insert one reusable symbol into a new drawing", "ADCENTER → Folders → architecture-library.dwg → Blocks → Insert"),
            ("Open new-office-dynamic-blocks.dwg and change one dynamic block's grip or visibility state", "OPEN new-office-dynamic-blocks.dwg → select dynamic block → grip / Properties"),
            ("Open title-block.dwg and draw the balloon symbol (circle + leader stub)", "C → radius 5"),
            ("Define attributes PART_NO, DESC and QTY with prompts and default values", "ATTDEF → tag/prompt/default"),
            ("Create the block BALLOON from the circle plus its attribute definitions", "B → name BALLOON → select objects"),
            ("Insert the balloon against each component and fill in the attribute values", "I → BALLOON → answer prompts"),
            ("Edit one balloon attribute, then preview the data extraction used by the Lab 14 part list", "ATTEDIT / EATTEDIT → DATAEXTRACTION"),
        ],
        test="The library block inserts at the correct scale, the dynamic state changes without exploding, "
             "and Data Extraction lists one row per BALLOON with the values you entered.",
    ),
    dict(
        num=12, topic=4,
        title="External References and PDF Import",
        objective="LO4 — assemble drawings from shared reference content (A4, K4)",
        desc="Repair and verify the relative Landscaping_REV1 Xref in the supplied office-layout host, "
             "then attach a title block and a PDF underlay and import vector geometry.",
        build="A host drawing whose landscaping Xref resolves from the lab folder, with an additional live "
              "title-block Xref and an imported PDF geometry sample.",
        services="XREF/ATTACH, External References palette, PDFATTACH, PDFIMPORT",
        dwg="title-block.dwg",
        steps=[
            ("Keep new-office-layout-with-xref.dwg and Landscaping_REV1.dwg together, then open the host", "OPEN new-office-layout-with-xref.dwg"),
            ("Open External References and confirm Landscaping_REV1 is Found using a relative path", "XR → Landscaping_REV1 → Saved Path: .\\Landscaping_REV1.dwg"),
            ("If unresolved, select a new path in the current lab folder, reload, and retain a relative path", "XR → Change Path → Select New Path → Reload"),
            ("Attach title-block.dwg as an additional Xref at 0,0, scale 1", "XATTACH → title-block.dwg"),
            ("Attach the supplied drawing-sheet PDF as an underlay and snap to its geometry", "PDFATTACH → ex1-drawing-sheet.pdf"),
            ("Import the PDF's vector geometry into the drawing and inspect the created objects", "PDFIMPORT → select underlay area"),
        ],
        test="Both Xrefs show Loaded, Landscaping_REV1 uses a relative path and survives reopening the "
             "folder elsewhere, while PDFIMPORT produces editable AutoCAD objects from the underlay.",
    ),
]
