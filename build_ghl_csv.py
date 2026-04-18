"""
Build GHL advanced bulk-upload CSV.
20 posts × 5 platforms = 100 rows.
Platform-tuned captions, schedule, alt text, hashtags, first comment, UTMs.
"""
import csv
from datetime import date, timedelta
from pathlib import Path

OUT = Path(__file__).parent / "ghl-batch2-20posts.csv"
CDN_PLACEHOLDER = "[GHL_CDN_URL]"  # replace after media upload

NOTE = "🤖 Designed by Claude Code · auto-published via GoHighLevel + n8n. Zero manual clicks."
BRAND = "#Skynetlabs #Waseemnasir #NomadCEO"

POSTS = [
 (1,  "ai-agent-hire-2026-waseem-nasir-nomad-ceo",
      "In 2026, not hiring an AI agent is like refusing email in 2005.",
      "Cheap. Never sleeps. Learns your style in an afternoon.",
      "Which task would you hand off first?",
      ["AIAutomation","BuildInPublic","AIAgents","FounderLife","Solopreneur","AI2026","SmallBusinessTips","AutomationForBusiness"],
      "ai-agent-automation-2026"),
 (2,  "sleep-8-hours-agents-work-24-ai-automation",
      "I sleep 8 hours. My agents work 24.",
      "If your business stops when you stop — you have a job, not a business.",
      "What did your agents ship while you slept?",
      ["AIAgents","n8n","FounderLife","PassiveIncome","AutomationForBusiness","Solopreneur","BuildInPublic","AI2026"],
      "24-7-agents-automation"),
 (3,  "busy-vs-productive-founder-leverage-2026",
      "Everyone's busy. Nobody's productive.",
      "Inbox zero = symptom. 50 meetings = friction. Grinding without systems = avoidance.",
      "What were you busy with last week that produced nothing?",
      ["Productivity","FounderLife","AntiHustle","DeepWork","Solopreneur","BuildInPublic","TimeManagement"],
      "productivity-vs-busy"),
 (4,  "more-agents-not-more-hours-ai-automation",
      "You don't need more hours. You need more agents.",
      "Founders winning in 2026 run 16-agent stacks and work 4 hours a day.",
      "How many hours a week are you trading for agent-tasks?",
      ["AIAutomation","Leverage","FounderLife","AIAgents","Solopreneur","BuildInPublic","AI2026"],
      "more-agents-less-hours"),
 (5,  "todo-list-ai-prompt-list-n8n-workflow",
      "Your to-do list is your AI's prompt list.",
      "Every repeating task = workflow. Every 'next week' = cron job.",
      "If your to-do list was a prompt, what's task #1?",
      ["PromptEngineering","n8n","AIAutomation","NoCode","AIAgents","Productivity","AI2026"],
      "todo-as-prompt"),
 (6,  "linkedin-free-personal-brand-growth-2026",
      "LinkedIn is free. Most still can't use it.",
      "900M users. Lowest competition. Organic reach still works.",
      "What free tool are you underusing?",
      ["LinkedInGrowth","PersonalBrand","ContentStrategy","Solopreneur","LinkedInTips","B2BMarketing","FounderLife"],
      "linkedin-underused"),
 (7,  "ship-ugly-iterate-public-founder-rule-01",
      "Rule 01: Ship ugly. Iterate in public. Get paid.",
      "First landing page: ugly. Made $5k. First n8n workflow: 3 nodes. Replaced a VA.",
      "What are you overthinking instead of shipping?",
      ["BuildInPublic","ShipFast","IndieHackers","FounderLife","Solopreneur","MVP","StartupLife"],
      "ship-ugly-rule-01"),
 (8,  "client-2am-ai-video-automation-remotion",
      "Client at 2am: 'how did you ship 12 videos in one night?' Me: 'I didn't. My agents did. I was sleeping.'",
      "This is what leverage looks like in 2026.",
      "If you could text me one question at 2am — what would it be?",
      ["AIAutomation","VideoAutomation","Remotion","AIAgents","ContentCreation","Solopreneur","BuildInPublic"],
      "2am-client-dm"),
 (9,  "skill-stack-beats-degree-stack-2026",
      "Skill stack > degree stack.",
      "Nobody asks about your diploma when you ship. They ask about your GitHub, your workflows, your results.",
      "One skill you taught yourself this year?",
      ["SelfTaught","SkillStack","BuildInPublic","IndiePreneur","CareerAdvice","FounderLife","LearnInPublic"],
      "skill-stack-vs-degree"),
 (10, "charge-5k-2-hours-freelance-pricing-strategy",
      "I charge $5k for work that takes 2 hours. That's the point.",
      "Clients pay for the 10 years of skill compressed into those 2 hours.",
      "Most you've charged for under-2-hour work?",
      ["FreelancerLife","PricingStrategy","AgencyLife","ValueBased","Solopreneur","Consultants","BusinessGrowth"],
      "pricing-value-not-hours"),
 (11, "cold-email-vs-ai-dms-14-percent-outreach",
      "Cold email: 1.2%. AI-personalized DMs: 14%. Same list. Same offer. Only variable: the agent.",
      "The era of 'spray and pray' is dead.",
      "Which outreach channel actually works for you?",
      ["ColdOutreach","SalesAutomation","AIPersonalization","B2BSales","LeadGen","FounderLife","AIAutomation"],
      "cold-email-vs-ai-dms"),
 (12, "ai-wont-replace-you-people-using-ai-will",
      "AI won't replace you. People using AI will.",
      "~18 months before 'I don't use AI' sounds like 'I don't use email' did in 2005.",
      "What's honestly stopping you from daily AI use?",
      ["AI2026","FutureOfWork","AIAdoption","AIAutomation","CareerAdvice","Solopreneur","BuildInPublic"],
      "ai-wont-replace-you"),
 (13, "stop-learning-start-shipping-builder-mindset",
      "Stop learning. Start shipping.",
      "The 47th tutorial won't make you an expert. Shipping an ugly v1 will.",
      "What are you 'learning' instead of shipping?",
      ["ShipFast","BuildInPublic","LearnByDoing","IndieHackers","Solopreneur","MVP","MakerMindset"],
      "stop-learning-start-shipping"),
 (14, "n8n-51-nodes-vs-excel-workflow-automation",
      "Me: 51-node n8n workflow. Them: still opening Excel. Client: 'how are you 10x faster?' Me: agents. lots of agents.",
      "Your stack is either n8n + agents — or it's slowly obsolete.",
      "First thing you'd automate with 1 free hour?",
      ["n8n","AIAutomation","NoCode","WorkflowAutomation","AIAgents","Solopreneur","FounderLife"],
      "n8n-vs-excel"),
 (15, "agents-leverage-squared-solo-founder-50k",
      "Talent is leverage. Agents are leverage squared.",
      "A solo who wires agents outships a 10-person agency.",
      "One task you'd clone into an agent today?",
      ["SoloFounder","AIAgents","Leverage","AIAutomation","BuildInPublic","Solopreneur","FounderLife"],
      "agents-leverage-squared"),
 (16, "25-digital-products-sold-bali-nomad-ceo",
      "Sold 25 digital products while in Bali. Laptop was in Pakistan.",
      "Location doesn't matter. Timezone doesn't matter. Systems matter.",
      "Ever made money while offline? Story?",
      ["PassiveIncome","DigitalProducts","DigitalNomad","RemoteLife","Solopreneur","BuildInPublic","Automation"],
      "sold-offline-bali"),
 (17, "prompt-engineering-skill-2026-future-work",
      "The skill you're sleeping on in 2026: prompt engineering.",
      "Not coding. Not design. The skill of telling a machine what you want — precisely.",
      "One skill you feel you're late on?",
      ["PromptEngineering","AI2026","FutureSkills","AIAutomation","CareerAdvice","Solopreneur","BuildInPublic"],
      "prompt-engineering-2026"),
 (18, "upwork-dead-outbound-lead-gen-freelancer",
      "Hot take: Upwork is dead. Long live outbound.",
      "If your business depends on someone else's platform — you don't have a business. You have a hobby with extra steps.",
      "Where do your best clients actually find you?",
      ["Outbound","LeadGen","FreelancerLife","OwnYourAudience","B2BSales","Solopreneur","BuildInPublic"],
      "upwork-dead-outbound"),
 (19, "ai-orchestration-8-projects-one-day-founder",
      "Founder ships 8 projects in one day. Truth: I didn't write 8. I orchestrated them. Claude drafted. n8n routed. Remotion rendered.",
      "The new title isn't 'founder.' It's 'conductor.'",
      "8 projects/day — believable or capped at 3?",
      ["AIOrchestration","Productivity","SoloFounder","AIAgents","BuildInPublic","FounderLife","AIAutomation"],
      "8-projects-one-day"),
 (20, "built-bali-sold-new-york-remote-nomad-ceo",
      "Built in Bali. Sold in New York.",
      "Old play: move where money is. New play: send systems where money is, stay where you love.",
      "Where are you building from? Drop your city.",
      ["DigitalNomad","RemoteLife","BuildFromAnywhere","FounderLife","Solopreneur","RemoteWork","BuildInPublic"],
      "built-bali-sold-ny"),
]

