"""
Playwright PNG render — guaranteed 1080x1350 per post.
Usage: python render_all.py
Output: ./png/waseem-viral-XX-NAME.png (20 files)
"""
import asyncio, os, sys
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).parent
HTML = HERE / "PREVIEW.html"
OUT = HERE / "png"
OUT.mkdir(exist_ok=True)

TITLES = {
    1:"ai-agent-hire-2026-waseem-nasir-nomad-ceo",
    2:"sleep-8-hours-agents-work-24-ai-automation",
    3:"busy-vs-productive-founder-leverage-2026",
    4:"more-agents-not-more-hours-ai-automation",
    5:"todo-list-ai-prompt-list-n8n-workflow",
    6:"linkedin-free-personal-brand-growth-2026",
    7:"ship-ugly-iterate-public-founder-rule-01",
    8:"client-2am-ai-video-automation-remotion",
    9:"skill-stack-beats-degree-stack-2026",
    10:"charge-5k-2-hours-freelance-pricing-strategy",
    11:"cold-email-vs-ai-dms-14-percent-outreach",
    12:"ai-wont-replace-you-people-using-ai-will",
    13:"stop-learning-start-shipping-builder-mindset",
    14:"n8n-51-nodes-vs-excel-workflow-automation",
    15:"agents-leverage-squared-solo-founder-50k",
    16:"25-digital-products-sold-bali-nomad-ceo",
    17:"prompt-engineering-skill-2026-future-work",
    18:"upwork-dead-outbound-lead-gen-freelancer",
    19:"ai-orchestration-8-projects-one-day-founder",
    20:"built-bali-sold-new-york-remote-nomad-ceo"
}

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(args=["--allow-file-access-from-files"])
        ctx = await browser.new_context(viewport={"width":1200,"height":1500}, device_scale_factor=2)
        page = await ctx.new_page()
        await page.goto(HTML.as_uri())
        await page.wait_for_load_state("networkidle")
        # Inject CSS to unscale all posts to native 1080x1350
        await page.add_style_tag(content="""
            .post{width:1080px !important;height:1350px !important;overflow:visible !important;box-shadow:none !important;margin:0 !important;border-radius:0 !important}
            .scale{transform:scale(1) !important;width:1080px !important;height:1350px !important}
        """)
        await page.wait_for_timeout(1000)

        for n, name in TITLES.items():
            el = page.locator(f"#p{n}")
            await el.wait_for(state="visible")
            path = OUT / f"waseem-viral-{name}.png"
            await el.screenshot(path=str(path), omit_background=False)
            print(f"[{n:02d}/20] {name}.png")

        await browser.close()
    print(f"\ndone. {len(TITLES)} PNGs in {OUT}")

if __name__ == "__main__":
    asyncio.run(main())
