from common import *

refs = [
    ('American Cancer Society. (2026, January 14). <em>Key statistics for cervical cancer</em>. ', 'https://www.cancer.org/cancer/types/cervical-cancer/about/key-statistics.html'),
    ('Centers for Disease Control and Prevention. (2024a, July 3). <em>About HPV</em>. ', 'https://www.cdc.gov/hpv/about/index.html'),
    ('Centers for Disease Control and Prevention. (2024b, August 20). <em>HPV vaccination</em>. ', 'https://www.cdc.gov/hpv/vaccines/index.html'),
    ('Centers for Disease Control and Prevention. (2024c, December 11). <em>Reducing risk for cervical cancer</em>. ', 'https://www.cdc.gov/cervical-cancer/prevention/index.html'),
    ('Centers for Disease Control and Prevention. (2025a, March 3). <em>Cancers caused by HPV</em>. ', 'https://www.cdc.gov/hpv/about/cancers-caused-by-hpv.html'),
    ('Centers for Disease Control and Prevention. (2025b, February 26). <em>Screening for cervical cancer</em>. ', 'https://www.cdc.gov/cervical-cancer/screening/index.html'),
    ('City of Cincinnati. (n.d.). <em>Health Department</em>. ', 'https://www.cincinnati-oh.gov/health/'),
    ('Hamilton County Public Health. (n.d.). <em>Home page</em>. ', 'https://hamiltoncountyhealth.org/'),
    ('National Cancer Institute. (2024, August 2). <em>Cervical cancer causes, risk factors, and prevention</em>. ', 'https://www.cancer.gov/types/cervical/causes-risk-prevention'),
    ('National Cancer Institute &amp; Centers for Disease Control and Prevention. (n.d.). <em>Incidence rate report for Ohio by county: Cervix (all stages), 2019–2023</em> [Data table]. State Cancer Profiles. Retrieved November 6, 2026, from ', 'https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=39&amp;areatype=county&amp;cancer=057&amp;race=00&amp;sex=2&amp;age=001&amp;stage=999&amp;year=0&amp;type=incd&amp;sortVariableName=rate&amp;sortOrder=default&amp;output=0'),
    ('Ohio Department of Health. (n.d.). <em>Breast &amp; Cervical Cancer Project</em>. ', 'https://odh.ohio.gov/know-our-programs/breast-cervical-cancer-project'),
    ('University of Cincinnati. (n.d.). <em>Primary care: University Health Services</em>. ', 'https://med.uc.edu/landing-pages/university-health/health-clinics-and-services/uhs-services'),
    ('World Health Organization. (2026, July 3). <em>Cervical cancer</em>. ', 'https://www.who.int/news-room/fact-sheets/detail/cervical-cancer'),
]
entries = "".join(
    f'<p style="margin: 0; padding-left: 0.5in; text-indent: -0.5in; line-height: 2; overflow-wrap: anywhere">{t}<a href="{u}" target="_blank" rel="noopener noreferrer">{u}</a></p>'
    for t, u in refs)

intro = '<p style="margin: 0">Every fact and number on this site comes from the trusted sources below. They are listed in APA 7th edition style, in alphabetical order. Select any link to read the original source.</p>'

listbox = f'''<section aria-labelledby="ref-title" style="margin-top: 48px; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 20px; padding: 48px 56px">
<h2 id="ref-title" style="margin: 0 0 16px; text-align: center; font-size: 26px; font-weight: 800; color: {INK}">References</h2>
<div style="font-size: 18px; color: {INK}">{entries}</div>
</section>'''

tk = takeaway('<p style="margin: 0">This site uses <strong>13 sources</strong> from trusted health groups, including the Centers for Disease Control and Prevention, the National Cancer Institute, the World Health Organization, the American Cancer Society, and local health departments. When you look up health facts, check that they come from sources like these.</p>')

body = page_header("Sources", "References", intro, "book") + wrap(listbox + tk)
emit("References.dc.html", page("References: HPV and Cervical Cancer Prevention", "References.dc.html", body, 2500))
emit_static("References.dc.html", "References: HPV and Cervical Cancer Prevention", body)
