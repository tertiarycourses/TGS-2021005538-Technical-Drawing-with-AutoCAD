"""
SINGLE SOURCE OF TRUTH — WSQ Technical Drawing with AutoCAD (TGS-2021005538).

Every artifact (PPT, LP, LG, LG.md, labs index) is generated from this file plus
data_domain1.py … data_domain5.py so they stay 100% aligned. Content is carried
over from the legacy deck 'WSQ - Master Trainer Slides - Technical Drawing with
AutoCAD - v11.pptx' (reference/) and rebuilt in the Tertiary house style.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "WSQ Technical Drawing with AutoCAD"
SHORT_TITLE  = "WSQ Technical Drawing with AutoCAD"   # used in output filenames
COURSE_CODE  = "TGS-2021005538"
VERSION      = "v12"
VERSION_DATE = "18 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 2

# Skills Framework alignment (from the legacy deck, slides 8–10)
TSC_TITLE = "Technical Drawing"
TSC_CODE  = "DSN-TDR-3005-1.11"
TSC_ABILITIES = [
    "A1: Read and visualise technical drawings according to briefs",
    "A2: Produce two-dimensional (2D) and three-dimensional (3D) technical drawings based on input from stakeholders",
    "A3: Create part lists for new design to facilitate technical drawing",
    "A4: Oversee the development and construction of new designs' prototypes, in collaboration with organisation's production function",
    "A5: Produce drawings and specifications, that conform to the requirements of relevant standards for submission",
]
TSC_KNOWLEDGE = [
    "K1: Symbols, standards and conventions used in technical drawings within one's field and region",
    "K2: Methods of technical drawing by instruments and computer-aided design (CAD) systems",
    "K3: Types of technical drawings",
    "K4: Fundamentals of drafting design documentation",
    "K5: Concepts of information technology (IT) to facilitate the usage of technical drawing software",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Read and visualize AutoCAD technical drawings",
    "LO2: Produce 2D and 3D technical drawings using AutoCAD",
    "LO3: Create part lists using AutoCAD",
    "LO4: Create AutoCAD design documentation",
    "LO5: Produce design specification using AutoCAD",
]

# ------------------------------------------------------------------ topics
# num, code, title, subtitle, weighting (ability/knowledge mapping), concepts
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with AutoCAD",
         subtitle="AutoCAD User Interface · Workspace Settings · Navigation · Units",
         weighting="A1 · K1",
         concepts=[
            ("User interface", "Application menu, Quick Access Toolbar, ribbon tabs and panels, drawing area, command window and status bar."),
            ("Workspaces", "Drafting & Annotation, 3D Basics and 3D Modeling — task-oriented sets of ribbons, menus and palettes."),
            ("Model vs paper space", "Design at 1:1 in model space; compose scaled drawing sheets in paper-space layouts."),
            ("Precision aids", "Grid and snap, ortho mode, polar tracking, object snaps and dynamic input keep every pick exact."),
            ("Navigation", "Zoom, pan, ViewCube and the wheel mouse move you around a drawing without changing it."),
            ("Units and limits", "UNITS sets the length/angle format and precision; LIMITS frames the working area of the drawing."),
         ]),
    dict(num=2, code="02",
         title="Technical Drawing with AutoCAD",
         subtitle="Basic AutoCAD Operations · Drawing Objects · Isometric Drawing",
         weighting="A2 · K2",
         concepts=[
            ("Lines & polylines", "LINE draws separate segments; PLINE creates one connected object of line and arc segments."),
            ("Circles & arcs", "Circles by centre/radius or diameter; arcs by combinations of start, centre, end, radius and angle."),
            ("Rectangles & polygons", "RECTANG builds closed rectangular polylines; POLYGON draws 3–1024-sided regular polygons."),
            ("Ellipses, splines & points", "Ellipses from axis endpoints; splines as smooth curves through fit points; points as snap nodes."),
            ("Construction geometry", "Construction lines (XLINE) and rays give infinite reference lines for projecting views."),
            ("2D isometric drawing", "ISODRAFT turns on isometric planes so a flat drawing represents a 3D projection."),
         ]),
    dict(num=3, code="03",
         title="Modifying Objects",
         subtitle="Move · Copy · Rotate · Offset · Mirror · Trim · Fillet · Arrays",
         weighting="A3 · K3",
         concepts=[
            ("Relocate & duplicate", "MOVE, COPY and ROTATE reposition objects from a base point to a second point or angle."),
            ("Offset & mirror", "OFFSET creates parallel copies at a set distance; MIRROR reflects half a symmetric design."),
            ("Trim & extend", "Quick and Standard modes cut objects back to, or extend them to meet, boundary edges."),
            ("Fillet & chamfer", "FILLET rounds a corner with a radius; CHAMFER bevels it with distances or an angle."),
            ("Arrays", "Rectangular, polar and path arrays distribute copies in rows/columns, around a centre, or along a curve."),
            ("Stretch, scale & explode", "STRETCH lengthens with a crossing window; SCALE resizes about a base point; EXPLODE breaks compounds."),
         ]),
    dict(num=4, code="04",
         title="Organizing Objects",
         subtitle="Object Properties · Layers · Blocks, Attributes & Reusable Content",
         weighting="A4 · K4",
         concepts=[
            ("Object properties", "Colour, linetype and lineweight — set ByLayer and inspected in the Properties palette (PR)."),
            ("Layers", "The primary method of organising a drawing by function; control on/off, freeze/thaw, lock and plot."),
            ("Grips", "Multi-functional grips stretch, move, rotate, scale and copy objects without typing a command."),
            ("Hide & isolate", "Temporarily isolate the objects you are working on and hide the rest of the drawing."),
            ("Blocks & attributes", "Blocks are reusable symbols; attributes attach part numbers and data — the basis of part lists."),
            ("External references", "Xrefs attach another drawing (or PDF underlay) so teams share one live reference file."),
         ]),
    dict(num=5, code="05",
         title="Design Documentation",
         subtitle="Text · Dimensions · Tables & Part Lists · Layouts, Viewports & Plotting",
         weighting="A5 · K5",
         concepts=[
            ("Text & text styles", "Single-line and multiline text; a text style controls font, height and justification centrally."),
            ("Dimensions", "Linear, aligned, angular, radial, diameter, ordinate and arc-length dimensions annotate real sizes."),
            ("Dimension styles", "A named collection of settings — arrowheads, text placement, tolerances — applied consistently."),
            ("Multileaders & clouds", "Multileaders point notes at features; revision clouds flag changed areas for checking."),
            ("Tables & part lists", "TABLE creates row/column data such as bills of materials extracted from block attributes."),
            ("Layouts & plotting", "Scaled viewports on a titled layout sheet, printed with PLOT or published to PDF/DWF."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "AutoCAD Foundations, Drawing & Modifying Objects",
    2: "Organizing Objects, Design Documentation & Assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — produce a dimensioned AutoCAD technical drawing, 1.5 hours, open book.",
    note="A minimum of 75% attendance (SSG Digital Attendance record) and a 'Competent' assessment result are required for funding.",
)

# ------------------------------------------------------------------ links
PRACTICE_EXAM_URL = "https://exams.tertiaryinfotech.com/practice-exams/autodesk/autocad"
LMS_URL = "https://lms-tms.tertiaryinfotech.com"

RECOMMENDED_COURSES = [
    "WSQ - Architecture Drawing with Revit",
    "WSQ - Product Design with Fusion 360",
    "WSQ - AutoCAD Civil 3D for Infrastructure Design",
    "WSQ - Technical Drawing with AutoCAD Mechanical",
    "WSQ - Technical Drawing with AutoCAD Electrical",
]
