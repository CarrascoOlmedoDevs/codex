"""Build the long-format raw dataset for HTAB v0 from source snapshots.

Reads the snapshots in data/htab/sources/, writes data/htab/raw.csv with columns

    series_id,domain,metric,entity,year,value,unit,direction,role,
    source_url,source_note,quality_flag,methodology_break

and checks values retrieved through the OWID grapher against the git-archived
OWID vintage where one exists (genome, transistors, PV). Values are stored
unchanged; no normalization happens here.

Usage: python src/build_raw.py
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "htab" / "sources"
OUT = ROOT / "data" / "htab" / "raw.csv"

OWID_GIT = "https://github.com/owid/owid-datasets"
OWID_GIT_HEAD = "6155d4ca1ea14ef30e753010a25521eeb416e8a2"
OWID_GIT_2022 = "78e2021"

# Methodology breaks listed in UNIVERSE.md (used in the primary analysis).
PREREGISTERED_BREAKS = {("genome", 2008)}

SERIES = [
    dict(
        series_id="genome", role="fast", domain="genomics",
        metric="cost_per_genome", entity="World", unit="USD (nominal)",
        direction="lower_is_better", file="owid_genome.csv", col=3,
        source_url="https://ourworldindata.org/grapher/cost-of-sequencing-a-full-human-genome",
        source_note="NHGRI DNA Sequencing Costs via OWID grapher; retrieved 2026-09-26",
        quality_flag="tool_transcribed;checked_vs_git_2022",
    ),
    dict(
        series_id="transistors", role="fast", domain="semiconductors",
        metric="transistors_per_microprocessor", entity="World", unit="count",
        direction="higher_is_better", file="owid_transistors.csv", col=3,
        source_url="https://ourworldindata.org/grapher/transistors-per-microprocessor",
        source_note="Rupp & Horowitz via OWID grapher; frontier maximum, values carried forward in some years; retrieved 2026-09-26",
        quality_flag="tool_transcribed;checked_vs_git_2022;frontier_max",
    ),
    dict(
        series_id="supercomputer", role="fast", domain="compute",
        metric="fastest_supercomputer_rmax", entity="World", unit="GFLOP/s",
        direction="higher_is_better", file="owid_supercomputer.csv", col=3,
        source_url="https://ourworldindata.org/grapher/supercomputer-power-flops",
        source_note="TOP500 #1 Rmax via OWID grapher; retrieved 2026-09-26; spot-checked against known TOP500 #1 systems",
        quality_flag="tool_transcribed;spot_checked_top500;frontier_max",
    ),
    dict(
        series_id="dram", role="fast", domain="memory",
        metric="dram_price_per_tb", entity="World", unit="USD per TB (as published by OWID)",
        direction="lower_is_better", file="owid_dram.csv", col=1,
        source_url="https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage",
        source_note="McCallum via OWID grapher, column Memory; retrieved 2026-09-26; nominal/real basis not verified",
        quality_flag="tool_transcribed;unverified",
    ),
    dict(
        series_id="pv", role="fast", domain="energy",
        metric="pv_module_cost", entity="World", unit="USD/W (constant USD)",
        direction="lower_is_better", file="owid_pv.csv", col=3,
        source_url="https://ourworldindata.org/grapher/solar-pv-prices",
        source_note="Nemet / IRENA via OWID grapher; retrieved 2026-09-26",
        quality_flag="tool_transcribed;checked_vs_git_lafond",
    ),
]

GIT_SERIES = [
    dict(
        series_id="ag_tfp", role="control", domain="agriculture",
        metric="agricultural_tfp_index", entity="World", unit="index",
        direction="higher_is_better", file="git_ag_tfp.csv", colname="tfp",
        source_note="USDA ERS International Agricultural Productivity via owid-datasets",
    ),
    dict(
        series_id="wheat", role="control", domain="agriculture",
        metric="wheat_yield", entity="World", unit="t/ha",
        direction="higher_is_better", file="git_wheat.csv",
        colname="Wheat (FAO (2017) & Bayliss-Smith (1984))",
        source_note="FAO via owid-datasets",
    ),
    dict(
        series_id="us_tfp", role="control", domain="whole_economy",
        metric="total_factor_productivity", entity="United States", unit="index",
        direction="higher_is_better", file="git_bcl_productivity.csv",
        colname="Total Factor Productivity (TFP) (Bergeaud, Cette, and Lecat (2016))",
        source_note="Bergeaud, Cette & Lecat (2016) via owid-datasets",
    ),
]


def read_rows(path):
    with open(path, newline="") as f:
        return list(csv.reader(f))


def owid_rows(spec):
    rows = read_rows(SRC / spec["file"])
    out = []
    for r in rows[1:]:
        year = int(r[0] if spec["col"] == 1 else r[2])
        val = r[spec["col"]]
        if val.strip():
            out.append((year, float(val)))
    return out


def git_rows(spec):
    rows = read_rows(SRC / spec["file"])
    header = rows[0]
    idx = header.index(spec["colname"])
    out = []
    for r in rows[1:]:
        if r[0] == spec["entity"] and r[idx].strip():
            out.append((int(r[1]), float(r[idx])))
    return out


def check(series_id, fetched, check_file, colname, entity="World", tol=0.01):
    """Compare fetched values with an archived vintage; return list of messages."""
    rows = read_rows(SRC / check_file)
    header = rows[0]
    idx = header.index(colname)
    archived = {int(r[1]): float(r[idx]) for r in rows[1:]
                if r[0] == entity and r[idx].strip()}
    fetched = dict(fetched)
    common = sorted(set(archived) & set(fetched))
    diffs = [(y, fetched[y], archived[y]) for y in common
             if abs(fetched[y] / archived[y] - 1) > tol]
    msg = f"{series_id}: {len(common)} overlapping years vs archived vintage, {len(diffs)} differ by >{tol:.0%}"
    lines = [msg] + [f"    {y}: fetched {a:.6g} vs archived {b:.6g}" for y, a, b in diffs]
    return lines, len(common), diffs


def main():
    records = []
    fetched = {}
    for spec in SERIES:
        vals = owid_rows(spec)
        fetched[spec["series_id"]] = vals
        for year, v in vals:
            records.append(dict(
                series_id=spec["series_id"], domain=spec["domain"], metric=spec["metric"],
                entity=spec["entity"], year=year, value=repr(v), unit=spec["unit"],
                direction=spec["direction"], role=spec["role"], source_url=spec["source_url"],
                source_note=spec["source_note"], quality_flag=spec["quality_flag"],
                methodology_break=int((spec["series_id"], year) in PREREGISTERED_BREAKS),
            ))
    for spec in GIT_SERIES:
        for year, v in git_rows(spec):
            records.append(dict(
                series_id=spec["series_id"], domain=spec["domain"], metric=spec["metric"],
                entity=spec["entity"], year=year, value=repr(v), unit=spec["unit"],
                direction=spec["direction"], role=spec["role"],
                source_url=f"{OWID_GIT}/tree/{OWID_GIT_HEAD}",
                source_note=spec["source_note"], quality_flag="git_archived",
                methodology_break=int((spec["series_id"], year) in PREREGISTERED_BREAKS),
            ))

    fields = ["series_id", "domain", "metric", "entity", "year", "value", "unit",
              "direction", "role", "source_url", "source_note", "quality_flag",
              "methodology_break"]
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(records)

    report = []
    ok = True
    for sid, cfile, col in [
        ("genome", "git_2022_genome_check.csv", "cost_per_genome"),
        ("transistors", "git_2022_transistors_check.csv", None),
        ("pv", "git_pv_check.csv", "Unit cost"),
    ]:
        header = read_rows(SRC / cfile)[0]
        colname = col or header[2]
        lines, n, diffs = check(sid, fetched[sid], cfile, colname)
        report += lines
        if n == 0:
            ok = False
    counts = {}
    for r in records:
        counts[r["series_id"]] = counts.get(r["series_id"], 0) + 1
    print(f"wrote {OUT.relative_to(ROOT)}: {len(records)} rows")
    for k, v in counts.items():
        print(f"  {k}: {v} rows")
    print("verification:")
    print("\n".join("  " + l for l in report))
    (ROOT / "data" / "htab" / "verification.txt").write_text("\n".join(report) + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
