import streamlit as st
from career_engine import recommend_careers

st.set_page_config(
    page_title="FutureMirror AI",
    page_icon="🪞",
    layout="wide"
)

# ═══════════════════════════════════════════════════════════════
# GLOBAL SPACE THEME — Starry Night inspired
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

/* ── Root palette — Van Gogh Starry Night inspired ── */
:root {
  --space-bg:      #050714;
  --space-mid:     #0a0d26;
  --nebula-purple: #1a0a3d;
  --nebula-blue:   #0a1a4a;
  --nebula-teal:   #062a3a;
  --purple-bright: #7C3AED;
  --purple-light:  #a78bfa;
  --purple-pale:   #c4b5fd;
  --indigo:        #4F46E5;
  --gold:          #f4c430;
  --gold-dim:      #a87d10;
  --cyan-glow:     #38bdf8;
  --card-bg:       rgba(255,255,255,0.038);
  --card-border:   rgba(167,139,250,0.18);
  --text-main:     #e2e8f0;
  --text-muted:    #94a3b8;
  --green-accent:  #10b981;
  --amber-accent:  #f59e0b;
}

/* ── Full-page dark space background ── */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"] {
  background: var(--space-bg) !important;
  font-family: 'Inter', sans-serif !important;
  color: var(--text-main) !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: rgba(8,8,30,0.97) !important;
  border-right: 1px solid var(--card-border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-main) !important; }
[data-testid="stSidebar"] .stRadio label {
  color: var(--purple-pale) !important;
  font-size: 15px !important;
}

/* ── Main content wrapper ── */
[data-testid="stMainBlockContainer"],
.main .block-container {
  background: transparent !important;
  position: relative;
  z-index: 1;
}

/* ── Headings & body text ── */
h1, h2, h3, h4, h5, h6 { color: var(--purple-pale) !important; }
p, li, span, div         { color: var(--text-main); }
label                    { color: var(--text-muted) !important; }

/* ── Streamlit native widgets ── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] div[data-baseweb],
[data-testid="stMultiSelect"] div[data-baseweb] {
  background: rgba(255,255,255,0.05) !important;
  border: 1px solid var(--card-border) !important;
  color: var(--text-main) !important;
  border-radius: 10px !important;
}
/* ── Slider — subtle dark track with a thin accent ── */
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
  background: var(--purple-pale) !important;
  border: 2px solid var(--purple-bright) !important;
  box-shadow: 0 0 8px rgba(124,58,237,0.5) !important;
  width: 18px !important;
  height: 18px !important;
}
/* track fill (the colored portion to the left of thumb) */
[data-testid="stSlider"] [data-baseweb="slider"] div[class*="Track"] div:first-child {
  background: linear-gradient(90deg, var(--indigo), var(--purple-bright)) !important;
  height: 4px !important;
}
/* track background (unfilled right side) */
[data-testid="stSlider"] [data-baseweb="slider"] div[class*="Track"] {
  background: rgba(255,255,255,0.08) !important;
  height: 4px !important;
}
/* kill the full-width purple fill that Streamlit injects */
[data-testid="stSlider"] div[data-baseweb="slider"] > div {
  background: transparent !important;
}
[data-testid="stSlider"] div[data-baseweb="slider"] {
  background: transparent !important;
}
/* The inner progress/fill div Streamlit uses */
[data-testid="stSlider"] [data-baseweb="slider"] div[style*="background"] {
  background: linear-gradient(90deg, var(--indigo), var(--purple-bright)) !important;
}
/* Override any full-block purple */
[data-testid="stSlider"] * {
  background-color: transparent !important;
}
[data-testid="stSlider"] [role="slider"] {
  background-color: var(--purple-pale) !important;
}
[data-testid="stSlider"] [data-testid="stTickBarMin"],
[data-testid="stSlider"] [data-testid="stTickBarMax"] {
  color: var(--text-muted) !important;
  font-size: 12px !important;
}

/* ── Buttons ── */
[data-testid="stButton"] button {
  background: linear-gradient(135deg, var(--indigo), var(--purple-bright)) !important;
  color: white !important;
  border: none !important;
  border-radius: 12px !important;
  font-weight: 600 !important;
  letter-spacing: 0.5px !important;
  transition: opacity .2s, transform .15s, box-shadow .2s !important;
}
[data-testid="stButton"] button:hover {
  opacity: 0.9 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 0 22px rgba(124,58,237,0.5) !important;
}

/* ── Expanders ── */
[data-testid="stExpander"] {
  background: var(--card-bg) !important;
  border: 1px solid var(--card-border) !important;
  border-radius: 14px !important;
}
[data-testid="stExpander"] summary { color: var(--purple-pale) !important; }

/* ── Metrics ── */
[data-testid="stMetric"] {
  background: rgba(124,58,237,0.12) !important;
  border-radius: 10px !important;
  padding: 8px 14px !important;
  border: 1px solid var(--card-border) !important;
}
[data-testid="stMetricValue"] { color: var(--purple-pale) !important; }

/* ── Info / success / warning boxes ── */
[data-testid="stAlert"] {
  background: rgba(255,255,255,0.04) !important;
  border-radius: 12px !important;
  border: 1px solid var(--card-border) !important;
  color: var(--text-main) !important;
}

/* ── Divider ── */
hr { border-color: var(--card-border) !important; opacity: 0.5; }

/* ── Progress bar ── */
[data-testid="stProgressBar"] div {
  background: linear-gradient(90deg, var(--indigo), var(--purple-bright), var(--cyan-glow)) !important;
}

/* ── Containers with border ── */
[data-testid="stVerticalBlock"] [data-testid="stVerticalBlockBorderWrapper"] {
  background: var(--card-bg) !important;
  border: 1px solid var(--card-border) !important;
  border-radius: 14px !important;
}

/* ─────────────────────────────────────────────────────────────
   STARRY NIGHT CANVAS — full-page animated background
───────────────────────────────────────────────────────────── */
#starry-canvas {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  pointer-events: none;
  z-index: 0;
}

