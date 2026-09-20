# Panel match review packet

400 figures ({'B': 120, 'C': 80, 'A': 200}), 714 panel rows. Open `figures/` beside `annotation.csv`
and fill one row per panel. Rows marked `double_annotated: yes` (80 figures) are reviewed by
two people independently, for the agreement number.

Each image shows the figure with detected panels boxed and lettered. Under it, per panel: the
definition span assigned to it, where that span came from, and how many "use" sentences were attached.

Fill `box_correct`, `letter_correct`, `definition_correct`, `use_correct` with **y**, **n** or **?**.

- **box_correct = y** when the box holds exactly one panel, whole, with its scale bar or axes intact.
  Mark **n** if it splits a panel, merges two panels, or cuts off the axis or scale bar.
- **letter_correct = y** when the letter drawn on the box is the panel's own label in the figure.
- **definition_correct = y** when the printed span describes *that panel and no other*. A span covering
  two panels is **n**. An empty span is **n** only if the caption does define that panel.
- **use_correct = y** when every listed sentence refers to that panel. Mark **n** if any sentence is
  about a different panel or figure. If there are no use sentences, leave blank.
- Put anything odd in `note` (swapped caption, missing panel, figure is a table, and so on).

Do not consult the original paper online. Judge only what the image and the printed spans show.
