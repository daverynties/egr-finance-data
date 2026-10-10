# EGRPS enrollment, Schools of Choice, class size and child population: testing the reader's claims
Compiled Oct 10, 2026. Raw files are in this folder (`ccd_dir_*.json`, `ccd_lea_*.json`, `nces_detail.html`, `cr_B09001_latest.json`, `cr_B14002_latest.json`).

## Year-by-year table (NCES Common Core of Data, district ID 2612480)
"Year" is the fall of the school year. The pupil-teacher ratio is fall enrollment ÷ teacher FTE, which I calculated. **It is not class size.** Teacher FTE covers every teacher, including specialists, and CCD reports FTE as whole numbers through 2023.

| School year | Enrollment | Teacher FTE | Pupils per teacher | Source |
|---|---:|---:|---:|---|
| 2010–11 | 2,977 | 153 | 19.46 | U1 |
| 2011–12 | 2,976 | 155 | 19.20 | U1 |
| 2012–13 | 2,990 | 160 | 18.69 | U1 |
| 2013–14 | 2,989 | 160 | 18.68 | U1 |
| 2014–15 | 2,950 | 159 | 18.55 | U2 |
| 2015–16 | 2,959 | 153 | 19.34 | U1 |
| 2016–17 | 2,939 | 152 | 19.34 | U2 |
| 2017–18 | 2,910 | 155 | 18.77 | U1 |
| 2018–19 | 2,886 | 171 | 16.88 | U2 |
| 2019–20 | 2,895 | 163 | 17.76 | U1 |
| 2020–21 | 2,818 | 160 | 17.61 | U2 |
| 2021–22 | 2,895 | 170 | 17.03 | U2 |
| 2022–23 | 2,946 | 160 | 18.41 | U2 |
| 2023–24 | 2,941 | 161 | 18.27 | U2 |
| 2024–25 | 2,992 | 163.63 | 18.29 (NCES) | N |

- U1 = https://educationdata.urban.org/api/v1/school-districts/ccd/directory/{YEAR}/?leaid=2612480 (Urban Institute mirror of NCES CCD)
- U2 = https://educationdata.urban.org/api/v1/school-districts/ccd/directory/{YEAR}/?state_location=MI&county_code=26081
- N = https://nces.ed.gov/ccd/districtsearch/district_detail.asp?ID2=2612480
- The audited blended funding count for 2024–25 was 2,981. This is a different measure, taken from the EGRPS FY2025 audit already cited on the site.

**Schools of Choice:** these are new admissions only, not the total number of SOC students enrolled.
- 2010: 16 new students accepted, down from 19 in 2009. https://www.mackinac.org/13559 and https://www.mlive.com/news/grand-rapids/2010/09/record_number_of_students_use.html
- 2011–12: no seats offered. 2012–13: 33 seats offered, 23 of them expected to go to siblings. https://www.mlive.com/news/grand-rapids/2012/03/kent_county_schools_districts.html
- 2014–15: 14 enrolled from 16 seats. 2015–16: 51 enrolled from 54 seats. https://www.mlive.com/news/grand-rapids/2015/10/see_kent_county_school_of_choi.html
- 2026–27: about 27–28 seats per grade, K–5 only. Grades 6–12 enter through Section 6 tuition enrollment, which is separate. https://www.egrps.org/enrollment/schools-of-choice