/* ─── Drifting rockets ─── */
@keyframes rocketDrift1 {
  0%   { transform: translate(0,0)      rotate(-42deg); }
  20%  { transform: translate(22px,-15px) rotate(-38deg); }
  50%  { transform: translate(8px,-28px)  rotate(-46deg); }
  75%  { transform: translate(-12px,-12px) rotate(-41deg); }
  100% { transform: translate(0,0)      rotate(-42deg); }
}
@keyframes rocketDrift2 {
  0%   { transform: translate(0,0)       rotate(135deg); }
  33%  { transform: translate(-18px,10px) rotate(131deg); }
  66%  { transform: translate(-6px,20px)  rotate(138deg); }
  100% { transform: translate(0,0)       rotate(135deg); }
}
@keyframes rocketDrift3 {
  0%   { transform: translate(0,0)      rotate(-60deg); }
  40%  { transform: translate(14px,-18px) rotate(-55deg); }
  70%  { transform: translate(-8px,-22px) rotate(-63deg); }
  100% { transform: translate(0,0)      rotate(-60deg); }
}
.drift-rocket {
  position: fixed;
  pointer-events: none;
  z-index: 2;
  filter: drop-shadow(0 0 12px rgba(167,139,250,0.7));
}
.drift-rocket.r1 {
  font-size: 30px; top: 10vh; right: 6vw;
  animation: rocketDrift1 9s ease-in-out infinite;
  opacity: 0.72;
}
.drift-rocket.r2 {
  font-size: 20px; top: 60vh; left: 3vw;
  animation: rocketDrift2 14s ease-in-out infinite;
  animation-delay: -5s;
  opacity: 0.45;
}
.drift-rocket.r3 {
  font-size: 16px; top: 35vh; right: 2vw;
  animation: rocketDrift3 11s ease-in-out infinite;
  animation-delay: -3s;
  opacity: 0.35;
  filter: drop-shadow(0 0 8px rgba(56,189,248,0.6));
}

/* ─── Hero ─── */
@keyframes heroGlow {
  0%,100% { box-shadow: 0 0 50px rgba(124,58,237,0.28), 0 0 100px rgba(56,189,248,0.06); }
  50%      { box-shadow: 0 0 80px rgba(124,58,237,0.5),  0 0 140px rgba(56,189,248,0.12); }
}
@keyframes heroSwirl {
  0%   { transform: rotate(0deg)   scale(1); }
  50%  { transform: rotate(180deg) scale(1.08); }
  100% { transform: rotate(360deg) scale(1); }
}
.space-hero {
  position: relative;
  background: linear-gradient(135deg, #13063d 0%, #0b0a2e 35%, #071836 70%, #0a0d26 100%);
  border: 1px solid rgba(167,139,250,0.28);
  border-radius: 24px;
  padding: 60px 40px;
  text-align: center;
  margin-bottom: 28px;
  overflow: hidden;
  animation: heroGlow 5s ease-in-out infinite;
}
/* Van Gogh swirl overlays inside hero */
.space-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 120% 60% at 20% 40%, rgba(79,70,229,0.12) 0%, transparent 55%),
    radial-gradient(ellipse 80% 80%  at 80% 20%, rgba(124,58,237,0.10) 0%, transparent 55%),
    radial-gradient(ellipse 100% 50% at 50% 90%, rgba(56,189,248,0.06) 0%, transparent 55%);
  pointer-events: none;
}
.space-hero h1 {
  font-size: 52px !important;
  font-weight: 700 !important;
  color: #ffffff !important;
  margin-bottom: 10px;
  letter-spacing: -1px;
  text-shadow: 0 0 30px rgba(167,139,250,0.6), 0 0 60px rgba(124,58,237,0.3);
}
.space-hero p {
  font-size: 19px;
  color: var(--purple-pale);
  margin: 0;
}
/* Hero twinkling stars */
.hero-star {
  position: absolute;
  border-radius: 50%;
  background: white;
  animation: twinkle ease-in-out infinite;
}
/* Hero sparkle cross-stars */
.hero-sparkle {
  position: absolute;
  font-size: 14px;
  color: rgba(244,196,48,0.7);
  animation: twinkle ease-in-out infinite;
  text-shadow: 0 0 8px rgba(244,196,48,0.9);
}
@keyframes twinkle {
  0%,100% { opacity:0.12; transform:scale(0.6); }
  50%      { opacity:1;    transform:scale(1.4); }
}

/* ─── Space card ─── */
.space-card {
  background: rgba(255,255,255,0.035);
  border: 1px solid rgba(167,139,250,0.15);
  border-radius: 18px;
  padding: 28px;
  margin-top: 18px;
  backdrop-filter: blur(8px);
  transition: border-color .3s, box-shadow .3s;
}
.space-card:hover {
  border-color: rgba(167,139,250,0.3);
  box-shadow: 0 0 30px rgba(124,58,237,0.1);
}
.space-card h2, .space-card h3 {
  color: var(--purple-pale) !important;
}

/* ─── Feature rows ─── */
.feat-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid rgba(167,139,250,0.08);
}
.feat-icon { font-size: 22px; min-width: 30px; }
.feat-text { color: var(--text-main); font-size: 15px; line-height:1.5; }

/* ─── Quote ─── */
.space-quote {
  text-align: center;
  font-size: 20px;
  font-style: italic;
  color: var(--purple-pale);
  padding: 28px 20px;
  margin: 24px 0;
  border-top: 1px solid rgba(167,139,250,0.15);
  border-bottom: 1px solid rgba(167,139,250,0.15);
  text-shadow: 0 0 20px rgba(167,139,250,0.3);
}

/* ─── Career library card ─── */
.lib-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(167,139,250,0.13);
  border-radius: 14px;
  padding: 20px 22px;
  margin-bottom: 12px;
  transition: border-color .2s, background .2s, box-shadow .2s;
}
.lib-card:hover {
  border-color: rgba(167,139,250,0.4);
  background: rgba(124,58,237,0.07);
  box-shadow: 0 0 20px rgba(124,58,237,0.12);
}
.lib-card h4 { color: var(--purple-pale) !important; margin:0 0 6px 0; }
.lib-card p  { color: var(--text-muted); margin: 3px 0; font-size:14px; }
.lib-badge {
  display: inline-block;
  background: rgba(124,58,237,0.18);
  border: 1px solid rgba(167,139,250,0.25);
  border-radius: 6px;
  padding: 2px 9px;
  font-size: 12px;
  color: var(--purple-pale);
  margin-right: 6px;
  margin-top: 6px;
}

/* ─── About stat card ─── */
.stat-card {
  background: rgba(124,58,237,0.1);
  border: 1px solid rgba(167,139,250,0.2);
  border-radius: 14px;
  padding: 22px;
  text-align: center;
  transition: box-shadow .3s;
}
.stat-card:hover {
  box-shadow: 0 0 25px rgba(124,58,237,0.2);
}
.stat-card .num {
  font-size: 36px;
  font-weight: 700;
  color: var(--purple-pale);
}
.stat-card .lbl {
  font-size: 13px;
  color: var(--text-muted);
  margin-top: 4px;
}

