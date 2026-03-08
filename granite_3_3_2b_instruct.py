!pip install -U transformers
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="ibm-granite/granite-3.3-2b-instruct")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)

!pip install -q gradio

import gradio as gr
import json
import re
from datetime import datetime
from typing import Tuple, Dict, List
import random

# ============================================================================
# HTML QUICK-STYLER v3.1
# CHANGES FROM v3.0:
# - 5 redesigned elegant templates with unique color palettes & fonts
# - Style Chatbot now ACTUALLY MODIFIES the generated HTML/CSS in real-time
# - Templates auto-generate on click (no extra step needed)
# ============================================================================

import gradio as gr
from datetime import datetime
from typing import Dict, List, Tuple
import re
import urllib.parse

# ============================================================================
# COLOR PALETTE GENERATOR
# ============================================================================

class ColorPaletteGenerator:
    @staticmethod
    def generate_palette(style: str = "modern", theme: str = "dark") -> Dict[str, str]:
        dark_bg  = {'background': '#0f172a', 'surface': '#1e293b',
                    'text_primary': '#f1f5f9', 'text_secondary': '#cbd5e1', 'border': '#334155'}
        light_bg = {'background': '#f8fafc', 'surface': '#ffffff',
                    'text_primary': '#0f172a', 'text_secondary': '#475569', 'border': '#e2e8f0'}
        base = dark_bg if theme.lower() == "dark" else light_bg

        accent_colors = {
            'modern':   {'primary': '#667eea', 'secondary': '#764ba2', 'accent': '#f093fb'},
            'vibrant':  {'primary': '#ff6b6b', 'secondary': '#ff8e72', 'accent': '#f5576c'},
            'ocean':    {'primary': '#0099cc', 'secondary': '#006699', 'accent': '#00ccff'},
            'forest':   {'primary': '#27ae60', 'secondary': '#1e8449', 'accent': '#52be80'},
            'sunset':   {'primary': '#ff8c42', 'secondary': '#ff6b35', 'accent': '#ffa751'},
            'luxury':   {'primary': '#b8860b', 'secondary': '#8b6914', 'accent': '#FFD700'},
            'creative': {'primary': '#9b59b6', 'secondary': '#8e44ad', 'accent': '#e74c3c'},
            'minimal':  {'primary': '#2c3e50', 'secondary': '#34495e', 'accent': '#3498db'},
            # New elegant palettes for templates
            'midnight': {'primary': '#c9a84c', 'secondary': '#a07830', 'accent': '#f0d080'},
            'rose':     {'primary': '#c0496a', 'secondary': '#8b2a45', 'accent': '#f07090'},
            'nordic':   {'primary': '#4a90d9', 'secondary': '#2c5f8a', 'accent': '#7eb8f7'},
            'emerald':  {'primary': '#2ecc71', 'secondary': '#1a7a45', 'accent': '#a8edbc'},
            'charcoal': {'primary': '#e8e0d0', 'secondary': '#c8bfa8', 'accent': '#f5f0e8'},
        }
        return {**base, **accent_colors.get(style.lower(), accent_colors['modern'])}


# ============================================================================
# IMAGE HELPER
# ============================================================================

class ImageHelper:
    BASE = "https://source.unsplash.com"

    @staticmethod
    def extract_keywords(title: str, description: str, user_keywords: str = "") -> List[str]:
        if user_keywords.strip():
            kws = [k.strip() for k in re.split(r'[,\s]+', user_keywords) if k.strip()]
            return kws[:4]
        stop = {'the','a','an','and','or','is','in','on','with','for','to','of',
                'this','that','our','your','we','my','i','are','was','were',
                'section','page','website','banner','hero','footer','form'}
        combined = (title + ' ' + description).lower()
        words = re.findall(r'\b[a-z]{4,}\b', combined)
        seen, kws = set(), []
        for w in words:
            if w not in stop and w not in seen:
                seen.add(w); kws.append(w)
            if len(kws) == 4: break
        return kws if kws else ['technology', 'design', 'business', 'modern']

    @staticmethod
    def hero_url(keywords, w=1600, h=900):
        return f"{ImageHelper.BASE}/{w}x{h}/?{urllib.parse.quote(','.join(keywords[:3]))}"

    @staticmethod
    def portfolio_url(idx, keywords, w=800, h=600):
        return f"{ImageHelper.BASE}/{w}x{h}/?{urllib.parse.quote(','.join(keywords[:2]))}&sig={idx}"

    @staticmethod
    def about_url(keywords, w=1000, h=600):
        return f"{ImageHelper.BASE}/{w}x{h}/?{urllib.parse.quote(','.join(keywords[:2]))},team,office"


# ============================================================================
# TEMPLATE DEFINITIONS — each has its own complete CSS personality
# ============================================================================

