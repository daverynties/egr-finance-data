# Map sources

## Rendered (programmatic, Python + matplotlib; no AI imagery)
- `01-base-dark.png`, `02-walkshed.png`, `03-bike-paths.png`, `04..07-concept-*.png`: OpenStreetMap data via Overpass API (`https://overpass-api.de/api/interpreter`), bbox 42.940,-85.640,42.972,-85.595, fetched 2026-10-09. © OpenStreetMap contributors, ODbL. Scripts: `fetch.py`, `render.py`, `overlays.py`; raw data `osm.json`.
- Orientation checked against David's Google Maps screenshot: Wealthy St SE runs NW→SE; Gaslight site lies north of Wealthy and west of Lakeside Dr; Lakeside curves along Reeds Lake to the east; EGR High School lies south of Wealthy, with Lake Dr SE further south. The OSM Wealthy/Lakeside node is at 42.94966, -85.61185.
- Walk rings are straight-line (400 m ≈ 5 min, 800 m ≈ 10 min) from 42.9515, -85.6142. They are not network walk times.

## Downloaded public maps (`public/`)
| File | Source URL |
|---|---|
| zoning-map.pdf | https://www.eastgrmi.gov/DocumentCenter/View/29 (City of EGR Zoning Map, via https://www.eastgrmi.gov/97/Maps) |
| master-plan-2026.pdf | https://www.eastgrmi.gov/DocumentCenter/View/4658/EGR-Master-Plan-Update---2026 (2026 Master Plan Amendment, which includes zoning and subarea maps) |
| master-plan-2018.pdf | https://www.eastgrmi.gov/DocumentCenter/View/1621/EGR-Master-Plan---June-2018 (2018 Master Plan, which includes the Gaslight Village future land use map) |
| gaslight-parking-map.pdf | https://www.eastgrmi.gov/DocumentCenter/View/4219/Gaslight-Village-Parking-Map |
| reeds-lake-trail-map.pdf | https://www.eastgrmi.gov/DocumentCenter/View/22 |
| street-map.pdf | https://www.eastgrmi.gov/DocumentCenter/View/27 |
| usgs-imagery-gaslight.jpg | USGS The National Map, USGSImageryOnly: https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/export?bbox=-85.6290,42.9415,-85.6000,42.9600&bboxSR=4326&imageSR=3857&size=1600,1400&format=jpg&f=image (public domain) |