PLATFORMS = {
 "Instagram":   {"time":"18:00","tag_limit":20,"char_cap":2200,"first_comment_supported":True},
 "LinkedIn":    {"time":"09:00","tag_limit":5, "char_cap":3000,"first_comment_supported":True},
 "Facebook":    {"time":"19:00","tag_limit":3, "char_cap":5000,"first_comment_supported":False},
 "Twitter":     {"time":"12:00","tag_limit":2, "char_cap":280, "first_comment_supported":False},
 "Pinterest":   {"time":"20:00","tag_limit":3, "char_cap":500, "first_comment_supported":False},
}

START = date(2026,5,1)

def build_caption(platform, post):
    pid, slug, hook, body, q, tags, cat = post
    limit = PLATFORMS[platform]["tag_limit"]
    cap = PLATFORMS[platform]["char_cap"]

    branded = ["Skynetlabs","Waseemnasir","NomadCEO"]
    chosen = (branded + tags)[:limit]
    ht = " ".join("#"+t for t in chosen)

    if platform == "Instagram":
        caption = f"{hook}\n\n{body}\n\n{q} ⬇️\n\n{NOTE}\n\n{ht}"
    elif platform == "LinkedIn":
        caption = f"{hook}\n\n{body}\n\n{q}\n\n{NOTE}\n\n{ht}"
    elif platform == "Facebook":
        caption = f"{hook}\n\n{body}\n\n{q} 👇\n\n{NOTE}\n\n{ht}"
    elif platform == "Twitter":
        short = f"{hook}\n\n{q}"
        if len(short) + len(ht) + 2 > 270:
            short = hook[:250] + "…"
        caption = f"{short}\n\n{ht}"
    elif platform == "Pinterest":
        caption = f"{hook} — {body} {q} Designed by Claude Code, auto-published via GoHighLevel + n8n. {ht}"
    return caption[:cap]

