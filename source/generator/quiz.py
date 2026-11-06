from common import *
import json

intro = '<p style="margin: 0">Five quick questions check the three learning goals on this site. Pick an answer to see right away if you got it, plus a short explanation. Your score shows at the end.</p>'

Q = [
    {"goal": "Learning goal 1: Risk factors", "q": "Which of these raises the risk of cervical cancer?",
     "opts": ["Drinking coffee", "Smoking", "Exercising often", "Wearing glasses"], "a": 1,
     "exp": "Smoking or breathing in secondhand smoke increases the risk of cervical cancer (National Cancer Institute [NCI], 2024).",
     "href": "RiskFactors.dc.html", "page": "Risk Factors"},
    {"goal": "Learning goal 1: Risk factors", "q": "Can someone spread HPV without having symptoms?",
     "opts": ["Yes", "No", "Only if they feel sick"], "a": 0,
     "exp": "HPV can spread even when there are no signs or symptoms (Centers for Disease Control and Prevention [CDC], 2024a).",
     "href": "RiskFactors.dc.html", "page": "Risk Factors"},
    {"goal": "Learning goal 2: Prevention", "q": "Through what age is the HPV vaccine recommended for everyone not already vaccinated?",
     "opts": ["18", "21", "26", "45"], "a": 2,
     "exp": "HPV vaccination is recommended for everyone through age 26 who is not already vaccinated (CDC, 2024c).",
     "href": "Prevention.dc.html", "page": "Prevention"},
    {"goal": "Learning goal 2: Prevention", "q": "At what age should Pap tests start?",
     "opts": ["16", "18", "21", "30"], "a": 2,
     "exp": "Pap tests start at age 21 and are done every 3 years if results are normal (CDC, 2025b).",
     "href": "Prevention.dc.html", "page": "Prevention"},
    {"goal": "Learning goal 3: Local resources", "q": "Which Ohio program offers no-cost cervical cancer screening to people who qualify?",
     "opts": ["Hamilton County Public Health vaccine record requests", "The Breast and Cervical Cancer Project", "UC urgent care"], "a": 1,
     "exp": "Ohio’s Breast and Cervical Cancer Project offers no-cost cervical cancer screening to people who qualify (Ohio Department of Health, n.d.).",
     "href": "Resources.dc.html", "page": "Local Resources"},
]

script = """class Component extends DCLogic {
constructor(props) {
super(props);
this.state = { i: 0, picked: null, score: 0, done: false };
}
renderVals() {
const Q = %s;
const s = this.state;
const q = Q[s.i];
const answered = s.picked !== null;
const letters = ['A', 'B', 'C', 'D'];
const options = q.opts.map((label, idx) => ({
label: label,
letter: letters[idx],
isIdle: !answered,
isRight: answered && idx === q.a,
isWrong: answered && idx === s.picked && idx !== q.a,
isDim: answered && idx !== q.a && idx !== s.picked,
pick: () => {
if (this.state.picked !== null) return;
this.setState({ picked: idx, score: this.state.score + (idx === q.a ? 1 : 0) });
}
}));
const wasRight = answered && s.picked === q.a;
const segments = Q.map((x, k) => ({ filled: k < s.i || (k === s.i && answered), empty: !(k < s.i || (k === s.i && answered)) }));
let msg = 'Good start. Review the pages below, then try again.';
if (s.score === 5) msg = 'Perfect score! You know how to protect yourself.';
else if (s.score >= 3) msg = 'Nice work! Review the pages below to fill in any gaps.';
return {
notDone: !s.done,
done: s.done,
num: s.i + 1,
goal: q.goal,
question: q.q,
options: options,
answered: answered,
wasRight: wasRight,
wasWrong: answered && !wasRight,
correctText: q.opts[q.a],
explanation: q.exp,
reviewHref: q.href,
reviewPage: q.page,
nextLabel: s.i < Q.length - 1 ? 'Next question' : 'See my score',
segments: segments,
score: s.score,
scoreMsg: msg,
next: () => {
if (this.state.i < Q.length - 1) this.setState({ i: this.state.i + 1, picked: null });
else this.setState({ done: true });
},
restart: () => this.setState({ i: 0, picked: null, score: 0, done: false })
};
}
}""" % json.dumps(Q, ensure_ascii=False)

