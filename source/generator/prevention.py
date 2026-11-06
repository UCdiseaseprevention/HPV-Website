from common import *

intro = '<p style="margin: 0"><strong>Prevention</strong> means stopping a disease before it starts, or finding it early when it is easier to treat. These seven steps work best together. Start with the checklist, then read the details for each step.</p>'

checks = [
    ("vaccine", "syringe", "Get the HPV vaccine", True),
    ("screening", "search", "Get screened on schedule", True),
    ("followup", "clipboard", "Follow up on abnormal results", False),
    ("condoms", "shield", "Use condoms", False),
    ("partners", "rings", "Limit the number of sexual partners", False),
    ("smoke", "nosmoke", "Don’t smoke, and avoid secondhand smoke", False),
    ("help", "dollar", "Use free or low-cost help", False),
]
items = []
for i, (id_, ic, label, top) in enumerate(checks, 1):
    star = f'<span style="font-size: 12px; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase; color: {WARM_TX}; background: {WARM_LT}; border-radius: 999px; padding: 2px 10px">Top step</span>' if top else ""
    items.append(f'''<li style="list-style: none"><a href="#{id_}" style="text-decoration: none; color: {INK}; background: #FFFFFF; border: 2px solid {TEAL if top else LINE}; border-radius: 16px; padding: 16px; display: flex; gap: 14px; align-items: center; min-height: 72px">
<span style="flex: 0 0 auto; width: 30px; height: 30px; border-radius: 8px; border: 2px solid {TEAL}; background: {TEAL if top else "#FFFFFF"}; display: flex; align-items: center; justify-content: center">{icon("check", 18, "#FFFFFF" if top else TEAL, 3)}</span>
<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-weight: 800; font-size: 18px; line-height: 1.3">{i}. {label}</span>{star}</span>
<span style="margin-left: auto; flex: 0 0 auto">{icon(ic, 22, TEAL)}</span></a></li>''')
checklist = f'''<section aria-labelledby="check-title" style="margin-top: 48px; background: {TEAL_BG}; border: 1px solid {LINE}; border-radius: 24px; padding: 32px">
<div style="display: flex; gap: 14px; align-items: center; margin-bottom: 20px">{tile("clipboard", "#FFFFFF")}<div><h2 id="check-title" style="margin: 0; font-size: 30px; font-weight: 800; color: {TEAL_DK}">Your Prevention Checklist</h2><p style="margin: 0; color: #374151">Select a step to jump to its details.</p></div></div>
<ul style="margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px">{"".join(items)}</ul>
</section>'''


def step_head(n, ic, title, id_):
    return f'<div style="display: flex; gap: 14px; align-items: center">{tile(ic, TEAL, "#FFFFFF", 56, 28)}<div><p style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: {TEAL_TX}">Step {n}</p><h2 id="{id_}" style="margin: 0; font-size: 28px; line-height: 1.2; font-weight: 800; color: {TEAL_DK}">{title}</h2></div></div>'


CDC1 = cite("Centers for Disease Control and Prevention [CDC], 2024c")
B = cite("CDC, 2024b")
S = cite("CDC, 2025b")

vaccine = card(f'''{step_head(1, "syringe", "Get the HPV vaccine", "vaccine")}
<p style="margin: 0">A <strong>vaccine</strong> is a shot that teaches your body to fight a germ. The HPV vaccine is <strong>recommended for everyone through age 26</strong> who is not already vaccinated {CDC1}.</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px">
<div style="background: {TEAL_BG}; border-radius: 16px; padding: 20px"><p style="margin: 0; font-size: 15px; font-weight: 700; color: {TEAL_TX}">Started before age 15</p><p style="margin: 2px 0 8px; font-size: 36px; font-weight: 800; color: {TEAL}; line-height: 1.1">2 doses</p><p style="margin: 0; font-size: 17px">If started before age 15, 2 doses are needed, given 6 to 12 months apart {B}.</p></div>
<div style="background: {TEAL_BG}; border: 2px solid {TEAL}; border-radius: 16px; padding: 20px"><p style="margin: 0; font-size: 15px; font-weight: 700; color: {TEAL_TX}">Started at age 15 or older (includes anyone starting in college)</p><p style="margin: 2px 0 8px; font-size: 36px; font-weight: 800; color: {TEAL}; line-height: 1.1">3 doses</p><p style="margin: 0; font-size: 17px">If started at age 15 or older, 3 doses are given over 6 months {B}.</p></div>
<div style="background: {WARM_LT}; border-radius: 16px; padding: 20px"><p style="margin: 0; font-size: 15px; font-weight: 700; color: {WARM_TX}">How well it works</p><p style="margin: 2px 0 8px; font-size: 36px; font-weight: 800; color: {WARM}; line-height: 1.1">Over 90%</p><p style="margin: 0; font-size: 17px">HPV vaccination can prevent <strong>over 90% of cancers caused by HPV</strong> {cite("CDC, 2025a")}.</p></div>
</div>
<p style="margin: 0">A <strong>dose</strong> is one shot. Adults 27–45 can talk with a doctor about whether it’s right for them {B}.</p>''')

