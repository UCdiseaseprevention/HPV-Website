from common import *

intro = '<p style="margin: 0">A <strong>risk factor</strong> is anything that raises your chance of getting a disease. Some risk factors you can change. Others you can’t. Knowing them helps you make a plan.</p>'


def tip(html):
    return f'''<div style="margin-top: auto; background: {WARM_LT}; border-radius: 14px; padding: 16px 18px; display: flex; gap: 12px; align-items: flex-start">{icon("bulb", 22, WARM)}<div><p style="margin: 0; font-size: 14px; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase; color: {WARM_TX}">What You Can Do</p><p style="margin: 2px 0 0; font-size: 17px">{html}</p></div></div>'''


def rcard(n, ic, title, body_html, tip_html):
    return card(f'''<div style="display: flex; gap: 14px; align-items: center">{tile(ic)}<div><p style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: {TEAL_TX}">Risk factor {n}</p><h3 style="margin: 0; font-size: 22px; line-height: 1.25; font-weight: 800; color: {TEAL_DK}">{title}</h3></div></div>
{body_html}
{tip(tip_html)}''')


CDC1 = cite("Centers for Disease Control and Prevention [CDC], 2024a")
NCI1 = cite("National Cancer Institute [NCI], 2024")
NCI = cite("NCI, 2024")

c1 = rcard(1, "bulb", "Knowledge gaps",
           f'<p style="margin: 0">HPV can spread <strong>without any signs or symptoms</strong> (changes you can see or feel), so people may not know they have it {CDC1}. Many students also don’t know that <strong>HPV can cause cancer</strong> or that <strong>a vaccine can prevent it</strong>.</p>',
           'Learn the basics on the <a href="Main.dc.html">Home page</a>, then share what you learned with a friend.')
c2 = rcard(2, "heart", "Attitudes and beliefs",
           '<p style="margin: 0">Some people fear vaccine <strong>side effects</strong> (unwanted reactions to a vaccine or medicine). Others feel embarrassed about <strong>screening</strong> (tests that look for problems early, before you feel sick).</p>',
           f'Many people have <strong>no side effects</strong> from the HPV vaccine, and the most common ones are mild, like a sore arm, headache, or feeling tired {cite("CDC, 2024b")}.')
c3 = rcard(3, "chat", "Social environment",
           '<p style="margin: 0">Friends, partners, family, and social media <strong>misinformation</strong> (false information) can discourage vaccination.</p>',
           'Check what you hear against trusted health sources. Start with the Myth vs. Fact box below.')

myths = [
    ("“If I’m over 18, it’s too late.”", f"HPV vaccination is recommended for <strong>everyone through age 26</strong> who is not already vaccinated {cite('CDC, 2024c')}."),
    ("“I’d know if I had HPV.”", f"HPV can spread even when there are <strong>no signs or symptoms</strong> {cite('CDC, 2024a')}."),
    ("“An abnormal Pap test means I have cancer.”", f"An abnormal result <strong>usually does not mean cancer</strong>, and in most cases treatment prevents cervical cancer from developing {cite('CDC, 2025b')}."),
    ("“I got the vaccine, so I don’t need screening.”", f"Vaccinated women should <strong>still get regular cervical cancer screening</strong> starting at age 21 {cite('CDC, 2025a')}."),
]
rows = []
for m, f in myths:
    rows.append(f'''<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px">
<div style="background: #FFFFFF; border: 2px solid {WARM_LINE}; border-radius: 14px; padding: 16px 18px; display: flex; gap: 12px; align-items: flex-start"><span style="flex: 0 0 auto; width: 30px; height: 30px; border-radius: 999px; background: {WARM_LT}; display: flex; align-items: center; justify-content: center">{icon("x", 18, WARM, 3)}</span><p style="margin: 0"><strong style="color: {WARM_TX}">Myth:</strong> {m}</p></div>
<div style="background: #FFFFFF; border: 2px solid #99D5CB; border-radius: 14px; padding: 16px 18px; display: flex; gap: 12px; align-items: flex-start"><span style="flex: 0 0 auto; width: 30px; height: 30px; border-radius: 999px; background: {TEAL_LT}; display: flex; align-items: center; justify-content: center">{icon("check", 18, TEAL, 3)}</span><p style="margin: 0"><strong style="color: {TEAL_TX}">Fact:</strong> {f}</p></div>
</div>''')
mythbox = f'''<section aria-labelledby="myth-title" style="margin: 20px 0; background: {TEAL_BG}; border: 1px solid {LINE}; border-radius: 24px; padding: 28px; display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; gap: 14px; align-items: center; flex-wrap: wrap">{tile("chat", "#FFFFFF")}<div><p style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: {TEAL_TX}">Social environment</p><h3 id="myth-title" style="margin: 0; font-size: 26px; font-weight: 800; color: {TEAL_DK}">Myth vs. Fact</h3></div></div>
<p style="margin: 0; font-size: 16px; color: #374151"><strong>Words to know:</strong> a <strong>Pap test</strong> checks the cervix (the lower part of the uterus, or womb) for cell changes. <strong>Abnormal</strong> means not normal.</p>
{"".join(rows)}
</section>'''

