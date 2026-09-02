# -*- coding: utf-8 -*-
from PIL import Image, ImageOps
import io, base64, os, html

SRC="assets_original"
PAPER=(238,231,218)

def enc(fn, maxdim=980, q=68):
    p=os.path.join(SRC,fn)
    im=Image.open(p); im=ImageOps.exif_transpose(im)
    if im.mode in ("RGBA","P","LA"):
        bg=Image.new("RGB",im.size,PAPER); im=im.convert("RGBA"); bg.paste(im,mask=im.split()[-1]); im=bg
    else: im=im.convert("RGB")
    w,h=im.size; s=min(1.0, maxdim/max(w,h))
    if s<1.0: im=im.resize((round(w*s),round(h*s)), Image.LANCZOS)
    b=io.BytesIO(); im.save(b,"JPEG",quality=q,optimize=True,progressive=True)
    return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()

_cache={}
def uri(fn, **kw):
    key=(fn,tuple(sorted(kw.items())))
    if key not in _cache: _cache[key]=enc(fn,**kw)
    return _cache[key]

# ---------- CONTENT ----------
PROJECTS=[
 dict(id="grandmas-kitchen", title="Grandma's Kitchen",
   cat="Residential · Kitchen",
   cover="abue1_orig.jpg",
   ba=("kitchen-before_orig.jpg","abue1_orig.jpg"),
   story=["For this family, the kitchen has always been more than a place to cook — it is the heart of the home, where everyone gathers. Her daughter dreamed of surprising her with a space that reflected all the warmth she pours into every meal.",
     "I began by studying how the room actually worked: the way morning light filled it, how the layout shaped her routines, and how the underused laundry room next door held real potential. While she was away for a month in Colombia, we opened the wall between the two rooms and introduced a generous island with plenty of storage.",
     "She came home to a kitchen that was brighter, more open, and more functional — and to a reaction that was everything we'd hoped for. More than a renovation, it became a centerpiece that celebrates who she is."],
   gallery=[("kitchen-before_orig.jpg","Before"),("abue1_orig.jpg","After"),("abue2_orig.jpg","After")]),

 dict(id="guest-bath", title="The Guest Bathroom",
   cat="Residential · Bathroom",
   cover="jb4_orig.jpg",
   ba=("bjb1_orig.jpg","jb1_orig.jpg"),
   story=["This guest bathroom was a labor of love. The client wanted her guests to feel truly welcomed, but the existing shower was dated and uninviting.",
     "She trusted me with full creative direction — from selecting the tile to choosing the perfect shower door. I focused on a clean, elegant look that would feel both timeless and warm.",
     "The result is a complete transformation. The space now reflects her hospitality, and her guests agree."],
   gallery=[("bjb1_orig.jpg","Before"),("bjb2_orig.jpg","Before"),("bjb3_orig.jpg","Before"),("jb1_orig.jpg","After"),("jb2_orig.jpg","After"),("jb4_orig.jpg","After")]),

 dict(id="master-bath", title="Master Bathroom Renovation",
   cat="Residential · Bathroom",
   cover="arc1_orig.png",
   ba=("brc1_orig.jpg","arc1_orig.png"),
   story=["This primary bathroom updated an outdated 1980s space to match the elegance of the rest of the home. The vision was modern function paired with timeless style — calm, refined, and a little bit spa.",
     "Clean lines, quality finishes, and a soft neutral palette set a restful mood, while thoughtful layout changes improved the flow. Careful attention to fixtures, surfaces, and lighting tied it back to the rest of the residence.",
     "The result is a restorative retreat that feels cohesive with the home and the way the clients live."],
   gallery=[("brc1_orig.jpg","Before"),("brc2_orig.jpg","Before"),("brc3_orig.jpg","Before"),("arc1_orig.png","After"),("arc2_orig.png","After"),("arc3_orig.png","After")]),

 dict(id="modern-warm", title="Modern Warmth in a Compact Home",
   cat="Residential · Whole Home",
   cover="0ffa019c-b69f-44e7-bd4f-cfbdf2d5c62e_1_orig.jpg",
   ba=("patio-before_1_orig.jpeg","patio-after_1_orig.jpeg"),
   story=["This apartment was a chance to create something fresh and deeply personal. The client wanted a clean slate — a home that felt cozy, stylish, and full of character.",
     "The biggest move was rethinking the kitchen layout. Removing a dividing wall opened up the main living area, improved the flow, and let natural light reach every corner. From there, a warm-but-modern palette and carefully chosen furniture layered in comfort without sacrificing style.",
     "The finished home feels elevated yet lived-in — a seamless blend of function and design that's unmistakably hers."],
   gallery=[("patio-before_1_orig.jpeg","Before"),("screenshot-2023-06-28-at-9-40-17-pm_1_orig.jpeg","Before"),
     ("whatsapp-image-2023-06-21-at-11-00-31-am-copy_1_orig.jpeg","Before"),("whatsapp-image-2023-06-21-at-11-00-32-am-copy_1_orig.jpeg","Before"),
     ("whatsapp-image-2023-06-21-at-11-00-32-am_1_orig.jpeg","Before"),("whatsapp-image-2023-06-21-at-11-00-33-am_1_orig.jpeg","Before"),
     ("patio-after_1_orig.jpeg","After"),("0ffa019c-b69f-44e7-bd4f-cfbdf2d5c62e_1_orig.jpg","After"),
     ("living-room-and-desk_1_orig.jpg","After"),("bedroom-with-paintings_1_orig.jpg","After"),
     ("finish-dining-room_1_orig.png","After"),("island-area_1_orig.png","After")]),

 dict(id="new-beginnings", title="New Beginnings",
   cat="Residential · Apartment",
   cover="f8047d01-936a-4868-bf79-532ec98a5af7_1_orig.jpg",
   ba=None,
   story=["This project was about helping a mother and her young daughter create a real sense of home during a major life transition. The goal was a space that felt safe, grounding, and full of warmth.",
     "The design leaned into comfort and calm: soft textures, a soothing palette, and furniture that balanced function with emotional ease. Natural light was emphasized to keep the apartment open and nurturing, while styling details added personality and a lived-in sense of belonging.",
     "The home now feels warm, welcoming, and hopeful — a fresh start expressed through design."],
   gallery=[("f8047d01-936a-4868-bf79-532ec98a5af7_1_orig.jpg",None),("05a0f1a4-3dc1-4599-92df-0d469411b5d0_1_orig.jpg",None),
     ("5eb812c5-a944-4346-bfba-d1324741112e_1_orig.jpg",None),("9660c2d9-6438-44b3-96e0-6629e14a0dd7_1_orig.jpg",None),
     ("5b57a4fd-f5ea-4ef7-a00b-bf09e1f92bf6_1_orig.jpg",None),("6b266288-fcc6-49cf-b59c-e13a1bd8656c_1_orig.jpg",None),
     ("f5a66807-216b-48d6-8637-424f07a39853_1_orig.jpg",None),("f9fa62fe-f728-492e-9736-6bc6dfc4c0c5_1_orig.jpg",None)]),

 dict(id="compact-45", title="Designing Within 45m²",
   cat="Residential · Small Space · Colombia",
   cover="10_orig.jpg",
   ba=None,
   story=["This 45-square-meter (about 484 sq ft) apartment in Colombia showed just how much is possible in a small footprint. The client wanted a home that felt open and welcoming, with clever storage to make the most of every meter.",
     "The plan prioritized natural light, multifunctional furniture, and built-in storage — efficiency without giving up style. Careful layout and the right pieces made the apartment feel far larger than its square footage.",
     "The result proves that thoughtful design can make even the smallest spaces both beautiful and genuinely livable."],
   gallery=[("01_orig.jpg",None),("02_orig.jpg",None),("03_orig.jpg",None),
     ("04_orig.jpg",None),("05_orig.jpg",None),("06_orig.jpg",None),
     ("07_orig.jpg",None),("08_orig.jpg",None),("09_orig.jpg",None),
     ("10_orig.jpg",None),("11_orig.jpg",None),("12_orig.jpg",None),
     ("13_orig.jpg",None),("14_orig.jpg",None),("15_orig.jpg",None),
     ("17_orig.jpg",None),("19_orig.jpeg",None),("20_orig.jpeg",None),
     ("21_orig.jpeg",None),("22_orig.jpeg",None),("23_orig.jpeg",None),
     ("img-8615_orig.jpeg",None),("img-8622_orig.jpeg",None),("img-8623_orig.jpeg",None)]),

 dict(id="corporate-lobby", title="Corporate Lobby Upgrade",
   cat="Commercial · Lobby & Office",
   cover="img-0202_1_orig.jpeg",
   ba=None,
   story=["As this growing company started attracting higher-profile clients, its lobby no longer matched the brand. First impressions were becoming more important than ever.",
     "The goal was a welcoming, modern space that signaled credibility and attention to detail — a refined layout, clean contemporary furniture, and subtle branding through color, artwork, and finishes. The refresh also extended to the bathroom and kitchenette so the whole office felt cohesive.",
     "The result is a polished, professional environment that sets the tone the moment a client walks through the door."],
   gallery=[("img-9791_1_orig.jpeg","Before"),("img-9792_1_orig.jpeg","Before"),("img-9793_1_orig.jpeg","Before"),
     ("img-9784_1_orig.jpeg","Before"),("img-9785_1_orig.jpeg","Before"),("img-9788_1_orig.jpeg","Before"),
     ("img-0600_1_orig.jpeg","Before"),("img-0601_1_orig.jpeg","Before"),("img-0602_1_orig.jpeg","Before"),
     ("img-0208_1_orig.jpeg","After"),("img-0209-2_1_orig.jpeg","After"),("img-0210-2_1_orig.jpeg","After"),
     ("img-0202_1_orig.jpeg","After"),("img-0203_1_orig.jpeg","After"),("img-0205_1_orig.jpeg","After"),
     ("img-0849_1_orig.jpeg","After"),("img-0938_1_orig.jpeg","After"),("img-0164_1_orig.jpeg","After"),
     ("img-0214_1_orig.jpeg","After"),("img-0217_1_orig.jpeg","After"),("img-0157_1_orig.jpeg","After")]),

 dict(id="the-office", title="The Office",
   cat="Commercial · Office",
   cover="img-0664_1_orig.jpeg",
   ba=None,
   story=["This fast-paced project called for a complete office refresh on a tight timeline and budget — a space that was highly functional and stylish, and that reflected the client's personality.",
     "The brief included added storage, a new desk, and a custom bar area, all within a palette inspired by the client's love of Ohio State. Smart sourcing, clean choices, and multifunctional pieces made it come together quickly without cutting corners.",
     "The finished office is sleek and well-organized — personal yet professional, delivered on time and on budget."],
   gallery=[("img-0130_1_orig.jpeg","Before"),("img-0131_1_orig.jpeg","Before"),("img-0132_1_orig.jpeg","Before"),
     ("img-0841_1_orig.jpeg","Before"),("img-0843_1_orig.jpeg","Before"),("img-0845_1_orig.jpeg","Before"),
     ("office-1_1_orig.jpg","After"),("office-2_1_orig.jpg","After"),("office-4_1_orig.jpg","After"),
     ("img-0664_1_orig.jpeg","After"),("img-1876_1_orig.jpg","After"),("img-1886_1_orig.jpg","After")]),

 dict(id="asheville", title="Modern Functionality in Asheville",
   cat="Residential · Kitchen · Asheville, NC",
   cover="img-5401_orig.jpeg",
   ba=None,
   story=["This kitchen renovation was about modernizing a dated space and making it work harder day to day — more storage, a smarter layout, and a warm, contemporary feel.",
     "We extended the kitchen for more usable space and added a built-in bench with hidden storage for seating and practicality. Reconfigured cabinetry maximized capacity while keeping clean lines, and a mix of closed storage and open shelving added flexibility and warmth. Natural wood tones paired with crisp, light finishes kept everything fresh and open.",
     "The kitchen now feels expansive and inviting — the true heart of the home, designed to elevate everyday living."],
   gallery=[("screenshot-2025-07-07-at-19-32-55_orig.jpeg","Before"),("image-7-7-25-at-19-33_orig.jpg","Before"),
     ("screenshot-2025-07-07-at-19-32-48_orig.jpeg","Before"),
     ("img-5399_orig.jpeg","After"),("img-5398_orig.jpeg","After"),("img-5400_orig.jpeg","After"),
     ("img-5397_orig.jpeg","After"),("img-5403_orig.jpeg","After"),("img-5396_orig.jpeg","After"),
     ("img-5401_orig.jpeg","After"),("img-5406_orig.jpeg","After")]),
]