class ElegantTemplates:

    # ── 1. MIDNIGHT GOLD — luxury dark with gold accents ──
    @staticmethod
    def midnight_gold(title="Luxury Studio", description="Hero, about, portfolio, testimonials, contact, footer"):
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Raleway:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

        :root {{
            --gold: #c9a84c;
            --gold-light: #f0d080;
            --bg: #0a0a0a;
            --surface: #111111;
            --surface2: #1a1a1a;
            --text: #f5f0e8;
            --muted: #888880;
            --border: #2a2a2a;
        }}

        @keyframes fadeUp   {{ from {{ opacity:0; transform:translateY(40px); }} to {{ opacity:1; transform:translateY(0); }} }}
        @keyframes shimmer  {{ 0%,100% {{ opacity:0.6; }} 50% {{ opacity:1; }} }}
        @keyframes lineGrow {{ from {{ width:0; }} to {{ width:60px; }} }}

        html {{ scroll-behavior:smooth; }}

        body {{
            font-family: 'Raleway', sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.8;
        }}

        /* NAV */
        header {{
            padding: 1.8rem 4rem;
            position: fixed; top:0; width:100%; z-index:100;
            border-bottom: 1px solid rgba(201,168,76,0.15);
            background: rgba(10,10,10,0.92);
            backdrop-filter: blur(16px);
            display: flex; justify-content:space-between; align-items:center;
        }}
        .logo {{
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem; font-weight:700;
            color: var(--gold); letter-spacing:0.05em;
        }}
        nav a {{
            color: var(--muted); text-decoration:none;
            margin-left: 2.5rem; font-size:0.85rem;
            letter-spacing:0.12em; text-transform:uppercase;
            transition: color 0.3s;
        }}
        nav a:hover {{ color: var(--gold); }}

        /* HERO */
        .hero {{
            min-height: 100vh;
            background: linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.5)),
                        url('https://source.unsplash.com/1600x900/?luxury,studio,elegant') center/cover;
            display: flex; align-items:center; justify-content:center;
            text-align: center; padding: 6rem 2rem 4rem;
            animation: fadeUp 1.2s ease both;
        }}
        .hero-content {{ max-width:800px; }}
        .hero-eyebrow {{
            font-size:0.8rem; letter-spacing:0.3em; text-transform:uppercase;
            color: var(--gold); margin-bottom:1.5rem;
        }}
        .hero h1 {{
            font-family: 'Playfair Display', serif;
            font-size: clamp(3rem, 8vw, 7rem); font-weight:900;
            line-height: 1.05; margin-bottom:1.5rem;
            color: var(--text);
        }}
        .hero h1 em {{ font-style:italic; color:var(--gold); }}
        .hero p {{ font-size:1.1rem; color:rgba(245,240,232,0.7); max-width:500px; margin:0 auto 2.5rem; }}
        .gold-line {{
            width:60px; height:1px; background:var(--gold);
            margin: 0 auto 2rem; animation: lineGrow 1s 0.5s ease both;
        }}

        /* BUTTONS */
        .btn-gold {{
            display:inline-block; padding:1rem 3rem;
            border:1px solid var(--gold); color:var(--gold);
            text-decoration:none; font-size:0.82rem;
            letter-spacing:0.2em; text-transform:uppercase;
            transition: all 0.3s; cursor:pointer; background:transparent;
            font-family: 'Raleway', sans-serif; font-weight:500;
        }}
        .btn-gold:hover {{
            background:var(--gold); color:var(--bg);
        }}
        .btn-solid {{
            background:var(--gold); color:var(--bg);
            border:1px solid var(--gold);
        }}
        .btn-solid:hover {{
            background:var(--gold-light); border-color:var(--gold-light);
        }}

        /* SECTIONS */
        main {{ padding-top: 80px; }}
        section {{ padding: 7rem 4rem; max-width:1200px; margin:0 auto; }}

        .section-label {{
            font-size:0.75rem; letter-spacing:0.3em; text-transform:uppercase;
            color:var(--gold); margin-bottom:1rem;
        }}
        h2 {{
            font-family:'Playfair Display',serif;
            font-size:clamp(2rem,4vw,3.5rem); font-weight:700;
            margin-bottom:1rem; line-height:1.2;
        }}
        .divider {{ width:60px; height:1px; background:var(--gold); margin:1.5rem 0 3rem; }}

        /* ABOUT */
        .about-grid {{
            display:grid; grid-template-columns:1fr 1fr; gap:5rem; align-items:center;
        }}
        .about-img {{
            width:100%; aspect-ratio:3/4; object-fit:cover;
            filter: grayscale(20%) contrast(1.1);
        }}
        .about-text p {{ color:var(--muted); font-size:1.05rem; margin-bottom:1rem; }}

        /* PORTFOLIO */
        .portfolio-grid {{
            display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem;
        }}
        .portfolio-item {{
            aspect-ratio:1;
            background:url('https://source.unsplash.com/600x600/?art,design&sig=__IDX__') center/cover;
            position:relative; overflow:hidden; cursor:pointer;
        }}
        .portfolio-item::after {{
            content:attr(data-title);
            position:absolute; inset:0;
            background:rgba(201,168,76,0.88);
            display:flex; align-items:center; justify-content:center;
            font-family:'Playfair Display',serif; font-size:1.2rem;
            color:var(--bg); opacity:0; transition:opacity 0.4s;
            font-weight:700;
        }}
        .portfolio-item:hover::after {{ opacity:1; }}

        /* TESTIMONIALS */
        .testimonials {{ background:var(--surface); padding:7rem 4rem; }}
        .testimonials-inner {{ max-width:1200px; margin:0 auto; }}
        .testimonials-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:3rem; margin-top:4rem; }}
        .testimonial {{
            border-left:2px solid var(--gold);
            padding-left:2rem;
        }}
        .testimonial blockquote {{
            font-family:'Playfair Display',serif; font-size:1.15rem;
            font-style:italic; color:var(--text); margin-bottom:1.5rem;
            line-height:1.7;
        }}
        .testimonial cite {{ color:var(--gold); font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase; }}

        /* CONTACT */
        .contact-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:5rem; align-items:start; }}
        .contact-info h2 {{ margin-bottom:0.5rem; }}
        .contact-info p {{ color:var(--muted); margin-bottom:2rem; }}
        .contact-form {{ display:flex; flex-direction:column; gap:1.2rem; }}
        .contact-form input, .contact-form textarea {{
            background:transparent; border:none; border-bottom:1px solid var(--border);
            color:var(--text); padding:0.8rem 0; font-family:'Raleway',sans-serif;
            font-size:0.95rem; outline:none; transition:border-color 0.3s;
        }}
        .contact-form input:focus, .contact-form textarea:focus {{
            border-bottom-color: var(--gold);
        }}
        .contact-form input::placeholder, .contact-form textarea::placeholder {{
            color:var(--muted); font-size:0.85rem; letter-spacing:0.08em;
        }}

        /* FOOTER */
        footer {{
            padding:3rem 4rem;
            border-top:1px solid var(--border);
            display:flex; justify-content:space-between; align-items:center;
            font-size:0.82rem; color:var(--muted);
        }}
        footer .footer-logo {{
            font-family:'Playfair Display',serif; color:var(--gold);
        }}

        @media(max-width:768px) {{
            header {{ padding:1.2rem 1.5rem; }}
            section {{ padding:4rem 1.5rem; }}
            .about-grid, .contact-grid {{ grid-template-columns:1fr; }}
            .portfolio-grid {{ grid-template-columns:repeat(2,1fr); }}
            footer {{ flex-direction:column; gap:1rem; text-align:center; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">{title}</div>
        <nav>
            <a href="#about">About</a>
            <a href="#portfolio">Work</a>
            <a href="#testimonials">Reviews</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>

    <div class="hero">
        <div class="hero-content">
            <p class="hero-eyebrow">Est. 2024 — Award Winning Studio</p>
            <div class="gold-line"></div>
            <h1>Crafting <em>Timeless</em><br>Experiences</h1>
            <p>Where luxury meets artistry. We create spaces and brands that endure.</p>
            <a href="#portfolio" class="btn-gold">View Our Work</a>
        </div>
    </div>

    <main>
        <section id="about">
            <div class="about-grid">
                <img class="about-img" src="https://source.unsplash.com/600x800/?luxury,interior,elegant" alt="About">
                <div class="about-text">
                    <p class="section-label">Our Story</p>
                    <h2>Beauty in Every Detail</h2>
                    <div class="divider"></div>
                    <p>We believe that true luxury lies in the details. Founded with a passion for excellence, our studio has spent over a decade perfecting the art of refined design.</p>
                    <p>Every project is approached with the same dedication — to create something that resonates, endures, and transcends trends.</p>
                    <br>
                    <button class="btn-gold">Our Philosophy</button>
                </div>
            </div>
        </section>

        <section id="portfolio">
            <p class="section-label">Selected Works</p>
            <h2>Our Portfolio</h2>
            <div class="divider"></div>
            <div class="portfolio-grid">
                <div class="portfolio-item" style="background-image:url('https://source.unsplash.com/600x600/?luxury,gold&sig=1')" data-title="Aurum Collection"></div>
                <div class="portfolio-item" style="background-image:url('https://source.unsplash.com/600x600/?interior,dark&sig=2')" data-title="Dark Velvet"></div>
                <div class="portfolio-item" style="background-image:url('https://source.unsplash.com/600x600/?architecture,minimal&sig=3')" data-title="White Label"></div>
                <div class="portfolio-item" style="background-image:url('https://source.unsplash.com/600x600/?fashion,luxury&sig=4')" data-title="Noir Series"></div>
                <div class="portfolio-item" style="background-image:url('https://source.unsplash.com/600x600/?jewelry,gold&sig=5')" data-title="Golden Hour"></div>
                <div class="portfolio-item" style="background-image:url('https://source.unsplash.com/600x600/?modern,design&sig=6')" data-title="Maison Edit"></div>
            </div>
        </section>
    </main>

    <div class="testimonials" id="testimonials">
        <div class="testimonials-inner">
            <p class="section-label">Kind Words</p>
            <h2>Client Voices</h2>
            <div class="divider"></div>
            <div class="testimonials-grid">
                <div class="testimonial">
                    <blockquote>"Working with this studio was transformative. They understood our vision before we could articulate it."</blockquote>
                    <cite>— Isabelle Laurent, Creative Director</cite>
                </div>
                <div class="testimonial">
                    <blockquote>"The attention to detail is unlike anything I've experienced. Every element felt considered and intentional."</blockquote>
                    <cite>— Marcus Chen, Founder</cite>
                </div>
                <div class="testimonial">
                    <blockquote>"They don't just design — they craft identity. Our brand feels alive for the first time."</blockquote>
                    <cite>— Sophia Reeves, CEO</cite>
                </div>
            </div>
        </div>
    </div>

    <main>
        <section id="contact">
            <div class="contact-grid">
                <div class="contact-info">
                    <p class="section-label">Get In Touch</p>
                    <h2>Let's Create Together</h2>
                    <div class="divider"></div>
                    <p>We work with select clients each year. If you're ready to elevate your brand, we'd love to hear from you.</p>
                    <p style="color:var(--gold);font-size:0.85rem;letter-spacing:0.1em;">hello@studio.com</p>
                </div>
                <form class="contact-form" onsubmit="return false;">
                    <input type="text" placeholder="YOUR NAME">
                    <input type="email" placeholder="YOUR EMAIL">
                    <input type="text" placeholder="PROJECT TYPE">
                    <textarea rows="4" placeholder="TELL US ABOUT YOUR PROJECT"></textarea>
                    <button type="submit" class="btn-gold btn-solid" style="width:fit-content;border:none;font-family:'Raleway',sans-serif;font-size:0.82rem;letter-spacing:0.2em;cursor:pointer;">SEND ENQUIRY</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <span class="footer-logo">{title}</span>
        <span>&copy; {datetime.now().year} All rights reserved.</span>
        <nav style="display:flex;gap:2rem;">
            <a href="#" style="color:var(--muted);text-decoration:none;">Privacy</a>
            <a href="#" style="color:var(--muted);text-decoration:none;">Terms</a>
        </nav>
    </footer>
</body>
</html>'''
        return html

    # ── 2. NORDIC FROST — clean Scandinavian light theme ──
    @staticmethod
    def nordic_frost(title="Nordic Design Co.", description="Hero, features, about, pricing, contact, footer"):
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

        :root {{
            --ink: #1a1f2e;
            --blue: #3d6cbf;
            --blue-soft: #e8eef8;
            --bg: #f4f2ee;
            --surface: #ffffff;
            --muted: #8a8f9a;
            --border: #e0ddd8;
            --accent: #e8e0d0;
        }}

        @keyframes fadeIn {{ from {{ opacity:0; transform:translateY(20px); }} to {{ opacity:1; transform:translateY(0); }} }}
        @keyframes float  {{ 0%,100% {{ transform:translateY(0); }} 50% {{ transform:translateY(-8px); }} }}

        html {{ scroll-behavior:smooth; }}
        body {{
            font-family:'DM Sans', sans-serif;
            background:var(--bg);
            color:var(--ink);
            line-height:1.7;
        }}

        /* NAV */
        header {{
            padding:1.5rem 5rem;
            background:var(--bg);
            border-bottom:1px solid var(--border);
            position:sticky; top:0; z-index:100;
            display:flex; justify-content:space-between; align-items:center;
        }}
        .logo {{
            font-family:'DM Serif Display', serif;
            font-size:1.5rem; color:var(--ink);
        }}
        nav a {{
            color:var(--muted); text-decoration:none;
            margin-left:2rem; font-size:0.9rem; font-weight:500;
            transition:color 0.3s;
        }}
        nav a:hover {{ color:var(--blue); }}
        .nav-cta {{
            background:var(--ink); color:#fff !important;
            padding:0.6rem 1.6rem; border-radius:4px;
            font-weight:600 !important;
        }}

        /* HERO */
        .hero {{
            padding:8rem 5rem 6rem;
            display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center;
            animation:fadeIn 0.9s ease both;
        }}
        .hero-text .eyebrow {{
            display:inline-block;
            background:var(--blue-soft); color:var(--blue);
            padding:0.3rem 1rem; border-radius:50px;
            font-size:0.8rem; font-weight:600; letter-spacing:0.05em;
            margin-bottom:1.5rem;
        }}
        .hero-text h1 {{
            font-family:'DM Serif Display', serif;
            font-size:clamp(2.8rem,5vw,4.5rem);
            line-height:1.1; color:var(--ink); margin-bottom:1.5rem;
        }}
        .hero-text h1 em {{ font-style:italic; color:var(--blue); }}
        .hero-text p {{ color:var(--muted); font-size:1.05rem; margin-bottom:2.5rem; max-width:420px; }}
        .hero-btns {{ display:flex; gap:1rem; flex-wrap:wrap; }}
        .hero-img {{
            background:url('https://source.unsplash.com/700x600/?scandinavian,minimal,design') center/cover;
            border-radius:4px; aspect-ratio:4/3;
        }}

        /* BUTTONS */
        .btn-primary {{
            background:var(--ink); color:#fff;
            padding:0.85rem 2rem; border:none; border-radius:4px;
            font-family:'DM Sans',sans-serif; font-size:0.9rem; font-weight:600;
            cursor:pointer; transition:all 0.2s;
        }}
        .btn-primary:hover {{ background:var(--blue); transform:translateY(-1px); }}
        .btn-outline {{
            background:transparent; color:var(--ink);
            padding:0.85rem 2rem; border:1.5px solid var(--ink); border-radius:4px;
            font-family:'DM Sans',sans-serif; font-size:0.9rem; font-weight:600;
            cursor:pointer; transition:all 0.2s;
        }}
        .btn-outline:hover {{ background:var(--ink); color:#fff; }}

        /* STATS STRIP */
        .stats {{
            background:var(--ink); color:#fff;
            padding:3rem 5rem;
            display:grid; grid-template-columns:repeat(4,1fr);
            text-align:center; gap:2rem;
        }}
        .stat-num {{
            font-family:'DM Serif Display',serif;
            font-size:2.8rem; color:var(--blue); display:block;
        }}
        .stat-label {{ font-size:0.85rem; color:rgba(255,255,255,0.6); margin-top:0.3rem; }}

        /* FEATURES */
        .features {{ padding:7rem 5rem; }}
        .features h2 {{
            font-family:'DM Serif Display',serif;
            font-size:2.5rem; margin-bottom:0.5rem;
        }}
        .features .sub {{ color:var(--muted); margin-bottom:4rem; }}
        .features-grid {{
            display:grid; grid-template-columns:repeat(3,1fr); gap:2.5rem;
        }}
        .feature-card {{
            padding:2.5rem; background:var(--surface);
            border:1px solid var(--border); border-radius:4px;
            transition:all 0.3s;
        }}
        .feature-card:hover {{
            border-color:var(--blue);
            box-shadow:0 12px 40px rgba(61,108,191,0.12);
            transform:translateY(-4px);
        }}
        .feature-num {{
            font-family:'DM Serif Display',serif; font-size:2rem;
            color:var(--blue-soft); border:1px solid var(--border);
            width:52px; height:52px; display:flex; align-items:center; justify-content:center;
            border-radius:4px; margin-bottom:1.5rem; font-style:italic;
            color:var(--blue);
        }}
        .feature-card h3 {{ font-size:1.15rem; font-weight:600; margin-bottom:0.5rem; }}
        .feature-card p {{ color:var(--muted); font-size:0.92rem; }}

        /* PRICING */
        .pricing {{ padding:7rem 5rem; background:var(--surface); }}
        .pricing h2 {{
            font-family:'DM Serif Display',serif; font-size:2.5rem; margin-bottom:0.5rem;
        }}
        .pricing .sub {{ color:var(--muted); margin-bottom:4rem; }}
        .pricing-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:2rem; }}
        .pricing-card {{
            padding:2.5rem; border:1px solid var(--border); border-radius:4px;
            position:relative; transition:all 0.3s;
        }}
        .pricing-card.featured {{
            border-color:var(--blue);
            background:var(--blue);
            color:#fff;
        }}
        .pricing-card.featured .price-sub,
        .pricing-card.featured li {{ color:rgba(255,255,255,0.75) !important; }}
        .pricing-card.featured h3 {{ color:#fff; }}
        .price {{ font-family:'DM Serif Display',serif; font-size:3rem; margin:1rem 0; }}
        .price-sub {{ font-size:0.85rem; color:var(--muted); }}
        .pricing-card h3 {{ font-size:1.1rem; font-weight:700; }}
        .pricing-card ul {{ list-style:none; margin:1.5rem 0 2rem; }}
        .pricing-card li {{ padding:0.4rem 0; color:var(--muted); font-size:0.92rem; }}
        .pricing-card li::before {{ content:'→ '; color:var(--blue); }}
        .pricing-card.featured li::before {{ color:rgba(255,255,255,0.8); }}

        /* CONTACT */
        .contact {{ padding:7rem 5rem; }}
        .contact-wrap {{
            background:var(--ink); border-radius:8px;
            padding:5rem; display:grid; grid-template-columns:1fr 1fr; gap:5rem;
            align-items:start;
        }}
        .contact-info h2 {{
            font-family:'DM Serif Display',serif; color:#fff; font-size:2.5rem; margin-bottom:1rem;
        }}
        .contact-info p {{ color:rgba(255,255,255,0.5); }}
        .contact-info .email {{
            display:inline-block; margin-top:1.5rem;
            font-size:1rem; color:rgba(255,255,255,0.8);
            border-bottom:1px solid rgba(255,255,255,0.2);
            padding-bottom:0.3rem;
        }}
        .contact-form {{ display:flex; flex-direction:column; gap:1rem; }}
        .contact-form input, .contact-form textarea {{
            padding:1rem 1.2rem; border:1px solid rgba(255,255,255,0.1);
            background:rgba(255,255,255,0.06); color:#fff;
            border-radius:4px; font-family:'DM Sans',sans-serif; font-size:0.9rem;
            outline:none; transition:border-color 0.3s;
        }}
        .contact-form input:focus, .contact-form textarea:focus {{
            border-color:var(--blue);
        }}
        .contact-form input::placeholder, .contact-form textarea::placeholder {{
            color:rgba(255,255,255,0.3);
        }}
        .btn-white {{
            background:#fff; color:var(--ink);
            padding:0.9rem 2rem; border:none; border-radius:4px;
            font-family:'DM Sans',sans-serif; font-weight:700; font-size:0.9rem;
            cursor:pointer; transition:all 0.2s; width:fit-content;
        }}
        .btn-white:hover {{ background:var(--blue); color:#fff; }}

        /* FOOTER */
        footer {{
            padding:2rem 5rem;
            border-top:1px solid var(--border);
            display:flex; justify-content:space-between; align-items:center;
            font-size:0.85rem; color:var(--muted);
        }}
        footer .footer-logo {{ font-family:'DM Serif Display',serif; color:var(--ink); }}

        @media(max-width:900px) {{
            header, .hero, .features, .pricing, .contact, .stats, footer {{
                padding-left:1.5rem; padding-right:1.5rem;
            }}
            .hero, .contact-wrap {{ grid-template-columns:1fr; }}
            .features-grid, .pricing-grid, .stats {{ grid-template-columns:repeat(2,1fr); }}
            .hero-img {{ display:none; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">{title}</div>
        <nav>
            <a href="#features">Services</a>
            <a href="#pricing">Pricing</a>
            <a href="#contact">Contact</a>
            <a href="#contact" class="nav-cta">Get Started</a>
        </nav>
    </header>

    <div class="hero">
        <div class="hero-text">
            <span class="eyebrow">✦ Design Studio</span>
            <h1>Simple.<br><em>Intentional.</em><br>Beautiful.</h1>
            <p>We craft clean digital experiences grounded in Nordic design principles — functionality, clarity, and quiet elegance.</p>
            <div class="hero-btns">
                <button class="btn-primary">Start a Project</button>
                <button class="btn-outline">See Our Work</button>
            </div>
        </div>
        <div class="hero-img"></div>
    </div>

    <div class="stats">
        <div><span class="stat-num">200+</span><div class="stat-label">Projects Delivered</div></div>
        <div><span class="stat-num">98%</span><div class="stat-label">Client Satisfaction</div></div>
        <div><span class="stat-num">8yr</span><div class="stat-label">In Business</div></div>
        <div><span class="stat-num">40+</span><div class="stat-label">Countries Served</div></div>
    </div>

    <div class="features" id="features">
        <h2>What We Do</h2>
        <p class="sub">End-to-end digital solutions for forward-thinking brands</p>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-num">01</div>
                <h3>Brand Identity</h3>
                <p>Strategy-led visual identities that communicate your values clearly and memorably.</p>
            </div>
            <div class="feature-card">
                <div class="feature-num">02</div>
                <h3>Web Design</h3>
                <p>Clean, conversion-focused websites built with precision and purpose.</p>
            </div>
            <div class="feature-card">
                <div class="feature-num">03</div>
                <h3>UX Strategy</h3>
                <p>Research-backed user experience design that removes friction and builds trust.</p>
            </div>
        </div>
    </div>

    <div class="pricing" id="pricing">
        <h2>Transparent Pricing</h2>
        <p class="sub">No hidden fees. No surprises. Just great work.</p>
        <div class="pricing-grid">
            <div class="pricing-card">
                <h3>Essential</h3>
                <div class="price">$2,400</div>
                <div class="price-sub">one-time project fee</div>
                <ul>
                    <li>Brand Guidelines</li>
                    <li>Logo Suite</li>
                    <li>2 Revision Rounds</li>
                    <li>14-day Delivery</li>
                </ul>
                <button class="btn-outline">Get Started</button>
            </div>
            <div class="pricing-card featured">
                <h3>Studio</h3>
                <div class="price">$5,800</div>
                <div class="price-sub">most popular package</div>
                <ul>
                    <li>Full Brand Identity</li>
                    <li>5-page Website</li>
                    <li>Unlimited Revisions</li>
                    <li>30-day Delivery</li>
                </ul>
                <button class="btn-white">Get Started</button>
            </div>
            <div class="pricing-card">
                <h3>Enterprise</h3>
                <div class="price">Custom</div>
                <div class="price-sub">tailored to your needs</div>
                <ul>
                    <li>Dedicated Team</li>
                    <li>Full Digital Suite</li>
                    <li>Priority Support</li>
                    <li>Ongoing Retainer</li>
                </ul>
                <button class="btn-outline">Contact Us</button>
            </div>
        </div>
    </div>

    <div class="contact" id="contact">
        <div class="contact-wrap">
            <div class="contact-info">
                <h2>Let's Build Something Remarkable</h2>
                <p>Have a project in mind? We'd love to learn more about your goals and how we can help.</p>
                <span class="email">hello@nordic.design</span>
            </div>
            <form class="contact-form" onsubmit="return false;">
                <input type="text" placeholder="Your name">
                <input type="email" placeholder="Email address">
                <textarea rows="4" placeholder="Tell us about your project..."></textarea>
                <button type="submit" class="btn-white">Send Message →</button>
            </form>
        </div>
    </div>

    <footer>
        <div class="footer-logo">{title}</div>
        <div>&copy; {datetime.now().year} All rights reserved</div>
        <div style="display:flex;gap:2rem;">
            <a href="#" style="color:var(--muted);text-decoration:none;">Privacy</a>
            <a href="#" style="color:var(--muted);text-decoration:none;">Terms</a>
        </div>
    </footer>
</body>
</html>'''
        return html

    # ── 3. EMERALD TECH — modern SaaS dark with green ──
    @staticmethod
    def emerald_tech(title="LaunchPad SaaS", description="Hero, features, pricing, testimonials, contact, footer"):
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

        :root {{
            --green: #00d97e;
            --green-dim: rgba(0,217,126,0.12);
            --bg: #080c10;
            --surface: #0f1419;
            --surface2: #161d26;
            --text: #e8f0fe;
            --muted: #6b7a8f;
            --border: #1e2a38;
        }}

        @keyframes fadeUp  {{ from {{ opacity:0; transform:translateY(24px); }} to {{ opacity:1; transform:translateY(0); }} }}
        @keyframes blink   {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:0; }} }}
        @keyframes glow    {{ 0%,100% {{ box-shadow:0 0 20px rgba(0,217,126,0.3); }} 50% {{ box-shadow:0 0 40px rgba(0,217,126,0.6); }} }}

        html {{ scroll-behavior:smooth; }}
        body {{ font-family:'Space Grotesk',sans-serif; background:var(--bg); color:var(--text); line-height:1.7; }}

        /* GRID BACKGROUND */
        body::before {{
            content:''; position:fixed; inset:0; pointer-events:none; z-index:0;
            background-image:
                linear-gradient(rgba(0,217,126,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,217,126,0.03) 1px, transparent 1px);
            background-size:60px 60px;
        }}

        /* NAV */
        header {{
            position:fixed; top:0; width:100%; z-index:100;
            padding:1.2rem 4rem;
            background:rgba(8,12,16,0.85); backdrop-filter:blur(16px);
            border-bottom:1px solid var(--border);
            display:flex; justify-content:space-between; align-items:center;
        }}
        .logo {{
            font-family:'Space Mono', monospace;
            font-size:1.2rem; color:var(--green);
            letter-spacing:-0.02em;
        }}
        .logo span {{ color:var(--text); }}
        nav a {{
            color:var(--muted); text-decoration:none;
            margin-left:2rem; font-size:0.9rem; font-weight:500;
            transition:color 0.3s;
        }}
        nav a:hover {{ color:var(--green); }}
        .nav-cta {{
            background:var(--green); color:var(--bg) !important;
            padding:0.55rem 1.4rem; border-radius:6px; font-weight:700 !important;
        }}

        /* HERO */
        .hero {{
            min-height:100vh; padding:9rem 4rem 5rem;
            display:flex; flex-direction:column; align-items:center; justify-content:center;
            text-align:center; position:relative; z-index:1;
            animation:fadeUp 0.9s ease both;
        }}
        .hero-badge {{
            display:inline-flex; align-items:center; gap:0.5rem;
            background:var(--green-dim); border:1px solid rgba(0,217,126,0.25);
            color:var(--green); padding:0.4rem 1rem; border-radius:50px;
            font-size:0.82rem; font-weight:600; margin-bottom:2rem;
        }}
        .badge-dot {{ width:7px; height:7px; border-radius:50%; background:var(--green); animation:blink 1.5s infinite; }}
        .hero h1 {{
            font-size:clamp(3rem,7vw,6rem); font-weight:700; line-height:1.05;
            margin-bottom:1.5rem; letter-spacing:-0.03em;
        }}
        .hero h1 .highlight {{
            color:var(--green);
            text-shadow:0 0 40px rgba(0,217,126,0.4);
        }}
        .hero p {{ font-size:1.15rem; color:var(--muted); max-width:560px; margin:0 auto 3rem; }}
        .hero-btns {{ display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }}

        /* BUTTONS */
        .btn-green {{
            background:var(--green); color:var(--bg);
            padding:0.9rem 2.4rem; border:none; border-radius:8px;
            font-family:'Space Grotesk',sans-serif; font-size:0.95rem; font-weight:700;
            cursor:pointer; transition:all 0.25s; animation:glow 3s ease infinite;
        }}
        .btn-green:hover {{ transform:translateY(-2px); filter:brightness(1.1); }}
        .btn-ghost {{
            background:transparent; color:var(--text);
            padding:0.9rem 2.4rem; border:1px solid var(--border); border-radius:8px;
            font-family:'Space Grotesk',sans-serif; font-size:0.95rem; font-weight:600;
            cursor:pointer; transition:all 0.25s;
        }}
        .btn-ghost:hover {{ border-color:var(--green); color:var(--green); }}

        /* FEATURES */
        .features {{ padding:7rem 4rem; position:relative; z-index:1; }}
        .section-tag {{
            display:inline-block;
            font-family:'Space Mono',monospace; font-size:0.78rem;
            color:var(--green); margin-bottom:1rem;
        }}
        .features h2 {{
            font-size:clamp(2rem,4vw,3rem); font-weight:700;
            letter-spacing:-0.02em; margin-bottom:0.5rem;
        }}
        .features .sub {{ color:var(--muted); margin-bottom:4rem; }}
        .features-grid {{
            display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem;
        }}
        .feature-card {{
            background:var(--surface); padding:2.5rem;
            border:1px solid var(--border); border-radius:12px;
            transition:all 0.3s; position:relative; overflow:hidden;
        }}
        .feature-card::before {{
            content:''; position:absolute; top:0; left:0; right:0;
            height:2px; background:linear-gradient(90deg,var(--green),transparent);
            transform:scaleX(0); transform-origin:left; transition:transform 0.3s;
        }}
        .feature-card:hover {{ border-color:rgba(0,217,126,0.3); transform:translateY(-4px); }}
        .feature-card:hover::before {{ transform:scaleX(1); }}
        .feature-icon {{
            font-size:1.8rem; margin-bottom:1.2rem;
            width:50px; height:50px; display:flex; align-items:center; justify-content:center;
            background:var(--green-dim); border-radius:10px;
        }}
        .feature-card h3 {{ font-size:1.1rem; font-weight:600; margin-bottom:0.6rem; }}
        .feature-card p {{ color:var(--muted); font-size:0.9rem; line-height:1.6; }}

        /* PRICING */
        .pricing {{ padding:7rem 4rem; background:var(--surface); position:relative; z-index:1; }}
        .pricing h2 {{ font-size:clamp(2rem,4vw,3rem); font-weight:700; letter-spacing:-0.02em; margin-bottom:0.5rem; }}
        .pricing .sub {{ color:var(--muted); margin-bottom:4rem; }}
        .pricing-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; align-items:start; }}
        .pricing-card {{
            background:var(--bg); padding:2.5rem;
            border:1px solid var(--border); border-radius:12px;
            position:relative; transition:border-color 0.3s;
        }}
        .pricing-card.featured {{
            border-color:var(--green);
            background:var(--surface2);
        }}
        .pop-tag {{
            position:absolute; top:-12px; left:50%; transform:translateX(-50%);
            background:var(--green); color:var(--bg);
            padding:0.25rem 1rem; border-radius:50px; font-size:0.78rem; font-weight:700;
            font-family:'Space Mono',monospace;
        }}
        .pricing-card h3 {{ font-size:1rem; font-weight:600; color:var(--muted); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:1.2rem; }}
        .price {{ font-size:3.5rem; font-weight:700; letter-spacing:-0.03em; }}
        .price sub {{ font-size:1rem; font-weight:400; color:var(--muted); }}
        .pricing-card ul {{ list-style:none; margin:1.8rem 0 2rem; }}
        .pricing-card li {{
            padding:0.45rem 0; color:var(--muted); font-size:0.9rem;
            display:flex; align-items:center; gap:0.6rem;
        }}
        .pricing-card li::before {{ content:'✓'; color:var(--green); font-weight:700; }}

        /* TESTIMONIALS */
        .testimonials {{ padding:7rem 4rem; position:relative; z-index:1; }}
        .testimonials h2 {{ font-size:clamp(2rem,4vw,3rem); font-weight:700; letter-spacing:-0.02em; margin-bottom:4rem; }}
        .testimonials-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }}
        .testimonial {{
            background:var(--surface); padding:2rem;
            border:1px solid var(--border); border-radius:12px;
        }}
        .t-stars {{ color:var(--green); margin-bottom:1rem; font-size:0.85rem; }}
        .testimonial p {{ color:var(--text); font-size:0.95rem; line-height:1.6; margin-bottom:1.5rem; }}
        .t-author {{ display:flex; align-items:center; gap:0.8rem; }}
        .t-avatar {{
            width:38px; height:38px; border-radius:50%;
            background:var(--green-dim); border:1px solid var(--green);
            display:flex; align-items:center; justify-content:center;
            font-size:0.78rem; font-weight:700; color:var(--green);
            font-family:'Space Mono',monospace;
        }}
        .t-name {{ font-size:0.88rem; font-weight:600; }}
        .t-role {{ font-size:0.78rem; color:var(--muted); }}

        /* CONTACT */
        .contact {{
            padding:7rem 4rem; position:relative; z-index:1;
            background:linear-gradient(180deg,var(--bg) 0%, var(--surface) 100%);
        }}
        .contact-wrap {{ max-width:600px; margin:0 auto; text-align:center; }}
        .contact h2 {{ font-size:clamp(2rem,4vw,3rem); font-weight:700; letter-spacing:-0.02em; margin-bottom:1rem; }}
        .contact p {{ color:var(--muted); margin-bottom:3rem; }}
        .contact-form {{ display:flex; flex-direction:column; gap:1rem; text-align:left; }}
        .contact-form input, .contact-form textarea {{
            background:var(--surface); border:1px solid var(--border);
            color:var(--text); padding:1rem 1.2rem; border-radius:8px;
            font-family:'Space Grotesk',sans-serif; font-size:0.95rem; outline:none;
            transition:border-color 0.3s;
        }}
        .contact-form input:focus, .contact-form textarea:focus {{ border-color:var(--green); }}
        .contact-form input::placeholder, .contact-form textarea::placeholder {{ color:var(--muted); }}

        /* FOOTER */
        footer {{
            padding:2rem 4rem; border-top:1px solid var(--border);
            display:flex; justify-content:space-between; align-items:center;
            font-size:0.82rem; color:var(--muted); position:relative; z-index:1;
        }}
        footer .footer-logo {{
            font-family:'Space Mono',monospace; color:var(--green); font-size:1rem;
        }}

        @media(max-width:900px) {{
            header, .hero, .features, .pricing, .testimonials, .contact, footer {{
                padding-left:1.5rem; padding-right:1.5rem;
            }}
            .features-grid, .pricing-grid, .testimonials-grid {{ grid-template-columns:1fr; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">{title[:8]}<span>.io</span></div>
        <nav>
            <a href="#features">Features</a>
            <a href="#pricing">Pricing</a>
            <a href="#testimonials">Reviews</a>
            <a href="#contact" class="nav-cta">Start Free</a>
        </nav>
    </header>

    <div class="hero">
        <div class="hero-badge"><div class="badge-dot"></div> Now in Public Beta</div>
        <h1>Ship Faster.<br>Scale <span class="highlight">Smarter.</span><br>Grow Bigger.</h1>
        <p>The all-in-one platform that removes your bottlenecks and lets your team move at the speed of ideas.</p>
        <div class="hero-btns">
            <button class="btn-green">Start Free — No Card Needed</button>
            <button class="btn-ghost">Watch Demo ▶</button>
        </div>
    </div>

    <div class="features" id="features">
        <div class="section-tag">// features</div>
        <h2>Everything You Need</h2>
        <p class="sub">Built by engineers who've felt the pain of clunky tools</p>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Blazing Performance</h3>
                <p>Sub-100ms response times. Built on edge infrastructure that scales automatically.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔐</div>
                <h3>Enterprise Security</h3>
                <p>SOC2 Type II certified. Zero-trust architecture with end-to-end encryption.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔗</div>
                <h3>200+ Integrations</h3>
                <p>Connect with every tool in your stack. Webhooks, APIs, and native connectors.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Real-time Analytics</h3>
                <p>Live dashboards that surface the metrics that actually matter to your team.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3>AI Automation</h3>
                <p>Automate repetitive workflows with intelligent agents that learn from your patterns.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌍</div>
                <h3>Global CDN</h3>
                <p>Deploy to 40+ regions with a single command. 99.99% uptime guaranteed.</p>
            </div>
        </div>
    </div>

    <div class="pricing" id="pricing">
        <div class="section-tag">// pricing</div>
        <h2>Simple, Honest Pricing</h2>
        <p class="sub">Start free. Scale when you're ready.</p>
        <div class="pricing-grid">
            <div class="pricing-card">
                <h3>Starter</h3>
                <div class="price">$0<sub>/mo</sub></div>
                <ul>
                    <li>Up to 3 projects</li>
                    <li>10K API calls/mo</li>
                    <li>Community support</li>
                    <li>Basic analytics</li>
                </ul>
                <button class="btn-ghost">Get Started Free</button>
            </div>
            <div class="pricing-card featured">
                <div class="pop-tag">MOST POPULAR</div>
                <h3>Pro</h3>
                <div class="price">$49<sub>/mo</sub></div>
                <ul>
                    <li>Unlimited projects</li>
                    <li>1M API calls/mo</li>
                    <li>Priority support</li>
                    <li>Advanced analytics</li>
                    <li>Custom domains</li>
                </ul>
                <button class="btn-green">Start Pro Trial</button>
            </div>
            <div class="pricing-card">
                <h3>Enterprise</h3>
                <div class="price">Custom</div>
                <ul>
                    <li>Unlimited everything</li>
                    <li>Dedicated SLA</li>
                    <li>White-glove onboarding</li>
                    <li>SSO / SAML</li>
                </ul>
                <button class="btn-ghost">Talk to Sales</button>
            </div>
        </div>
    </div>

    <div class="testimonials" id="testimonials">
        <div class="section-tag">// testimonials</div>
        <h2>Trusted by 10,000+ Teams</h2>
        <div class="testimonials-grid">
            <div class="testimonial">
                <div class="t-stars">★★★★★</div>
                <p>"We cut our deployment time from 2 hours to under 8 minutes. This platform is an absolute game-changer."</p>
                <div class="t-author">
                    <div class="t-avatar">AK</div>
                    <div><div class="t-name">Alex Kim</div><div class="t-role">CTO, Streamline</div></div>
                </div>
            </div>
            <div class="testimonial">
                <div class="t-stars">★★★★★</div>
                <p>"The analytics alone are worth the price. We finally understand what our users actually do."</p>
                <div class="t-author">
                    <div class="t-avatar">MR</div>
                    <div><div class="t-name">Maya Rao</div><div class="t-role">Head of Product, Velo</div></div>
                </div>
            </div>
            <div class="testimonial">
                <div class="t-stars">★★★★★</div>
                <p>"Support team responds in under 10 minutes. I've never experienced anything like this from a SaaS."</p>
                <div class="t-author">
                    <div class="t-avatar">JB</div>
                    <div><div class="t-name">James Burke</div><div class="t-role">Founder, Capsule</div></div>
                </div>
            </div>
        </div>
    </div>

    <div class="contact" id="contact">
        <div class="contact-wrap">
            <div class="section-tag">// contact</div>
            <h2>Ready to Launch?</h2>
            <p>Join 10,000+ teams who've already made the switch. Takes 60 seconds to get started.</p>
            <form class="contact-form" onsubmit="return false;">
                <input type="text" placeholder="Your name">
                <input type="email" placeholder="Work email">
                <textarea rows="3" placeholder="Tell us about your use case..."></textarea>
                <button type="submit" class="btn-green">Request Early Access →</button>
            </form>
        </div>
    </div>

    <footer>
        <div class="footer-logo">{title[:8]}.io</div>
        <div>&copy; {datetime.now().year} All rights reserved</div>
        <div style="display:flex;gap:2rem;">
            <a href="#" style="color:var(--muted);text-decoration:none;">Privacy</a>
            <a href="#" style="color:var(--muted);text-decoration:none;">Status</a>
            <a href="#" style="color:var(--muted);text-decoration:none;">Docs</a>
        </div>
    </footer>
</body>
</html>'''
        return html

    # ── 4. ROSE EDITORIAL — magazine-style blog/portfolio ──
    @staticmethod
    def rose_editorial(title="The Edit", description="Hero, about, portfolio, testimonials, contact, footer"):
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

        :root {{
            --rose: #c0496a;
            --rose-light: #f9eef1;
            --bg: #faf8f6;
            --ink: #1c1917;
            --warm: #8c7b6e;
            --border: #e8e0d8;
            --surface: #ffffff;
        }}

        @keyframes fadeIn {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
        @keyframes slideRight {{ from {{ transform:translateX(-30px); opacity:0; }} to {{ transform:translateX(0); opacity:1; }} }}

        html {{ scroll-behavior:smooth; }}
        body {{ font-family:'Jost',sans-serif; background:var(--bg); color:var(--ink); line-height:1.7; }}

        /* NAV */
        header {{
            padding:0 5rem;
            height:70px;
            border-bottom:1px solid var(--border);
            background:var(--bg);
            position:sticky; top:0; z-index:100;
            display:grid; grid-template-columns:1fr auto 1fr; align-items:center;
        }}
        nav.left {{ display:flex; gap:2rem; }}
        nav.right {{ display:flex; gap:2rem; justify-content:flex-end; }}
        nav a {{
            color:var(--warm); text-decoration:none;
            font-size:0.8rem; font-weight:400; letter-spacing:0.12em; text-transform:uppercase;
            transition:color 0.3s;
        }}
        nav a:hover {{ color:var(--rose); }}
        .logo-center {{
            font-family:'Cormorant Garamond',serif;
            font-size:2rem; font-weight:600; text-align:center; color:var(--ink);
            letter-spacing:0.08em;
        }}

        /* HERO — editorial split */
        .hero {{
            display:grid; grid-template-columns:1fr 1fr; min-height:90vh;
            animation:fadeIn 1s ease both;
        }}
        .hero-left {{
            padding:5rem;
            display:flex; flex-direction:column; justify-content:center;
            border-right:1px solid var(--border);
        }}
        .issue-tag {{
            font-size:0.75rem; letter-spacing:0.25em; text-transform:uppercase;
            color:var(--rose); margin-bottom:2rem; display:flex; align-items:center; gap:0.8rem;
        }}
        .issue-tag::before {{ content:''; flex:0 0 30px; height:1px; background:var(--rose); }}
        .hero-left h1 {{
            font-family:'Cormorant Garamond',serif;
            font-size:clamp(3.5rem,6vw,6rem); font-weight:400;
            line-height:1.0; margin-bottom:2rem; color:var(--ink);
        }}
        .hero-left h1 em {{ font-style:italic; color:var(--rose); }}
        .hero-left p {{ color:var(--warm); font-size:1rem; max-width:380px; margin-bottom:3rem; }}
        .hero-right {{
            background:url('https://source.unsplash.com/800x900/?fashion,editorial,portrait') center/cover;
        }}

        /* BUTTONS */
        .btn-rose {{
            display:inline-block; padding:0.9rem 2.5rem;
            background:var(--rose); color:#fff;
            text-decoration:none; font-size:0.8rem; letter-spacing:0.15em; text-transform:uppercase;
            font-weight:500; transition:all 0.25s; cursor:pointer; border:none; font-family:'Jost',sans-serif;
        }}
        .btn-rose:hover {{ background:var(--ink); }}
        .btn-line {{
            display:inline-block; padding:0.9rem 2.5rem;
            background:transparent; color:var(--ink);
            border:1px solid var(--ink); font-size:0.8rem; letter-spacing:0.15em; text-transform:uppercase;
            font-weight:500; transition:all 0.25s; cursor:pointer; font-family:'Jost',sans-serif;
        }}
        .btn-line:hover {{ background:var(--ink); color:#fff; }}

        /* SECTIONS */
        .section-header {{
            display:flex; align-items:center; gap:1.5rem; margin-bottom:4rem;
        }}
        .section-header h2 {{
            font-family:'Cormorant Garamond',serif;
            font-size:clamp(2rem,4vw,3.5rem); font-weight:400; white-space:nowrap;
        }}
        .section-line {{ flex:1; height:1px; background:var(--border); }}

        /* ABOUT */
        .about {{ padding:8rem 5rem; display:grid; grid-template-columns:1fr 2fr; gap:5rem; align-items:center; }}
        .about-label {{
            writing-mode:vertical-lr; text-orientation:mixed;
            font-size:0.75rem; letter-spacing:0.25em; text-transform:uppercase;
            color:var(--rose); transform:rotate(180deg);
        }}
        .about-text h2 {{
            font-family:'Cormorant Garamond',serif;
            font-size:clamp(2rem,3.5vw,3rem); font-weight:400; margin-bottom:1.5rem;
        }}
        .about-text p {{ color:var(--warm); margin-bottom:1rem; font-size:1rem; line-height:1.9; }}

        /* PORTFOLIO */
        .portfolio {{ padding:0 5rem 8rem; }}
        .portfolio-masonry {{
            display:grid; grid-template-columns:repeat(3,1fr);
            grid-template-rows:auto; gap:1.5rem;
        }}
        .portfolio-item {{
            overflow:hidden; cursor:pointer; position:relative;
        }}
        .portfolio-item img {{
            width:100%; display:block; transition:transform 0.5s ease;
            filter:saturate(0.8);
        }}
        .portfolio-item:hover img {{ transform:scale(1.04); filter:saturate(1); }}
        .portfolio-item:nth-child(1) {{ grid-row:span 2; }}
        .portfolio-caption {{
            padding:1rem 0 0.5rem;
            font-size:0.8rem; letter-spacing:0.1em; text-transform:uppercase;
            color:var(--warm);
        }}

        /* TESTIMONIALS */
        .testimonials {{
            padding:8rem 5rem; background:var(--ink); color:var(--bg);
        }}
        .testimonials .section-header h2 {{ color:var(--bg); }}
        .testimonials .section-line {{ background:rgba(255,255,255,0.15); }}
        .testimonials-grid {{ display:grid; grid-template-columns:repeat(2,1fr); gap:4rem; }}
        .testimonial blockquote {{
            font-family:'Cormorant Garamond',serif;
            font-size:1.4rem; font-style:italic; color:var(--bg);
            line-height:1.5; margin-bottom:1.5rem;
        }}
        .testimonial cite {{
            font-size:0.8rem; letter-spacing:0.15em; text-transform:uppercase;
            color:var(--rose);
        }}

        /* CONTACT */
        .contact {{
            padding:8rem 5rem;
            display:grid; grid-template-columns:1fr 1fr; gap:5rem;
        }}
        .contact-left h2 {{
            font-family:'Cormorant Garamond',serif;
            font-size:clamp(2.5rem,4vw,4rem); font-weight:400;
            line-height:1.1; margin-bottom:1.5rem;
        }}
        .contact-left h2 em {{ font-style:italic; color:var(--rose); }}
        .contact-left p {{ color:var(--warm); }}
        .contact-form {{ display:flex; flex-direction:column; gap:1.2rem; }}
        .contact-form input, .contact-form textarea {{
            background:transparent; border:none; border-bottom:1px solid var(--border);
            color:var(--ink); padding:0.8rem 0; font-family:'Jost',sans-serif;
            font-size:0.95rem; outline:none; transition:border-color 0.3s;
        }}
        .contact-form input:focus, .contact-form textarea:focus {{ border-bottom-color:var(--rose); }}
        .contact-form input::placeholder, .contact-form textarea::placeholder {{
            color:var(--warm); font-size:0.85rem; letter-spacing:0.05em;
        }}

        /* FOOTER */
        footer {{
            padding:2.5rem 5rem; border-top:1px solid var(--border);
            display:flex; justify-content:space-between; align-items:center;
            font-size:0.78rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--warm);
        }}

        @media(max-width:900px) {{
            header {{ grid-template-columns:auto; padding:0 1.5rem; height:auto; padding:1rem 1.5rem; }}
            nav.left, nav.right {{ display:none; }}
            .hero, .contact {{ grid-template-columns:1fr; }}
            .hero-right {{ height:300px; }}
            .about, .testimonials-grid {{ grid-template-columns:1fr; }}
            section, .about, .portfolio, .testimonials, .contact, footer {{ padding-left:1.5rem; padding-right:1.5rem; }}
            .portfolio-masonry {{ grid-template-columns:1fr 1fr; }}
            .portfolio-item:nth-child(1) {{ grid-row:auto; }}
        }}
    </style>
</head>
<body>
    <header>
        <nav class="left">
            <a href="#about">About</a>
            <a href="#portfolio">Work</a>
        </nav>
        <div class="logo-center">{title}</div>
        <nav class="right">
            <a href="#testimonials">Press</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>

    <div class="hero">
        <div class="hero-left">
            <div class="issue-tag">Vol. 01 — 2024</div>
            <h1>Where <em>Art</em><br>Meets<br>Purpose.</h1>
            <p>We tell stories through image, texture, and type. Creative direction for brands that refuse to be ordinary.</p>
            <div style="display:flex;gap:1rem;">
                <button class="btn-rose">See Our Work</button>
                <button class="btn-line">About Us</button>
            </div>
        </div>
        <div class="hero-right"></div>
    </div>

    <section class="about" id="about">
        <div class="about-label">Our Story</div>
        <div class="about-text">
            <h2>Designed with Intention, Crafted with Care</h2>
            <p>We're an independent creative studio working at the intersection of editorial design and brand storytelling. Founded in 2018, we've collaborated with writers, artists, and brands across 25 countries.</p>
            <p>We believe in work that makes people pause — and feel something real.</p>
            <br>
            <button class="btn-line">Read Our Manifesto</button>
        </div>
    </section>

    <section class="portfolio" id="portfolio">
        <div class="section-header">
            <h2>Selected Works</h2>
            <div class="section-line"></div>
        </div>
        <div class="portfolio-masonry">
            <div class="portfolio-item">
                <img src="https://source.unsplash.com/600x900/?editorial,fashion&sig=1" alt="Project 1">
                <div class="portfolio-caption">Maison Blanche — Brand Identity</div>
            </div>
            <div class="portfolio-item">
                <img src="https://source.unsplash.com/600x400/?minimal,art&sig=2" alt="Project 2">
                <div class="portfolio-caption">Reverie Magazine — Art Direction</div>
            </div>
            <div class="portfolio-item">
                <img src="https://source.unsplash.com/600x400/?design,print&sig=3" alt="Project 3">
                <div class="portfolio-caption">Lune — Campaign Design</div>
            </div>
            <div class="portfolio-item">
                <img src="https://source.unsplash.com/600x400/?photography,portrait&sig=4" alt="Project 4">
                <div class="portfolio-caption">The Observer — Editorial</div>
            </div>
            <div class="portfolio-item">
                <img src="https://source.unsplash.com/600x400/?lifestyle,elegant&sig=5" alt="Project 5">
                <div class="portfolio-caption">Odette — Packaging</div>
            </div>
        </div>
    </section>

    <section class="testimonials" id="testimonials">
        <div class="section-header">
            <h2>Kind Words</h2>
            <div class="section-line"></div>
        </div>
        <div class="testimonials-grid">
            <div class="testimonial">
                <blockquote>"They gave our brand a soul. Working with this studio changed everything about how we present ourselves to the world."</blockquote>
                <cite>— Céline Moreau, Creative Director, Maison Blanche</cite>
            </div>
            <div class="testimonial">
                <blockquote>"The editorial work they produced for our spring issue was the most shared thing we've ever published. Exceptional talent."</blockquote>
                <cite>— Thomas Reid, Editor, Reverie Magazine</cite>
            </div>
        </div>
    </section>

    <section class="contact" id="contact">
        <div class="contact-left">
            <h2>Let's Make<br>Something <em>Beautiful</em><br>Together.</h2>
            <p>We take on a limited number of projects each season to ensure dedicated attention to every client.</p>
        </div>
        <form class="contact-form" onsubmit="return false;">
            <input type="text" placeholder="Your Name">
            <input type="email" placeholder="Email Address">
            <input type="text" placeholder="Type of Project">
            <textarea rows="4" placeholder="Tell us about your vision..."></textarea>
            <button type="submit" class="btn-rose" style="width:fit-content;">Submit Enquiry</button>
        </form>
    </section>

    <footer>
        <span>{title} &copy; {datetime.now().year}</span>
        <span style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1rem;letter-spacing:0.05em;">Made with intention</span>
        <span>hello@studio.com</span>
    </footer>
</body>
</html>'''
        return html

    # ── 5. CHARCOAL RESTAURANT — food & hospitality ──
    @staticmethod
    def charcoal_restaurant(title="Ember & Oak", description="Hero, about, features, testimonials, contact, footer"):
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Outfit:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

        :root {{
            --amber: #c8773a;
            --amber-light: #f5e6d8;
            --bg: #1a1510;
            --surface: #231e18;
            --text: #f2ead8;
            --muted: #8a7a68;
            --border: #2e2820;
        }}

        @keyframes fadeUp {{ from {{ opacity:0; transform:translateY(30px); }} to {{ opacity:1; transform:translateY(0); }} }}
        @keyframes flicker {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:0.85; }} }}

        html {{ scroll-behavior:smooth; }}
        body {{ font-family:'Outfit',sans-serif; background:var(--bg); color:var(--text); line-height:1.8; }}

        /* NAV */
        header {{
            padding:1.5rem 5rem;
            position:fixed; top:0; width:100%; z-index:100;
            background:rgba(26,21,16,0.92); backdrop-filter:blur(12px);
            border-bottom:1px solid var(--border);
            display:flex; justify-content:space-between; align-items:center;
        }}
        .logo {{
            font-family:'Libre Baskerville',serif;
            font-size:1.6rem; color:var(--amber); letter-spacing:0.04em;
        }}
        nav a {{
            color:var(--muted); text-decoration:none;
            margin-left:2.5rem; font-size:0.85rem; letter-spacing:0.1em; text-transform:uppercase;
            transition:color 0.3s;
        }}
        nav a:hover {{ color:var(--amber); }}
        .reserve-btn {{
            background:var(--amber); color:var(--bg) !important;
            padding:0.6rem 1.6rem; font-weight:500 !important;
        }}

        /* HERO */
        .hero {{
            min-height:100vh;
            background:
                linear-gradient(to bottom, rgba(26,21,16,0.3) 0%, rgba(26,21,16,0.6) 60%, rgba(26,21,16,1) 100%),
                url('https://source.unsplash.com/1800x1100/?restaurant,fine-dining,dark') center/cover fixed;
            display:flex; flex-direction:column; align-items:center; justify-content:center;
            text-align:center; padding:5rem 2rem;
            animation:fadeUp 1.2s ease both;
        }}
        .hero-divider {{
            display:flex; align-items:center; gap:1rem; margin-bottom:2rem;
            color:var(--amber); font-size:0.75rem; letter-spacing:0.3em; text-transform:uppercase;
        }}
        .hero-divider::before, .hero-divider::after {{ content:''; width:40px; height:1px; background:var(--amber); }}
        .hero h1 {{
            font-family:'Libre Baskerville',serif;
            font-size:clamp(3.5rem,8vw,8rem); font-weight:400;
            line-height:1; margin-bottom:1.5rem; color:var(--text);
        }}
        .hero h1 em {{ font-style:italic; color:var(--amber); animation:flicker 4s ease infinite; }}
        .hero .tagline {{
            font-size:0.95rem; color:rgba(242,234,216,0.65);
            letter-spacing:0.2em; text-transform:uppercase; margin-bottom:3.5rem;
        }}
        .hero-btns {{ display:flex; gap:1.5rem; justify-content:center; }}

        /* BUTTONS */
        .btn-amber {{
            display:inline-block; padding:1rem 3rem;
            background:var(--amber); color:var(--bg);
            font-size:0.82rem; letter-spacing:0.15em; text-transform:uppercase;
            font-weight:500; transition:all 0.3s; cursor:pointer; border:none;
            font-family:'Outfit',sans-serif;
        }}
        .btn-amber:hover {{ background:#d9885a; }}
        .btn-ghost-amber {{
            display:inline-block; padding:1rem 3rem;
            background:transparent; color:var(--amber);
            border:1px solid var(--amber); font-size:0.82rem; letter-spacing:0.15em;
            text-transform:uppercase; font-weight:500; transition:all 0.3s; cursor:pointer;
            font-family:'Outfit',sans-serif;
        }}
        .btn-ghost-amber:hover {{ background:var(--amber); color:var(--bg); }}

        /* SECTIONS */
        section {{ padding:8rem 5rem; }}

        .section-ornament {{
            text-align:center; color:var(--amber); font-size:1.2rem; margin-bottom:0.5rem;
            letter-spacing:0.3em;
        }}
        h2 {{
            font-family:'Libre Baskerville',serif;
            font-size:clamp(2rem,4vw,3.5rem); font-weight:400;
            text-align:center; margin-bottom:1rem;
        }}
        .section-sub {{ text-align:center; color:var(--muted); margin-bottom:5rem; letter-spacing:0.05em; }}

        /* ABOUT */
        .about {{ background:var(--surface); }}
        .about-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:5rem; align-items:center; }}
        .about-img {{
            width:100%; aspect-ratio:3/4; object-fit:cover;
        }}
        .about-text .about-quote {{
            font-family:'Libre Baskerville',serif;
            font-size:1.3rem; font-style:italic;
            color:var(--amber); border-left:2px solid var(--amber);
            padding-left:1.5rem; margin-bottom:2rem; line-height:1.6;
        }}
        .about-text p {{ color:var(--muted); margin-bottom:1rem; }}

        /* MENU HIGHLIGHTS */
        .menu {{ }}
        .menu-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:2rem; }}
        .menu-card {{
            text-align:center; padding:2.5rem 1.5rem;
            border:1px solid var(--border); background:var(--surface);
            transition:border-color 0.3s;
        }}
        .menu-card:hover {{ border-color:var(--amber); }}
        .menu-img {{
            width:100%; aspect-ratio:1; object-fit:cover; margin-bottom:1.5rem;
        }}
        .menu-card h3 {{ font-family:'Libre Baskerville',serif; font-size:1.1rem; margin-bottom:0.3rem; }}
        .menu-card .price {{ color:var(--amber); font-size:0.9rem; letter-spacing:0.1em; }}
        .menu-card p {{ color:var(--muted); font-size:0.88rem; margin-top:0.5rem; }}

        /* TESTIMONIALS */
        .testimonials {{ background:var(--surface); }}
        .testimonials-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:3rem; }}
        .testimonial {{ text-align:center; padding:0 1rem; }}
        .testimonial .t-stars {{ color:var(--amber); font-size:1rem; margin-bottom:1.2rem; }}
        .testimonial blockquote {{
            font-family:'Libre Baskerville',serif; font-style:italic;
            font-size:1rem; color:var(--text); line-height:1.7; margin-bottom:1.5rem;
        }}
        .testimonial cite {{ font-size:0.8rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--muted); }}

        /* CONTACT / RESERVE */
        .contact {{ text-align:center; }}
        .contact-grid {{
            display:grid; grid-template-columns:1fr 1fr; gap:5rem;
            text-align:left; max-width:900px; margin:0 auto;
        }}
        .contact-info p {{ color:var(--muted); margin-bottom:0.5rem; }}
        .contact-info strong {{ color:var(--text); font-weight:500; display:block; margin-bottom:1.5rem; font-size:0.95rem; }}
        .contact-form {{ display:flex; flex-direction:column; gap:1.2rem; }}
        .contact-form input, .contact-form select, .contact-form textarea {{
            background:transparent; border:none; border-bottom:1px solid var(--border);
            color:var(--text); padding:0.8rem 0; font-family:'Outfit',sans-serif; font-size:0.95rem;
            outline:none; transition:border-color 0.3s;
        }}
        .contact-form input:focus, .contact-form select:focus {{ border-bottom-color:var(--amber); }}
        .contact-form input::placeholder {{ color:var(--muted); }}
        .contact-form select {{ color:var(--muted); background:var(--bg); }}

        /* FOOTER */
        footer {{
            padding:3rem 5rem; border-top:1px solid var(--border);
            display:flex; justify-content:space-between; align-items:center;
            font-size:0.82rem; color:var(--muted);
        }}
        footer .footer-logo {{
            font-family:'Libre Baskerville',serif; color:var(--amber); font-size:1.2rem;
        }}

        @media(max-width:900px) {{
            header, section, footer {{ padding-left:1.5rem; padding-right:1.5rem; }}
            .about-grid, .contact-grid {{ grid-template-columns:1fr; }}
            .menu-grid, .testimonials-grid {{ grid-template-columns:1fr; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">{title}</div>
        <nav>
            <a href="#about">Story</a>
            <a href="#menu">Menu</a>
            <a href="#testimonials">Reviews</a>
            <a href="#contact" class="reserve-btn">Reserve</a>
        </nav>
    </header>

    <div class="hero">
        <div class="hero-divider">Est. 2012 — Fine Dining</div>
        <h1>Where Fire<br>Meets <em>Flavour.</em></h1>
        <p class="tagline">Wood-fired cuisine · Locally sourced · Seasonally inspired</p>
        <div class="hero-btns">
            <button class="btn-amber">Reserve a Table</button>
            <button class="btn-ghost-amber">View Menu</button>
        </div>
    </div>

    <section class="about" id="about">
        <div class="about-grid">
            <img class="about-img" src="https://source.unsplash.com/600x800/?chef,kitchen,dark" alt="Chef">
            <div class="about-text">
                <div class="section-ornament">✦</div>
                <h2 style="text-align:left;margin-bottom:1.5rem;">The Story of<br>Ember & Oak</h2>
                <div class="about-quote">"Food is the ultimate expression of care — we grow it, prepare it, and share it with love."</div>
                <p>Founded in 2012 by Chef Marco Vidal, {title} was born from a simple belief: great food deserves great fire. Our wood-burning kitchen is the heart of everything we do.</p>
                <p>We source exclusively from small local farms within 100 miles, changing our menu with every season to honour what the land provides.</p>
                <br>
                <button class="btn-ghost-amber">Meet the Team</button>
            </div>
        </div>
    </section>

    <section class="menu" id="menu">
        <div class="section-ornament">✦ ✦ ✦</div>
        <h2>Signature Dishes</h2>
        <p class="section-sub">Crafted with fire, served with love</p>
        <div class="menu-grid">
            <div class="menu-card">
                <img class="menu-img" src="https://source.unsplash.com/400x400/?steak,grill&sig=1" alt="Dish">
                <h3>Prime Rib-Eye</h3>
                <div class="price">$58</div>
                <p>28-day dry-aged, oak-fired, served with bone marrow butter</p>
            </div>
            <div class="menu-card">
                <img class="menu-img" src="https://source.unsplash.com/400x400/?salmon,food&sig=2" alt="Dish">
                <h3>Cedar Salmon</h3>
                <div class="price">$42</div>
                <p>Wild Pacific salmon, cedar plank smoked, seasonal greens</p>
            </div>
            <div class="menu-card">
                <img class="menu-img" src="https://source.unsplash.com/400x400/?dessert,chocolate&sig=3" alt="Dish">
                <h3>Dark Chocolate Tart</h3>
                <div class="price">$16</div>
                <p>Valrhona 70%, salted caramel, hazelnut praline</p>
            </div>
        </div>
    </section>

    <section class="testimonials" id="testimonials">
        <div class="section-ornament">✦</div>
        <h2>Guest Voices</h2>
        <p class="section-sub">Words from those who've dined with us</p>
        <div class="testimonials-grid">
            <div class="testimonial">
                <div class="t-stars">★★★★★</div>
                <blockquote>"The best meal I've had in a decade. The rib-eye alone is worth making the journey for."</blockquote>
                <cite>— James L., Food Critic</cite>
            </div>
            <div class="testimonial">
                <div class="t-stars">★★★★★</div>
                <blockquote>"Intimate, warm, and utterly transported. Every dish tells a story of the season."</blockquote>
                <cite>— Anita K., Regular Guest</cite>
            </div>
            <div class="testimonial">
                <div class="t-stars">★★★★★</div>
                <blockquote>"We celebrated our anniversary here and it was truly magical. The team made us feel like family."</blockquote>
                <cite>— David & Sarah M.</cite>
            </div>
        </div>
    </section>

    <section class="contact" id="contact">
        <div class="section-ornament">✦</div>
        <h2>Reserve Your Table</h2>
        <p class="section-sub">We recommend booking in advance — tables fill quickly</p>
        <div class="contact-grid">
            <div class="contact-info">
                <p>Address</p>
                <strong>42 Hearth Street, London EC1A 1BB</strong>
                <p>Hours</p>
                <strong>Tue–Sat: 6pm–11pm<br>Sunday: 12pm–4pm</strong>
                <p>Phone</p>
                <strong>+44 20 7946 0958</strong>
            </div>
            <form class="contact-form" onsubmit="return false;">
                <input type="text" placeholder="Full Name">
                <input type="email" placeholder="Email Address">
                <input type="date">
                <select><option>2 Guests</option><option>3 Guests</option><option>4 Guests</option><option>5+ Guests</option></select>
                <textarea rows="3" placeholder="Special requests or dietary requirements..."></textarea>
                <button type="submit" class="btn-amber" style="width:fit-content;">Request Reservation</button>
            </form>
        </div>
    </section>

    <footer>
        <div class="footer-logo">{title}</div>
        <span>&copy; {datetime.now().year} — All rights reserved</span>
        <div style="display:flex;gap:2rem;">
            <a href="#" style="color:var(--muted);text-decoration:none;">Privacy</a>
            <a href="#" style="color:var(--muted);text-decoration:none;">Allergen Info</a>
        </div>
    </footer>
</body>
</html>'''
        return html


# ============================================================================
# HTML PAGE BUILDER (for custom generation)
# ============================================================================

class ColorPaletteGenerator:
    @staticmethod
    def generate_palette(style: str = "modern", theme: str = "dark") -> Dict[str, str]:
        dark_bg  = {'background': '#0f172a', 'surface': '#1e293b',
                    'text_primary': '#f1f5f9', 'text_secondary': '#cbd5e1', 'border': '#334155'}
        light_bg = {'background': '#f8fafc', 'surface': '#ffffff',
                    'text_primary': '#0f172a', 'text_secondary': '#475569', 'border': '#e2e8f0'}
        base = dark_bg if theme.lower() == "dark" else light_bg
        accent_colors = {
            'modern':   {'primary': '#667eea', 'secondary': '#764ba2', 'accent': '#f093fb'},
            'vibrant':  {'primary': '#ff6b6b', 'secondary': '#ff8e72', 'accent': '#f5576c'},
            'ocean':    {'primary': '#0099cc', 'secondary': '#006699', 'accent': '#00ccff'},
            'forest':   {'primary': '#27ae60', 'secondary': '#1e8449', 'accent': '#52be80'},
            'sunset':   {'primary': '#ff8c42', 'secondary': '#ff6b35', 'accent': '#ffa751'},
            'luxury':   {'primary': '#b8860b', 'secondary': '#8b6914', 'accent': '#FFD700'},
            'creative': {'primary': '#9b59b6', 'secondary': '#8e44ad', 'accent': '#e74c3c'},
            'minimal':  {'primary': '#2c3e50', 'secondary': '#34495e', 'accent': '#3498db'},
        }
        return {**base, **accent_colors.get(style.lower(), accent_colors['modern'])}


class HTMLPageBuilder:
    @staticmethod
    def extract_sections(description):
        section_keywords = {
            'hero':['hero','banner','landing'], 'features':['features','services','benefits'],
            'about':['about','team','company'], 'portfolio':['portfolio','gallery','work','projects'],
            'testimonials':['testimonial','reviews','feedback'], 'pricing':['pricing','plans','cost'],
            'contact':['contact','form','reach'], 'footer':['footer','bottom'],
        }
        desc_lower = description.lower()
        sections = []
        for stype, kws in section_keywords.items():
            for kw in kws:
                if kw in desc_lower:
                    sections.append(stype); break
        return sections if sections else ['hero','features','contact','footer']

    @staticmethod
    def generate_meta_tags(title, description):
        return f'''    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description[:160]}">'''

    @staticmethod
    def generate_section_html(section_type, palette, use_images=False, img_keywords=None):
        kws = img_keywords or ['technology','design','business']
        hero_bg = (
            f'background:linear-gradient(rgba(0,0,0,0.55),rgba(0,0,0,0.55)),url("{ImageHelper.hero_url(kws)}") center/cover no-repeat;'
        ) if use_images else f"background:linear-gradient(135deg,{palette['primary']} 0%,{palette['secondary']} 60%,{palette['accent']} 100%);"

        sections = {
            'hero': f'''        <section class="hero" id="hero" style="{hero_bg}">
            <div class="hero-content">
                <h1>Welcome to Your Site</h1>
                <p>Create amazing web experiences with modern design</p>
                <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
                    <button class="btn btn-primary">Get Started</button>
                    <button class="btn btn-secondary" style="border-color:white;color:white;">Learn More</button>
                </div>
            </div>
        </section>''',
            'features': '''        <section class="features" id="features">
            <h2>Our Features</h2>
            <div class="features-grid">
                <div class="feature-card"><div class="feature-icon">⚡</div><h3>Fast</h3><p>Lightning-quick performance</p></div>
                <div class="feature-card"><div class="feature-icon">🔒</div><h3>Secure</h3><p>Enterprise-grade security</p></div>
                <div class="feature-card"><div class="feature-icon">📈</div><h3>Scalable</h3><p>Grow without limits</p></div>
                <div class="feature-card"><div class="feature-icon">🎨</div><h3>Beautiful</h3><p>Stunning design</p></div>
            </div>
        </section>''',
            'about': f'''        <section class="about" id="about">
            <div class="about-inner">
                {f'<img src="{ImageHelper.about_url(kws)}" alt="About" style="width:100%;max-width:500px;border-radius:16px;">' if use_images else ''}
                <div class="about-text">
                    <h2>About Us</h2>
                    <p>We create beautiful, functional websites that help your business grow.</p>
                    <button class="btn btn-primary" style="margin-top:1.5rem;">Learn More</button>
                </div>
            </div>
        </section>''',
            'portfolio': f'''        <section class="portfolio" id="portfolio">
            <h2>Our Work</h2>
            <div class="portfolio-grid">
                {''.join([f'<div class="portfolio-item" style="background:url(\'{ImageHelper.portfolio_url(i,kws)}\') center/cover;"><div class="portfolio-overlay"><span>Project {i+1}</span></div></div>' for i in range(6)]) if use_images else ''.join([f'<div class="portfolio-item"><span>Project {i+1}</span></div>' for i in range(6)])}
            </div>
        </section>''',
            'testimonials': '''        <section class="testimonials" id="testimonials">
            <h2>What People Say</h2>
            <div class="testimonials-grid">
                <div class="testimonial"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Absolutely amazing results!"</p><div class="testimonial-author"><div class="author-avatar">SJ</div><span>Sarah Johnson, CEO</span></div></div>
                <div class="testimonial"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Highly recommended service!"</p><div class="testimonial-author"><div class="author-avatar">MW</div><span>Mark Williams, CTO</span></div></div>
                <div class="testimonial"><div class="stars">⭐⭐⭐⭐⭐</div><p>"Outstanding quality work."</p><div class="testimonial-author"><div class="author-avatar">ED</div><span>Emily Davis, Designer</span></div></div>
            </div>
        </section>''',
            'pricing': '''        <section class="pricing" id="pricing">
            <h2>Pricing Plans</h2>
            <div class="pricing-grid">
                <div class="pricing-card"><h3>Starter</h3><p class="price">$29<span>/mo</span></p><ul><li>✅ 5 Projects</li><li>✅ Basic Support</li></ul><button class="btn btn-secondary">Choose</button></div>
                <div class="pricing-card featured"><div class="badge">⭐ Popular</div><h3>Pro</h3><p class="price">$79<span>/mo</span></p><ul><li>✅ Unlimited</li><li>✅ Priority Support</li></ul><button class="btn btn-primary">Choose</button></div>
                <div class="pricing-card"><h3>Enterprise</h3><p class="price">$199<span>/mo</span></p><ul><li>✅ Custom</li><li>✅ Dedicated Support</li></ul><button class="btn btn-secondary">Choose</button></div>
            </div>
        </section>''',
            'contact': '''        <section class="contact" id="contact">
            <h2>Get in Touch</h2>
            <form class="contact-form" onsubmit="return false;">
                <div class="form-row"><input type="text" placeholder="Your Name" required><input type="email" placeholder="Your Email" required></div>
                <input type="text" placeholder="Subject">
                <textarea rows="5" placeholder="Your Message..." required></textarea>
                <button type="submit" class="btn btn-primary" style="width:100%;">Send Message ✉️</button>
            </form>
        </section>''',
            'footer': f'''        <footer class="footer">
            <div class="footer-content">
                <div class="footer-brand"><h3 style="color:{palette['primary']};">YourBrand</h3><p>Building the future.</p></div>
                <div class="footer-links"><a href="#hero">Home</a><a href="#features">Features</a><a href="#contact">Contact</a></div>
            </div>
            <div style="text-align:center;padding-top:1rem;font-size:0.85rem;color:var(--text-secondary);">&copy; {datetime.now().year} YourBrand. All rights reserved.</div>
        </footer>'''
        }
        return sections.get(section_type, '')

    @staticmethod
    def generate_css(palette, animated=True, theme="dark"):
        anim_kf = """
        @keyframes fadeInUp  { from{opacity:0;transform:translateY(30px)} to{opacity:1;transform:translateY(0)} }
        @keyframes slideDown { from{opacity:0;transform:translateY(-30px)} to{opacity:1;transform:translateY(0)} }
        @keyframes float     { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }
        @keyframes glow      { 0%,100%{box-shadow:0 0 20px rgba(102,126,234,.4)} 50%{box-shadow:0 0 40px rgba(102,126,234,.8)} }
        """ if animated else ""
        header_bg = "rgba(15,23,42,0.95)" if theme=="dark" else "rgba(255,255,255,0.95)"
        return f'''    <style>
        *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
        :root{{--primary:{palette['primary']};--secondary:{palette['secondary']};--accent:{palette['accent']};--background:{palette['background']};--surface:{palette['surface']};--text-primary:{palette['text_primary']};--text-secondary:{palette['text_secondary']};--border:{palette['border']};}}
        {anim_kf}
        html{{scroll-behavior:smooth;}}
        body{{font-family:'Segoe UI',sans-serif;background:var(--background);color:var(--text-primary);line-height:1.7;}}
        header{{background:{header_bg};backdrop-filter:blur(14px);padding:1.1rem 2rem;position:sticky;top:0;z-index:100;border-bottom:1px solid var(--border);}}
        header nav{{display:flex;justify-content:space-between;align-items:center;max-width:1200px;margin:0 auto;}}
        .logo{{font-size:1.8rem;font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
        header nav a{{color:var(--text-secondary);text-decoration:none;margin:0 1rem;font-weight:500;transition:color .3s;}}
        header nav a:hover{{color:var(--primary);}}
        main{{max-width:1200px;margin:0 auto;padding:0 2rem;}}
        section{{padding:5rem 0;}}
        h1{{font-size:clamp(2rem,5vw,4rem);font-weight:800;margin-bottom:1rem;}}
        h2{{font-size:clamp(1.5rem,3vw,2.5rem);text-align:center;margin-bottom:3rem;font-weight:700;}}
        h3{{font-size:1.3rem;margin-bottom:.5rem;}}
        .hero{{color:white;padding:8rem 2rem;text-align:center;min-height:600px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;{("animation:fadeInUp .9s ease both;" if animated else "")}}}
        .hero-content{{position:relative;z-index:1;max-width:700px;margin:0 auto;}}
        .hero h1{{color:white;text-shadow:0 2px 20px rgba(0,0,0,.4);{("animation:slideDown .8s ease both;" if animated else "")}}}
        .hero p{{font-size:1.25rem;opacity:.92;margin-bottom:2.5rem;}}
        .btn{{padding:.85rem 2.2rem;border:none;border-radius:50px;font-size:1rem;cursor:pointer;font-weight:700;display:inline-block;transition:all .3s;}}
        .btn-primary{{background:linear-gradient(135deg,var(--primary),var(--accent));color:white;box-shadow:0 4px 20px rgba(0,0,0,.25);{("animation:glow 3s ease infinite;" if animated else "")}}}
        .btn-primary:hover{{transform:translateY(-3px) scale(1.03);}}
        .btn-secondary{{background:transparent;color:var(--primary);border:2px solid var(--primary);}}
        .btn-secondary:hover{{background:var(--primary);color:white;}}
        .features-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:2rem;}}
        .feature-card{{background:var(--surface);padding:2.5rem 2rem;border-radius:16px;border:1px solid var(--border);transition:all .3s;text-align:center;}}
        .feature-card:hover{{transform:translateY(-10px);border-color:var(--primary);box-shadow:0 24px 48px rgba(0,0,0,.2);}}
        .feature-icon{{font-size:2.8rem;margin-bottom:1rem;display:block;{("animation:float 3s ease-in-out infinite;" if animated else "")}}}
        .feature-card h3{{color:var(--primary);}} .feature-card p{{color:var(--text-secondary);}}
        .about{{padding:4rem 2rem;background:var(--surface);border-radius:24px;}}
        .about-inner{{max-width:1000px;margin:0 auto;display:flex;gap:3rem;align-items:center;flex-wrap:wrap;}}
        .about-text p{{color:var(--text-secondary);}}
        .portfolio-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;}}
        .portfolio-item{{aspect-ratio:4/3;background:linear-gradient(135deg,var(--primary),var(--secondary));border-radius:16px;cursor:pointer;transition:all .35s;display:flex;align-items:center;justify-content:center;font-size:1.1rem;color:white;font-weight:600;position:relative;overflow:hidden;}}
        .portfolio-item:hover{{transform:scale(1.04);box-shadow:0 24px 48px rgba(0,0,0,.3);}}
        .portfolio-overlay{{position:absolute;inset:0;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .3s;border-radius:16px;}}
        .portfolio-item:hover .portfolio-overlay{{opacity:1;}}
        .testimonials-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2rem;}}
        .testimonial{{background:var(--surface);padding:2rem;border-left:4px solid var(--primary);border-radius:12px;}}
        .stars{{font-size:1.1rem;margin-bottom:.8rem;}}
        .testimonial p{{font-style:italic;color:var(--text-secondary);margin-bottom:1rem;}}
        .testimonial-author{{display:flex;align-items:center;gap:.8rem;}}
        .author-avatar{{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--accent));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;color:white;}}
        .testimonial span{{font-weight:600;color:var(--primary);}}
        .pricing-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:2rem;align-items:center;}}
        .pricing-card{{background:var(--surface);padding:2.5rem 2rem;border-radius:16px;border:1px solid var(--border);text-align:center;transition:all .3s;position:relative;}}
        .pricing-card.featured{{border-color:var(--primary);box-shadow:0 20px 50px rgba(0,0,0,.3);transform:scale(1.06);}}
        .badge{{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--primary),var(--accent));color:white;padding:.3rem 1.2rem;border-radius:50px;font-size:.85rem;font-weight:700;}}
        .price{{font-size:3rem;color:var(--primary);font-weight:800;margin:1.2rem 0;}} .price span{{font-size:1rem;color:var(--text-secondary);}}
        .pricing-card ul{{list-style:none;margin:1.5rem 0 2rem;text-align:left;}} .pricing-card li{{padding:.4rem 0;color:var(--text-secondary);}}
        .contact{{max-width:680px;margin:0 auto;text-align:center;}}
        .contact-form{{display:flex;flex-direction:column;gap:1.2rem;text-align:left;margin-top:2rem;}}
        .form-row{{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;}}
        .contact-form input,.contact-form textarea{{padding:1rem 1.2rem;border:1.5px solid var(--border);border-radius:10px;background:var(--surface);color:var(--text-primary);font-family:inherit;font-size:1rem;outline:none;transition:border-color .3s;}}
        .contact-form input:focus,.contact-form textarea:focus{{border-color:var(--primary);}}
        .footer{{background:var(--surface);border-top:1px solid var(--border);padding:3rem 2rem;margin-top:4rem;}}
        .footer-content{{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:2rem;padding-bottom:1.5rem;}}
        .footer-links{{display:flex;gap:1.5rem;}} .footer-links a{{color:var(--text-secondary);text-decoration:none;transition:color .3s;}} .footer-links a:hover{{color:var(--primary);}}
        @media(max-width:768px){{header nav{{flex-direction:column;gap:1rem;text-align:center;}}.hero{{padding:5rem 1.5rem;}}main{{padding:0 1rem;}}section{{padding:3rem 0;}}.form-row{{grid-template-columns:1fr;}}.pricing-card.featured{{transform:scale(1);}}}}
    </style>'''


class HTMLGenerationEngine:
    @staticmethod
    def generate_page(title, description, style="modern", theme="dark", animated=True, use_images=False, image_keywords=""):
        palette  = ColorPaletteGenerator.generate_palette(style, theme)
        sections = HTMLPageBuilder.extract_sections(description)
        meta     = HTMLPageBuilder.generate_meta_tags(title, description)
        css      = HTMLPageBuilder.generate_css(palette, animated, theme)
        img_kws  = ImageHelper.extract_keywords(title, description, image_keywords)
        sections_html = '\n\n'.join([
            HTMLPageBuilder.generate_section_html(s, palette, use_images, img_kws)
            for s in sections if HTMLPageBuilder.generate_section_html(s, palette, use_images, img_kws)
        ])
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{meta}
{css}
</head>
<body>
    <header>
        <nav>
            <span class="logo">{title}</span>
            <div><a href="#features">Features</a><a href="#about">About</a><a href="#portfolio">Portfolio</a><a href="#contact">Contact</a></div>
        </nav>
    </header>
    <main>
{sections_html}
    </main>
</body>
</html>'''
        return html, palette


# ============================================================================
# CODE EXPLAINER
# ============================================================================

class CodeExplainer:
    @staticmethod
    def explain(html_code):
        if not html_code.strip():
            return "⚠️ No HTML code found. Please generate a page first."
        parts = ["## 📖 Plain-English Code Explanation\n"]
        if '<meta' in html_code:
            parts.append("### 🏷️ META Tags\n- `charset=UTF-8` → supports all languages\n- `viewport` → mobile-responsive\n- `<title>` → browser tab text\n- `og:` tags → social media sharing previews\n")
        if ':root' in html_code:
            parts.append("### 🎨 CSS Variables (`:root`)\nAll colours defined once as variables (`--primary`, `--surface`, etc). Changing one updates the entire page.\n")
        if '@keyframes' in html_code:
            parts.append("### 🎬 Animations (`@keyframes`)\n- `fadeInUp` — elements rise into view\n- `slideDown` — hero title drops in\n- `float` — icons bob continuously\n- `glow` — buttons pulse softly\n")
        if 'sticky' in html_code:
            parts.append("### 📌 Sticky Nav\n`position:sticky; top:0` keeps the nav visible while scrolling. `backdrop-filter:blur` creates a frosted-glass effect.\n")
        if 'class="hero"' in html_code:
            parts.append("### 🦸 Hero Section\nLarge banner. Uses CSS gradient or Unsplash photo. A `::before` pseudo-element adds an atmospheric glow overlay.\n")
        if 'features-grid' in html_code:
            parts.append("### ⚡ Features Grid\n`grid-template-columns: repeat(auto-fit, minmax(230px,1fr))` auto-adjusts columns by screen width.\n")
        if 'portfolio-grid' in html_code:
            parts.append("### 🖼️ Portfolio\n6 tiles in a responsive grid. Hover reveals a dark overlay. `aspect-ratio:4/3` keeps consistent proportions.\n")
        if 'pricing-grid' in html_code:
            parts.append("### 💰 Pricing Cards\nFeatured card scaled up 6% to draw attention. Badge positioned with `position:absolute`.\n")
        if 'contact-form' in html_code:
            parts.append("### 📬 Contact Form\n2-column row for name+email. Focus states add a coloured glow. `onsubmit=return false` prevents page reload.\n")
        if '@media' in html_code:
            parts.append("### 📱 Responsive\n`@media(max-width:768px)` adapts layout for phones — stacks nav, reduces padding, fixes pricing card scale.\n")
        if 'source.unsplash.com' in html_code:
            parts.append("### 🖼️ Unsplash Images\nFree photos fetched by keyword URL — no API key needed. `sig=N` makes each portfolio tile unique.\n")
        parts.append("---\n✅ **Self-contained** — save as `.html`, open in any browser. No server needed.")
        return '\n'.join(parts)


# ============================================================================
# STYLE CHATBOT — now ACTUALLY MODIFIES the HTML
# ============================================================================

class StyleChatbot:

    @staticmethod
    def apply_modification(html_code: str, topic: str, variant: int) -> str:
        """Actually modify the CSS in the HTML string based on topic and variant."""
        if not html_code.strip():
            return html_code

        mods = {
            'font': [
                # Variant 0: elegant serif headings
                lambda h: re.sub(
                    r"(h1\s*,\s*h2[^{]*\{)",
                    r"\1 font-family:'Georgia',serif; letter-spacing:-0.01em;",
                    h
                ) if "font-family:'Georgia'" not in h else h,
                # Variant 1: modern mono for h2
                lambda h: re.sub(
                    r"(h2\s*\{[^}]*)(font-size)",
                    r"\1font-family:'Courier New',monospace; text-transform:uppercase; letter-spacing:0.08em; \2",
                    h
                ) if "Courier New" not in h else h,
                # Variant 2: larger, bolder h1
                lambda h: re.sub(
                    r"(h1\s*\{[^}]*font-size\s*:\s*)clamp\([^)]+\)",
                    r"\1clamp(3rem,7vw,6rem)",
                    h
                ),
            ],
            'button': [
                # Variant 0: sharp corners
                lambda h: h.replace('border-radius:50px', 'border-radius:4px'),
                # Variant 1: uppercase bold
                lambda h: re.sub(
                    r'(\.btn\s*\{[^}]*)(cursor:pointer)',
                    r'\1text-transform:uppercase; letter-spacing:0.12em; \2',
                    h
                ) if 'text-transform:uppercase' not in h else h,
                # Variant 2: flat solid primary
                lambda h: re.sub(
                    r'(\.btn-primary\s*\{[^}]*)background\s*:\s*linear-gradient\([^;]+\)',
                    r'\1background: var(--primary)',
                    h
                ),
            ],
            'card': [
                # Variant 0: glassmorphism
                lambda h: re.sub(
                    r'(\.feature-card\s*\{[^}]*background\s*:\s*)[^;]+;',
                    r'\1rgba(255,255,255,0.04); backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);',
                    h
                ),
                # Variant 1: rounder
                lambda h: re.sub(
                    r'(\.feature-card\s*\{[^}]*)border-radius\s*:\s*\d+px',
                    r'\1border-radius:24px',
                    h
                ),
                # Variant 2: stronger hover shadow
                lambda h: re.sub(
                    r'(\.feature-card:hover\s*\{[^}]*)box-shadow\s*:[^;]+;',
                    r'\1box-shadow:0 32px 64px rgba(0,0,0,0.4);',
                    h
                ),
            ],
            'hero': [
                # Variant 0: full-screen
                lambda h: h.replace('min-height:600px', 'min-height:100vh').replace('min-height: 600px', 'min-height: 100vh'),
                # Variant 1: larger text
                lambda h: re.sub(
                    r'(\.hero\s+h1\s*\{[^}]*)text-shadow',
                    r'\1font-size:clamp(3rem,8vw,7rem); text-shadow',
                    h
                ) if 'font-size:clamp(3rem,8vw' not in h else h,
                # Variant 2: center padded
                lambda h: h.replace('padding:8rem 2rem', 'padding:10rem 3rem'),
            ],
            'spacing': [
                # Variant 0: more section padding
                lambda h: re.sub(r'section\s*\{[^}]*padding\s*:\s*5rem 0', lambda m: m.group().replace('5rem', '7rem'), h),
                # Variant 1: wider main
                lambda h: h.replace('max-width:1200px', 'max-width:1400px'),
                # Variant 2: larger gap in grids
                lambda h: h.replace('gap:2rem', 'gap:3rem'),
            ],
            'animation': [
                # Variant 0: slower hero
                lambda h: h.replace('fadeInUp 0.9s ease', 'fadeInUp 1.4s ease'),
                # Variant 1: springy buttons
                lambda h: re.sub(
                    r'(\.btn[^-][^}]*)(transition\s*:\s*all [^;]+;)',
                    r'\1transition: all 0.4s cubic-bezier(0.34,1.56,0.64,1);',
                    h
                ),
                # Variant 2: slower float
                lambda h: h.replace('float 3s ease-in-out infinite', 'float 5s ease-in-out infinite'),
            ],
            'color_primary': [
                lambda h: re.sub(r'--primary\s*:\s*#[a-fA-F0-9]{3,6};', '--primary: #e63946;', h),
                lambda h: re.sub(r'--primary\s*:\s*#[a-fA-F0-9]{3,6};', '--primary: #2ecc71;', h),
                lambda h: re.sub(r'--primary\s*:\s*#[a-fA-F0-9]{3,6};', '--primary: #f39c12;', h),
            ],
            'border': [
                lambda h: re.sub(r'border-radius\s*:\s*16px', 'border-radius:0', h),
                lambda h: re.sub(r'border-radius\s*:\s*16px', 'border-radius:32px', h),
                lambda h: h,
            ],
        }

        fn_list = mods.get(topic)
        if fn_list:
            fn = fn_list[variant % len(fn_list)]
            try:
                return fn(html_code)
            except Exception:
                return html_code
        return html_code

    @staticmethod
    def respond(message: str, html_code: str, history: list) -> Tuple[str, str, list]:
        import random
        msg = message.lower().strip()

        if not html_code.strip():
            reply = "⚠️ Please **generate a page first**, then I can modify it for you!"
            history.append((message, reply))
            return "", html_code, history

        # ── Parse intent ──
        topic = None
        action_map = {
            'font':         ['font','typeface','typography','heading style','serif','sans','mono'],
            'button':       ['button','btn','sharp','rounded button','pill','cta'],
            'card':         ['card','glass','glassmorphism','frosted','box shadow','feature card'],
            'hero':         ['hero','full screen','fullscreen','bigger hero','tall','banner height'],
            'spacing':      ['spacing','padding','margin','gap','whitespace','breathing room','wider'],
            'animation':    ['animation','slow','faster','speed','springy','bounce','transition'],
            'color_primary':['red','green','orange','different color','change color','color scheme','primary color'],
            'border':       ['sharp corners','square','no border radius','round','pill shape','corner'],
        }
        for t, kws in action_map.items():
            if any(kw in msg for kw in kws):
                topic = t
                break

        if topic:
            variant = random.randint(0, 2)
            new_html = StyleChatbot.apply_modification(html_code, topic, variant)

            changed = new_html != html_code
            if changed:
                reply = f"✅ **Done!** I've applied a **{topic.replace('_',' ')} update** to your page.\n\n👁️ Switch to the **Live Preview** tab and click **Load Preview** to see the change!\n\n💡 Not quite right? Send another message to try a different variation."
            else:
                reply = f"ℹ️ The **{topic.replace('_',' ')}** style was already at that setting or couldn't be auto-applied to this specific page type.\n\n💡 Try: re-generate your page first, then request the change again."
            html_code = new_html
        elif any(w in msg for w in ['undo','revert','original','reset']):
            reply = "↩️ To reset, go to the **Generate Page** tab and click **✨ Generate HTML Page** again — this will restore the original page."
        elif any(w in msg for w in ['help','what can','options','list']):
            reply = """🤖 **I can directly modify your HTML — just ask!**

| Say this... | What changes |
|---|---|
| *"make font more elegant"* | Adds serif font to headings |
| *"make buttons sharp"* | Removes pill border-radius |
| *"add glass effect"* | Glassmorphism on feature cards |
| *"make hero full screen"* | Sets hero to 100vh height |
| *"add more spacing"* | Increases section padding |
| *"slow down animations"* | Reduces animation speed |
| *"change primary color to red"* | Updates --primary CSS variable |
| *"make corners round"* | Increases border-radius to 32px |

Changes apply **instantly** to the code — then preview in the Live Preview tab!"""
        elif any(w in msg for w in ['hello','hi','hey']):
            reply = "👋 Hi! I can **directly modify** your generated HTML. Try: *\"make the hero full screen\"* or *\"add a glass effect to cards\"*."
        else:
            reply = f"""🤔 I didn't catch a specific change for *"{message}"*.

Try one of these:
- *"make the hero full screen"*
- *"add glass effect to cards"*  
- *"make buttons sharp / rounded"*
- *"change primary color to red / green / orange"*
- *"add more whitespace"*
- *"slow down animations"*

Or type **help** to see everything I can do!"""

        history.append((message, reply))
        return "", html_code, history


# ============================================================================
# WRAPPER FUNCTIONS
# ============================================================================

generation_history = []

def generate_html_page(title, description, style, theme, animated, use_images, img_kw):
    if not title.strip() or not description.strip():
        return "", "❌ Please provide both title and description!", ""
    try:
        html_output, palette = HTMLGenerationEngine.generate_page(title, description, style, theme, animated, use_images, img_kw)
        color_info = (f"**{style} / {theme}** {'🎬' if animated else '🚫'} {'🖼️ Images ON' if use_images else '📐 No Images'} · "
                      f"Primary: `{palette['primary']}` · Accent: `{palette['accent']}`")
        generation_history.append({'title':title,'html':html_output,'timestamp':datetime.now().isoformat()})
        return html_output, "✅ Page generated! Head to Live Preview to see it.", color_info
    except Exception as e:
        return "", f"❌ Error: {str(e)}", ""

def show_preview(html_text):
    if not html_text.strip():
        return "<p style='text-align:center;padding:80px;color:#888;'>Generate a page first, then click Load Preview.</p>"
    return html_text

def explain_code(html_code):
    return CodeExplainer.explain(html_code)

def get_color_suggestions(style, theme):
    palette = ColorPaletteGenerator.generate_palette(style, theme)
    return ("**Palette — `" + style + "` · `" + theme + "`**\n\n| Token | Value |\n|---|---|\n"
            + '\n'.join([f"| {k.replace('_',' ').title()} | `{v}` |" for k,v in palette.items()]))

def chatbot_respond(message, html_code, history):
    msg_out, html_out, hist_out = StyleChatbot.respond(message, html_code, history)
    return msg_out, html_out, hist_out

# ── Template generators (auto-generate on click) ──
def load_midnight_gold():
    html = ElegantTemplates.midnight_gold("Aurum Studio")
    return html, "✅ Midnight Gold template loaded! Click 👁️ Live Preview to see it.", "**Template: Midnight Gold** — Luxury dark theme · Gold accents · Playfair Display serif · Full portfolio"

def load_nordic_frost():
    html = ElegantTemplates.nordic_frost("Nordic Design Co.")
    return html, "✅ Nordic Frost template loaded! Click 👁️ Live Preview to see it.", "**Template: Nordic Frost** — Clean Scandinavian light theme · DM Serif · Stats strip · Pricing"

def load_emerald_tech():
    html = ElegantTemplates.emerald_tech("LaunchPad")
    return html, "✅ Emerald Tech template loaded! Click 👁️ Live Preview to see it.", "**Template: Emerald Tech** — Dark SaaS · Green accents · Space Grotesk · Grid background"

def load_rose_editorial():
    html = ElegantTemplates.rose_editorial("The Edit Studio")
    return html, "✅ Rose Editorial template loaded! Click 👁️ Live Preview to see it.", "**Template: Rose Editorial** — Magazine layout · Cormorant Garamond · Split hero · Masonry portfolio"

def load_charcoal_restaurant():
    html = ElegantTemplates.charcoal_restaurant("Ember & Oak")
    return html, "✅ Restaurant template loaded! Click 👁️ Live Preview to see it.", "**Template: Charcoal Restaurant** — Dark food theme · Libre Baskerville · Menu cards · Reservation form"


# ============================================================================
# GRADIO UI
# ============================================================================

print("🚀 Loading HTML Quick-Styler v3.1 ...")
css_theme = gr.themes.Soft(primary_hue="violet", secondary_hue="blue")

with gr.Blocks(theme=css_theme, title="HTML Quick-Styler v3.1") as demo:

    gr.Markdown("""
    # 🎨 HTML Quick-Styler v3.1
    ### Generate · Preview · Explain · Modify — Professional HTML Pages in Seconds
    """)

    with gr.Tabs():

        # ══ TAB 1: GENERATE ══
        with gr.TabItem("🎯 Generate Page"):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### 📝 Page Settings")
                    page_title = gr.Textbox(label="Page Title", value="Modern Portfolio Website")
                    page_description = gr.Textbox(
                        label="Describe your page (use keywords like: hero, features, about, portfolio, pricing, contact, footer)",
                        value="Hero section, features, portfolio gallery, testimonials, pricing plans, contact form, footer",
                        lines=4
                    )
                    with gr.Row():
                        color_style = gr.Dropdown(
                            ["modern","vibrant","ocean","forest","sunset","luxury","creative","minimal"],
                            value="modern", label="🎨 Color Style"
                        )
                        theme_choice = gr.Radio(["dark","light"], value="dark", label="🌙 Theme")
                    with gr.Row():
                        animated_toggle = gr.Checkbox(value=True,  label="🎬 Animations")
                        use_images      = gr.Checkbox(value=False, label="🖼️ Unsplash Images")
                    image_keywords = gr.Textbox(label="📷 Image Keywords", placeholder="e.g. technology, office", value="")
                    generate_btn = gr.Button("✨ Generate HTML Page", variant="primary", size="lg")

                with gr.Column(scale=1):
                    gr.Markdown("### 📄 Generated Code")
                    html_output = gr.Code(language="html", label="Generated HTML/CSS", lines=24)
                    status_msg  = gr.Markdown()
                    color_info  = gr.Markdown()

            generate_btn.click(
                generate_html_page,
                inputs=[page_title, page_description, color_style, theme_choice, animated_toggle, use_images, image_keywords],
                outputs=[html_output, status_msg, color_info]
            )

        # ══ TAB 2: LIVE PREVIEW ══
        with gr.TabItem("👁️ Live Preview"):
            gr.Markdown("### 🔍 Live Preview — click to render your page")
            preview_btn    = gr.Button("🔄 Load Preview", variant="primary", size="lg")
            preview_output = gr.HTML(value="<p style='text-align:center;padding:80px;color:#888;'>Generate or load a template, then click Load Preview.</p>")
            preview_btn.click(show_preview, inputs=[html_output], outputs=[preview_output])

        # ══ TAB 3: EXPLAIN ══
        with gr.TabItem("📖 Explain My Code"):
            gr.Markdown("### 📖 Plain-English Code Explanation")
            explain_btn     = gr.Button("📖 Explain My Code", variant="primary", size="lg")
            explanation_out = gr.Markdown("_Generate a page first, then click Explain._")
            explain_btn.click(explain_code, inputs=[html_output], outputs=[explanation_out])

        # ══ TAB 4: STYLE CHATBOT ══
        with gr.TabItem("🤖 Improve My Style"):
            gr.Markdown("""### 🤖 Style Assistant — Modifies Your HTML Directly
Type what you want to change and I'll update the code instantly.

**Examples:** `make hero full screen` · `add glass effect` · `sharp buttons` · `change color to red` · `more spacing`
""")
            chatbot = gr.Chatbot(height=380, label="Style Assistant")
            with gr.Row():
                chat_input = gr.Textbox(
                    placeholder="e.g. make hero full screen, sharp buttons, glass cards, change color to red...",
                    label="Your request", scale=4, lines=1
                )
                send_btn = gr.Button("Apply ✨", variant="primary", scale=1)

            gr.Markdown("💡 _After applying a change, go to **Live Preview** → **Load Preview** to see the result._")

            send_btn.click(chatbot_respond, inputs=[chat_input, html_output, chatbot], outputs=[chat_input, html_output, chatbot])
            chat_input.submit(chatbot_respond, inputs=[chat_input, html_output, chatbot], outputs=[chat_input, html_output, chatbot])

        # ══ TAB 5: ELEGANT TEMPLATES ══
        with gr.TabItem("✨ Elegant Templates"):
            gr.Markdown("""### ✨ Premium Templates — Click to Load Instantly
Each template has its own unique typography, color palette, and layout. After clicking, go to **👁️ Live Preview** to see it rendered.
""")
            with gr.Row():
                with gr.Column():
                    gr.Markdown("""#### 🥇 Midnight Gold
**Dark luxury** studio site
- Gold + black palette
- Playfair Display serif
- Full portfolio grid
- Underline-hover nav""")
                    midnight_btn = gr.Button("Load Midnight Gold →", variant="primary")

                with gr.Column():
                    gr.Markdown("""#### ❄️ Nordic Frost
**Scandinavian** light theme
- Clean whites + blue
- DM Serif Display
- Stats strip
- 3-tier pricing""")
                    nordic_btn = gr.Button("Load Nordic Frost →", variant="primary")

                with gr.Column():
                    gr.Markdown("""#### 💚 Emerald Tech
**SaaS / startup** dark
- Grid background
- Space Grotesk mono
- Animated glow CTA
- Feature cards w/ hover line""")
                    emerald_btn = gr.Button("Load Emerald Tech →", variant="primary")

            with gr.Row():
                with gr.Column():
                    gr.Markdown("""#### 🌹 Rose Editorial
**Magazine / portfolio** light
- Split editorial hero
- Cormorant Garamond
- Masonry portfolio
- Dark testimonials block""")
                    rose_btn = gr.Button("Load Rose Editorial →", variant="primary")

                with gr.Column():
                    gr.Markdown("""#### 🔥 Charcoal Restaurant
**Restaurant / hospitality** dark
- Fixed-background hero
- Libre Baskerville serif
- Menu cards w/ photos
- Reservation form""")
                    charcoal_btn = gr.Button("Load Charcoal Restaurant →", variant="primary")

                with gr.Column():
                    gr.Markdown("*(More templates coming soon)*")

            gr.Markdown("---\n✅ After loading a template, go to **👁️ Live Preview** → click **Load Preview** to see it rendered.")

            template_out = [html_output, status_msg, color_info]
            midnight_btn.click(load_midnight_gold,       outputs=template_out)
            nordic_btn.click(load_nordic_frost,          outputs=template_out)
            emerald_btn.click(load_emerald_tech,         outputs=template_out)
            rose_btn.click(load_rose_editorial,          outputs=template_out)
            charcoal_btn.click(load_charcoal_restaurant, outputs=template_out)

        # ══ TAB 6: COLOR PALETTES ══
        with gr.TabItem("🎨 Color Palettes"):
            gr.Markdown("### 🌈 Explore Palettes")
            with gr.Row():
                style_sel = gr.Radio(["modern","vibrant","ocean","forest","sunset","luxury","creative","minimal"], value="modern", label="Style")
                theme_sel = gr.Radio(["dark","light"], value="dark", label="Theme")
            palette_btn     = gr.Button("Show Palette", variant="primary")
            palette_display = gr.Markdown()
            palette_btn.click(get_color_suggestions, inputs=[style_sel, theme_sel], outputs=[palette_display])

        # ══ TAB 7: GUIDE ══
        with gr.TabItem("📚 Guide"):
            gr.Markdown("""
# 📖 HTML Quick-Styler v3.1 Guide

## 🆕 What's New
| | Change |
|---|---|
| ✨ | 5 completely redesigned elegant templates |
| 🤖 | Style chatbot now **actually modifies** your HTML code |
| ⚡ | Templates load instantly — no extra generate step |
| 🎨 | Each template has unique fonts, layout, and color personality |

## Templates at a Glance
| Template | Style | Font | Best For |
|---|---|---|---|
| Midnight Gold | Dark · Gold | Playfair Display | Luxury / Studio |
| Nordic Frost | Light · Blue | DM Serif Display | Agency / SaaS |
| Emerald Tech | Dark · Green | Space Grotesk | Startup / SaaS |
| Rose Editorial | Light · Rose | Cormorant Garamond | Magazine / Portfolio |
| Charcoal Restaurant | Dark · Amber | Libre Baskerville | Food / Hospitality |

## Style Chatbot Commands
| Command | What it does |
|---|---|
| `make hero full screen` | Sets hero to 100vh |
| `add glass effect` | Glassmorphism on cards |
| `sharp buttons` | Removes pill border-radius |
| `round buttons` | 32px border-radius |
| `elegant font` | Adds Georgia serif to headings |
| `change color to red/green/orange` | Updates primary CSS variable |
| `more spacing` | Increases section padding |
| `slow animations` | Slows animation speed |
| `wider layout` | Increases max-width to 1400px |

## Custom Page Generation
Mention these keywords in your description:
`hero` · `features` · `about` · `portfolio` · `testimonials` · `pricing` · `contact` · `footer`
""")

print("\n✅ HTML Quick-Styler v3.1 Ready!\n")
demo.launch(share=True, show_error=True, show_api=False)