def build_first_comment(post):
    pid, slug, hook, body, q, tags, cat = post
    url = f"https://skynetjoe.com/?utm_source=social&utm_medium=post&utm_campaign=batch2&utm_content={slug}"
    return f"More systems like this → {url}\n\nDrop questions below, I reply to every one. — Waseem"

def build_alt(post):
    pid, slug, hook, body, q, tags, cat = post
    return f"Waseem Nasir premium social post: {hook} Nomad CEO brand · Skynetlabs · designed by Claude Code · automated via GoHighLevel and n8n."

rows = []
for i, post in enumerate(POSTS):
    pid, slug, hook, body, q, tags, cat = post
    day = START + timedelta(days=i)
    date_str = day.strftime("%m/%d/%Y")
    image_file = f"{slug}.png"
    image_url = f"{CDN_PLACEHOLDER}/{image_file}"
    for platform, cfg in PLATFORMS.items():
        rows.append({
          "post_id": f"{pid:02d}",
          "seo_slug": slug,
          "image_file": image_file,
          "image_url": image_url,
          "platform": platform,
          "scheduled_date": date_str,
          "scheduled_time": cfg["time"],
          "caption": build_caption(platform, post),
          "first_comment": build_first_comment(post) if cfg["first_comment_supported"] else "",
          "alt_text": build_alt(post),
          "engagement_question": q,
          "category": cat,
          "utm_source": "ghl",
          "utm_medium": platform.lower(),
          "utm_campaign": "batch2-viral-20",
          "utm_content": slug,
        })

fields = ["post_id","seo_slug","image_file","image_url","platform","scheduled_date","scheduled_time",
          "caption","first_comment","alt_text","engagement_question","category",
          "utm_source","utm_medium","utm_campaign","utm_content"]
with OUT.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
    w.writeheader()
    w.writerows(rows)

# Also write simple GHL-import-only CSV (4 core columns)
SIMPLE = Path(__file__).parent / "ghl-batch2-simple-import.csv"
with SIMPLE.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(["Post Date","Post Time","Channel","Post Content","Media URL","First Comment"])
    for r in rows:
        w.writerow([r["scheduled_date"], r["scheduled_time"], r["platform"], r["caption"], r["image_url"], r["first_comment"]])

print(f"wrote {OUT} ({len(rows)} rows)")
print(f"wrote {SIMPLE} (simple GHL format)")
print(f"\nposts: {len(POSTS)} | platforms: {len(PLATFORMS)} | total rows: {len(rows)}")
print("\nschedule: 20 days starting", START)
print("\nreplace [GHL_CDN_URL] after uploading PNGs to GHL Media Library.")
