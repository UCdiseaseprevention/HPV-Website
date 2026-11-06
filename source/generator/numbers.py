from common import *


def stat(label, big, text, color=TEAL):
    return card(f'''<p style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: {TEAL_TX}">{label}</p>
<p style="margin: 0; font-size: 46px; font-weight: 800; line-height: 1.05; color: {color}">{big}</p>
<p style="margin: 0">{text}</p>''', "gap: 10px")


intro = f'''<p style="margin: 0">Numbers help us see how big a health problem is. Here is what the data say about HPV and <strong>cervical cancer</strong>, which is cancer of the cervix (the lower part of the uterus, or womb, that opens into the vagina).</p>'''

explainer = f'''<section aria-labelledby="terms-title" style="margin-top: 48px; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px">
<h2 id="terms-title" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap">Two words to know</h2>
<div style="background: {TEAL_LT}; border-radius: 20px; padding: 26px; display: flex; gap: 16px; align-items: flex-start">{tile("users", "#FFFFFF")}<div><p style="margin: 0; font-size: 22px; font-weight: 800; color: {TEAL_DK}">Prevalence</p><p style="margin: 4px 0 0">Prevalence = <strong>how many people have it right now</strong>.</p></div></div>
<div style="background: {WARM_LT}; border-radius: 20px; padding: 26px; display: flex; gap: 16px; align-items: flex-start">{tile("calendar", "#FFFFFF", WARM)}<div><p style="margin: 0; font-size: 22px; font-weight: 800; color: {WARM_TX}">Incidence</p><p style="margin: 4px 0 0">Incidence = <strong>how many new cases happen in a period of time</strong>.</p></div></div>
</section>'''

WHO1 = cite("World Health Organization [WHO], 2026")
WHO = cite("WHO, 2026")
world = h2("Worldwide", "globe") + grid([
    stat("Rank among cancers in women", "5th", f"Cervical cancer is the <strong>fifth most common cancer in women</strong> worldwide {WHO1}."),
    stat("New cases (incidence)", "604,000", f"About <strong>604,000 new cases</strong> of cervical cancer were estimated in 2024 {WHO}."),
    stat("Deaths", "280,000", f"About <strong>280,000 deaths</strong> from cervical cancer occurred in 2024 {WHO}.", WARM),
], 280)

CDC1 = cite("Centers for Disease Control and Prevention [CDC], 2024a")
CDC = cite("CDC, 2024a")
ACS1 = cite("American Cancer Society [ACS], 2026")
ACS = cite("ACS, 2026")
C25 = cite("CDC, 2025a")

us = h2("United States", "flag") + grid([
    stat("HPV prevalence", "42 million+", f"<strong>Prevalence:</strong> more than <strong>42 million Americans</strong> are infected with types of HPV known to cause disease {CDC1}."),
    stat("HPV incidence", "13 million", f"<strong>HPV incidence:</strong> about <strong>13 million Americans</strong>, including teens, become infected each year {CDC}."),
    stat("Cervical cancer incidence", "13,490", f"<strong>Cervical cancer incidence:</strong> about <strong>13,490 new cases</strong> of invasive cervical cancer (cancer that has grown from the surface of the cervix into deeper tissue) are expected in 2026 {ACS1}."),
    stat("Deaths", "4,200", f"<strong>Deaths:</strong> about <strong>4,200 women</strong> are expected to die from cervical cancer in 2026 {ACS}.", WARM),
    stat("Caused by HPV", "9 in 10+", f"More than <strong>9 out of 10</strong> cervical cancer cases are caused by HPV {C25}. Each year, about <strong>10,800 women</strong> are diagnosed with cervical cancer caused by HPV, and nearly <strong>200,000</strong> are diagnosed with cervical <strong>precancer</strong> (cell changes that could turn into cancer if not treated) {C25}."),
    stat("All HPV cancers", "36,000", f"HPV causes about <strong>36,000 cases of cancer</strong> in men and women each year {CDC}."),
], 300)