IMG={}; _keys={}
import re as _re
def _key(fn,tag):
    base=_re.sub(r'[^a-z0-9]','', fn.rsplit('.',1)[0].replace('_orig','').lower())[:22]
    k=(base or 'img')+('' if tag=='p' else tag)
    i=1; kk=k
    while kk in IMG and _keys.get(kk)!=(fn,tag): kk=k+str(i); i+=1
    return kk
def reg(fn, kind='p'):
    # kind: 'p' standard photo, 'h' hero (larger), 'q' portrait
    key=_key(fn,kind)
    if key not in IMG:
        if kind=='h': IMG[key]=uri(fn,maxdim=1200,q=70)
        elif kind=='q': IMG[key]=uri(fn,maxdim=760,q=80)
        else: IMG[key]=uri(fn,maxdim=980,q=64)
        _keys[key]=(fn,kind)
    return key
def esc(s): return html.escape(s, quote=True)

# ---------- build fragments ----------
def card(p):
    return f'''<button class="work-card reveal" data-project="{p['id']}" aria-label="Open project: {esc(p['title'])}">
  <span class="work-card__img"><img data-img="{reg(p['cover'])}" alt="{esc(p['title'])}" loading="lazy"></span>
  <span class="work-card__meta">
    <span class="eyebrow">{esc(p['cat'])}</span>
    <span class="work-card__title">{esc(p['title'])}</span>
    <span class="work-card__cue">View project</span>
  </span>
</button>'''

