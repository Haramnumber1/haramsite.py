from flask import Flask, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# ============================================================
#  POSTĂRILE BLOGULUI — adaugă sau modifică aici
# ============================================================
posts = [
    {
        "id": 1,
        "title": "Bun venit pe blogul meu!",
        "content": "Acesta este primul meu articol. Salut tuturor! Sunt foarte bucuros că ați ajuns aici.",
        "date": "14 Martie 2025"
    },
    {
        "id": 2,
        "title": "De ce am creat acest blog",
        "content": "Am creat acest blog pentru a împărtăși gândurile și experiențele mele cu lumea. Sper că veți găsi ceva interesant aici.",
        "date": "14 Martie 2025"
    },
]

# ============================================================
#  CSS + JS comun pentru toate paginile
# ============================================================
STYLE = """
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0f0f0f;
  --surface:#1a1a1a;
  --border:#2a2a2a;
  --text:#e8e8e8;
  --muted:#888;
  --accent:#e8c547;
  --danger:#e05555;
}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}

nav{
  border-bottom:1px solid var(--border);
  padding:18px 0;
  position:sticky;top:0;
  background:rgba(15,15,15,0.95);
  backdrop-filter:blur(10px);
  z-index:100;
}
.nav-inner{
  max-width:780px;margin:0 auto;padding:0 24px;
  display:flex;justify-content:space-between;align-items:center;
}
.nav-brand{
  font-family:'Playfair Display',serif;
  font-size:22px;color:var(--text);
}
.nav-brand span{color:var(--accent)}
.nav-links{display:flex;gap:24px;align-items:center}
.nav-links a{color:var(--muted);font-size:14px;transition:color 0.2s}
.nav-links a:hover{color:var(--text);text-decoration:none}
.btn{
  display:inline-block;
  background:var(--accent);color:#0f0f0f;
  font-size:13px;font-weight:500;
  padding:9px 20px;border-radius:4px;
  border:none;cursor:pointer;
  transition:opacity 0.2s;font-family:'Inter',sans-serif;
}
.btn:hover{opacity:0.85;text-decoration:none;color:#0f0f0f}
.btn-ghost{
  background:transparent;color:var(--muted);
  border:1px solid var(--border);
  font-size:13px;font-weight:400;
  padding:8px 18px;border-radius:4px;
  cursor:pointer;font-family:'Inter',sans-serif;
  transition:all 0.2s;
}
.btn-ghost:hover{border-color:var(--muted);color:var(--text)}
.btn-danger{
  background:transparent;color:var(--danger);
  border:1px solid var(--danger);
  font-size:12px;padding:6px 14px;border-radius:4px;
  cursor:pointer;font-family:'Inter',sans-serif;
  transition:all 0.2s;
}
.btn-danger:hover{background:var(--danger);color:#fff}

.container{max-width:780px;margin:0 auto;padding:48px 24px}

/* Card post */
.post-card{
  border:1px solid var(--border);
  border-radius:8px;padding:28px;
  margin-bottom:20px;
  background:var(--surface);
  transition:border-color 0.2s;
}
.post-card:hover{border-color:#444}
.post-date{font-size:12px;color:var(--muted);letter-spacing:0.05em;margin-bottom:10px}
.post-title{
  font-family:'Playfair Display',serif;
  font-size:26px;font-weight:700;
  color:var(--text);margin-bottom:12px;line-height:1.3;
}
.post-title a{color:inherit}
.post-title a:hover{color:var(--accent);text-decoration:none}
.post-excerpt{font-size:15px;color:var(--muted);line-height:1.7;margin-bottom:18px}
.post-actions{display:flex;gap:10px;align-items:center}

/* Post complet */
.post-full .post-title{font-size:36px;margin-bottom:8px}
.post-full .post-content{
  font-size:16px;line-height:1.85;color:#ccc;
  margin-top:28px;white-space:pre-wrap;
}
.back-link{color:var(--muted);font-size:14px;display:inline-block;margin-bottom:32px}
.back-link:hover{color:var(--text)}

/* Form */
.form-group{margin-bottom:20px}
.form-group label{display:block;font-size:13px;color:var(--muted);margin-bottom:8px;letter-spacing:0.03em}
.form-group input,.form-group textarea{
  width:100%;background:var(--surface);
  border:1px solid var(--border);border-radius:6px;
  color:var(--text);font-family:'Inter',sans-serif;
  font-size:15px;padding:12px 16px;
  transition:border-color 0.2s;resize:vertical;
}
.form-group input:focus,.form-group textarea:focus{
  outline:none;border-color:var(--accent);
}
.form-group textarea{min-height:200px}
.page-title{
  font-family:'Playfair Display',serif;
  font-size:32px;margin-bottom:32px;
}

/* Hero */
.hero{
  text-align:center;padding:64px 0 48px;
  border-bottom:1px solid var(--border);margin-bottom:40px;
}
.hero h1{
  font-family:'Playfair Display',serif;
  font-size:clamp(36px,6vw,64px);
  font-weight:700;line-height:1.1;
  margin-bottom:16px;
}
.hero h1 em{color:var(--accent);font-style:italic}
.hero p{font-size:16px;color:var(--muted);max-width:440px;margin:0 auto 28px}

/* Empty state */
.empty{text-align:center;padding:64px 0;color:var(--muted)}
.empty p{margin-bottom:20px;font-size:16px}

/* Separator */
.sep{width:40px;height:2px;background:var(--accent);margin:0 0 24px}
</style>
"""

