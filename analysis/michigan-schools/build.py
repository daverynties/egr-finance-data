"""Build precomputed JSON for /michigan-schools/ from public 2024-25 Michigan school finance files.

Inputs (downloaded, not committed):
  25_Bulletin1014Export.xlsx  - MDE Bulletin 1014, 2024-25 (General Fund revenue/expenditure per pupil)
  25_Bulletin1011Export.xlsx  - MDE Bulletin 1011, 2024-25 (fund-level balance sheet, revenue, expenditure)
  25-Port-74vSchool-Level-Expend-Download-File.csv - CEPI school-level per-pupil expenditures, 2024-25
  fid_2024-25/2025_CEPI_33_FID_REVENUE_DATA.xlsx   - CEPI FID revenue (used only for ISD names)
Usage: python3 build.py <src_dir> <out_dir>
"""
import json, sys, statistics as st
import pandas as pd

src, out = sys.argv[1], sys.argv[2]
b14 = pd.read_excel(f"{src}/25_Bulletin1014Export.xlsx", header=1, dtype={"DCode": str, "CC": str})
b14 = b14[b14.DCode.notna()].copy()
b11 = pd.read_excel(f"{src}/25_Bulletin1011Export.xlsx", header=1, dtype={"DCode": str})
gf = b11[b11.Fund == 1].set_index("DCode")
rev = pd.read_excel(f"{src}/fid_2024-25/2025_CEPI_33_FID_REVENUE_DATA.xlsx", sheet_name="District Revenue Data",
                    header=4, usecols=[1, 2, 3], dtype=str).dropna()
rev.columns = ["isd_code", "isd", "dcode"]
isd = {r.dcode.zfill(5): r.isd.strip() for r in rev.drop_duplicates("dcode").itertuples()}
bld = pd.read_csv(f"{src}/25-Port-74vSchool-Level-Expend-Download-File.csv", dtype={"District Code": str, "Building Code": str})

def r0(x): return None if pd.isna(x) else int(round(float(x)))
def r2(x): return None if pd.isna(x) else round(float(x), 2)

districts = []
for r in b14.itertuples(index=False):
    d = r._asdict() if hasattr(r, "_asdict") else None
for _, r in b14.iterrows():
    code = r.DCode
    suf = int(code[2:])
    g = gf.loc[code] if code in gf.index else None
    totrev = float(r["TOTREV"]); fte = float(r["AVG FTE"])
    fb = float(g.ENDFUNDBAL) if g is not None else None
    gfexp = float(g.TOTEXPOUT) if g is not None else None
    districts.append({
        "code": code, "name": r["District Name"].strip(), "county": r["DistCounty"].strip().title(),
        "isd": isd.get(code), "type": "Charter (PSA)" if (700 <= suf <= 799 or suf >= 900) else "Traditional",
        "fte": round(fte, 2), "rev": r0(totrev), "revpp": r0(r["AVG TOTREV"]),
        "locpp": r0(r["AVG LOCREV"]), "stpp": r0(r["AVG STREV"]), "fedpp": r0(r["AVG FEDREV"]),
        "locsh": round(float(r["LOCREV"]) / totrev, 4) if totrev else None,
        "stsh": round(float(r["STREV"]) / totrev, 4) if totrev else None,
        "fedsh": round(float(r["FEDREV"]) / totrev, 4) if totrev else None,
        "exp": r0(r["TOTEXP"]), "exppp": r0(r["AVG TOTEXP"]),
        "instpp": r0(r["AVG ITOT"]), "sspp": r0(r["AVG SSTOT"]), "admpp": r0(r["AVG ADM"]),
        "opspp": r0(r["AVG OPMNT"]), "trnpp": r0(r["AVG TRANS"]),
        "tsal": r0(r["AVG T SAL"]), "tfte": r2(r["Teacher FTE"]), "ppt": r0(r["AVG P TCHR"]),
        "fb": r0(fb), "fbpct": round(fb / gfexp, 4) if (fb is not None and gfexp) else None,
    })

def med(k, rows):
    v = [d[k] for d in rows if d.get(k) is not None]
    return round(st.median(v), 4 if k.endswith("sh") or k == "fbpct" else 0) if v else None
keys = ["fte", "revpp", "locpp", "stpp", "fedpp", "locsh", "stsh", "exppp", "instpp", "sspp", "admpp", "opspp", "trnpp", "tsal", "ppt", "fbpct"]
state = {"median": {k: med(k, districts) for k in keys},
         "median_traditional": {k: med(k, [d for d in districts if d["type"] == "Traditional"]) for k in keys},
         "weighted": {"revpp": round(b14.TOTREV.sum() / b14["AVG FTE"].sum()), "exppp": round(b14.TOTEXP.sum() / b14["AVG FTE"].sum())},
         "count": len(districts), "count_traditional": sum(d["type"] == "Traditional" for d in districts)}

buildings = {}
for _, r in bld.iterrows():
    buildings.setdefault(r["District Code"].zfill(5), []).append({
        "code": r["Building Code"], "name": r["Building Name"].strip(), "fte": r2(r["Building Audited FTE"]),
        "site": r2(r["Total Site Level Total PPE"]), "dw": r2(r["Total Districtwide PPE"]),
        "fed": r2(float(r["Building Federal PPE"]) + float(r["Districtwide Federal PPE"])),
        "total": r2(r["Total Building PPE"])})
bvals = [b["total"] for v in buildings.values() for b in v if b["total"] and b["fte"] and b["fte"] > 0]
state["median_building_ppe"] = round(st.median(bvals))
state["building_count"] = sum(len(v) for v in buildings.values())

meta = {"year": "2024-25", "built": pd.Timestamp.now().strftime("%Y-%m-%d")}
json.dump({"meta": meta, "state": state, "districts": districts}, open(f"{out}/districts.json", "w"), separators=(",", ":"))
json.dump(buildings, open(f"{out}/buildings.json", "w"), separators=(",", ":"))
print(len(districts), "districts;", state["building_count"], "buildings; missing isd:", sum(d["isd"] is None for d in districts),
      "missing fb:", sum(d["fb"] is None for d in districts))
print(json.dumps(state, indent=1))
print(json.dumps([d for d in districts if d["code"] == "41090"][0], indent=1))
print(json.dumps(buildings["41090"], indent=1))