def ba_block(p):
    if not p.get("ba"): return ""
    before,after=p["ba"]
    lb,la=p.get("ba_labels",("Before","After"))
    return f'''<div class="ba" role="group" aria-label="Before and after comparison. Use the slider to compare.">
  <img class="ba-img ba-after" data-img="{reg(after)}" alt="After">
  <img class="ba-img ba-before" data-img="{reg(before)}" alt="Before">
  <span class="ba-tag ba-tag--l">{esc(lb)}</span>
  <span class="ba-tag ba-tag--r">{esc(la)}</span>
  <div class="ba-line" aria-hidden="true"></div>
  <button class="ba-handle" role="slider" aria-label="Compare before and after"
     aria-valuemin="0" aria-valuemax="100" aria-valuenow="50" tabindex="0">
     <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6L4 12l5 6M15 6l5 6-5 6"/></svg>
  </button>
</div>'''

def gallery(p):
    items=[]
    for fn,label in p["gallery"]:
        tag=f'<span class="g-tag">{esc(label)}</span>' if label else ""
        k=reg(fn)
        items.append(f'''<button class="g-item" data-full="{k}" aria-label="View larger image">
  <img data-img="{k}" alt="{esc(p['title'])} photo" loading="lazy">{tag}</button>''')
    return '<div class="gallery">'+''.join(items)+'</div>'