# ============================================================
#  PAGINA PRINCIPALĂ — lista postărilor
# ============================================================
@app.route("/")
def index():
    cards = ""
    if posts:
        for p in reversed(posts):
            excerpt = p["content"][:120] + ("..." if len(p["content"]) > 120 else "")
            cards += f"""
            <div class="post-card">
              <div class="post-date">{p['date']}</div>
              <div class="post-title"><a href="/post/{p['id']}">{p['title']}</a></div>
              <div class="post-excerpt">{excerpt}</div>
              <div class="post-actions">
                <a class="btn" href="/post/{p['id']}">Citește →</a>
                <a class="btn-ghost" href="/edit/{p['id']}">Editează</a>
                <form method="POST" action="/delete/{p['id']}" style="display:inline" onsubmit="return confirm('Ștergi postarea?')">
                  <button class="btn-danger" type="submit">Șterge</button>
                </form>
              </div>
            </div>"""
    else:
        cards = """<div class="empty">
          <p>Niciun articol încă. Fii primul!</p>
          <a class="btn" href="/new">+ Scrie primul articol</a>
        </div>"""

    return f"""<!DOCTYPE html><html lang="ro"><head>{STYLE}<title>Blogul Meu</title></head><body>
    <nav><div class="nav-inner">
      <div class="nav-brand">Haram<span>Blog</span></div>
      <div class="nav-links">
        <a href="/">Acasă</a>
        <a href="/new" class="btn">+ Articol nou</a>
      </div>
    </div></nav>
    <div class="container">
      <div class="hero">
        <h1>Blogul meu<br><em>personal</em></h1>
        <p>Gânduri, idei și povești împărtășite cu lumea.</p>
        <a class="btn" href="/new">+ Scrie ceva nou</a>
      </div>
      {cards}
    </div></body></html>"""

# ============================================================
#  PAGINA POSTARE COMPLETĂ
# ============================================================
@app.route("/post/<int:post_id>")
def post(post_id):
    p = next((x for x in posts if x["id"] == post_id), None)
    if not p:
        return redirect("/")
    return f"""<!DOCTYPE html><html lang="ro"><head>{STYLE}<title>{p['title']}</title></head><body>
    <nav><div class="nav-inner">
      <div class="nav-brand">Haram<span>Blog</span></div>
      <div class="nav-links">
        <a href="/">Acasă</a>
        <a href="/new" class="btn">+ Articol nou</a>
      </div>
    </div></nav>
    <div class="container post-full">
      <a class="back-link" href="/">← Înapoi la blog</a>
      <div class="sep"></div>
      <div class="post-date">{p['date']}</div>
      <div class="post-title">{p['title']}</div>
      <div class="post-content">{p['content']}</div>
      <div style="margin-top:40px;display:flex;gap:10px">
        <a class="btn-ghost" href="/edit/{p['id']}">Editează</a>
        <form method="POST" action="/delete/{p['id']}" onsubmit="return confirm('Ștergi postarea?')">
          <button class="btn-danger" type="submit">Șterge</button>
        </form>
      </div>
    </div></body></html>"""

# ============================================================
#  ADAUGĂ POSTARE NOUĂ
# ============================================================
@app.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if title and content:
            new_id = max((p["id"] for p in posts), default=0) + 1
            posts.append({
                "id": new_id,
                "title": title,
                "content": content,
                "date": datetime.now().strftime("%d %B %Y")
            })
        return redirect("/")
    return f"""<!DOCTYPE html><html lang="ro"><head>{STYLE}<title>Articol nou</title></head><body>
    <nav><div class="nav-inner">
      <div class="nav-brand">Haram<span>Blog</span></div>
      <div class="nav-links"><a href="/">Acasă</a></div>
    </div></nav>
    <div class="container">
      <a class="back-link" href="/">← Înapoi</a>
      <div class="page-title">Articol nou</div>
      <form method="POST">
        <div class="form-group">
          <label>Titlu</label>
          <input type="text" name="title" placeholder="Titlul articolului..." required/>
        </div>
        <div class="form-group">
          <label>Conținut</label>
          <textarea name="content" placeholder="Scrie articolul tău aici..." required></textarea>
        </div>
        <button class="btn" type="submit">Publică articolul</button>
      </form>
    </div></body></html>"""

# ============================================================
#  EDITEAZĂ POSTARE
# ============================================================
@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    p = next((x for x in posts if x["id"] == post_id), None)
    if not p:
        return redirect("/")
    if request.method == "POST":
        p["title"] = request.form.get("title", p["title"]).strip()
        p["content"] = request.form.get("content", p["content"]).strip()
        return redirect(f"/post/{post_id}")
    return f"""<!DOCTYPE html><html lang="ro"><head>{STYLE}<title>Editează</title></head><body>
    <nav><div class="nav-inner">
      <div class="nav-brand">Haram<span>Blog</span></div>
      <div class="nav-links"><a href="/">Acasă</a></div>
    </div></nav>
    <div class="container">
      <a class="back-link" href="/post/{p['id']}">← Înapoi la articol</a>
      <div class="page-title">Editează articolul</div>
      <form method="POST">
        <div class="form-group">
          <label>Titlu</label>
          <input type="text" name="title" value="{p['title']}" required/>
        </div>
        <div class="form-group">
          <label>Conținut</label>
          <textarea name="content" required>{p['content']}</textarea>
        </div>
        <button class="btn" type="submit">Salvează</button>
      </form>
    </div></body></html>"""

# ============================================================
#  ȘTERGE POSTARE
# ============================================================
@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return redirect("/")

# ============================================================
if __name__ == "__main__":
    app.run(debug=True)
