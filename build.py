"""Builds the ScienceGloon website pages (plain HTML, no cookies, no analytics, no third-party requests)."""
from pathlib import Path

NAME, CONTACT, YEAR = "ScienceGloon", "daniel@lagowski.es", 2026
EFFECTIVE = "October 12, 2026"
LINKS = ('<a href="https://www.youtube.com/@sciencegloon">YouTube @sciencegloon</a> &middot; '
         '<a href="https://www.tiktok.com/@sciencegloon">TikTok @sciencegloon</a> &middot; '
         '<a href="https://www.instagram.com/sciencegloon/">Instagram @sciencegloon</a> &middot; '
         '<a href="https://www.facebook.com/sciencegloon">Facebook</a>')


def page(path: str, title: str, desc: str, body: str, noindex: bool = False) -> None:
    up = "../" if "/" in path else ""
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">{robots}
<link rel="icon" href="{up}favicon.png"><link rel="stylesheet" href="{up}style.css"></head><body><div class="wrap">
<header><a class="brand" href="{up or './'}"><img src="{up}assets/logo-120.png" alt="{NAME} logo" width="40" height="40">{NAME}</a>
<nav><a href="{up or './'}">Home</a><a href="{up}privacy/">Privacy</a><a href="{up}terms/">Terms</a></nav></header>
{body}
<footer><a href="{up or './'}">Home</a><a href="{up}privacy/">Privacy Policy</a><a href="{up}terms/">Terms of Service</a><br>
&copy; {YEAR} {NAME} &middot; Contact: <a href="mailto:{CONTACT}">{CONTACT}</a></footer></div></body></html>
"""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


page("index.html", f"{NAME} - ciencia explicada en un minuto",
     "Short Spanish videos that explain one science question a day, every claim with its source.", f"""
