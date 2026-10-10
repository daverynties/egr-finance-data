from render import *
from matplotlib.patches import Polygon as P
from matplotlib.lines import Line2D
# Geometry in (lat,lon). Wealthy/Lakeside node 42.94966,-85.61185. Site N of Wealthy, W of Lakeside.
site=[(42.9506,-85.6158),(42.9530,-85.6150),(42.9534,-85.6134),(42.9500,-85.6122)]
green=[(42.9516,-85.6131),(42.9524,-85.6129),(42.9521,-85.6124),(42.9512,-85.6125)]
lakewalk=[(42.9497,-85.6135),(42.9504,-85.6140),(42.9512,-85.6133),(42.9518,-85.6127),(42.9522,-85.6119),(42.9524,-85.6113)]
hub=(42.9516,-85.6153)
xing=[(42.94985,-85.6122),(42.9503,-85.6136),(42.9510,-85.6151),(42.9519,-85.6123)]
def L(ax,pts,**k): ax.plot([p[1] for p in pts],[p[0] for p in pts],**k)
def wayline(ax,name,col,lw,lo=None,hi=None,minlat=None):
  for e in d['elements']:
    t=e.get('tags',{})
    if t.get('name','').startswith(name) and 'geometry' in e:
      g=[p for p in e['geometry'] if (lo is None or p['lon']>=lo) and (hi is None or p['lon']<=hi) and (minlat is None or p['lat']>=minlat)]
      if len(g)>1: ax.plot([p['lon'] for p in g],[p['lat'] for p in g],color=col,lw=lw,zorder=6,solid_capstyle='round',alpha=.9)
def ped(ax):
  ax.add_patch(P([(b,a) for a,b in site],fc='#ffd16633',ec='#ffd166',lw=1.5,ls='--',zorder=5))
  ax.add_patch(P([(b,a) for a,b in green],fc='#2ec4b6',ec='w',lw=.6,zorder=6))
  L(ax,lakewalk,color='#ffd166',lw=3.5,zorder=7)
  wayline(ax,'Wealthy Street','#ffb3c1',4,lo=-85.6200)
  for a,b in xing: ax.plot(b,a,'s',color='w',ms=5,zorder=8)
  ax.text(-85.6168,42.9540,'Car-free core\n(service/emergency only)',color='#ffd166',fontsize=7,ha='center',zorder=9)
  ax.text(-85.6112,42.9512,'Village Green\n(1 ac, deeded)',color='#2ec4b6',fontsize=6.5,zorder=9)
def bikes(ax):
  wayline(ax,'Reeds Lake Trail','#2ec4b6',3.2); wayline(ax,'Lakeside Drive','#2ec4b6',3.2,minlat=42.9462)
  wayline(ax,'Lake Drive Southeast','#f77f00',2.8,hi=-85.6105)
  for n in ['Greenwood Avenue','Bagley Avenue']: wayline(ax,n,'#a3e635',2.6)
  wayline(ax,'Wealthy Street','#a3e635',2.6,lo=-85.6215)
def shuttle(ax):
  loop=[hub,(42.9510,-85.6150),(42.9500,-85.6122),(42.9488,-85.6118),(42.9470,-85.6112),(42.9466,-85.6107),(42.9480,-85.6145),(42.9496,-85.6176),(42.9506,-85.6165),hub]
  L(ax,loop,color='#c77dff',lw=2.6,ls=(0,(4,2)),zorder=7)
  for s in [(42.9488,-85.6118),(42.9466,-85.6107),(42.9496,-85.6176),(42.9524,-85.6119)]: ax.plot(s[1],s[0],'o',color='#c77dff',mec='w',ms=6,zorder=8)
  ax.plot(hub[1],hub[0],'H',color='#ff6b6b',mec='w',ms=15,zorder=9)
  ax.text(hub[1]-.0035,hub[0]+.0016,'Edge mobility hub\n(220–300 cars, bike hall,\nservice court, shuttle bays)',color='#ff6b6b',fontsize=6.5,ha='right',zorder=9)
LEG={'ped':[('#ffd166',3.5,'Lake Walk (spine)'),('#ffb3c1',4,'Wealthy 20 mph village street'),('#2ec4b6',6,'Village Green'),('w',0,'■ raised crossings')],
 'bike':[('#2ec4b6',3,'Reeds Lake Ring'),('#a3e635',2.6,'School Loop (greenways + Wealthy)'),('#f77f00',2.8,'Grand Rapids link (Lake Dr)')],
 'sh':[('#c77dff',2.6,'Shuttle → autonomous loop'),('#ff6b6b',6,'Edge mobility hub')]}
def leg(ax,keys):
  h=[Line2D([],[],color=c,lw=w,label=l) for k in keys for c,w,l in LEG[k]]
  ax.legend(handles=h,loc='lower right',fontsize=6.5,facecolor='#0f1b2d',labelcolor='w',edgecolor='#2a3a55')
NOTE='Concept overlay (schematic, not engineered) on real OSM base.'
for fn,title,fs,keys in [('04-concept-pedestrian-core.png','Concept: car-free core and Lake Walk',[ped],['ped']),
  ('05-concept-bike-loops.png','Concept: three bike loops',[bikes],['bike']),
  ('06-concept-shuttle-hub.png','Concept: edge mobility hub and shuttle/pod loop',[shuttle],['sh']),
  ('07-concept-combined.png','Gaslight Village 2040: Lake Walk Plan (combined concept)',[bikes,ped,shuttle],['ped','bike','sh'])]:
  f,a=base(title+' — '+NOTE,dim=.6)
  for g in fs: g(a)
  leg(a,keys); f.savefig(fn,facecolor=f.get_facecolor(),bbox_inches='tight'); plt.close(f)
