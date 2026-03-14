from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>HaramServer — Regulament</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#07080d;--surface:#0e1018;--card:#12151f;--border:#1e2235;
  --text:#e2e8f8;--muted:#5a6380;
  --accent:#5865f2;--accent2:#eb459e;--gold:#faa61a;--green:#57f287;--red:#ed4245;
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Syne',sans-serif;min-height:100vh;overflow-x:hidden}
body::before{
  content:'';position:fixed;inset:0;pointer-events:none;
  background:radial-gradient(ellipse 80% 50% at 20% 0%,rgba(88,101,242,0.08),transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 100%,rgba(235,69,158,0.06),transparent 60%);
}
.particles{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.particle{position:absolute;width:2px;height:2px;border-radius:50%;opacity:0;animation:float linear infinite}
@keyframes float{0%{transform:translateY(100vh);opacity:0}10%{opacity:0.4}90%{opacity:0.2}100%{transform:translateY(-10vh) translateX(40px);opacity:0}}
nav{position:sticky;top:0;z-index:100;background:rgba(7,8,13,0.88);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:0 32px}
.nav-inner{max-width:1000px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:62px}
.logo{display:flex;align-items:center;gap:10px;font-size:17px;font-weight:800;letter-spacing:-0.02em}
.logo-icon{width:34px;height:34px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:16px;box-shadow:0 0 20px rgba(88,101,242,0.4)}
.logo span{color:var(--accent)}
.nav-tabs{display:flex;gap:4px}
.tab-btn{background:transparent;border:none;color:var(--muted);font-family:'Syne',sans-serif;font-size:13px;font-weight:600;letter-spacing:0.02em;padding:8px 18px;border-radius:8px;cursor:pointer;transition:all 0.2s;white-space:nowrap}
.tab-btn:hover{color:var(--text);background:rgba(255,255,255,0.05)}
.tab-btn.active{color:var(--text);background:rgba(88,101,242,0.15);box-shadow:inset 0 0 0 1px rgba(88,101,242,0.3)}
.tab-dot{display:inline-block;width:6px;height:6px;border-radius:50%;margin-right:7px;vertical-align:middle}
.hero{text-align:center;padding:70px 24px 50px;position:relative;z-index:1}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(88,101,242,0.1);border:1px solid rgba(88,101,242,0.25);border-radius:100px;padding:6px 16px;font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--accent);letter-spacing:0.1em;margin-bottom:22px;animation:fadeDown 0.6s ease both}
.hero-badge::before{content:'●';font-size:8px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.3}}
.hero h1{font-size:clamp(38px,6vw,72px);font-weight:800;line-height:1.0;letter-spacing:-0.03em;margin-bottom:14px;animation:fadeDown 0.7s ease 0.1s both}
.hero h1 .grad{background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--muted);animation:fadeDown 0.7s ease 0.2s both}
.content{max-width:860px;margin:0 auto;padding:0 24px 80px;position:relative;z-index:1}
.panel{display:none;animation:fadeIn 0.35s ease both}
.panel.active{display:block}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:28px}
.stat{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:18px;text-align:center}
.stat-num{font-size:26px;font-weight:800;color:var(--accent)}
.stat-label{font-size:10px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-top:4px;letter-spacing:0.05em}
.section-card{background:var(--card);border:1px solid var(--border);border-radius:14px;margin-bottom:14px;overflow:hidden;transition:border-color 0.3s,box-shadow 0.3s}
.section-card:hover{border-color:rgba(88,101,242,0.3);box-shadow:0 0 30px rgba(88,101,242,0.1)}
.section-header{display:flex;align-items:center;gap:14px;padding:18px 22px;cursor:pointer;user-select:none}
.section-icon{width:38px;height:38px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0}
.section-title{font-size:15px;font-weight:700;margin-bottom:2px}
.section-sub{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted)}
.section-arrow{color:var(--muted);font-size:11px;margin-left:auto;transition:transform 0.3s}
.section-card.open .section-arrow{transform:rotate(180deg)}
.section-body{display:none;padding:0 22px 22px;border-top:1px solid var(--border)}
.section-card.open .section-body{display:block}
.rule-list{list-style:none;padding-top:14px}
.rule-list li{display:flex;align-items:flex-start;gap:11px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.04);font-size:14px;line-height:1.6;color:#b0bcd8}
.rule-list li:last-child{border-bottom:none}
.rule-list li::before{content:'›';color:var(--accent);font-size:15px;font-weight:700;flex-shrink:0;margin-top:1px}
.rule-list li strong{color:var(--text)}
.warn-box{background:rgba(237,66,69,0.08);border:1px solid rgba(237,66,69,0.2);border-radius:9px;padding:13px 17px;margin-top:14px;font-size:13px;color:#ff8a8c;display:flex;align-items:flex-start;gap:9px;font-family:'JetBrains Mono',monospace}
.warn-box::before{content:'⚠';font-size:15px;flex-shrink:0}
.info-box{background:rgba(88,101,242,0.08);border:1px solid rgba(88,101,242,0.2);border-radius:9px;padding:13px 17px;margin-top:14px;font-size:13px;color:#a5b4fc;font-family:'JetBrains Mono',monospace;line-height:1.7}
.mm-card{background:linear-gradient(135deg,rgba(88,101,242,0.1),rgba(235,69,158,0.05));border:1px solid rgba(88,101,242,0.2);border-radius:11px;padding:18px;margin:14px 0}
.mm-title{font-size:12px;font-weight:700;color:var(--accent);margin-bottom:10px;letter-spacing:0.06em;text-transform:uppercase}
.mm-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:11px}
.mm-step{background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:7px;padding:11px;text-align:center;font-size:12px;color:var(--muted)}
.mm-step .step-num{font-size:20px;font-weight:800;color:var(--accent);display:block;margin-bottom:3px}
.staff-hero{background:linear-gradient(135deg,rgba(88,101,242,0.08),rgba(235,69,158,0.05));border:1px solid rgba(88,101,242,0.15);border-radius:14px;padding:30px;text-align:center;margin-bottom:22px}
.staff-hero h2{font-size:26px;font-weight:800;margin-bottom:7px}
.staff-hero p{font-size:13px;color:var(--muted);font-family:'JetBrains Mono',monospace}
.cmd-box{display:inline-flex;align-items:center;gap:10px;background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:8px;padding:9px 18px;margin:14px 0;font-family:'JetBrains Mono',monospace;font-size:15px}
.cmd-slash{color:var(--accent);font-weight:700}
.founders-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:11px;margin:16px 0}
.founder-card{background:var(--card);border:1px solid var(--border);border-radius:11px;padding:18px;text-align:center;transition:all 0.25s;position:relative;overflow:hidden}
.founder-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(88,101,242,0.05),transparent);opacity:0;transition:opacity 0.3s}
.founder-card:hover::before{opacity:1}
.founder-card:hover{border-color:rgba(88,101,242,0.3);transform:translateY(-2px)}
.founder-avatar{width:56px;height:56px;border-radius:50%;margin:0 auto 10px;display:flex;align-items:center;justify-content:center;font-size:24px;border:2px solid var(--border)}
.founder-name{font-size:15px;font-weight:700;margin-bottom:3px}
.founder-role{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.05em}
.apply-card{background:linear-gradient(135deg,rgba(87,242,135,0.08),rgba(88,101,242,0.05));border:1px solid rgba(87,242,135,0.2);border-radius:14px;padding:26px;text-align:center}
.apply-card h3{font-size:19px;font-weight:800;margin-bottom:7px}
.apply-card p{font-size:13px;color:var(--muted);margin-bottom:18px;font-family:'JetBrains Mono',monospace}
.apply-btn{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;font-family:'Syne',sans-serif;font-size:14px;font-weight:700;padding:13px 30px;border-radius:9px;cursor:pointer;transition:all 0.25s;box-shadow:0 4px 20px rgba(88,101,242,0.3)}
.apply-btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(88,101,242,0.4)}
@keyframes fadeDown{from{opacity:0;transform:translateY(-12px)}to{opacity:1;transform:none}}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@media(max-width:600px){
  nav{padding:0 14px}.tab-btn{padding:7px 11px;font-size:12px}
  .hero{padding:44px 16px 32px}.mm-steps{grid-template-columns:1fr}.stats{grid-template-columns:1fr 1fr}
}
</style>
</head>
<body>
<div class="particles" id="particles"></div>
<nav>
  <div class="nav-inner">
    <div class="logo"><div class="logo-icon">⚔</div>Haram<span>Server</span></div>
    <div class="nav-tabs">
      <button class="tab-btn active" onclick="showTab('regulament',this)"><span class="tab-dot" style="background:#5865f2"></span>Regulament</button>
      <button class="tab-btn" onclick="showTab('trading',this)"><span class="tab-dot" style="background:#faa61a"></span>Trading</button>
      <button class="tab-btn" onclick="showTab('staff',this)"><span class="tab-dot" style="background:#57f287"></span>Staff</button>
    </div>
  </div>
