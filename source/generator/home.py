from common import *

C1 = cite("Centers for Disease Control and Prevention [CDC], 2024a")
C = cite("CDC, 2024a")
C25a = cite("CDC, 2025a")

hero_art = f'''<svg class="hero-art" width="300" height="300" viewBox="0 0 300 300" role="img" aria-label="Illustration of a teal shield with a check mark blocking virus particles" style="flex: 0 0 auto">
<circle cx="150" cy="150" r="138" fill="#0F766E" opacity="0.35"/>
<circle cx="150" cy="150" r="104" fill="#0F766E" opacity="0.5"/>
<path d="M150 64 L218 90 V150 C218 196 186 226 150 242 C114 226 82 196 82 150 V90 Z" fill="#FFFFFF"/>
<path d="M122 152 L142 172 L182 130" fill="none" stroke="#0F766E" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
<g fill="none" stroke="#FDBA74" stroke-width="4" stroke-linecap="round">
<circle cx="52" cy="70" r="14"/><path d="M52 48v8M52 84v8M30 70h8M66 70h8M37 55l5 5M62 80l5 5M37 85l5-5M62 60l5-5"/>
<circle cx="256" cy="232" r="12"/><path d="M256 213v7M256 244v7M237 232h7M268 232h7M243 219l4 4M265 241l4 4M243 245l4-4M265 223l4-4"/>
<circle cx="258" cy="66" r="8"/><circle cx="44" cy="238" r="9"/>
</g>
</svg>'''

hero = f'''<section style="background: {TEAL_DK}; color: #FFFFFF">
<div style="max-width: 1160px; margin: 0 auto; padding: 72px 24px; display: flex; align-items: center; justify-content: space-between; gap: 40px; flex-wrap: wrap">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 20px">
<p style="margin: 0; font-size: 15px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #FDBA74">For college students in Hamilton County, ages 18–26</p>
<h1 class="hero-h1" style="margin: 0; font-size: 60px; line-height: 1.05; font-weight: 800">HPV is common. <span style="color: #99F6E4">Cervical cancer is preventable.</span></h1>
<p style="margin: 0; font-size: 21px; max-width: 620px; color: #E6F4F1">A quick, judgment-free guide for college students. Learn what HPV is, what raises your risk, and the simple steps that protect you, whatever your gender.</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 8px">
<a class="btn" href="Prevention.dc.html" style="display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 10px 22px; border-radius: 999px; font-weight: 700; font-size: 17px; text-decoration: none; background: #FDBA74; color: #431407">See how to protect yourself{icon("arrowright", 18, "#431407")}</a>
<a class="btn" href="Quiz.dc.html" style="display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 10px 22px; border-radius: 999px; font-weight: 700; font-size: 17px; text-decoration: none; background: transparent; color: #FFFFFF; border: 2px solid #FFFFFF">Take the quiz</a>
</div>
</div>
{hero_art}
</div>
</section>'''

purpose = f'''<section aria-labelledby="purpose-title" style="margin-top: 56px; background: {TEAL_BG}; border: 1px solid {LINE}; border-radius: 20px; padding: 32px; display: flex; gap: 20px; align-items: flex-start; flex-wrap: wrap">
{tile("target", "#FFFFFF", TEAL, 52, 26)}
<div style="flex: 1 1 320px; min-width: 0">
<h2 id="purpose-title" style="margin: 0 0 8px; font-size: 26px; font-weight: 800; color: {TEAL_DK}">Why This Site Exists</h2>
<p style="margin: 0; font-size: 19px">The purpose of this website is to educate college students in Hamilton County about HPV and cervical cancer prevention. It explains risk factors, prevention methods, and local resources to help students make informed healthcare decisions.</p>
</div>
</section>'''