c4 = rcard(4, "rings", "Sexual behavior",
           f'<p style="margin: 0">People who become sexually active at a young age, <strong>especially before 18</strong>, or who have <strong>multiple sexual partners</strong> are more likely to be infected with a high-risk type of HPV, meaning a type that can lead to cancer {NCI1}.</p>',
           'Talk openly with partners, and use the steps on the <a href="Prevention.dc.html">Prevention page</a>, like condoms and the HPV vaccine.')
c5 = rcard(5, "dollar", "Access and cost",
           f'<p style="margin: 0">Transportation, clinic hours, cost, and not knowing where to go can keep students from getting care. <strong>Most health insurance plans cover vaccines</strong> {cite("CDC, 2024b")}, and in Ohio <strong>most women have insurance that covers cervical cancer screening at no cost</strong> {cite("Ohio Department of Health, n.d.")}.</p>',
           'See the <a href="Resources.dc.html">Local Resources page</a> for low-cost and no-cost options in Cincinnati and Ohio.')
c6 = rcard(6, "activity", "Biological and health factors",
           f'''<ul style="margin: 0; padding-left: 22px; display: flex; flex-direction: column; gap: 8px">
<li>A <strong>high-risk HPV infection that lasts for years</strong> is the main cause of cervical cancer {NCI}.</li>
<li>A weakened <strong>immune system</strong> (the body’s defense against germs) lowers the body’s ability to fight HPV {NCI}. Women living with <strong>HIV</strong> (a virus that weakens the immune system) are <strong>6 times more likely</strong> to develop cervical cancer than women without HIV {cite("World Health Organization [WHO], 2026")}.</li>
<li><strong>Smoking</strong> or breathing in <strong>secondhand smoke</strong> (smoke from someone else’s cigarette) increases the risk of cervical cancer {NCI}.</li>
</ul>''',
           'You can’t control every risk, but you can choose not to smoke. Tell your health care provider about any health conditions you have.')

g1 = grid([c1, c2, c3], 300)
g2 = grid([c4, c5, c6], 300)

tk = takeaway(f'<p style="margin: 0">Some risk factors, like a <strong>long-lasting high-risk HPV infection</strong> or a <strong>weakened immune system</strong>, are hard to control {NCI}. Many others, like <strong>smoking, knowing the facts, and getting care</strong>, are things you can act on today.</p>')

body = page_header("Risk Factors", "What Raises Your Risk?", intro, "alert") + wrap('<div style="height: 48px"></div>' + g1 + mythbox + g2 + tk)
emit("RiskFactors.dc.html", page("Risk Factors: HPV and Cervical Cancer", "RiskFactors.dc.html", body, 3600))
emit_static("RiskFactors.dc.html", "Risk Factors: HPV and Cervical Cancer", body)
