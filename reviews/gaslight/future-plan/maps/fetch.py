import requests,json
bbox="42.940,-85.640,42.972,-85.595"
q=f"""[out:json][timeout:90];(way["highway"]({bbox});way["natural"="water"]({bbox});relation["natural"="water"]({bbox});way["leisure"~"park|pitch|playground|track"]({bbox});way["landuse"~"grass|recreation_ground"]({bbox});way["building"]({bbox});way["amenity"~"school|parking"]({bbox}););out geom;"""
for u in ["https://overpass-api.de/api/interpreter","https://overpass.kumi.systems/api/interpreter"]:
  try:
    r=requests.post(u,data={"data":q},timeout=120,headers={"User-Agent":"egr-plan/1.0"});r.raise_for_status();json.dump(r.json(),open("osm.json","w"));print(u,len(r.json()["elements"]));break
  except Exception as e: print(u,e)