objs = [
    ("1", "alert", "Identify <strong>three risk factors</strong> for HPV and cervical cancer.", "RiskFactors.dc.html", "Go to Risk Factors"),
    ("2", "shieldcheck", "Identify <strong>two prevention methods</strong>, including HPV vaccination and cervical cancer screening.", "Prevention.dc.html", "Go to Prevention"),
    ("3", "pin", "Identify <strong>one local or state resource</strong> for prevention care.", "Resources.dc.html", "Go to Local Resources"),
]
obj_cards = []
for n, ic, txt, href, lab in objs:
    obj_cards.append(card(f'''<div style="display: flex; align-items: center; justify-content: space-between">{tile(ic)}<span style="font-size: 44px; font-weight: 800; color: {TEAL_LT}; line-height: 1" aria-hidden="true">0{n}</span></div>
<p style="margin: 0; font-size: 19px">{txt}</p>
<a href="{href}" style="font-weight: 700; display: inline-flex; align-items: center; gap: 6px; min-height: 44px">{lab}{icon("arrowright", 16, TEAL)}</a>'''))

learn = h2("What You’ll Learn", "book", sub="After visiting this site, students will be able to:") + grid(obj_cards, 280)

facts = [
    ("virus", "Very common", f"<strong>HPV (human papillomavirus) is a very common virus</strong>. A virus is a tiny germ that can make you sick. Nearly everyone who is not vaccinated will get HPV at some point in their lives {C1}."),
    ("users", "How it spreads", f"It spreads through <strong>intimate skin-to-skin contact</strong>, including vaginal, anal, or oral sex, even when the person has <strong>no signs or symptoms</strong> {C}."),
    ("clock", "Most clear up", f"About <strong>9 out of 10 HPV infections go away on their own</strong> within 2 years {C}."),
    ("alert", "Some cause cancer", f"Infections that last longer can cause cancers of the <strong>cervix</strong> (the lower part of the uterus, or womb, that opens into the vagina), vagina, vulva (the outer genital area), penis, anus, and back of the throat {C}."),
    ("calendar", "Cancer is slow", f"Cancer usually takes <strong>years, even decades</strong>, to develop after a person gets HPV {C25a}."),
]
fact_cards = [card(f'<div style="display: flex; gap: 14px; align-items: center">{tile(ic)}<h3 style="margin: 0; font-size: 21px; font-weight: 800; color: {TEAL_DK}">{t}</h3></div><p style="margin: 0">{tx}</p>') for ic, t, tx in facts]
what = h2("What Is HPV?", "virus", sub="The basics, in plain language.") + grid(fact_cards, 300)

# Infographic
steps = [
    ("1", "HPV infection", "The virus passes through skin-to-skin contact.", "#E6F4F1", "#99D5CB", ("HPV vaccine", TEAL, "#FFFFFF", "syringe", "Stop it here")),
    ("2", "Most go away on their own", "The body clears most infections.", "#E6F4F1", "#99D5CB", None),
    ("3", "Some high-risk infections last for years", "High-risk HPV types are the ones that can lead to cancer.", "#FFF4EA", "#F3C9A8", None),
    ("4", "Abnormal cells on the cervix (precancer)", "Cells change but are not cancer yet. Precancer can be treated.", "#FFEDD5", "#F3C9A8", ("Screening + follow-up", WARM, "#FFFFFF", "search", "Catch it here")),
    ("5", "Cancer if not found and treated", "Precancer can turn into cancer over time.", "#FED7AA", "#EA9A63", None),
]
chain = []
for i, (n, t, d, bg, bd, badge) in enumerate(steps):
    if badge:
        lab, bbg, bfg, bic, pre = badge
        b = f'<div style="display: flex; flex-direction: column; align-items: center; gap: 4px; min-height: 76px; justify-content: flex-end"><span style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: {TEAL_TX if bbg == TEAL else WARM_TX}">{pre}</span><span style="display: inline-flex; align-items: center; gap: 6px; background: {bbg}; color: {bfg}; font-weight: 800; font-size: 15px; padding: 6px 12px; border-radius: 999px; white-space: nowrap">{icon(bic, 16, bfg)}{lab}</span><svg width="14" height="10" viewBox="0 0 14 10" aria-hidden="true"><path d="M0 0h14L7 10z" fill="{bbg}"/></svg></div>'
    else:
        b = '<div style="min-height: 76px" aria-hidden="true"></div>'
    chain.append(f'''<li style="flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; gap: 6px; list-style: none">{b}
<div style="flex: 1 1 auto; background: {bg}; border: 2px solid {bd}; border-radius: 16px; padding: 18px; display: flex; flex-direction: column; gap: 8px">
<span style="width: 32px; height: 32px; border-radius: 999px; background: #FFFFFF; border: 2px solid {bd}; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 15px; color: {TEAL_DK}" aria-hidden="true">{n}</span>
<h3 style="margin: 0; font-size: 18px; line-height: 1.3; font-weight: 800; color: {INK}">{t}</h3>
<p style="margin: 0; font-size: 15px; line-height: 1.5; color: #374151">{d}</p>
</div></li>''')
    if i < len(steps) - 1:
        chain.append(f'<li aria-hidden="true" style="list-style: none; display: flex; align-items: center; justify-content: center; padding-top: 76px"><span class="chev" style="display: flex">{icon("chevron", 26, TEAL, 3)}</span></li>')