/* ─── Floating decorative stars scattered on page ─── */
@keyframes floatStar {
  0%,100% { transform: translateY(0px) rotate(0deg);   opacity: 0.55; }
  33%      { transform: translateY(-8px) rotate(15deg);  opacity: 0.9;  }
  66%      { transform: translateY(4px) rotate(-10deg); opacity: 0.4;  }
}
.page-star {
  position: fixed;
  pointer-events: none;
  z-index: 1;
  animation: floatStar ease-in-out infinite;
  font-size: 16px;
  color: rgba(196,181,253,0.6);
  text-shadow: 0 0 10px rgba(167,139,250,0.8);
}

/* ─── Shooting star overlay divs ─── */
@keyframes shootStar {
  0%   { transform: translateX(0) translateY(0) scaleX(1); opacity: 0; }
  5%   { opacity: 1; }
  100% { transform: translateX(600px) translateY(250px) scaleX(2.5); opacity: 0; }
}
.shoot {
  position: fixed;
  width: 3px; height: 3px;
  border-radius: 50%;
  background: white;
  box-shadow: 0 0 6px 2px rgba(255,255,255,0.8), -30px 0 12px rgba(196,181,253,0.4);
  pointer-events: none;
  z-index: 1;
  animation: shootStar linear infinite;
}
</style>

<!-- ═══ STARRY NIGHT CANVAS ═══ -->
<canvas id="starry-canvas"></canvas>

<!-- ═══ DRIFTING ROCKETS (3) ═══ -->
<div class="drift-rocket r1">🚀</div>
<div class="drift-rocket r2">🚀</div>
<div class="drift-rocket r3">🚀</div>

<!-- ═══ FLOATING DECORATIVE STARS ═══ -->
<div class="page-star" style="top:18%;left:1.5vw;animation-duration:5.2s;animation-delay:0s;font-size:20px;">✦</div>
<div class="page-star" style="top:42%;left:2vw;animation-duration:7.1s;animation-delay:-2s;font-size:12px;">★</div>
<div class="page-star" style="top:72%;left:1vw;animation-duration:6.3s;animation-delay:-1s;font-size:18px;">✦</div>
<div class="page-star" style="top:8%;right:10vw;animation-duration:4.8s;animation-delay:-3s;font-size:14px;color:rgba(244,196,48,0.6);text-shadow:0 0 10px rgba(244,196,48,0.9);">★</div>
<div class="page-star" style="top:88%;right:2vw;animation-duration:8s;animation-delay:-0.5s;font-size:16px;">✦</div>
<div class="page-star" style="top:30%;right:1.5vw;animation-duration:5.8s;animation-delay:-4s;font-size:11px;">✧</div>
<div class="page-star" style="top:58%;right:3vw;animation-duration:6.6s;animation-delay:-1.5s;font-size:22px;color:rgba(56,189,248,0.5);text-shadow:0 0 12px rgba(56,189,248,0.8);">✦</div>

<!-- ═══ SHOOTING STARS ═══ -->
<div class="shoot" style="top:8%;left:5%;animation-duration:7s;animation-delay:0s;"></div>
<div class="shoot" style="top:22%;left:15%;animation-duration:11s;animation-delay:-4s;"></div>
<div class="shoot" style="top:60%;left:2%;animation-duration:9s;animation-delay:-7s;opacity:0.6;background:rgba(196,181,253,0.9);"></div>
<div class="shoot" style="top:40%;left:30%;animation-duration:13s;animation-delay:-2s;"></div>