**Under-18 population, City of East Grand Rapids**
- 2010 Census: 10,694 people, 31.6% under 18, which works out to about 3,379. Codex found 3,384 from the published count of 7,310 adults (https://www2.census.gov/library/publications/2012/dec/cph-1-24.pdf). The two figures agree within rounding. https://www.census.gov/quickfacts/eastgrandrapidscitymichigan
- 2020 Census: 3,518 aged 0–17. https://citypopulation.de/en/usa/places/michigan/kent/2623980__east_grand_rapids/ (a republication of 2020 Census data)
- ACS 2020–24 5-year, table B09001: 3,801 ±240. https://api.censusreporter.org/1.0/data/show/latest?table_ids=B09001&geo_ids=16000US2623980

**Residents in private school (ACS 2020–24 5-year, table B14002, city):** of K–12 students living in the city, about 2,542 attend public school and about 272 attend private school. That makes roughly **9.7% private**. The margins of error are wide; individual cells are ±10 to ±150. "Public" here also includes residents who attend other districts or charter schools. https://api.censusreporter.org/1.0/data/show/latest?table_ids=B14002&geo_ids=16000US2623980

## Verdict on each claim
1. **Class sizes have risen sharply since 2020: not supported.** Pupils per teacher went from 17.6 (2020–21) to 18.3 (2024–25). That is a small rise, and still below the 2010–11 figure of 19.5. Enrollment rose about 6% (2,818 → 2,992), but much of that is the recovery from the COVID dip in 2020. No public source reports actual class-section sizes.
2. **The trend is visible back to 2010–2012: contradicted.** Enrollment was flat or slightly down from 2010 to 2019 (2,977 → 2,895), and the ratio fell.
3. **SOC is driving growth and its share is at a record high: cannot be tested.** No public series of total SOC or nonresident students was retrieved. MI School Data's "Non-Resident Status" report has these numbers, but it is an interactive tool that could not be exported here. The historical record shows the board deliberately capped SOC, and new admissions ranged from 0 to about 51 a year.
4. **The under-18 population has grown: supported, modestly.** About 3,379 in 2010, 3,518 in 2020, and 3,801 ±240 in the ACS estimate.
5. **Many resident families choose private schools: partly supported.** About 1 in 10 resident K–12 students attend private school. The estimate is uncertain, and the data counts students, not families.

## Gaps
- Total SOC and nonresident counts by year. The source is the MI School Data Non-Resident Status report: https://www.mischooldata.org/schools-of-choice-and-other-non-resident-enrollments
- Residents attending other public districts. Michigan has no simple public count of where resident students go.
- Actual class sizes. Only district section data would show these.
- Census Bureau API access now requires a key, so ACS figures for earlier years were not pulled.
- City boundaries do not exactly match district boundaries.

## Agreement table (me / Codex / Claude)
The Claude Code run produced no data. Its web and file permissions were blocked, so it returned only "untested" verdicts.

| Number | Me | Codex | Status |
|---|---|---|---|
| 2024–25 enrollment 2,992; teacher FTE 163.63; ratio 18.29 | yes | yes | Agree. Re-checked at the NCES page |
| 2020–21 enrollment | 2,818 (CCD) | 2,816.4 (funding membership) | Agree; different measures |
| 2014–15 enrollment | 2,950 (CCD) | 2,967 (Capitol Confidential) | Small gap; different count date and source |
| 2022–23 / 2023–24 | 2,946 / 2,941 | 2,945.0 / 2,936.6 | Agree within measure differences |
| 2010 under-18 | ~3,379 | 3,384 | Agree |
| 2020 under-18 | 3,518 | 3,518 | Agree |
| Latest ACS under-18 | 3,801 ±240 | ~3,800 | Agree |
| 2010 SOC admissions 16 (19 in 2009) | yes | yes | Agree |
| Pupil-teacher ratio 19.2 (2020–21) and 20.6 (2024–25) | — | only Codex (michiganschoolalmanac.com) | **Not used.** Different staffing basis, and it conflicts with NCES 18.29 |
| Private enrollment 17.8% | 9.7% K–12 | 17.8%, all levels (neilsberg) | **Not used.** Includes preschool and college; I used the K–12 figure |
| 2025–26 forecast of 2,985 | — | only Codex (district newsletter) | **Not used.** A forecast, not verified |

## Proposed addition for the school page (style matches `school-note`)
```html
<div class="school-note"><strong>Enrollment and class size over time.</strong> Enrollment was 2,977 in 2010–11 and 2,992 in 2024–25. It dipped to 2,818 in 2020–21 and has since recovered. There were about 18 students per teacher in 2024–25, compared with 19.5 in 2010–11. This ratio counts all teachers, so it is not the same as class size. The district caps Schools of Choice to K–5 and sets seats each year; a yearly count of all nonresident students is not published in an easy-to-use form. <span class="school-source">Sources: NCES Common Core of Data (district 2612480), 2010–11 to 2024–25; EGRPS Schools of Choice page.</span></div>
<div class="school-note"><strong>Children in the city.</strong> East Grand Rapids had about 3,380 residents under 18 in 2010 and 3,518 in 2020. The latest Census survey estimate is about 3,800. Roughly 1 in 10 resident K–12 students attend a private school, though that survey estimate is uncertain. <span class="school-source">Sources: U.S. Census 2010 and 2020; American Community Survey 2020–24 5-year, tables B09001 and B14002.</span></div>
```
