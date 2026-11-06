from common import *

intro = '<p style="margin: 0">Ready for the next step? These campus, city, county, and state programs can help you get the HPV vaccine, screening, and follow-up care. Many options are <strong>low-cost or no-cost</strong>.</p>'


def row(label, html):
    return f'<div style="display: flex; flex-direction: column; gap: 2px"><p style="margin: 0; font-size: 13px; font-weight: 800; letter-spacing: 0.07em; text-transform: uppercase; color: {TEAL_TX}">{label}</p><p style="margin: 0">{html}</p></div>'


def rc(ic, kind, name, offers, who, how, url, short):
    return card(f'''<div style="display: flex; gap: 14px; align-items: center">{tile(ic, TEAL, "#FFFFFF", 56, 28)}<div><p style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: {WARM_TX}">{kind}</p><h2 style="margin: 0; font-size: 24px; line-height: 1.25; font-weight: 800; color: {TEAL_DK}">{name}</h2></div></div>
<div style="height: 1px; background: {LINE}"></div>
{row("What it offers", offers)}
{row("Who it’s for", who)}
{row("How to get started", how)}
<div style="margin-top: auto; padding-top: 6px">{btn(url, "Visit Website", True, True, f"Visit Website: {short} (opens in a new tab)", "external")}</div>''')


UC = cite("University of Cincinnati, n.d.")
ODH = cite("Ohio Department of Health, n.d.")
CITY = cite("City of Cincinnati, n.d.")
HC = cite("Hamilton County Public Health, n.d.")
tel = lambda num, label: f'<a href="tel:{num}" style="font-weight: 800">{label}</a>'

cards = [
    rc("building", "On campus", "UC University Health Services",
       f"<strong>Urgent care</strong> (care for problems that need attention soon but are not emergencies) and <strong>primary care</strong> (everyday care, like checkups) for UC students, including <strong>immunizations</strong> (vaccines) and <strong>women’s health services</strong> {UC}.",
       "UC students.",
       f"Students can ask about the <strong>HPV vaccine</strong> and <strong>cervical cancer screening</strong> {UC}.",
       "https://med.uc.edu/landing-pages/university-health/health-clinics-and-services/uhs-services", "UC University Health Services"),
    rc("dollar", "Statewide", "Ohio Department of Health Breast and Cervical Cancer Project (BCCP)",
       f"<strong>No-cost cervical cancer screening</strong> and <strong>diagnostic testing</strong> (tests that find the cause of an abnormal result) for people who qualify, plus a <strong>Patient Navigation Program</strong> that helps people find providers, schedule appointments, and understand their insurance {ODH}.",
       "People who qualify. A quick phone call can tell you if you do.",
       f"Call {tel('+18444302227', '1-844-430-BCCP (2227)')} to see if you qualify {ODH}.",
       "https://odh.ohio.gov/know-our-programs/breast-cervical-cancer-project", "Ohio Breast and Cervical Cancer Project"),
    rc("heart", "City", "Cincinnati Health Department",
       f"A <strong>federally qualified health center</strong> (a community health center that receives federal funding) with <strong>six primary care health centers</strong> offering medical and <strong>ob/gyn care</strong> (care for reproductive health and pregnancy), each with an <strong>on-site pharmacy</strong> {CITY}.",
       "People in Cincinnati looking for primary care or ob/gyn care.",
       f"Call Community Health Centers at {tel('+15133577320', '513-357-7320')} {CITY}.",
       "https://www.cincinnati-oh.gov/health/", "Cincinnati Health Department"),
    rc("pin", "County", "Hamilton County Public Health",
       f"The <strong>county health department</strong>, offering clinical services, health promotion and education, and <strong>vaccine record requests</strong> {HC}.",
       "People who live in Hamilton County.",
       "Visit the website to explore services or request your vaccine record.",
       "https://hamiltoncountyhealth.org/", "Hamilton County Public Health"),
]

notsure = f'''<section aria-labelledby="ns-title" style="margin-top: 48px; background: {TEAL_DK}; color: #FFFFFF; border-radius: 24px; padding: 32px; display: flex; gap: 24px; align-items: flex-start; flex-wrap: wrap">
{tile("help", "#FFFFFF", TEAL, 56, 28)}
<div style="flex: 1 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 14px">
<h2 id="ns-title" style="margin: 0; font-size: 28px; font-weight: 800">Not sure where to start?</h2>
<p style="margin: 0; font-size: 20px; color: #E6F4F1">UC students can start at University Health Services. Not a UC student, or no insurance? Call BCCP at <a href="tel:+18444302227" style="color: #FDBA74; font-weight: 800">1-844-430-2227</a>.</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px">
<div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.25); border-radius: 14px; padding: 14px 16px; display: flex; gap: 10px; align-items: center">{icon("building", 22, "#99F6E4")}<span><strong>UC student?</strong> Start at University Health Services.</span></div>
<div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.25); border-radius: 14px; padding: 14px 16px; display: flex; gap: 10px; align-items: center">{icon("phone", 22, "#FDBA74")}<span><strong>Not a UC student, or no insurance?</strong> Call BCCP.</span></div>
</div>
</div>
</section>'''

tk = takeaway(f'<p style="margin: 0">You don’t have to figure this out alone. UC students can get care at <strong>University Health Services</strong> {UC}, and the <strong>BCCP</strong> offers no-cost cervical cancer screening to people who qualify {ODH}.</p>')

body = page_header("Local Resources", "Where to Get Care in Cincinnati and Ohio", intro, "pin") + wrap('<div style="height: 48px"></div>' + grid(cards, 340, 24) + notsure + tk)
emit("Resources.dc.html", page("Local Resources: HPV and Cervical Cancer Prevention", "Resources.dc.html", body, 2900))
emit_static("Resources.dc.html", "Local Resources: HPV and Cervical Cancer Prevention", body)