bars = f'''<figure style="margin: 24px 0 0; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 20px; padding: 28px">
<h3 style="margin: 0 0 4px; font-size: 22px; font-weight: 800; color: {TEAL_DK}">Prevalence vs. incidence: HPV in the U.S.</h3>
<p style="margin: 0 0 20px; font-size: 16px; color: #374151">Bars are drawn to scale.</p>
<div role="img" aria-label="Bar chart. More than 42 million Americans have disease-causing HPV right now. About 13 million become newly infected each year." style="display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; flex-direction: column; gap: 6px"><div style="display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; font-size: 16px"><span style="font-weight: 700">Have it right now (prevalence)</span><span style="font-weight: 800; color: {TEAL_TX}">42 million+</span></div><div style="height: 28px; background: {TEAL_LT}; border-radius: 8px"><div style="width: 100%; height: 28px; background: {TEAL}; border-radius: 8px"></div></div></div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; font-size: 16px"><span style="font-weight: 700">Newly infected each year (incidence)</span><span style="font-weight: 800; color: {WARM_TX}">13 million</span></div><div style="height: 28px; background: {TEAL_LT}; border-radius: 8px"><div style="width: 31%; height: 28px; background: {WARM}; border-radius: 8px"></div></div></div>
</div>
<figcaption style="margin-top: 16px; font-size: 15px; color: #374151">Source: {cite("CDC, 2024a")}.</figcaption>
</figure>'''

NCICDC = cite("National Cancer Institute &amp; Centers for Disease Control and Prevention, n.d.")
local = h2("Hamilton County, Ohio", "building", sub="Our home county, from 2019 to 2023.") + f'''<div style="background: #FFFFFF; border: 2px solid {TEAL}; border-radius: 24px; padding: 32px; display: flex; flex-direction: column; gap: 24px">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px">
<div style="background: {TEAL_BG}; border-radius: 16px; padding: 20px"><p style="margin: 0; font-size: 44px; font-weight: 800; color: {TEAL}; line-height: 1.1">36</p><p style="margin: 4px 0 0; font-weight: 600">new cases per year, on average</p></div>
<div style="background: {TEAL_BG}; border-radius: 16px; padding: 20px"><p style="margin: 0; font-size: 44px; font-weight: 800; color: {TEAL}; line-height: 1.1">8.3</p><p style="margin: 4px 0 0; font-weight: 600">cases per 100,000 females</p></div>
<div style="background: {TEAL_BG}; border-radius: 16px; padding: 20px"><p style="margin: 0; font-size: 44px; font-weight: 800; color: {TEAL}; line-height: 1.1">Stable</p><p style="margin: 4px 0 0; font-weight: 600">trend over time</p></div>
</div>
<p style="margin: 0">From 2019 to 2023, Hamilton County averaged <strong>36 new cervical cancer cases per year</strong>, a rate of <strong>8.3 cases per 100,000 females</strong>, and the trend was <strong>stable</strong> {NCICDC}.</p>
<p style="margin: 0; font-size: 16px; color: #374151">A <strong>rate</strong> lets us compare places with different numbers of people. A <strong>stable</strong> trend means the rate did not clearly go up or down.</p>
</div>'''

good = f'''<section aria-labelledby="good-title" style="margin-top: 48px; background: {TEAL_DK}; color: #FFFFFF; border-radius: 24px; padding: 32px; display: flex; gap: 24px; align-items: center; flex-wrap: wrap">
<div style="display: flex; align-items: center; gap: 16px">{tile("down", "#FFFFFF", TEAL, 64, 32)}<p style="margin: 0; font-size: 56px; font-weight: 800; line-height: 1; color: #99F6E4">11%</p></div>
<div style="flex: 1 1 380px; min-width: 0">
<h2 id="good-title" style="margin: 0 0 6px; font-size: 26px; font-weight: 800">Good news</h2>
<p style="margin: 0; color: #E6F4F1">Cervical cancer rates have <strong style="color: #FFFFFF">dropped by 11% each year among women ages 20–24</strong>, probably an early sign that HPV vaccination is working <span style="color: #CDEBE5">(ACS, 2026)</span>.</p>
</div>
</section>'''

tk = takeaway(f'<p style="margin: 0">HPV is very common. It causes <strong>more than 9 out of 10 cervical cancer cases</strong> {C25}. The good news: cervical cancer rates are <strong>falling fast among women ages 20–24</strong>, probably an early sign that the vaccine is working {ACS}.</p>')

body = page_header("The Numbers", "How Common Are HPV and Cervical Cancer?", intro, "chart") + wrap(explainer + world + us + bars + local + good + tk)
emit("Numbers.dc.html", page("The Numbers: HPV and Cervical Cancer", "Numbers.dc.html", body, 3500))
emit_static("Numbers.dc.html", "The Numbers: HPV and Cervical Cancer", body)