<h1>Ciencia explicada en un minuto.</h1>
<p class="lead">{NAME} makes one short Spanish-language video a day that explains a science question (physics, maths,
astronomy, how things work), simply and with its sources. Every number on screen comes with where it is from.</p>
<div class="card"><h2>What the {NAME} app does</h2>
<p>The {NAME} Publisher app is an internal publishing tool used only by the {NAME} team. It lets us:</p>
<ul><li>upload our own finished videos, with their titles, descriptions and covers, to our own YouTube channel, TikTok
account, Instagram account and Facebook Page;</li>
<li>read our own accounts' basic information and the statistics of our own videos, to check that uploads worked and to
learn which videos people find useful.</li></ul>
<p>The app does not offer accounts to the public and does not access anyone else's data.</p></div>
<div class="card"><h2>Follow {NAME}</h2><p>{LINKS}</p></div>
<p>Read our <a href="privacy/">Privacy Policy</a> and <a href="terms/">Terms of Service</a>. Questions:
<a href="mailto:{CONTACT}">{CONTACT}</a>.</p>""")

page("privacy/index.html", f"Privacy Policy - {NAME}", f"How the {NAME} app handles data.", f"""
<h1>Privacy Policy</h1><p class="lead">Effective date: {EFFECTIVE}</p>
<p>This policy explains how {NAME} ("we", "us") handles information when the {NAME} Publisher app accesses YouTube,
TikTok, Instagram and Facebook on our behalf. {NAME} is operated from Spain. Contact:
<a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Who uses the app</h2><p>The app is an internal tool. It is used only by the {NAME} team to publish our own videos to
our own accounts. It is not offered to the public, and it has no third-party users.</p>
<h2>Data we access</h2><p>When a team member signs in and grants permission, the app may access, for our own accounts only:</p>
<ul><li><strong>YouTube</strong> (scopes <code>youtube.upload</code> and <code>youtube</code>): permission to upload videos
and their covers to our own channel, to add them to our own playlists, and to read our own channel's information and
video statistics.</li>
<li><strong>TikTok</strong> (scopes <code>user.info.basic</code>, <code>user.info.stats</code> and <code>video.upload</code>):
permission to read our own account's basic profile and follower count and to send videos we made to our own TikTok
inbox as drafts. We review and publish every draft ourselves in the TikTok app.</li>
<li><strong>Instagram and Facebook</strong> (permissions <code>instagram_basic</code>, <code>instagram_content_publish</code>,
<code>pages_show_list</code>, <code>pages_read_engagement</code>, <code>pages_manage_posts</code>, and, when granted,
<code>instagram_manage_insights</code>, <code>read_insights</code> and <code>business_management</code>): permission to
publish our own videos to our own Instagram account and Facebook Page and to read their basic information, engagement
and view counts.</li></ul>
<h2>How we use it</h2><p>We use this access only to publish {NAME} videos on our own accounts and to measure how our own
videos perform. We do not use it for advertising, we do not sell it, and we do not share it with third parties except as
needed to deliver it to the platforms themselves.</p>
<h2>Google API Services User Data Policy</h2><p>{NAME}'s use and transfer of information received from Google APIs
adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data
Policy</a>, including the Limited Use requirements. The app uses the
<a href="https://developers.google.com/youtube/terms/api-services-terms-of-service">YouTube API Services</a>; by using
the app you also agree to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> and the
<a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</p>
<h2 id="youtube">YouTube API Services</h2><p>You can revoke the app's access to a Google account at any time at
<a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>.</p>
<h2>TikTok and Meta</h2><p>The app's use of TikTok follows the <a href="https://www.tiktok.com/legal/page/global/terms-of-service/en">TikTok
Terms of Service</a> and the TikTok Developer Terms; its use of Instagram and Facebook follows the
<a href="https://developers.facebook.com/terms/">Meta Platform Terms</a>.</p>
<h2>Storage and security</h2><p>Access tokens are stored privately on our own machine, readable only by the app's
operator, and never shared, sold or published. Video statistics are kept in our own database.</p>
<h2>Retention and deletion</h2><p>We keep tokens only while the app is in use and delete them, with the data obtained
through them, within 30 days of revoking access or on request to <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Your rights</h2><p>Under the GDPR you may ask us for access to, correction or deletion of any personal data we hold,
and you may complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es">AEPD</a>).</p>
<h2>Changes</h2><p>We will post any change to this policy on this page with a new effective date.</p>""")

page("terms/index.html", f"Terms of Service - {NAME}", f"Terms for the {NAME} app and website.", f"""
<h1>Terms of Service</h1><p class="lead">Effective date: {EFFECTIVE}</p>
<p>These terms apply to the {NAME} website and the {NAME} Publisher app. By using them you agree to these terms.</p>
<h2>The service</h2><p>The {NAME} Publisher app is an internal tool used by the {NAME} team to publish our own videos to
our own YouTube channel, TikTok account, Instagram account and Facebook Page. It has no third-party users; access is
limited to authorized team members.</p>
<h2>Third-party services</h2><p>The app uses YouTube API Services, TikTok's Content Posting API and Meta's Graph API. Its
use is also subject to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>, the
<a href="https://policies.google.com/privacy">Google Privacy Policy</a>, the
<a href="https://www.tiktok.com/legal/page/global/terms-of-service/en">TikTok Terms of Service</a> and the
<a href="https://developers.facebook.com/terms/">Meta Platform Terms</a>.</p>
<h2>Acceptable use</h2><p>You may not use the app to upload content you do not have the rights to, to violate any
platform's policies, or to access accounts or data that are not yours.</p>
<h2>Content</h2><p>{NAME} videos, texts and artwork are ours unless stated otherwise. Facts and figures belong to the
sources we cite. Our videos are informative; they are not professional, financial, legal or medical advice.</p>
<h2>No warranty</h2><p>The website and app are provided "as is", without warranties of any kind. To the extent permitted
by law, {NAME} is not liable for indirect or consequential damages arising from their use.</p>
<h2>Changes and termination</h2><p>We may change these terms or discontinue the app at any time. Changes will be posted
on this page.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of Spain.</p>
<h2>Contact</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p>""")

page("tiktok-callback/index.html", f"Authorization - {NAME}", f"{NAME} app authorization callback.", f"""
<h1>Authorization</h1>
<p id="msg" class="lead">Reading the authorization response&hellip;</p>
<p><textarea id="code" readonly rows="3" hidden></textarea></p>
<p><button id="copy" hidden>Copy code</button></p>
<p>This page only shows the one-time code that TikTok returns after you authorize the {NAME} app. It sends nothing
anywhere. Copy the code into the setup step within a few minutes; it expires and works only once.</p>
<script>
const q = new URLSearchParams(location.search), msg = document.getElementById('msg'), box = document.getElementById('code'), btn = document.getElementById('copy');
if (q.get('error')) {{ msg.textContent = 'TikTok returned an error: ' + q.get('error') + ' ' + (q.get('error_description') || ''); }}
else if (q.get('code')) {{ msg.textContent = 'Authorized. State: ' + (q.get('state') || '(none)') + '. Code:'; box.value = q.get('code'); box.hidden = btn.hidden = false;
  btn.onclick = () => {{ box.select(); navigator.clipboard ? navigator.clipboard.writeText(box.value) : document.execCommand('copy'); btn.textContent = 'Copied'; }}; }}
else {{ msg.textContent = 'No authorization code in this address.'; }}
</script>""", noindex=True)
print("built")