</nav>

<div class="hero">
  <div class="hero-badge">SERVER OFICIAL</div>
  <h1>Regulament<br><span class="grad">& Reguli</span></h1>
  <p>// citește cu atenție înainte să interacționezi</p>
</div>

<div class="content">

  <!-- REGULAMENT -->
  <div class="panel active" id="panel-regulament">
    <div class="stats">
      <div class="stat"><div class="stat-num">5</div><div class="stat-label">REGULI CONDUCT</div></div>
      <div class="stat"><div class="stat-num">5</div><div class="stat-label">REGULI TRADING</div></div>
      <div class="stat"><div class="stat-num">∞</div><div class="stat-label">BAN SCAM</div></div>
    </div>

    <div class="section-card open">
      <div class="section-header" onclick="toggle(this)">
        <div class="section-icon" style="background:rgba(88,101,242,0.15)">🤝</div>
        <div><div class="section-title">Respect & Comportament</div><div class="section-sub">// conduită generală</div></div>
        <span class="section-arrow">▼</span>
      </div>
      <div class="section-body">
        <ul class="rule-list">
          <li>Respectul este <strong>obligatoriu</strong> față de toți membrii.</li>
          <li>Fără <strong>injurii grave</strong>, rasism, doxxing sau amenințări.</li>
          <li>Fără <strong>spam, flood</strong> sau tag abuziv.</li>
          <li>Fără reclame în DM <strong>fără acord</strong> prealabil.</li>
          <li>Staff-ul are <strong>ultimul cuvânt</strong> în orice dispută.</li>
        </ul>
      </div>
    </div>

    <div class="section-card">
      <div class="section-header" onclick="toggle(this)">
        <div class="section-icon" style="background:rgba(250,166,26,0.15)">💱</div>
        <div><div class="section-title">Reguli Generale Trading</div><div class="section-sub">// tranzacții & schimburi</div></div>
        <span class="section-arrow">▼</span>
      </div>
      <div class="section-body">
        <ul class="rule-list">
          <li>Toate tranzacțiile sunt pe <strong>propria răspundere</strong>.</li>
          <li>Recomandăm folosirea sistemului oficial <strong>Middleman</strong>.</li>
          <li>Este interzisă orice <strong>tentativă de scam</strong>.</li>
          <li>Orice scam confirmat = <strong>ban permanent</strong>.</li>
          <li>Dovezile trebuie să fie clare: <strong>screenshots + user ID</strong>.</li>
        </ul>
      </div>
    </div>

    <div class="section-card">
      <div class="section-header" onclick="toggle(this)">
        <div class="section-icon" style="background:rgba(87,242,135,0.15)">🛡️</div>
        <div><div class="section-title">Regulament Middleman (MM)</div><div class="section-sub">// intermediar oficial</div></div>
        <span class="section-arrow">▼</span>
      </div>
      <div class="section-body">
        <div class="mm-card">
          <div class="mm-title">Ce este MM?</div>
          <p style="font-size:13px;color:#b0bcd8;line-height:1.7">Middleman este un <strong style="color:var(--text)">intermediar neutru</strong> care asigură siguranța tranzacțiilor.</p>
          <div class="mm-steps">
            <div class="mm-step"><span class="step-num">1</span>Primește produsul / banii</div>
            <div class="mm-step"><span class="step-num">2</span>Verifică tranzacția</div>
            <div class="mm-step"><span class="step-num">3</span>Finalizează schimbul</div>
          </div>
        </div>
        <ul class="rule-list">
          <li>Doar <strong>MM oficial</strong> poate face intermedieri.</li>
          <li>Nu aveți voie să folosiți <strong>fake MM</strong>.</li>
          <li>Verificați întotdeauna <strong>user ID-ul MM</strong>.</li>
          <li>MM nu răspunde pentru: produse fake, conturi recuperate ulterior, dispute externe Discord.</li>
        </ul>
      </div>
    </div>

    <div class="section-card">
      <div class="section-header" onclick="toggle(this)">
        <div class="section-icon" style="background:rgba(237,66,69,0.15)">🚫</div>
        <div><div class="section-title">Acțiuni Interzise</div><div class="section-sub">// ban permanent + blacklist</div></div>
        <span class="section-arrow">▼</span>
      </div>
      <div class="section-body">
        <ul class="rule-list">
          <li><strong>Fake vouch</strong> — review-uri false.</li>
          <li><strong>Impersonare</strong> staff sau MM.</li>
          <li>Trimitere de <strong>link-uri suspecte</strong> / phishing.</li>
          <li><strong>Screenshots editate</strong> ca dovezi.</li>
        </ul>
        <div class="warn-box">Orice tentativă = ban permanent + blacklist imediat.</div>
      </div>
    </div>
  </div>

  <!-- TRADING -->
  <div class="panel" id="panel-trading">
    <div class="section-card open">
      <div class="section-header" onclick="toggle(this)">
        <div class="section-icon" style="background:rgba(250,166,26,0.15)">📋</div>
        <div><div class="section-title">Cum funcționează Trading?</div><div class="section-sub">// ghid complet</div></div>
        <span class="section-arrow">▼</span>
      </div>
      <div class="section-body">
        <div class="mm-card">
          <div class="mm-title">Pași pentru o tranzacție sigură</div>
          <div class="mm-steps">
            <div class="mm-step"><span class="step-num">1</span>Găsești partener</div>
            <div class="mm-step"><span class="step-num">2</span>Chemi MM oficial</div>
            <div class="mm-step"><span class="step-num">3</span>Trade complet</div>
          </div>
        </div>
        <ul class="rule-list">
          <li>Verifică <strong>reputația</strong> partenerului înainte de orice tranzacție.</li>
          <li>Nu trimite bani/produse <strong>fără MM</strong> pentru tranzacții mari.</li>
          <li>Toate disputele se rezolvă prin <strong>ticket oficial</strong>.</li>
          <li>Păstrează <strong>toate dovezile</strong> conversației.</li>
        </ul>
        <div class="info-box">💡 Sfat: Folosește întotdeauna MM oficial pentru tranzacții de valoare. Mai bine în siguranță!</div>
      </div>
    </div>

    <div class="section-card">
      <div class="section-header" onclick="toggle(this)">
        <div class="section-icon" style="background:rgba(237,66,69,0.15)">⚡</div>
        <div><div class="section-title">Sancțiuni Trading</div><div class="section-sub">// consecințe încălcări</div></div>
        <span class="section-arrow">▼</span>
      </div>
      <div class="section-body">
        <ul class="rule-list">
          <li><strong>Avertisment</strong> — prima abatere minoră.</li>
          <li><strong>Mute temporar</strong> — abateri repetate.</li>
          <li><strong>Ban temporar</strong> — tentativă de înșelăciune neconfirmată.</li>
          <li><strong>Ban permanent + blacklist</strong> — scam confirmat.</li>
        </ul>
        <div class="warn-box">Scam-ul confirmat cu dovezi = ban permanent fără apel.</div>
      </div>
    </div>
  </div>

  <!-- STAFF -->
  <div class="panel" id="panel-staff">
    <div class="staff-hero">
      <h2>👑 Echipa Staff</h2>
      <p>// oamenii care mențin ordinea în server</p>
      <div class="cmd-box"><span class="cmd-slash">/</span><span style="color:var(--text);font-weight:500">apply Aplicatie-Staff</span></div>
      <p style="font-size:12px;color:var(--muted);margin-top:6px">Asigurați-vă că ești cu botul <strong style="color:var(--text)">Appy</strong></p>
    </div>

    <p style="font-size:12px;color:var(--muted);font-family:'JetBrains Mono',monospace;margin-bottom:14px">// FONDATORI</p>
    <div class="founders-grid">
      <div class="founder-card">
        <div class="founder-avatar" style="background:linear-gradient(135deg,rgba(88,101,242,0.2),rgba(235,69,158,0.2))">👑</div>
        <div class="founder-name">Fondator #1</div>
        <div class="founder-role" style="color:var(--accent)">OWNER</div>
      </div>
      <div class="founder-card">
        <div class="founder-avatar" style="background:linear-gradient(135deg,rgba(250,166,26,0.2),rgba(88,101,242,0.1))">👑</div>
        <div class="founder-name">Barbosu</div>
        <div class="founder-role" style="color:var(--gold)">CO-OWNER</div>
      </div>
    </div>

    <div class="section-card open" style="margin-top:20px">
      <div class="section-header" onclick="toggle(this)">
        <div class="section-icon" style="background:rgba(87,242,135,0.15)">📝</div>
        <div><div class="section-title">Cerințe Staff</div><div class="section-sub">// ce trebuie să îndeplinești</div></div>
        <span class="section-arrow">▼</span>
      </div>
      <div class="section-body">
        <ul class="rule-list">
          <li>Să fii <strong>activ</strong> în server minim 2 săptămâni.</li>
          <li>Să ai un <strong>profil curat</strong>, fără avertismente.</li>
          <li>Să cunoști <strong>regulamentul complet</strong>.</li>
          <li>Să fii <strong>matur și responsabil</strong>.</li>
          <li>Disponibilitate de <strong>minim 2h/zi</strong>.</li>
        </ul>
        <div class="info-box">✅ Aplicațiile sunt revizuite de fondatori. Vei fi contactat în maxim 48h.</div>
      </div>
    </div>

    <div class="apply-card" style="margin-top:16px">
      <h3>Vrei să fii Staff?</h3>
      <p>// folosește comanda de mai jos în Discord</p>
      <button class="apply-btn" onclick="copyCmd()"><span>📋</span> Copiază comanda /apply</button>
      <p id="copy-confirm" style="font-size:12px;color:var(--green);margin-top:10px;opacity:0;transition:opacity 0.3s;font-family:'JetBrains Mono',monospace">✓ Comandă copiată!</p>
    </div>
  </div>

</div>

<script>
(function(){
  const c=document.getElementById('particles');
  for(let i=0;i<18;i++){
    const p=document.createElement('div');
    p.className='particle';
    p.style.cssText='left:'+Math.random()*100+'%;animation-delay:'+Math.random()*15+'s;animation-duration:'+(12+Math.random()*10)+'s;background:'+(Math.random()>.5?'var(--accent)':'var(--accent2)');
    c.appendChild(p);
  }
})();
function showTab(n,b){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(x=>x.classList.remove('active'));
  document.getElementById('panel-'+n).classList.add('active');
  b.classList.add('active');
}
function toggle(h){h.closest('.section-card').classList.toggle('open')}
function copyCmd(){
  navigator.clipboard.writeText('/apply Aplicatie-Staff').then(()=>{
    const e=document.getElementById('copy-confirm');
    e.style.opacity='1';setTimeout(()=>e.style.opacity='0',2500);
  });
}
</script>
</body>
</html>"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(debug=True)