def modal(p):
    story=''.join(f'<p>{esc(par)}</p>' for par in p['story'])
    ba=ba_block(p)
    ba_hint='<p class="ba-hint">Drag the handle to compare before &amp; after.</p>' if p.get("ba") else ""
    return f'''<article class="project" id="project-{p['id']}" role="dialog" aria-modal="true" aria-labelledby="pt-{p['id']}" hidden>
  <div class="project__inner">
    <button class="project__close" data-close aria-label="Close project">&times;</button>
    <span class="eyebrow">{esc(p['cat'])}</span>
    <h3 class="project__title" id="pt-{p['id']}">{esc(p['title'])}</h3>
    <div class="project__story">{story}</div>
    {ba}{ba_hint}
    <h4 class="project__gh">Gallery</h4>
    {gallery(p)}
  </div>
</article>'''

cards="\n".join(card(p) for p in PROJECTS)
modals="\n".join(modal(p) for p in PROJECTS)

HERO=reg("img-5396_orig.jpeg","h")
PORTRAIT=reg("facetune_orig.png","q")
ABOUT_IMG=reg("finish-dining-room_1_orig.png")
import json as _json
img_json=_json.dumps(IMG)

# ---------- assemble ----------
CSS = open("style.css").read()
JS  = open("script.js").read()

import json as _json
HTML = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rocío Fuhrmeister — Interior Design</title>
<meta name="description" content="Rocío Fuhrmeister is an interior designer creating warm, functional residential and commercial spaces — kitchens, baths, whole-home design, and offices.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#work">Skip to gallery</a>