optbase = "width: 100%; text-align: left; font-family: inherit; font-size: 18px; line-height: 1.4; min-height: 56px; padding: 14px 18px; border-radius: 14px; display: flex; gap: 14px; align-items: center"
letter = lambda bg, fg: f'<span style="flex: 0 0 auto; width: 32px; height: 32px; border-radius: 999px; background: {bg}; color: {fg}; font-weight: 800; font-size: 15px; display: flex; align-items: center; justify-content: center">{{{{opt.letter}}}}</span>'

quizbox = f'''<section aria-labelledby="quiz-title" style="margin-top: 48px; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 24px; padding: 36px; max-width: 820px; margin-left: auto; margin-right: auto">
<h2 id="quiz-title" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap">Quiz</h2>
<sc-if value="{{{{notDone}}}}" hint-placeholder-val="{{{{true}}}}">
<div style="display: flex; flex-direction: column; gap: 20px">
<div style="display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap">
<p style="margin: 0; font-weight: 800; color: {TEAL_TX}">Question {{{{num}}}} of 5</p>
<p style="margin: 0; font-size: 14px; font-weight: 700; background: {TEAL_LT}; color: {TEAL_TX}; border-radius: 999px; padding: 4px 12px">{{{{goal}}}}</p>
</div>
<div aria-hidden="true" style="display: flex; gap: 6px">
<sc-for list="{{{{segments}}}}" as="seg" hint-placeholder-count="5">
<sc-if value="{{{{seg.filled}}}}" hint-placeholder-val="{{{{false}}}}"><div style="flex: 1 1 0; height: 8px; border-radius: 999px; background: {TEAL}"></div></sc-if>
<sc-if value="{{{{seg.empty}}}}" hint-placeholder-val="{{{{true}}}}"><div style="flex: 1 1 0; height: 8px; border-radius: 999px; background: {TEAL_LT}"></div></sc-if>
</sc-for>
</div>
<h3 style="margin: 0; font-size: 28px; line-height: 1.3; font-weight: 800; color: {TEAL_DK}">{{{{question}}}}</h3>
<div role="group" aria-label="Answer choices" style="display: flex; flex-direction: column; gap: 10px">
<sc-for list="{{{{options}}}}" as="opt" hint-placeholder-count="4">
<sc-if value="{{{{opt.isIdle}}}}" hint-placeholder-val="{{{{true}}}}">
<button class="optbtn" type="button" onClick="{{{{opt.pick}}}}" style="{optbase}; cursor: pointer; background: #FFFFFF; color: {INK}; border: 2px solid {LINE}">{letter(TEAL_LT, TEAL_TX)}<span>{{{{opt.label}}}}</span></button>
</sc-if>
<sc-if value="{{{{opt.isRight}}}}" hint-placeholder-val="{{{{false}}}}">
<button type="button" disabled="disabled" style="{optbase}; background: {TEAL_LT}; color: {TEAL_DK}; border: 2px solid {TEAL}; font-weight: 700">{letter(TEAL, "#FFFFFF")}<span style="flex: 1 1 auto">{{{{opt.label}}}}</span><span style="display: flex; align-items: center; gap: 6px; font-size: 15px">{icon("check", 20, TEAL, 3)}Correct answer</span></button>
</sc-if>
<sc-if value="{{{{opt.isWrong}}}}" hint-placeholder-val="{{{{false}}}}">
<button type="button" disabled="disabled" style="{optbase}; background: {WARM_LT}; color: {WARM_TX}; border: 2px solid {WARM}; font-weight: 700">{letter(WARM, "#FFFFFF")}<span style="flex: 1 1 auto">{{{{opt.label}}}}</span><span style="display: flex; align-items: center; gap: 6px; font-size: 15px">{icon("x", 20, WARM, 3)}Your answer</span></button>
</sc-if>
<sc-if value="{{{{opt.isDim}}}}" hint-placeholder-val="{{{{false}}}}">
<button type="button" disabled="disabled" style="{optbase}; background: #F9FAFB; color: {MUTED}; border: 2px solid #E5E7EB">{letter("#E5E7EB", MUTED)}<span>{{{{opt.label}}}}</span></button>
</sc-if>
</sc-for>
</div>
<div aria-live="polite">
<sc-if value="{{{{answered}}}}" hint-placeholder-val="{{{{false}}}}">
<div style="background: {TEAL_BG}; border: 1px solid {LINE}; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; gap: 10px">
<sc-if value="{{{{wasRight}}}}" hint-placeholder-val="{{{{true}}}}"><p style="margin: 0; font-size: 22px; font-weight: 800; color: {TEAL_TX}; display: flex; align-items: center; gap: 8px">{icon("circlecheck", 24, TEAL)}Correct!</p></sc-if>
<sc-if value="{{{{wasWrong}}}}" hint-placeholder-val="{{{{false}}}}"><p style="margin: 0; font-size: 22px; font-weight: 800; color: {WARM_TX}">Not quite. The answer is: {{{{correctText}}}}</p></sc-if>
<p style="margin: 0">{{{{explanation}}}}</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center; justify-content: space-between">
<a href="{{{{reviewHref}}}}" style="font-weight: 700; min-height: 44px; display: inline-flex; align-items: center">Review: {{{{reviewPage}}}}</a>
<button class="btn" type="button" onClick="{{{{next}}}}" style="font-family: inherit; display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 10px 22px; border-radius: 999px; font-weight: 700; font-size: 17px; cursor: pointer; background: {TEAL}; color: #FFFFFF; border: 2px solid {TEAL}">{{{{nextLabel}}}}{icon("arrowright", 18, "#FFFFFF")}</button>
</div>
</div>
</sc-if>
</div>
</div>
</sc-if>
<sc-if value="{{{{done}}}}" hint-placeholder-val="{{{{false}}}}">
<div aria-live="polite" style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px">
{tile("circlecheck", TEAL_LT, TEAL, 72, 38)}
<p style="margin: 0; font-size: 15px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: {TEAL_TX}">Your score</p>
<p style="margin: 0; font-size: 64px; font-weight: 800; line-height: 1; color: {TEAL}">{{{{score}}}} / 5</p>
<p style="margin: 0; font-size: 21px; font-weight: 700">{{{{scoreMsg}}}}</p>
<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center">
<a href="RiskFactors.dc.html" style="font-weight: 700; min-height: 44px; display: inline-flex; align-items: center; padding: 0 10px">Risk Factors</a>
<a href="Prevention.dc.html" style="font-weight: 700; min-height: 44px; display: inline-flex; align-items: center; padding: 0 10px">Prevention</a>
<a href="Resources.dc.html" style="font-weight: 700; min-height: 44px; display: inline-flex; align-items: center; padding: 0 10px">Local Resources</a>
</div>
<button class="btn" type="button" onClick="{{{{restart}}}}" style="font-family: inherit; display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 10px 22px; border-radius: 999px; font-weight: 700; font-size: 17px; cursor: pointer; background: #FFFFFF; color: {TEAL_DK}; border: 2px solid {TEAL}">Try again</button>
</div>
</sc-if>
</section>'''