infographic = h2("From HPV to Cancer and How to Stop It", "activity", sub="Cervical cancer grows slowly, in steps. That gives you two chances to stop it.") + f'''<figure style="margin: 0; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 24px; padding: 28px">
<ol class="chain" aria-label="Five steps from HPV infection to cancer" style="margin: 0; padding: 0; display: flex; gap: 8px; align-items: stretch">
{"".join(chain)}
</ol>
<figcaption style="margin-top: 20px; padding-top: 16px; border-top: 1px solid {LINE}; font-size: 16px; color: #374151"><strong>Two places to stop it:</strong> the <strong>HPV vaccine</strong> works before an infection starts, and <strong>screening plus follow-up</strong> finds precancer so it can be treated. Most HPV infections go away on their own, and cancer usually takes years to develop {cite("CDC, 2024a, 2025a")}.</figcaption>
</figure>'''

explore_items = [
    ("Numbers.dc.html", "chart", "The Numbers", "How common HPV and cervical cancer are, from the world to Hamilton County."),
    ("RiskFactors.dc.html", "alert", "Risk Factors", "What raises your risk, plus myths and facts."),
    ("Prevention.dc.html", "shieldcheck", "Prevention", "Your checklist: vaccine, screening, and more."),
    ("Resources.dc.html", "pin", "Local Resources", "Where to get care in Cincinnati and Ohio."),
    ("Quiz.dc.html", "help", "Quick Quiz", "Five questions to test what you learned."),
    ("References.dc.html", "book", "References", "Every source used on this site."),
]
ex = [f'''<a href="{h}" style="text-decoration: none; color: {INK}; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 18px; padding: 22px; display: flex; gap: 14px; align-items: flex-start; min-height: 44px">{tile(ic, TEAL_LT, TEAL, 44, 22)}<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-weight: 800; font-size: 19px; color: {TEAL_DK}">{t}</span><span style="font-size: 16px; color: #374151">{d}</span></span></a>''' for h, ic, t, d in explore_items]
explore = h2("Explore the Site", "globe") + grid(ex, 300, 16)

tk = takeaway(f'<p style="margin: 0">HPV is very common, and <strong>about 9 out of 10 infections go away on their own</strong> {C}. Cervical cancer takes years to develop, so you have time to act {C25a}. Your two main tools are the <strong>HPV vaccine</strong> and <strong>regular screening</strong>.</p>')

body = hero + wrap(purpose + learn + what + infographic + explore + tk)
emit("Main.dc.html", page("Home: HPV and Cervical Cancer Prevention", "Main.dc.html", body, 3300))
emit_static("Main.dc.html", "Home: HPV and Cervical Cancer Prevention", body)
