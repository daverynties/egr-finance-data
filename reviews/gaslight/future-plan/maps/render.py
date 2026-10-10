import json,math,sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
d=json.load(open('osm.json'))
C=(42.9515,-85.6142)  # Gaslight site center (N of Wealthy, W of Lakeside)
S,N,Wb,E=42.9415,42.9600,-85.6290,-85.6000
k=math.cos(math.radians(C[0]))
def xy(g): return [p['lon'] for p in g],[p['lat'] for p in g]
def rings(e):
  if e['type']=='way': return [e['geometry']] if 'geometry' in e else []
  return [m['geometry'] for m in e.get('members',[]) if m.get('role')=='outer' and 'geometry' in m]
def base(title,dim=1.0):
  fig,ax=plt.subplots(figsize=(9,8.4),dpi=150); fig.patch.set_facecolor('#0f1b2d'); ax.set_facecolor('#16243a')
  for e in d['elements']:
    t=e.get('tags',{})
    for g in rings(e):
      pts=[(p['lon'],p['lat']) for p in g]
      if t.get('natural')=='water': ax.add_patch(Polygon(pts,fc='#071022',ec='#24406a',lw=.6,zorder=1))
      elif t.get('leisure') in('park','pitch','playground','track') or t.get('landuse') in('grass','recreation_ground'): ax.add_patch(Polygon(pts,fc='#1f4f55',ec='none',alpha=.8,zorder=1.5))
      elif t.get('amenity')=='school': ax.add_patch(Polygon(pts,fc='#24334f',ec='#3a4d70',lw=.5,zorder=1.2))
      elif t.get('amenity')=='parking': ax.add_patch(Polygon(pts,fc='#1c2a42',ec='none',zorder=1.3))
      elif 'building' in t: ax.add_patch(Polygon(pts,fc='#2a3a55',ec='none',zorder=2))
  W={'primary':3,'secondary':2.6,'tertiary':2,'residential':1.2,'unclassified':1.2,'service':.5}
  for e in d['elements']:
    h=e.get('tags',{}).get('highway')
    if h in W and 'geometry' in e:
      x,y=xy(e['geometry']); ax.plot(x,y,color='#5b6f8f' if W[h]>1.5 else '#3f5070',lw=W[h]*dim,zorder=3,solid_capstyle='round')
  lab=[('Wealthy St SE',42.9546,-85.6222,-30),('Lake Dr SE',42.9497,-85.6200,-30),('Lakeside Dr',42.9468,-85.6100,-55),
       ('REEDS LAKE',42.9545,-85.6040,0),('Gaslight\nVillage',42.9521,-85.6150,0),('EGR High\nSchool',42.9483,-85.6140,0),
       ('Wealthy\nElementary',42.9508,-85.6200,0),('◂ John Collins Park',42.9524,-85.6092,0)]
  for s,la,lo,r in lab: ax.text(lo,la,s,color='#c9d6ea' if s!='REEDS LAKE' else '#6f8fbf',fontsize=7.5 if r else 8,rotation=r,ha='center',va='center',zorder=9,family='DejaVu Sans',weight='bold' if s.startswith(('Gas','REE')) else 'normal')
  ax.set_xlim(Wb,E); ax.set_ylim(S,N); ax.set_aspect(1/k); ax.set_xticks([]); ax.set_yticks([])
  for sp in ax.spines.values(): sp.set_color('#2a3a55')
  ax.set_title(title,color='#e6edf7',fontsize=10,loc='left')
  ax.annotate('N',xy=(E-.0012,N-.0012),xytext=(E-.0012,N-.0030),color='w',ha='center',arrowprops=dict(arrowstyle='-|>',color='w'),fontsize=9,zorder=10)
  # scale bar 400 m
  dl=400/(111320*k); ax.plot([Wb+.001,Wb+.001+dl],[S+.0008]*2,color='w',lw=2,zorder=10); ax.text(Wb+.001+dl/2,S+.0013,'400 m',color='w',fontsize=7,ha='center',zorder=10)
  fig.text(.01,.005,'© OpenStreetMap contributors (ODbL). Rendered programmatically; data fetched Oct 2026 via Overpass API.',color='#8ea0bb',fontsize=6.5)
  return fig,ax
def ring(ax,m,col,lab):
  r=m/111320; th=[i/100*2*math.pi for i in range(101)]
  ax.plot([C[1]+r*math.cos(t)/k for t in th],[C[0]+r*math.sin(t) for t in th],color=col,lw=1.5,ls='--',zorder=8)
  ax.text(C[1],C[0]+r+.0002,lab,color=col,fontsize=7,ha='center',zorder=9)
if __name__=='__main__':
  f,a=base('Gaslight Village area, East Grand Rapids: base map'); f.savefig('01-base-dark.png',facecolor=f.get_facecolor(),bbox_inches='tight')
  f,a=base('Walk-shed from Gaslight center (5 min ≈ 400 m, 10 min ≈ 800 m, straight-line)',dim=.8)
  a.plot(C[1],C[0],'o',color='#ffd166',ms=7,zorder=9); ring(a,400,'#ffd166','5 min'); ring(a,800,'#ef8354','10 min')
  f.savefig('02-walkshed.png',facecolor=f.get_facecolor(),bbox_inches='tight')
  f,a=base('Existing bike and path network (OSM)',dim=.7)
  for e in d['elements']:
    t=e.get('tags',{}); h=t.get('highway')
    if 'geometry' not in e: continue
    x,y=xy(e['geometry'])
    if h=='cycleway' or 'Reeds Lake Trail' in t.get('name',''): a.plot(x,y,color='#2ec4b6',lw=2.4,zorder=6)
    elif h=='path': a.plot(x,y,color='#a3e635',lw=1.2,zorder=5)
    elif any(k2.startswith('cycleway') and t[k2] not in('no','separate') for k2 in t): a.plot(x,y,color='#f4a261',lw=2,zorder=6)
    elif h=='footway': a.plot(x,y,color='#7f8fa6',lw=.4,zorder=4)
  from matplotlib.lines import Line2D
  a.legend(handles=[Line2D([],[],color=c,lw=w,label=l) for c,w,l in [('#2ec4b6',2.4,'Reeds Lake Trail / cycleway'),('#a3e635',1.2,'Paths'),('#f4a261',2,'On-street bike tags'),('#7f8fa6',.6,'Sidewalks/footways')]],loc='lower right',fontsize=7,facecolor='#0f1b2d',labelcolor='w',edgecolor='#2a3a55')
  f.savefig('03-bike-paths.png',facecolor=f.get_facecolor(),bbox_inches='tight')
