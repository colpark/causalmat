"""Check 3: open rendered pages headless, click one node per lane, count images in the detail panel.

Expected per node: one image per cited panel id that was embedded, plus one per whole figure present in figs.

Usage: .venv/bin/python check_pages.py <page.html> [<page.html> ...]
"""
import asyncio
import json
import re
import sys
from pathlib import Path


async def run(paths):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.firefox.launch()
        page = await b.new_page(viewport={"width": 1400, "height": 1000})
        for path in paths:
            await page.goto("file://" + str(Path(path).resolve()))
            await page.wait_for_timeout(700)
            data = await page.evaluate("() => ({lanes: D.lanes.map(l=>l.label), nodes: D.nodes.filter(n=>n.kind!=='state')"
                                       ".map(n=>({id:n.id, lane:n.lane, panel_ids:n.panel_ids||[], figs:n.figs||[]})), "
                                       "panels: Object.keys(D.panels||{}), figs: Object.keys(D.figs||{})})")
            print(f"\n== {Path(path).name}")
            print(f"   lanes: {data['lanes']}")
            seen_lanes = set()
            for n in data["nodes"]:
                if n["lane"] in seen_lanes:
                    continue
                seen_lanes.add(n["lane"])
                embedded = [p_ for p_ in n["panel_ids"] if p_ in data["panels"]]
                figs = [f for f in n["figs"] if f in data["figs"]]
                expect = len(embedded) + len(figs)
                await page.evaluate(f"() => {{ const el=[...document.querySelectorAll('[data-id]')].find(e=>e.dataset.id==='{n['id']}');"
                                    f" if(el) el.dispatchEvent(new MouseEvent('click',{{bubbles:true}})); }}")
                await page.wait_for_timeout(350)
                got = await page.evaluate("() => document.querySelectorAll('aside img').length")
                ok = "OK " if got == expect else "MISMATCH"
                print(f"   {ok} node {n['id']} lane {n['lane']}: cites {len(n['panel_ids'])} ids "
                      f"({len(embedded)} embedded) + {len(figs)} figures -> expected {expect}, page shows {got}")
        await b.close()


asyncio.run(run(sys.argv[1:]))
