import json, copy, validate_city as V
D=json.load(open('city.json'))
def run(name, fn):
    d=copy.deepcopy(D); fn(d); json.dump(d,open('/tmp/mut.json','w'))
    rep=V.validate('/tmp/mut.json'); fails=[c['id'] for c in rep['checks'] if not c['ok']]
    print(f"{name:55s} -> {fails}")
B=lambda d:d['buildings']
def m1(d): B(d)['x'][500],B(d)['y'][500]=0.0,0.0
def m2(d): d['landmarks'][0]['num']+=2; 
def m3(d): B(d)['now'][1000]+=1
def m4(d): B(d)['num'][2000]+=2
def m5(d):
    a=next(s for s in d['streets'] if s['axis']=='EW' and s['cls']=='L'); b=next(s for s in d['streets'] if s['axis']=='NS' and s['cls']=='L'); b['name']=a['name']
def m6(d): B(d)['lv'][300]=40
def m7(d): d['sites'][0]['bi']=0
def m8(d): d['streets'].append(dict(id=len(d['streets']),name='Ghost Road',cls='L',kind='lattice',axis='EW',ward='oldtown',w=10,yard=3,pts=[[-300,-300],[300,-300]]))
def m9(d): B(d)['x'][700]=B(d)['x'][701]; B(d)['y'][700]=B(d)['y'][701]
def m10(d):
    i=next(i for i,v in enumerate(d['buildings']['now']) if v>0); d['buildings']['status'][i]=1
for n,f in [('building teleported into the river',m1),('landmark address number edited',m2),('one extra resident',m3),('building address number changed',m4),('two streets share a name',m5),('building 40 storeys',m6),('site re-pointed to the wrong building',m7),('street laid across the river',m8),('two buildings stacked on each other',m9),('occupied building flagged derelict',m10)]:
    run(n,f)
