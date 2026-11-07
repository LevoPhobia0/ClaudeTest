import json,sys,math
d,out=sys.argv[1],sys.argv[2]
B=(32.40,39.62,33.25,40.15)
def rdp(pts,eps):
    if len(pts)<3: return pts
    a,b=pts[0],pts[-1]; dx,dy=b[0]-a[0],b[1]-a[1]; L=math.hypot(dx,dy) or 1e-12
    imax,dmax=0,0
    for i in range(1,len(pts)-1):
        p=pts[i]; dd=abs(dy*p[0]-dx*p[1]+b[0]*a[1]-b[1]*a[0])/L if L>1e-12 else math.hypot(p[0]-a[0],p[1]-a[1])
        if dd>dmax: imax,dmax=i,dd
    if dmax>eps: return rdp(pts[:imax+1],eps)[:-1]+rdp(pts[imax:],eps)
    return [a,b]
def r(p): return [round(p[1],4),round(p[0],4)]
def polys(g):
    if g['type']=='Polygon': return [g['coordinates']]
    if g['type']=='MultiPolygon': return g['coordinates']
    return []
def lines(g):
    if g['type']=='LineString': return [g['coordinates']]
    if g['type']=='MultiLineString': return g['coordinates']
    return []
def bbox(cs):
    xs=[c[0] for c in cs]; ys=[c[1] for c in cs]; return min(xs),min(ys),max(xs),max(ys)
def inter(b): return not(b[2]<B[0] or b[0]>B[2] or b[3]<B[1] or b[1]>B[3])
G={'districts':[],'urban':[],'roads':[]}
adm=json.load(open(d+'/adm2.geojson',encoding='utf-8'))
for f in adm['features']:
    ps=polys(f['geometry']); allc=[c for p in ps for ring in p for c in ring]
    if not allc or not inter(bbox(allc)): continue
    rings=[]
    for p in ps:
        ring=rdp(p[0],0.0012)
        if len(ring)>=4: rings.append([r(c) for c in ring])
    # label point: area-weighted centroid of largest ring
    big=max(ps,key=lambda p:len(p[0]))[0]
    A=cx=cy=0
    for i in range(len(big)-1):
        x0,y0=big[i][:2]; x1,y1=big[i+1][:2]; cr=x0*y1-x1*y0; A+=cr; cx+=(x0+x1)*cr; cy+=(y0+y1)*cr
    A/=2; cx/=6*A; cy/=6*A
    G['districts'].append({'n':f['properties']['shapeName'],'c':[round(cy,4),round(cx,4)],'p':rings})
ua=json.load(open(d+'/ne_10m_urban_areas.geojson',encoding='utf-8'))
for f in ua['features']:
    for p in polys(f['geometry']):
        if inter(bbox(p[0])): G['urban'].append([r(c) for c in rdp(p[0],0.0008)])
rd=json.load(open(d+'/ne_10m_roads.geojson',encoding='utf-8'))
for f in rd['features']:
    for l in lines(f['geometry']):
        if len(l)>1 and inter(bbox(l)):
            G['roads'].append({'t':1 if f['properties'].get('type')=='Major Highway' else 2,'c':[r(c) for c in rdp(l,0.0005)]})
js='const GEO='+json.dumps(G,ensure_ascii=False,separators=(',',':'))+';'
open(out,'w',encoding='utf-8').write(js)
print(len(js),len(G['districts']),len(G['urban']),len(G['roads']),sum(len(x['c']) for x in G['roads']))
