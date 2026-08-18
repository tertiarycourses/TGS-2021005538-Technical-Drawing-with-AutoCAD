"""Topic 1 — Getting Started with AutoCAD (A1, K1): hands-on activities."""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Setting Up a New Drawing",
        objective="LO1 — read and visualize AutoCAD technical drawings; set up a drawing environment (A1, K1)",
        desc="Create a new metric drawing from the ACADISO template, choose the Drafting & Annotation "
             "workspace, set units and limits, then open a finished drawing and practise reading it "
             "with the zoom, pan and ViewCube navigation tools.",
        build="A correctly configured metric drawing (units, limits, workspace) saved as DWG, plus "
              "confident navigation of an existing technical drawing.",
        services="ACADISO template, UNITS, LIMITS, ZOOM, PAN, ViewCube",
        dwg="lab01-table.dwg",
        steps=[
            ("Start AutoCAD and create a new drawing from the ISO metric template", "NEW → acadiso.dwt"),
            ("Switch the workspace to Drafting & Annotation from the status bar gear icon", "WSCURRENT → Drafting & Annotation"),
            ("Set decimal length units with 0.00 precision and decimal degrees for angles", "UNITS → Length: Decimal, Precision 0.00"),
            ("Frame an A3-sized working area with drawing limits, then zoom to it", "LIMITS → 0,0 → 420,297  |  ZOOM → All"),
            ("Toggle the precision aids on the status bar: grid, snap, ortho, polar and object snap", "F7 grid · F9 snap · F8 ortho · F10 polar · F3 osnap"),
            ("Open lab01-table.dwg and navigate it: wheel-zoom, pan, zoom window and zoom extents", "OPEN lab01-table.dwg → Z → W / Z → E"),
            ("Identify the views, dimensions and title information in the drawing, then save your setup file", "SAVEAS → lab01-setup.dwg"),
        ],
        test="You can state the drawing's units, limits and workspace; zoom to any detail of "
             "lab01-table.dwg and back to extents; and your lab01-setup.dwg opens with the settings intact.",
    ),
]