<header class="nav" id="nav">
  <div class="wrap nav__row">
    <a class="brand" href="#top" aria-label="Rocío Fuhrmeister, Interior Design — home">
      <span class="brand__mark">RF</span>
      <span class="brand__txt"><b>Rocío Fuhrmeister</b><i>Interior Design</i></span>
    </a>
    <nav class="nav__links" aria-label="Primary">
      <a href="#studio">Studio</a>
      <a href="#work">Gallery</a>
      <a class="nav__cta" href="#contact">Get in touch</a>
    </nav>
    <button class="nav__toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <nav aria-label="Mobile">
    <a href="#studio">Studio</a><a href="#work">Gallery</a><a href="#contact">Get in touch</a>
  </nav>
</div>

<main id="top">
  <!-- HERO -->
  <section class="hero">
    <div class="wrap hero__grid">
      <div class="hero__copy">
        <span class="eyebrow">Interior Design · Residential &amp; Commercial</span>
        <h1 class="hero__title">Designing spaces<br>that feel like <em>you</em>.</h1>
        <p class="hero__lede">I'm Rocío Fuhrmeister — an interior designer helping homeowners and businesses turn ordinary rooms into warm, functional spaces they love to live and work in.</p>
        <div class="hero__cta">
          <a class="btn btn--solid" href="#work">View the gallery</a>
          <a class="btn btn--ghost" href="#contact">Book a consultation</a>
        </div>
        <p class="hero__meta">Kitchens · Baths · Whole-home · Commercial</p>
      </div>
      <div class="hero__media">
        <div class="hero__frame"><img data-img="{HERO}" alt="A bright kitchen and dining room designed by Rocío Fuhrmeister"></div>
      </div>
    </div>
  </section>

  <!-- STUDIO / ABOUT -->
  <section class="studio section" id="studio">
    <div class="wrap studio__grid">
      <div class="studio__media reveal">
        <img class="studio__portrait" data-img="{PORTRAIT}" alt="Portrait of Rocío Fuhrmeister">
      </div>
      <div class="studio__copy reveal">
        <span class="eyebrow">The studio</span>
        <h2 class="h-section">Where the heart is</h2>
        <p>Hi, I'm Rocío — an interior designer with a background in graphic design and a lifelong love of transforming spaces. As a kid I was forever rearranging rooms (sometimes the whole house) just to feel how a new layout could change the energy of a place.</p>
        <p>I've always been drawn to the details: the light, the flow, the textures, and the way every element comes together in harmony. Years as a graphic designer taught me color, balance, and visual storytelling — instincts that carry straight into my interiors. During the 2020 lockdown I earned my interior design certification and turned what I'd been doing for family and friends for years into work I'm proud to be paid for.</p>
        <p>Whether you're refreshing a single room or reimagining an entire home, I'd love to help you create a space that feels like you — one that reflects your style, supports your life, and brings you a little joy every day.</p>
        <p class="signature">Rocío</p>
      </div>
    </div>
  </section>

  <!-- SERVICES -->
  <section class="services section" id="services">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Services</span>
        <h2 class="h-section">How I can help</h2>
        <p class="section-head__lede">Full projects or a single room — here's where I most often step in.</p>
      </div>
      <div class="svc-grid">
        <div class="svc reveal"><h3>Full-Home Design</h3><p>From layout to the last cushion, one cohesive plan for your whole home. Ideal for new builds, fresh starts, and homes ready for a head-to-toe transformation.</p></div>
        <div class="svc reveal"><h3>Single-Room Refresh</h3><p>One room, reimagined. Perfect when a living room, bedroom, or nursery needs new life without a full renovation.</p></div>
        <div class="svc reveal"><h3>Kitchen &amp; Bath Renovation</h3><p>The rooms that work hardest, redesigned for how you actually live — smarter layouts, lasting materials, and finishes that feel timeless.</p></div>
        <div class="svc reveal"><h3>Commercial &amp; Office</h3><p>Lobbies, offices, and workspaces that make the right first impression and reflect your brand — functional, polished, and welcoming.</p></div>
      </div>
    </div>
  </section>

  <!-- PROCESS -->
  <section class="process section" id="process">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">The process</span>
        <h2 class="h-section">How we'll work together</h2>
        <p class="section-head__lede">A clear path from first conversation to the day you move back in.</p>
      </div>
      <ol class="steps">
        <li class="step reveal"><span class="step__n">01</span><h3>Consultation</h3><p>We start with a conversation about how you live, what's not working, and the feeling you're after. I see the space, take measurements, and listen.</p></li>
        <li class="step reveal"><span class="step__n">02</span><h3>Concept &amp; Design</h3><p>I turn your goals into a clear plan — layouts, palettes, materials, and furnishings — presented so you can picture the finished room before a thing is moved.</p></li>
        <li class="step reveal"><span class="step__n">03</span><h3>Sourcing &amp; Styling</h3><p>I source every piece, coordinate the trades, and manage the details, so the project stays on track and you don't have to chase anything.</p></li>
        <li class="step reveal"><span class="step__n">04</span><h3>The Reveal</h3><p>We bring it all together and step into a space that finally feels like home. This is my favorite part.</p></li>
      </ol>
    </div>
  </section>

  <!-- WORK -->
  <section class="work section" id="work">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Gallery</span>
        <h2 class="h-section">Recent projects</h2>
        <p class="section-head__lede">A few of the spaces that have deepened my love for this work. Tap any project to see the story and full gallery.</p>
      </div>
      <div class="work-grid">
        {cards}
      </div>
    </div>
  </section>

  <!-- QUOTE -->
  <section class="quote section">
    <div class="wrap">
      <blockquote class="reveal">
        <p>"A home should feel like the people in it — their style, their rhythm, the small things that bring them joy."</p>
        <cite>Rocío Fuhrmeister</cite>
      </blockquote>
    </div>
  </section>

  <!-- CONTACT -->
  <section class="contact section" id="contact">
    <div class="wrap contact__grid">
      <div class="contact__copy reveal">
        <span class="eyebrow">Get in touch</span>
        <h2 class="h-section">Let's bring your<br>space to life.</h2>
        <p>Tell me a little about your project and I'll be in touch soon.</p>
        <ul class="contact__list">
          <li><span>Email</span><a href="mailto:zurcfuhrmeister@gmail.com">zurcfuhrmeister@gmail.com</a></li>
          <li><span>Based in</span>North Carolina · available locally &amp; remotely</li>
          <li><span>Phone</span><a href="tel:+19417801547">(941) 780-1547</a></li>
          <li><span>Consultation</span>90-minute session · $125</li>
        </ul>
      </div>
      <form class="contact__form reveal" id="contactForm" novalidate>
        <div class="field"><label for="cf-name">Name</label><input id="cf-name" name="name" type="text" autocomplete="name" required></div>
        <div class="field"><label for="cf-email">Email</label><input id="cf-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="cf-type">Project type</label>
          <select id="cf-type" name="type">
            <option>Full-home design</option><option>Single-room refresh</option>
            <option>Kitchen &amp; bath renovation</option><option>Commercial / office</option><option>Not sure yet</option>
          </select>
        </div>
        <div class="field"><label for="cf-msg">Tell me about your project</label><textarea id="cf-msg" name="message" rows="4" required></textarea></div>
        <button class="btn btn--solid" type="submit">Send message</button>
        <p class="form-note" id="formNote" role="status"></p>
      </form>
    </div>
  </section>
</main>

<footer class="foot">
  <div class="wrap foot__row">
    <div class="foot__brand"><b>Rocío Fuhrmeister</b><span>Interior Design</span></div>
    <nav class="foot__nav" aria-label="Footer">
      <a href="#studio">Studio</a><a href="#work">Gallery</a><a href="#services">Services</a>
      <a href="#process">Process</a><a href="#contact">Contact</a>
    </nav>
    <p class="foot__copy">© <span id="yr"></span> Rocío Fuhrmeister · Interior Design</p>
  </div>
</footer>

<!-- project modals -->
<div class="overlay" id="overlay" hidden>
  {modals}
</div>

<!-- lightbox -->
<div class="lightbox" id="lightbox" hidden>
  <button class="lightbox__close" aria-label="Close image">&times;</button>
  <img id="lightboxImg" src="" alt="Enlarged project image">
</div>

<script>window.__IMG__={img_json};</script>
<script>{JS}</script>
</body>
</html>'''

with open("index.html","w") as f: f.write(HTML)
size=os.path.getsize("index.html")
print(f"index.html written: {size/1e6:.2f} MB")
