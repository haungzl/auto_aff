"""Download selected free-to-use Pexels photos at editorial size."""
import io, json, time, urllib.request
from pathlib import Path
from PIL import Image

root=Path(__file__).parent; selected=json.loads((root/'pexels_selected.json').read_text()); out=root/'public'/'images';out.mkdir(exist_ok=True)
for rec in selected:
    dest=out/f'article-{rec["index"]:02d}.webp'
    if dest.exists() and dest.stat().st_size>10000:
        rec['file']='/images/'+dest.name;print(rec['index'],'cached',flush=True);continue
    url=f'https://images.pexels.com/photos/{rec["id"]}/pexels-photo-{rec["id"]}.jpeg?auto=compress&cs=tinysrgb&w=1400'
    for attempt in range(5):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            data=urllib.request.urlopen(req,timeout=25).read()
            img=Image.open(io.BytesIO(data)).convert('RGB')
            img.thumbnail((1400,1000))
            img.save(dest,'WEBP',quality=82,method=6)
            rec['file']='/images/'+dest.name
            print(rec['index'],rec['id'],dest.stat().st_size,flush=True)
            break
        except Exception as e:
            if attempt==4:print('FAILED',rec['index'],str(e),flush=True)
            time.sleep(1)
(root/'image_credits.json').write_text(json.dumps(selected,indent=2))