tk = takeaway('<p style="margin: 0">Each question matches one of this site’s three learning goals: <strong>risk factors</strong>, <strong>prevention methods</strong>, and <strong>local resources</strong>. Missed one? Use the review link under each answer to go back to that page.</p>')

body = page_header("Quick Quiz", "Test What You Learned", intro, "help") + wrap(quizbox + tk)
emit("Quiz.dc.html", page("Quiz: HPV and Cervical Cancer Prevention", "Quiz.dc.html", body, 1900, script))

# ---------- Static (deployable) version of the quiz: plain JavaScript ----------
STYLE = {
    "optbase": optbase, "teal": TEAL, "tealdk": TEAL_DK, "tealtx": TEAL_TX, "teallt": TEAL_LT, "tealbg": TEAL_BG,
    "line": LINE, "warm": WARM, "warmtx": WARM_TX, "warmlt": WARM_LT, "ink": INK, "muted": MUTED,
    "check": icon("check", 20, TEAL, 3), "x": icon("x", 20, WARM, 3), "circlecheck": icon("circlecheck", 24, TEAL),
    "arrow": icon("arrowright", 18, "#FFFFFF"), "bigcheck": tile("circlecheck", TEAL_LT, TEAL, 72, 38),
}
static_box = f'''<section aria-labelledby="quiz-title" style="margin-top: 48px; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 24px; padding: 36px; max-width: 820px; margin-left: auto; margin-right: auto">
<h2 id="quiz-title" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap">Quiz</h2>
<div id="quiz"><noscript><p style="margin: 0">Please turn on JavaScript to take the quiz.</p></noscript></div>
</section>'''