screening = card(f'''{step_head(2, "search", "Get screened on schedule", "screening")}
<p style="margin: 0"><strong>Screening</strong> means testing for a problem early, before you have symptoms. It is for <strong>anyone with a cervix</strong> {S}.</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px">
<div style="border: 2px solid {TEAL}; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column"><p style="margin: 0; background: {TEAL}; color: #FFFFFF; font-weight: 800; font-size: 20px; padding: 12px 20px">Ages 21–29</p><div style="padding: 20px"><p style="margin: 0"><strong>Pap test every 3 years</strong> if results are normal {S}.</p></div></div>
<div style="border: 2px solid {TEAL_DK}; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column"><p style="margin: 0; background: {TEAL_DK}; color: #FFFFFF; font-weight: 800; font-size: 20px; padding: 12px 20px">Ages 30–65</p><div style="padding: 20px"><p style="margin: 0 0 8px">Talk to your doctor about <strong>one of three options</strong> {S}:</p><ul style="margin: 0; padding-left: 22px; display: flex; flex-direction: column; gap: 4px"><li>An HPV test alone every 5 years</li><li>An HPV test plus a Pap test (co-testing) every 5 years</li><li>A Pap test alone every 3 years</li></ul></div></div>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px">
<div style="background: {TEAL_BG}; border-radius: 16px; padding: 18px; display: flex; gap: 12px; align-items: flex-start">{icon("search", 24, TEAL)}<p style="margin: 0; font-size: 17px">The <strong>Pap test</strong> looks for cell changes on the cervix (the lower part of the uterus, or womb) {S}.</p></div>
<div style="background: {TEAL_BG}; border-radius: 16px; padding: 18px; display: flex; gap: 12px; align-items: flex-start">{icon("virus", 24, TEAL)}<p style="margin: 0; font-size: 17px">The <strong>HPV test</strong> looks for the virus that can cause those changes {S}.</p></div>
</div>''')

flow = []
fs = [("search", "Get tested"), ("clock", "Wait for results (up to three weeks)"), ("clipboard", "Not normal? Follow up right away")]
for i, (ic, t) in enumerate(fs):
    flow.append(f'<li style="list-style: none; flex: 1 1 0; min-width: 0; background: {WARM_LT if i == 2 else TEAL_BG}; border-radius: 14px; padding: 16px; display: flex; gap: 10px; align-items: center">{icon(ic, 22, WARM if i == 2 else TEAL)}<span style="font-weight: 700; font-size: 17px">{t}</span></li>')
    if i < 2:
        flow.append(f'<li aria-hidden="true" style="list-style: none; display: flex; align-items: center; justify-content: center"><span class="chev" style="display: flex">{icon("chevron", 22, TEAL, 3)}</span></li>')
followup = card(f'''{step_head(3, "clipboard", "Follow up on abnormal results", "followup")}
<ol class="chain" aria-label="Three steps after a screening test" style="margin: 0; padding: 0; display: flex; gap: 8px; align-items: stretch">{"".join(flow)}</ol>
<p style="margin: 0">Results can take <strong>up to three weeks</strong> {S}. If cells are not normal, <strong>follow up with your doctor right away</strong>, because treatment in most cases prevents cervical cancer from developing {S}.</p>''')

NCI1 = cite("National Cancer Institute [NCI], 2024")
small = grid([
    card(f'{step_head(4, "shield", "Use condoms", "condoms")}<p style="margin: 0">Condoms can <strong>lower the risk</strong> of passing HPV but <strong>do not completely prevent it</strong>, because HPV can infect areas the condom doesn’t cover {NCI1}.</p>'),
    card(f'{step_head(5, "rings", "Limit the number of sexual partners", "partners")}<p style="margin: 0">Having <strong>multiple partners</strong> raises the chance of getting a high-risk HPV type, which is a type that can lead to cancer {cite("NCI, 2024")}.</p>'),
    card(f'{step_head(6, "nosmoke", "Don’t smoke, and avoid secondhand smoke", "smoke")}<p style="margin: 0"><strong>Don’t smoke</strong>, and avoid <strong>secondhand smoke</strong>, which is smoke from someone else’s cigarette {cite("CDC, 2024c; NCI, 2024")}.</p>'),
], 300)

helpcard = f'''<article style="background: {WARM_LT}; border: 2px solid {WARM_LINE}; border-radius: 20px; padding: 28px; display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; gap: 14px; align-items: center">{tile("dollar", WARM, "#FFFFFF", 56, 28)}<div><p style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: {WARM_TX}">Step 7</p><h2 id="help" style="margin: 0; font-size: 28px; line-height: 1.2; font-weight: 800; color: {WARM_TX}">Use free or low-cost help</h2></div></div>
<p style="margin: 0">Ohio’s <strong>Breast and Cervical Cancer Project</strong> offers <strong>no-cost cervical cancer screening</strong> to people who qualify {cite("Ohio Department of Health, n.d.")}.</p>
<div>{btn("Resources.dc.html", "Find local resources", True, icon_name="arrowright")}</div>
</article>'''

tk = takeaway(f'<p style="margin: 0">If you’re 26 or younger and not fully vaccinated, <strong>ask about the HPV vaccine</strong> {cite("CDC, 2024c")}. Starting at age 21, <strong>get screened on schedule</strong> and <strong>follow up on any abnormal result</strong> {S}.</p>')

sp = '<div style="height: 24px"></div>'
body = page_header("Prevention and Control", "How to Protect Yourself", intro, "shieldcheck") + wrap(checklist + '<div style="height: 48px"></div>' + vaccine + sp + screening + sp + followup + sp + small + sp + helpcard + tk)
emit("Prevention.dc.html", page("Prevention: HPV and Cervical Cancer", "Prevention.dc.html", body, 4000))
emit_static("Prevention.dc.html", "Prevention: HPV and Cervical Cancer", body)
