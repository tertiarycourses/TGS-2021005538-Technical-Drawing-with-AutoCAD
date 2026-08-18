"""Topic 2 — Technical Drawing with AutoCAD (A2, K2): hands-on activities."""

DOMAIN2 = [
    dict(
        num=2, topic=2,
        title="Creating Lines and Coordinates",
        objective="LO2 — produce 2D technical drawings using AutoCAD (A2, K2)",
        desc="Draw the outline of practice drawing EX-1 using the LINE and PLINE commands with "
             "absolute, relative and polar coordinate entry, working from its dimensioned drawing sheet.",
        build="The completed EX-1 profile drawn to size, matching the supplied solution DWG.",
        services="LINE, PLINE, coordinate entry (@dx,dy · @dist<angle), ORTHO, dynamic input",
        dwg="ex1.dwg",
        img="ex1.png",
        steps=[
            ("Open the EX-1 drawing sheet (ex1-drawing-sheet.pdf) and study the dimensions", ""),
            ("Start a new acadiso drawing and draw the first edge with absolute coordinates", "L → 0,0 → 100,0"),
            ("Continue the profile with relative coordinates for each dimensioned edge", "@0,50  ·  @-30,0  ·  @20<135"),
            ("Use ortho (F8) and polar tracking (F10) for the horizontal and vertical segments", "F8 · F10"),
            ("Close the profile back to the start point and check it forms one closed loop", "C (Close)"),
            ("Compare your result against the solution file ex1.dwg, then save", "OPEN ex1.dwg → SAVEAS ex1-mine.dwg"),
        ],
        test="Your outline closes exactly (LIST shows the final vertex at 0,0) and overlays the "
             "solution ex1.dwg with no visible deviation.",
    ),
    dict(
        num=3, topic=2,
        title="Circles, Rectangles and Polygons",
        objective="LO2 — produce 2D technical drawings using AutoCAD (A2, K2)",
        desc="Complete practice drawing EX-2 by adding circles (centre-radius, diameter, 2P/3P and Tan-Tan-Radius), "
             "a rectangle with chamfered/filleted corners and inscribed/circumscribed polygons.",
        build="The completed EX-2 drawing with all holes, rectangles and polygons placed to the sheet dimensions.",
        services="CIRCLE (Cen-Rad, 2P, 3P, TTR), RECTANG, POLYGON, object snaps",
        dwg="ex2.dwg",
        img="ex2.png",
        steps=[
            ("Open the EX-2 sheet (ex2-drawing-sheet.pdf) and identify each hole's centre", ""),
            ("Draw the main circles by centre point and radius, snapping to intersections", "C → cen point → 25"),
            ("Add a circle by diameter and one through two points on existing geometry", "C → D → 40  ·  C → 2P"),
            ("Draw a tangent-tangent-radius circle touching two existing circles", "C → TTR → pick 2 tangents → radius"),
            ("Create the rectangle feature, then a hexagon inscribed in a 30-radius circle", "REC → corner → @80,50  ·  POL → 6 → I → 30"),
            ("Verify against the solution ex2.dwg and save your drawing", "SAVEAS ex2-mine.dwg"),
        ],
        test="Every circle's centre and radius match the sheet (use LIST), the hexagon has 6 equal "
             "sides, and your drawing overlays ex2.dwg cleanly.",
    ),
    dict(
        num=4, topic=2,
        title="Polylines, Arcs, Ellipses and Splines",
        objective="LO2 — produce 2D technical drawings using AutoCAD (A2, K2)",
        desc="Draw practice drawing EX-3 combining polylines with arc segments, standalone arcs, an "
             "ellipse and a spline, plus construction lines to project feature positions between views.",
        build="The completed EX-3 drawing with mixed line/arc geometry drawn as clean, connected objects.",
        services="PLINE (Arc mode), ARC, ELLIPSE, SPLINE, XLINE, POINT/DIVIDE",
        dwg="ex3.dwg",
        img="ex3.png",
        steps=[
            ("Open the EX-3 sheet (ex3-drawing-sheet.pdf) and plan the outline as one polyline", ""),
            ("Draw the outline with PLINE, switching between Line and Arc segments as you go", "PL → pick → A (arc) → L (line)"),
            ("Place construction lines to project the centres of features between views", "XL → H / V through centres"),
            ("Add a three-point arc and a centre-start-end arc where the sheet shows open curves", "A → 3 points  ·  A → C"),
            ("Draw the ellipse from its axis endpoints and a smooth spline through the fit points", "EL → axis ends → half-width  ·  SPL"),
            ("Compare with ex3.dwg, purge the construction lines and save", "ERASE xlines → SAVEAS ex3-mine.dwg"),
        ],
        test="The outline is a single polyline (one object when selected), arcs and the ellipse match "
             "the sheet dimensions, and no construction lines remain in the final drawing.",
    ),
    dict(
        num=5, topic=2,
        title="2D Isometric Drawing",
        objective="LO2 — produce 2D and 3D technical drawings using AutoCAD (A2, K2)",
        desc="Use ISODRAFT to create a 2D isometric representation of the 3D object supplied in "
             "iso-object.dwg, switching isoplanes and drawing isocircles for the round features.",
        build="A flat isometric drawing of the 3D object — edges on the three isoplanes plus isocircle holes.",
        services="ISODRAFT, isoplanes (F5), ELLIPSE Isocircle, polar tracking",
        dwg="iso-object.dwg",
        img="iso-object.png",
        steps=[
            ("Open the object sheet iso-object-sheet.pdf and identify its three faces", ""),
            ("Turn on isometric drafting from the status bar and set the Top isoplane", "ISODRAFT → Isoplane Top (F5)"),
            ("Draw the top face edges along the 30°/150° isometric axes with polar tracking", "L with polar 30°/150°"),
            ("Switch to the Right and Left isoplanes and complete the vertical faces", "F5 → Right · F5 → Left"),
            ("Add the round features as isocircles on the correct isoplane", "EL → I (Isocircle) → centre → radius"),
            ("Compare your isometric with the 3D model in iso-object.dwg and save", "SAVEAS iso-mine.dwg"),
        ],
        test="Each face lies on the correct isoplane (edges at 30°/90°/150°), the isocircles read as "
             "ellipses aligned to their faces, and the drawing matches the supplied object's proportions.",
    ),
]
