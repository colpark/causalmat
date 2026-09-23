# Superseded: the harvested annotation label set

These 750 labels came from the saturation and OCR-box annotation detection, which was **withdrawn on
2026-09-23**. The removal it fed was destroying the figure (up to 45% of one panel) and the detection
itself was not reliable enough to decide anything on.

Kept rather than deleted so the withdrawal is auditable: this is what the detector produced, and
`docs/TRACES_V2_NECESSITY.md` cites the altered fractions that justified dropping it.

Nothing downstream reads these files. Do not build on them.