static_js = """<script>
(function () {
var Q = %s;
var S = %s;
var LINKS = {"RiskFactors.dc.html": "risk-factors.html", "Prevention.dc.html": "prevention.html", "Resources.dc.html": "resources.html"};
var st = { i: 0, picked: null, score: 0, done: false };
var root = document.getElementById('quiz');
var L = ['A', 'B', 'C', 'D'];
function letter(bg, fg, t) { return '<span style="flex: 0 0 auto; width: 32px; height: 32px; border-radius: 999px; background: ' + bg + '; color: ' + fg + '; font-weight: 800; font-size: 15px; display: flex; align-items: center; justify-content: center">' + t + '</span>'; }
function render(focusSel) {
  var h = '';
  if (!st.done) {
    var q = Q[st.i], answered = st.picked !== null;
    h += '<div style="display: flex; flex-direction: column; gap: 20px">';
    h += '<div style="display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap"><p style="margin: 0; font-weight: 800; color: ' + S.tealtx + '">Question ' + (st.i + 1) + ' of 5</p><p style="margin: 0; font-size: 14px; font-weight: 700; background: ' + S.teallt + '; color: ' + S.tealtx + '; border-radius: 999px; padding: 4px 12px">' + q.goal + '</p></div>';
    h += '<div aria-hidden="true" style="display: flex; gap: 6px">';
    for (var k = 0; k < Q.length; k++) { var f = k < st.i || (k === st.i && answered); h += '<div style="flex: 1 1 0; height: 8px; border-radius: 999px; background: ' + (f ? S.teal : S.teallt) + '"></div>'; }
    h += '</div>';
    h += '<h3 id="q-text" tabindex="-1" style="margin: 0; font-size: 28px; line-height: 1.3; font-weight: 800; color: ' + S.tealdk + '">' + q.q + '</h3>';
    h += '<div role="group" aria-labelledby="q-text" style="display: flex; flex-direction: column; gap: 10px">';
    q.opts.forEach(function (label, idx) {
      if (!answered) {
        h += '<button class="optbtn" type="button" data-idx="' + idx + '" style="' + S.optbase + '; cursor: pointer; background: #FFFFFF; color: ' + S.ink + '; border: 2px solid ' + S.line + '">' + letter(S.teallt, S.tealtx, L[idx]) + '<span>' + label + '</span></button>';
      } else if (idx === q.a) {
        h += '<button type="button" disabled style="' + S.optbase + '; background: ' + S.teallt + '; color: ' + S.tealdk + '; border: 2px solid ' + S.teal + '; font-weight: 700">' + letter(S.teal, '#FFFFFF', L[idx]) + '<span style="flex: 1 1 auto">' + label + '</span><span style="display: flex; align-items: center; gap: 6px; font-size: 15px">' + S.check + 'Correct answer</span></button>';
      } else if (idx === st.picked) {
        h += '<button type="button" disabled style="' + S.optbase + '; background: ' + S.warmlt + '; color: ' + S.warmtx + '; border: 2px solid ' + S.warm + '; font-weight: 700">' + letter(S.warm, '#FFFFFF', L[idx]) + '<span style="flex: 1 1 auto">' + label + '</span><span style="display: flex; align-items: center; gap: 6px; font-size: 15px">' + S.x + 'Your answer</span></button>';
      } else {
        h += '<button type="button" disabled style="' + S.optbase + '; background: #F9FAFB; color: ' + S.muted + '; border: 2px solid #E5E7EB">' + letter('#E5E7EB', S.muted, L[idx]) + '<span>' + label + '</span></button>';
      }
    });
    h += '</div><div aria-live="polite">';
    if (answered) {
      var right = st.picked === q.a;
      h += '<div style="background: ' + S.tealbg + '; border: 1px solid ' + S.line + '; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; gap: 10px">';
      h += right ? '<p id="fb" tabindex="-1" style="margin: 0; font-size: 22px; font-weight: 800; color: ' + S.tealtx + '; display: flex; align-items: center; gap: 8px">' + S.circlecheck + 'Correct!</p>'
                 : '<p id="fb" tabindex="-1" style="margin: 0; font-size: 22px; font-weight: 800; color: ' + S.warmtx + '">Not quite. The answer is: ' + q.opts[q.a] + '</p>';
      h += '<p style="margin: 0">' + q.exp + '</p>';
      h += '<div style="display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center; justify-content: space-between"><a href="' + LINKS[q.href] + '" style="font-weight: 700; min-height: 44px; display: inline-flex; align-items: center">Review: ' + q.page + '</a>';
      h += '<button class="btn" type="button" id="next" style="font-family: inherit; display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 10px 22px; border-radius: 999px; font-weight: 700; font-size: 17px; cursor: pointer; background: ' + S.teal + '; color: #FFFFFF; border: 2px solid ' + S.teal + '">' + (st.i < Q.length - 1 ? 'Next question' : 'See my score') + S.arrow + '</button></div></div>';
    }
    h += '</div></div>';
  } else {
    var msg = 'Good start. Review the pages below, then try again.';
    if (st.score === 5) msg = 'Perfect score! You know how to protect yourself.';
    else if (st.score >= 3) msg = 'Nice work! Review the pages below to fill in any gaps.';
    var a = 'font-weight: 700; min-height: 44px; display: inline-flex; align-items: center; padding: 0 10px';
    h += '<div aria-live="polite" style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px">' + S.bigcheck;
    h += '<p style="margin: 0; font-size: 15px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: ' + S.tealtx + '">Your score</p>';
    h += '<p id="score" tabindex="-1" style="margin: 0; font-size: 64px; font-weight: 800; line-height: 1; color: ' + S.teal + '">' + st.score + ' / 5</p>';
    h += '<p style="margin: 0; font-size: 21px; font-weight: 700">' + msg + '</p>';
    h += '<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center"><a href="risk-factors.html" style="' + a + '">Risk Factors</a><a href="prevention.html" style="' + a + '">Prevention</a><a href="resources.html" style="' + a + '">Local Resources</a></div>';
    h += '<button class="btn" type="button" id="restart" style="font-family: inherit; display: inline-flex; align-items: center; gap: 8px; min-height: 48px; padding: 10px 22px; border-radius: 999px; font-weight: 700; font-size: 17px; cursor: pointer; background: #FFFFFF; color: ' + S.tealdk + '; border: 2px solid ' + S.teal + '">Try again</button></div>';
  }
  root.innerHTML = h;
  if (focusSel) { var el = document.getElementById(focusSel); if (el) el.focus(); }
}
root.addEventListener('click', function (e) {
  var b = e.target.closest('button');
  if (!b || b.disabled) return;
  if (b.hasAttribute('data-idx')) {
    if (st.picked !== null) return;
    var idx = +b.getAttribute('data-idx');
    st.picked = idx; if (idx === Q[st.i].a) st.score++;
    render('fb');
  } else if (b.id === 'next') {
    if (st.i < Q.length - 1) { st.i++; st.picked = null; render('q-text'); } else { st.done = true; render('score'); }
  } else if (b.id === 'restart') {
    st = { i: 0, picked: null, score: 0, done: false }; render('q-text');
  }
});
render();
})();
</script>""" % (json.dumps(Q, ensure_ascii=False), json.dumps(STYLE, ensure_ascii=False))

static_body = page_header("Quick Quiz", "Test What You Learned", intro, "help") + wrap(static_box + tk)
emit_static("Quiz.dc.html", "Quiz: HPV and Cervical Cancer Prevention", static_body, static_js)