<script>
(function(){
  const canvas = document.getElementById('starry-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W, H, stars = [], swirls = [], floaters = [];
  let t = 0;

  function resize(){
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  /* ── Stars (200 small + 40 large glowing) ── */
  function initStars(){
    stars = [];
    // small background stars
    for(let i=0; i<220; i++){
      stars.push({
        x: Math.random()*W, y: Math.random()*H,
        r: Math.random()*1.4 + 0.2,
        alpha: Math.random()*0.55 + 0.2,
        pulse: Math.random()*Math.PI*2,
        pulseSpd: Math.random()*0.018 + 0.004,
        spd: Math.random()*0.12 + 0.02,
        dir: Math.random()*Math.PI*2,
        type: 'small'
      });
    }
    // larger glowing star-orbs (Starry Night "halos")
    for(let i=0; i<38; i++){
      const gold = Math.random() < 0.25;
      stars.push({
        x: Math.random()*W, y: Math.random()*H,
        r: Math.random()*3.5 + 1.5,
        alpha: Math.random()*0.45 + 0.25,
        pulse: Math.random()*Math.PI*2,
        pulseSpd: Math.random()*0.025 + 0.008,
        spd: Math.random()*0.08 + 0.01,
        dir: Math.random()*Math.PI*2,
        haloR: Math.random()*18 + 8,
        gold,
        type: 'large'
      });
    }
  }

  /* ── Van Gogh swirl paths ── */
  function initSwirls(){
    swirls = [];
    for(let i=0; i<6; i++){
      swirls.push({
        cx: Math.random()*W,
        cy: Math.random()*H,
        rx: Math.random()*220 + 100,
        ry: Math.random()*100 + 50,
        rot: Math.random()*Math.PI,
        speed: (Math.random()*0.0003 + 0.0001) * (Math.random()<0.5?1:-1),
        alpha: Math.random()*0.045 + 0.012,
        hue: Math.random()<0.4 ? 'purple' : (Math.random()<0.5 ? 'blue' : 'teal')
      });
    }
  }

  function drawSwirls(){
    swirls.forEach(s => {
      s.rot += s.speed;
      ctx.save();
      ctx.translate(s.cx, s.cy);
      ctx.rotate(s.rot);

      const colors = {
        purple: [`rgba(124,58,237,${s.alpha})`, `rgba(79,70,229,${s.alpha*0.4})`],
        blue:   [`rgba(56,189,248,${s.alpha*0.7})`, `rgba(30,100,200,${s.alpha*0.3})`],
        teal:   [`rgba(20,180,160,${s.alpha*0.6})`, `rgba(10,100,120,${s.alpha*0.2})`]
      };
      const [c1, c2] = colors[s.hue];
      const g = ctx.createRadialGradient(0,0,0, 0,0, Math.max(s.rx, s.ry));
      g.addColorStop(0, c1);
      g.addColorStop(0.5, c2);
      g.addColorStop(1, 'transparent');

      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.ellipse(0, 0, s.rx, s.ry, 0, 0, Math.PI*2);
      ctx.fill();
      ctx.restore();
    });
  }

  function drawStars(){
    stars.forEach(s => {
      s.pulse += s.pulseSpd;
      const a = s.alpha * (0.45 + 0.55*Math.sin(s.pulse));

      if(s.type === 'small'){
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI*2);
        ctx.fillStyle = `rgba(210,200,255,${a})`;
        ctx.fill();
      } else {
        // Glowing halo (Van Gogh's swirling star orbs)
        const col = s.gold ? `rgba(244,196,48,${a})` : `rgba(200,185,255,${a})`;
        const haloCol = s.gold ? `rgba(244,196,48,${a*0.18})` : `rgba(167,139,250,${a*0.15})`;

        // Outer halo glow
        const hg = ctx.createRadialGradient(s.x,s.y,0, s.x,s.y, s.haloR);
        hg.addColorStop(0, col);
        hg.addColorStop(0.35, s.gold ? `rgba(244,196,48,${a*0.5})` : `rgba(196,181,253,${a*0.45})`);
        hg.addColorStop(1, 'transparent');
        ctx.fillStyle = hg;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.haloR, 0, Math.PI*2);
        ctx.fill();

        // Core dot
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI*2);
        ctx.fillStyle = s.gold ? `rgba(255,240,160,${Math.min(a*1.5,1)})` : `rgba(240,235,255,${Math.min(a*1.5,1)})`;
        ctx.fill();
      }

      s.x += Math.cos(s.dir)*s.spd;
      s.y += Math.sin(s.dir)*s.spd;
      if(s.x<-20) s.x=W+20; if(s.x>W+20) s.x=-20;
      if(s.y<-20) s.y=H+20; if(s.y>H+20) s.y=-20;
    });
  }

  /* ── Big atmospheric nebula blobs ── */
  function drawNebulae(){
    const time = performance.now()/8000;
    const orbs = [
      {x:W*0.12, y:H*0.18, r:180, c:'rgba(124,58,237,', a:0.055},
      {x:W*0.85, y:H*0.72, r:220, c:'rgba(79,70,229,',  a:0.045},
      {x:W*0.5,  y:H*0.42, r:140, c:'rgba(56,189,248,', a:0.030},
      {x:W*0.22, y:H*0.78, r:160, c:'rgba(20,180,140,', a:0.028},
      {x:W*0.78, y:H*0.25, r:130, c:'rgba(167,139,250,',a:0.038},
    ];
    orbs.forEach((o,i) => {
      const pulse = 0.85 + 0.15*Math.sin(time*Math.PI*2 + i*1.3);
      const g = ctx.createRadialGradient(o.x,o.y,0, o.x,o.y, o.r*pulse);
      g.addColorStop(0, o.c + (o.a) + ')');
      g.addColorStop(0.5, o.c + (o.a*0.4) + ')');
      g.addColorStop(1,'transparent');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(o.x, o.y, o.r*pulse, 0, Math.PI*2);
      ctx.fill();
    });
  }

  function draw(){
    ctx.clearRect(0,0,W,H);
    drawNebulae();
    drawSwirls();
    drawStars();
    requestAnimationFrame(draw);
  }

  resize();
  initStars();
  initSwirls();
  draw();
  window.addEventListener('resize',()=>{ resize(); initStars(); initSwirls(); });
})();
</script>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════
st.sidebar.markdown("## 🪞 FutureMirror AI")
st.sidebar.markdown("<p style='color:#a78bfa;font-size:12px;margin-top:-10px;'>Navigate the cosmos of your future</p>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "",
    ["🏠 Home", "🪞 Discover My Future", "📚 Career Library", "ℹ️ About"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color:#475569;font-size:11px;text-align:center;'>🚀 Version 1.0 · Built by Ezmareh</p>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# HELPER
# ═══════════════════════════════════════════════════════════════
# Global university suggestions per broad career category
GLOBAL_UNIS = {
    "tech": [
        {"name": "MIT — Massachusetts Institute of Technology", "url": "https://web.mit.edu", "country": "🇺🇸"},
        {"name": "Stanford University", "url": "https://www.stanford.edu", "country": "🇺🇸"},
        {"name": "ETH Zurich", "url": "https://ethz.ch", "country": "🇨🇭"},
        {"name": "University of Toronto", "url": "https://www.utoronto.ca", "country": "🇨🇦"},
    ],
    "medicine": [
        {"name": "Johns Hopkins University", "url": "https://www.jhu.edu", "country": "🇺🇸"},
        {"name": "University of Oxford — Medicine", "url": "https://www.ox.ac.uk", "country": "🇬🇧"},
        {"name": "University of Melbourne", "url": "https://www.unimelb.edu.au", "country": "🇦🇺"},
        {"name": "Aga Khan University", "url": "https://www.aku.edu", "country": "🇵🇰"},
    ],
    "business": [
        {"name": "Harvard Business School", "url": "https://www.hbs.edu", "country": "🇺🇸"},
        {"name": "London Business School", "url": "https://www.london.edu", "country": "🇬🇧"},
        {"name": "INSEAD", "url": "https://www.insead.edu", "country": "🇫🇷"},
        {"name": "University of British Columbia", "url": "https://www.ubc.ca", "country": "🇨🇦"},
    ],
    "engineering": [
        {"name": "Imperial College London", "url": "https://www.imperial.ac.uk", "country": "🇬🇧"},
        {"name": "Caltech", "url": "https://www.caltech.edu", "country": "🇺🇸"},
        {"name": "TU Delft", "url": "https://www.tudelft.nl", "country": "🇳🇱"},
        {"name": "University of Melbourne", "url": "https://www.unimelb.edu.au", "country": "🇦🇺"},
    ],
    "arts": [
        {"name": "Royal College of Art", "url": "https://www.rca.ac.uk", "country": "🇬🇧"},
        {"name": "Parsons School of Design", "url": "https://www.newschool.edu/parsons", "country": "🇺🇸"},
        {"name": "RMIT University", "url": "https://www.rmit.edu.au", "country": "🇦🇺"},
        {"name": "University of Arts London", "url": "https://www.arts.ac.uk", "country": "🇬🇧"},
    ],
    "law": [
        {"name": "Harvard Law School", "url": "https://hls.harvard.edu", "country": "🇺🇸"},
        {"name": "University of Cambridge — Law", "url": "https://www.law.cam.ac.uk", "country": "🇬🇧"},
        {"name": "University of Melbourne — Law", "url": "https://law.unimelb.edu.au", "country": "🇦🇺"},
        {"name": "University of Toronto — Law", "url": "https://www.law.utoronto.ca", "country": "🇨🇦"},
    ],
    "default": [
        {"name": "University of Oxford", "url": "https://www.ox.ac.uk", "country": "🇬🇧"},
        {"name": "University of Cambridge", "url": "https://www.cam.ac.uk", "country": "🇬🇧"},
        {"name": "University of Toronto", "url": "https://www.utoronto.ca", "country": "🇨🇦"},
        {"name": "University of Melbourne", "url": "https://www.unimelb.edu.au", "country": "🇦🇺"},
    ],
}

def _pick_global_unis(career_name: str):
    c = career_name.lower()
    if any(k in c for k in ["software","ai ","data","cyber","cloud","developer","engineer","tech","computer","machine"]):
        return GLOBAL_UNIS["tech"]
    if any(k in c for k in ["doctor","nurse","dentist","pharma","medical","health","surgeon","psycholog","biomedical"]):
        return GLOBAL_UNIS["medicine"]
    if any(k in c for k in ["business","entrepreneur","marketing","accountant","finance","mba","economist"]):
        return GLOBAL_UNIS["business"]
    if any(k in c for k in ["mechanical","civil","electrical","chemical","aerospace","structural"]):
        return GLOBAL_UNIS["engineering"]
    if any(k in c for k in ["designer","graphic","ux","animator","architect","artist","creative","film","game"]):
        return GLOBAL_UNIS["arts"]
    if any(k in c for k in ["law","legal","barrister","solicitor","judge"]):
        return GLOBAL_UNIS["law"]
    return GLOBAL_UNIS["default"]


def render_reflection(career, score, info):
    st.subheader(career)
    st.metric("Compatibility", f"{score}%")

    st.markdown("### 💬 Future Snapshot")
    st.info(f"Imagine yourself a few years from now working as a **{career}**, using your skills to make a real impact every day.")

    st.markdown("### 🧠 Powers You'll Need")
    for power in info["powers"]:
        st.write(f"- {power}")

    st.markdown("### 🚀 First Mission")
    st.success(info["mission"])

    # Pakistani institutes
    institutes = info.get("institutes", [])
    if institutes:
        st.markdown("#### 🏫 Where to Study in Pakistan")
        for inst in institutes:
            st.markdown(f"- [{inst['name']}]({inst['url']})")

    # Global university suggestions
    global_unis = _pick_global_unis(career)
    st.markdown("#### 🌍 Top Global Universities for this Path")
    cols = st.columns(2)
    for i, uni in enumerate(global_unis):
        with cols[i % 2]:
            st.markdown(
                f"""<div style='background:rgba(124,58,237,0.1);border:1px solid rgba(167,139,250,0.2);
                border-radius:10px;padding:10px 14px;margin-bottom:8px;'>
                <span style='font-size:18px;'>{uni['country']}</span>&nbsp;
                <a href='{uni["url"]}' target='_blank'
                   style='color:#c4b5fd;font-size:13px;font-weight:600;text-decoration:none;'>{uni['name']}</a>
                </div>""",
                unsafe_allow_html=True
            )

    st.markdown("### 🎓 Journey Ahead")
    st.write(info["journey"])

    st.markdown("### ⚠ Biggest Obstacle")
    st.warning(info["obstacle"])


# ═══════════════════════════════════════════════════════════════
# HOME PAGE
# ═══════════════════════════════════════════════════════════════
if page == "🏠 Home":

    # Hero
    st.markdown("""
    <div class="space-hero">
      <!-- tiny hero dot-stars -->
      <div class="hero-star" style="width:3px;height:3px;top:12%;left:8%;animation-duration:2.1s;animation-delay:0s;"></div>
      <div class="hero-star" style="width:2px;height:2px;top:20%;left:22%;animation-duration:1.7s;animation-delay:.4s;"></div>
      <div class="hero-star" style="width:5px;height:5px;top:8%;left:55%;animation-duration:2.5s;animation-delay:.2s;box-shadow:0 0 8px rgba(244,196,48,0.8);background:#f4c430;"></div>
      <div class="hero-star" style="width:2px;height:2px;top:25%;left:75%;animation-duration:1.9s;animation-delay:.7s;"></div>
      <div class="hero-star" style="width:4px;height:4px;top:65%;left:90%;animation-duration:2.3s;animation-delay:.1s;box-shadow:0 0 6px rgba(167,139,250,0.8);"></div>
      <div class="hero-star" style="width:2px;height:2px;top:70%;left:10%;animation-duration:1.6s;animation-delay:.5s;"></div>
      <div class="hero-star" style="width:3px;height:3px;top:80%;left:40%;animation-duration:2.0s;animation-delay:.9s;"></div>
      <div class="hero-star" style="width:2px;height:2px;top:55%;left:60%;animation-duration:1.8s;animation-delay:.3s;"></div>
      <div class="hero-star" style="width:4px;height:4px;top:40%;left:3%;animation-duration:2.4s;animation-delay:.6s;box-shadow:0 0 8px rgba(56,189,248,0.7);background:#38bdf8;"></div>
      <div class="hero-star" style="width:2px;height:2px;top:30%;left:92%;animation-duration:1.5s;animation-delay:.2s;"></div>
      <div class="hero-star" style="width:3px;height:3px;top:85%;left:70%;animation-duration:2.2s;animation-delay:.8s;"></div>
      <!-- golden sparkle cross-stars (Van Gogh halos) -->
      <div class="hero-sparkle" style="top:10%;left:6%;animation-duration:2.3s;animation-delay:0s;">✦</div>
      <div class="hero-sparkle" style="top:15%;left:88%;animation-duration:1.8s;animation-delay:.5s;font-size:18px;">★</div>
      <div class="hero-sparkle" style="top:72%;left:5%;animation-duration:2.6s;animation-delay:.2s;font-size:12px;color:rgba(167,139,250,0.8);text-shadow:0 0 10px rgba(167,139,250,0.9);">✦</div>
      <div class="hero-sparkle" style="top:78%;left:93%;animation-duration:2.0s;animation-delay:.7s;font-size:16px;">✦</div>
      <div class="hero-sparkle" style="top:48%;left:95%;animation-duration:2.8s;animation-delay:.3s;font-size:10px;color:rgba(56,189,248,0.7);text-shadow:0 0 8px rgba(56,189,248,0.9);">★</div>
      <div class="hero-sparkle" style="top:55%;left:2%;animation-duration:1.6s;animation-delay:.9s;font-size:14px;">✧</div>
      <h1>🪞 FutureMirror AI</h1>
      <p>Who could you become tomorrow?</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <div class="space-card">
          <h3 style="margin-top:0;">🌍 Why FutureMirror AI?</h3>
          <p style="font-size:15px;line-height:1.7;color:#cbd5e1;">
            Choosing a career is one of the biggest decisions a student will ever make.
            Unfortunately, many students don't know where to begin.<br><br>
            <strong style="color:#a78bfa;">FutureMirror AI</strong> helps students explore personalized career paths
            based on their interests, strengths, personality and ambitions —
            powered by real AI, tailored for Pakistan.
          </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="space-card">
          <h3 style="margin-top:0;">🚀 What you'll receive</h3>
          <div class="feat-row"><span class="feat-icon">✨</span><span class="feat-text">Three personalized AI career paths</span></div>
          <div class="feat-row"><span class="feat-icon">🧠</span><span class="feat-text">Skills you need to master</span></div>
          <div class="feat-row"><span class="feat-icon">🏫</span><span class="feat-text">Pakistani universities to apply to</span></div>
          <div class="feat-row"><span class="feat-icon">🎯</span><span class="feat-text">A first mission to start today</span></div>
          <div class="feat-row" style="border:none;"><span class="feat-icon">🌟</span><span class="feat-text">Realistic compatibility scores</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="space-quote">
      "The future isn't something you find. It's something you build."
    </div>
    """, unsafe_allow_html=True)

    st.success("👉 Click **🪞 Discover My Future** in the sidebar to launch your journey.")


# ═══════════════════════════════════════════════════════════════
# DISCOVER PAGE
# ═══════════════════════════════════════════════════════════════
elif page == "🪞 Discover My Future":
    import time

    st.markdown("<h1 style='color:#c4b5fd;'>🪞 Discover My Future</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Answer a few questions and let FutureMirror AI explore three possible futures for you.</p>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name")
        age = st.slider("Age", 13, 25, 16)
        grade = st.selectbox("Current Grade",
            ["Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","University"])
        subjects = st.multiselect("Favorite Subjects",
            [
                "Mathematics", "Physics", "Biology", "Chemistry",
                "Environmental Science", "Astronomy", "Statistics",
                "Computer Science", "Information Technology",
                "Artificial Intelligence", "Robotics", "Electronics",
                "Business Studies", "Economics", "Accounting",
                "Sociology", "Psychology", "Political Science",
                "Law", "Mass Communication",
                "English Literature", "Urdu Literature", "History",
                "Geography", "Islamic Studies", "Philosophy",
                "Art & Design", "Music", "Drama & Theatre",
                "Physical Education", "Health Sciences",
                "Architecture", "Agriculture", "Home Economics",
            ]
        )

    with col2:
        interests = st.text_area("What are your biggest interests?",
            placeholder="Gaming, coding, football, business, helping people...")
        strengths = st.text_area("What are your biggest strengths?",
            placeholder="Creative, leadership, problem solving...")
        goals = st.text_area("What impact do you want to make?",
            placeholder="Build technology, help people, solve climate change...")

    st.divider()

    if st.button("🪞 Reveal My Futures", use_container_width=True):
        progress = st.progress(0)
        status = st.empty()

        status.write("🪞 Initializing Mirror...")
        progress.progress(20); time.sleep(0.8)
        status.write("🧠 Analyzing strengths...")
        progress.progress(45); time.sleep(0.8)
        status.write("📚 Matching careers with AI...")
        progress.progress(70)

        try:
            top_careers, career_info = recommend_careers(subjects, interests, strengths)
            progress.progress(100); time.sleep(0.4)
            status.success("✨ Mirror Unlocked!")

            # Space launch animation
            st.markdown("""
<style>
@keyframes rocketLaunch {
    0%   { bottom:20px; opacity:1; transform:translateX(-50%) rotate(-45deg) scale(1); }
    60%  { opacity:1;   transform:translateX(-50%) rotate(-45deg) scale(1.15); }
    80%  { opacity:0.8; }
    100% { bottom:240px; opacity:0; transform:translateX(-50%) rotate(-45deg) scale(0.7); }
}
@keyframes starTwinkle2 {
    0%,100% { opacity:0.12; transform:scale(0.65); }
    50%      { opacity:1;    transform:scale(1.4); }
}
@keyframes fadeIn2 { from{opacity:0;transform:translateY(8px);} to{opacity:1;transform:translateY(0);} }
@keyframes floatPlanet2 {
    0%,100%{transform:translateY(0) rotate(0deg);} 50%{transform:translateY(-10px) rotate(5deg);}
}
@keyframes swirlBg {
    0%   {transform:rotate(0deg) scale(1);}
    50%  {transform:rotate(180deg) scale(1.1);}
    100% {transform:rotate(360deg) scale(1);}
}
.sw2 {
    position:relative;
    background:linear-gradient(160deg,#030310 0%,#070720 30%,#0a0d28 60%,#130838 100%);
    border-radius:20px; height:220px; overflow:hidden;
    margin:20px 0 10px 0;
    animation:fadeIn2 0.5s ease;
    border:1px solid rgba(167,139,250,0.25);
    box-shadow:0 0 40px rgba(124,58,237,0.15), inset 0 0 60px rgba(79,70,229,0.05);
}
/* Swirling nebula inside launch panel */
.sw2-swirl {
    position:absolute;
    border-radius:50%;
    pointer-events:none;
    animation:swirlBg linear infinite;
}
.sw2-rocket {
    position:absolute; left:50%;
    transform:translateX(-50%) rotate(-45deg);
    font-size:56px;
    animation:rocketLaunch 2.2s ease-in forwards;
    animation-delay:0.15s;
    filter:drop-shadow(0 0 18px #ff6030) drop-shadow(0 0 8px rgba(244,196,48,0.6));
}
.sw2-star { position:absolute; animation:starTwinkle2 linear infinite; }
.sw2-planet { position:absolute; animation:floatPlanet2 3.5s ease-in-out infinite; }
.sw2-label {
    position:absolute; bottom:14px; width:100%; text-align:center;
    color:#c4b5fd; font-size:13px; font-weight:700;
    letter-spacing:3.5px; text-transform:uppercase;
    text-shadow:0 0 14px rgba(167,139,250,0.6);
}
</style>
<div class="sw2">
  <!-- swirling nebula blobs -->
  <div class="sw2-swirl" style="width:300px;height:120px;background:radial-gradient(ellipse,rgba(124,58,237,0.08),transparent);top:20%;left:10%;animation-duration:18s;"></div>
  <div class="sw2-swirl" style="width:250px;height:100px;background:radial-gradient(ellipse,rgba(79,70,229,0.07),transparent);top:40%;left:50%;animation-duration:24s;animation-delay:-8s;"></div>
  <div class="sw2-swirl" style="width:200px;height:80px;background:radial-gradient(ellipse,rgba(56,189,248,0.05),transparent);top:10%;left:60%;animation-duration:20s;animation-delay:-5s;"></div>
  <!-- cross-sparkles (Van Gogh halo stars) -->
  <span class="sw2-star" style="font-size:14px;top:8%;left:5%;animation-duration:1.2s;color:rgba(244,196,48,0.8);text-shadow:0 0 8px rgba(244,196,48,0.9);">✦</span>
  <span class="sw2-star" style="font-size:10px;top:12%;left:15%;animation-duration:1.8s;animation-delay:.3s;color:white;">★</span>
  <span class="sw2-star" style="font-size:14px;top:6%;left:28%;animation-duration:1.5s;animation-delay:.1s;color:rgba(244,196,48,0.7);text-shadow:0 0 6px rgba(244,196,48,0.8);">★</span>
  <span class="sw2-star" style="font-size:9px;top:18%;left:42%;animation-duration:2s;animation-delay:.6s;color:rgba(196,181,253,0.9);">✦</span>
  <span class="sw2-star" style="font-size:13px;top:9%;left:60%;animation-duration:1.3s;animation-delay:.4s;color:rgba(244,196,48,0.75);text-shadow:0 0 8px rgba(244,196,48,0.9);">✦</span>
  <span class="sw2-star" style="font-size:10px;top:20%;left:73%;animation-duration:1.7s;animation-delay:.2s;color:white;">★</span>
  <span class="sw2-star" style="font-size:9px;top:5%;left:86%;animation-duration:1.1s;animation-delay:.8s;color:rgba(196,181,253,0.9);">✦</span>
  <span class="sw2-star" style="font-size:15px;top:35%;left:10%;animation-duration:2.2s;animation-delay:.5s;color:rgba(244,196,48,0.6);text-shadow:0 0 10px rgba(244,196,48,0.8);">★</span>
  <span class="sw2-star" style="font-size:8px;top:40%;left:32%;animation-duration:1.4s;animation-delay:.7s;color:white;">✧</span>
  <span class="sw2-star" style="font-size:11px;top:38%;left:78%;animation-duration:1.9s;animation-delay:.1s;color:rgba(56,189,248,0.8);text-shadow:0 0 8px rgba(56,189,248,0.9);">✦</span>
  <span class="sw2-star" style="font-size:9px;top:52%;left:55%;animation-duration:1.6s;animation-delay:.9s;color:rgba(196,181,253,0.8);">★</span>
  <span class="sw2-star" style="font-size:7px;top:55%;left:90%;animation-duration:1.3s;animation-delay:.3s;color:white;">✦</span>
  <span class="sw2-star" style="font-size:12px;top:25%;left:95%;animation-duration:2.0s;animation-delay:.6s;color:rgba(244,196,48,0.7);">✦</span>
  <!-- planets -->
  <span class="sw2-planet" style="top:8%;left:80%;font-size:26px;animation-delay:0s;">🪐</span>
  <span class="sw2-planet" style="top:12%;left:3%;font-size:18px;animation-delay:1s;">🌙</span>
  <span class="sw2-planet" style="top:55%;left:88%;font-size:14px;animation-delay:0.5s;">⭐</span>
  <div class="sw2-rocket">🚀</div>
  <div class="sw2-label">🌌 your future is launching...</div>
</div>
""", unsafe_allow_html=True)

            st.divider()

            labels = [
                ("🟢 Reflection Alpha", True),
                ("🟣 Reflection Beta",  False),
                ("🔵 Reflection Gamma", False),
            ]
            for i, (label, expanded) in enumerate(labels):
                with st.expander(label, expanded=expanded):
                    career, score = top_careers[i]
                    info = career_info[career]
                    render_reflection(career, score, info)

        except Exception as e:
            progress.empty()
            status.error(f"❌ Something went wrong: {e}")


# ═══════════════════════════════════════════════════════════════
# CAREER LIBRARY
# ═══════════════════════════════════════════════════════════════
elif page == "📚 Career Library":

    st.markdown("<h1 style='color:#c4b5fd;'>📚 Career Library</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Explore 30 exciting careers and discover what each one involves.</p>", unsafe_allow_html=True)

    careers = [
        {"name":"👨‍⚕️ Doctor","description":"Diagnoses illnesses and treats patients.","salary":"$80k–250k/yr","skills":"Biology, Empathy, Communication","degree":"Medicine (MBBS/MD)"},
        {"name":"🩺 Nurse","description":"Provides patient care and supports doctors.","salary":"$50k–100k/yr","skills":"Compassion, Teamwork","degree":"Nursing"},
        {"name":"🦷 Dentist","description":"Treats teeth and oral health problems.","salary":"$90k–220k/yr","skills":"Precision, Biology","degree":"Dentistry"},
        {"name":"🧠 Psychologist","description":"Helps improve mental health and wellbeing.","salary":"$60k–130k/yr","skills":"Listening, Empathy","degree":"Psychology"},
        {"name":"💊 Pharmacist","description":"Dispenses medicines and advises patients.","salary":"$80k–140k/yr","skills":"Chemistry, Attention to Detail","degree":"Pharmacy"},
        {"name":"🧬 Biomedical Engineer","description":"Designs medical devices and healthcare technology.","salary":"$80k–150k/yr","skills":"Biology, Engineering","degree":"Biomedical Engineering"},
        {"name":"🤖 AI Engineer","description":"Develops artificial intelligence systems.","salary":"$100k–200k/yr","skills":"Python, Machine Learning","degree":"Computer Science"},
        {"name":"💻 Software Engineer","description":"Builds software and applications.","salary":"$90k–180k/yr","skills":"Programming, Problem Solving","degree":"Computer Science"},
        {"name":"🌐 Web Developer","description":"Creates websites and web applications.","salary":"$60k–130k/yr","skills":"HTML, CSS, JavaScript","degree":"Computer Science"},
        {"name":"📱 Mobile App Developer","description":"Builds Android and iOS applications.","salary":"$80k–160k/yr","skills":"Flutter, Java, Swift","degree":"Computer Science"},
        {"name":"📊 Data Scientist","description":"Uses data to solve real-world problems.","salary":"$90k–170k/yr","skills":"Python, Statistics","degree":"Data Science"},
        {"name":"🔒 Cybersecurity Analyst","description":"Protects organizations from cyber attacks.","salary":"$90k–170k/yr","skills":"Networking, Security","degree":"Cybersecurity"},
        {"name":"☁️ Cloud Engineer","description":"Builds and manages cloud infrastructure.","salary":"$100k–180k/yr","skills":"AWS, Azure","degree":"Computer Science"},
        {"name":"⚙️ Mechanical Engineer","description":"Designs machines and mechanical systems.","salary":"$70k–150k/yr","skills":"Physics, CAD","degree":"Mechanical Engineering"},
        {"name":"🏗️ Civil Engineer","description":"Designs roads, bridges and buildings.","salary":"$70k–140k/yr","skills":"Math, Engineering","degree":"Civil Engineering"},
        {"name":"⚡ Electrical Engineer","description":"Designs electrical systems and electronics.","salary":"$80k–150k/yr","skills":"Circuits, Physics","degree":"Electrical Engineering"},
        {"name":"🧪 Chemical Engineer","description":"Develops industrial chemical processes.","salary":"$80k–150k/yr","skills":"Chemistry, Math","degree":"Chemical Engineering"},
        {"name":"✈️ Aerospace Engineer","description":"Designs aircraft and spacecraft.","salary":"$100k–180k/yr","skills":"Physics, Engineering","degree":"Aerospace Engineering"},
        {"name":"💼 Entrepreneur","description":"Starts and grows successful businesses.","salary":"Varies","skills":"Leadership, Creativity","degree":"Business (optional)"},
        {"name":"📈 Business Analyst","description":"Improves businesses using data and strategy.","salary":"$70k–140k/yr","skills":"Analysis, Communication","degree":"Business"},
        {"name":"💰 Accountant","description":"Manages financial records and taxes.","salary":"$60k–120k/yr","skills":"Math, Accuracy","degree":"Accounting"},
        {"name":"📣 Marketing Manager","description":"Promotes products, services and brands.","salary":"$70k–150k/yr","skills":"Communication, Creativity","degree":"Marketing"},
        {"name":"⚖️ Lawyer","description":"Represents clients and provides legal advice.","salary":"$80k–200k/yr","skills":"Critical Thinking, Speaking","degree":"Law"},
        {"name":"🏛️ Architect","description":"Designs buildings and modern structures.","salary":"$70k–150k/yr","skills":"Design, Creativity","degree":"Architecture"},
        {"name":"🎨 Graphic Designer","description":"Creates logos, posters and digital artwork.","salary":"$50k–100k/yr","skills":"Adobe Suite, Creativity","degree":"Graphic Design"},
        {"name":"🖥️ UX Designer","description":"Designs user-friendly digital experiences.","salary":"$80k–150k/yr","skills":"UI/UX, Research","degree":"Design or CS"},
        {"name":"🎬 Animator","description":"Creates animations for films and games.","salary":"$60k–120k/yr","skills":"Animation, Creativity","degree":"Animation"},
        {"name":"🎮 Game Developer","description":"Builds exciting video games.","salary":"$70k–150k/yr","skills":"Programming, Game Design","degree":"Computer Science"},
        {"name":"📰 Journalist","description":"Researches and reports news stories.","salary":"$45k–100k/yr","skills":"Writing, Investigation","degree":"Journalism"},
        {"name":"👨‍🏫 Teacher","description":"Educates and inspires students.","salary":"$40k–90k/yr","skills":"Communication, Patience","degree":"Education"},
    ]

    search = st.text_input("🔍 Search careers...", placeholder="e.g. Engineer, Doctor, Designer")
    st.markdown("<br>", unsafe_allow_html=True)

    filtered = [c for c in careers if search.lower() in c["name"].lower()]

    for career in filtered:
        st.markdown(f"""
        <div class="lib-card">
          <h4>{career['name']}</h4>
          <p>{career['description']}</p>
          <span class="lib-badge">💰 {career['salary']}</span>
          <span class="lib-badge">🎓 {career['degree']}</span>
          <br>
          <p style="margin-top:8px;font-size:13px;color:#64748b;">🧠 {career['skills']}</p>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# ABOUT
# ═══════════════════════════════════════════════════════════════
elif page == "ℹ️ About":

    st.markdown("<h1 style='color:#c4b5fd;'>ℹ️ About FutureMirror AI</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="space-card">
      <h3 style="margin-top:0;">🌟 Our Mission</h3>
      <p style="font-size:15px;line-height:1.8;color:#cbd5e1;">
        Choosing a career can feel overwhelming. FutureMirror AI was created to help students
        explore careers that match their interests, strengths, and favourite subjects.<br><br>
        Instead of telling users what they <em>must</em> become, FutureMirror AI encourages them
        to discover multiple possibilities and start thinking about their future —
        with AI that understands Pakistan's education landscape.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Stats row
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><div class="num">30+</div><div class="lbl">Careers in Library</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><div class="num">3</div><div class="lbl">AI Futures per Student</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><div class="num">🇵🇰</div><div class="lbl">Pakistan-First Design</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="space-card">
          <h3 style="margin-top:0;">🎯 Features</h3>
          <div class="feat-row"><span class="feat-icon">✅</span><span class="feat-text">Personalized AI career recommendations</span></div>
          <div class="feat-row"><span class="feat-icon">✅</span><span class="feat-text">Three future career reflections</span></div>
          <div class="feat-row"><span class="feat-icon">✅</span><span class="feat-text">Career Library with 30 professions</span></div>
          <div class="feat-row"><span class="feat-icon">✅</span><span class="feat-text">Pakistani institute suggestions per career</span></div>
          <div class="feat-row" style="border:none;"><span class="feat-icon">✅</span><span class="feat-text">Realistic compatibility scores (44–88%)</span></div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="space-card">
          <h3 style="margin-top:0;">🛠 Tech Stack</h3>
          <div class="feat-row"><span class="feat-icon">🐍</span><span class="feat-text">Python 3</span></div>
          <div class="feat-row"><span class="feat-icon">🖥</span><span class="feat-text">Streamlit</span></div>
          <div class="feat-row"><span class="feat-icon">⚡</span><span class="feat-text">Groq API</span></div>
          <div class="feat-row" style="border:none;"><span class="feat-icon">🧠</span><span class="feat-text">LLaMA 3.3 70B</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="space-card" style="text-align:center;">
      <p style="font-size:13px;color:#64748b;margin:0;">👨‍💻 Developed by <strong style="color:#a78bfa;">Ezmareh Rehman</strong> &nbsp;·&nbsp; FutureMirror AI v1.0</p>
      <p style="font-size:13px;color:#475569;margin:6px 0 0 0;">Built as a school project to demonstrate how AI can guide students toward better career decisions.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="space-quote" style="margin-top:28px;">
      🚀 &nbsp;"Your future starts with the choices you make today."
    </div>
    """, unsafe_allow_html=True)
