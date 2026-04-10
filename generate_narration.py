"""
Generate narrated audio for each slide of the Frontier Models presentation.
Uses Microsoft Edge neural TTS (free, high quality, no API key needed).

Usage:
    python generate_narration.py

Output:
    presentations/narration/slide-01.mp3 through slide-15.mp3
    presentations/narration/full-narration.html  (auto-advancing player)
"""

import asyncio
import os
import edge_tts

# Voice: en-US-GuyNeural is a professional male voice
# Other good options: en-US-AriaNeural (female), en-US-DavisNeural (male, deeper)
VOICE = "en-US-GuyNeural"
OUTPUT_DIR = "presentations/narration"

# Speaker script for each slide (cleaned for TTS - no markdown formatting)
SLIDES = [
    {
        "file": "slide-01.mp3",
        "title": "Title",
        "script": (
            "Thank you for joining. Today I want to talk about something that's "
            "reshaping the cybersecurity landscape in ways most organizations aren't prepared for. "
            "We're seeing three forces converge at the same time: the rapid deployment of frontier "
            "AI models, an explosion of non-human identities driven by AI agents, and a shift to "
            "attacks that move at machine speed. Each of these is significant on its own, but "
            "together, they're creating a threat landscape that our traditional security models "
            "were never designed to handle. This is our point of view on what's happening, why "
            "it matters, and what organizations need to do about it."
        ),
    },
    {
        "file": "slide-02.mp3",
        "title": "Three Converging Forces",
        "script": (
            "Let me frame the three forces we're tracking. "
            "First: frontier model risks. These are the most capable AI systems, GPT-4, Claude, "
            "Gemini, and they bring a fundamentally new category of security risk. They're "
            "non-deterministic, opaque, and have structural vulnerabilities like prompt injection "
            "that cannot be patched in the traditional sense. "
            "Second: the NHI explosion. Every AI agent an organization deploys creates new "
            "non-human identities: API keys, OAuth tokens, service accounts. These now outnumber "
            "human identities by 50 to 500x in modern enterprises. And 97% of them have excessive "
            "privileges with almost no governance. "
            "Third: machine-speed threats. AI-powered attacks are compressing kill chains from "
            "hours to seconds. We saw the first confirmed cases of fully autonomous attack "
            "campaigns in 2025, with 80 to 90 percent running without human intervention. "
            "Our core thesis, and the red thread through this entire deck, is that identity is "
            "now the primary control plane for AI-era security. Not the network perimeter. "
            "Not the endpoint. Identity."
        ),
    },
    {
        "file": "slide-03.mp3",
        "title": "Divider: The Threat Landscape",
        "script": (
            "Let's start by understanding the threat landscape, and what makes this moment "
            "different from anything we've seen before."
        ),
    },
    {
        "file": "slide-04.mp3",
        "title": "Frontier Models: A New Risk Class",
        "script": (
            "This comparison is critical, because it explains why our existing security playbooks "
            "don't work for AI systems. "
            "Traditional software is deterministic: same input, same output. You can audit the "
            "source code. When you find a vulnerability, you write a patch and it's fixed. There "
            "are clear boundaries between what's an instruction and what's data. "
            "Frontier AI models break every one of those assumptions. Outputs vary unpredictably. "
            "The reasoning is embedded in billions of parameters that can't be meaningfully "
            "inspected. There's no source code to review. When you find a vulnerability like a "
            "jailbreak technique, the fix is retraining or adding guardrails, both of which are "
            "probabilistic. They reduce the problem but don't eliminate it. "
            "And crucially, instructions and data share the same channel, which is what makes "
            "prompt injection a structural problem, not just a bug. "
            "This isn't an incremental change. It's a paradigm shift in what securing software means."
        ),
    },
    {
        "file": "slide-05.mp3",
        "title": "The Mythos Gap",
        "script": (
            "Here's the slide I want everyone to sit with for a moment. "
            "The biggest security risk with frontier models isn't a technical vulnerability. "
            "It's the assumption that the AI knows what it's doing. That's the mythos. "
            "Organizations anthropomorphize these systems. They name them, they call them "
            "assistants, they treat them like trusted colleagues. Users share sensitive data "
            "without thinking twice. Teams deploy models without consulting security because "
            "it's just an API call. Vendor claims about safety training are accepted at face value. "
            "The data tells the story: only 34 percent of enterprises have AI-specific security "
            "controls in place. That means two-thirds of organizations are deploying frontier "
            "models with no adversarial testing, no threat model, no governance. "
            "They're flying blind, and confident about it. "
            "Closing this gap between perceived and actual security posture is foundational "
            "to everything else we'll discuss."
        ),
    },
    {
        "file": "slide-06.mp3",
        "title": "Novel Attack Surfaces",
        "script": (
            "Let me put numbers to the attack surface. "
            "Prompt injection attacks surged 340 percent year-over-year in Q4 2025. And critically, "
            "over 80 percent of those attacks are now indirect. Meaning the malicious instructions "
            "aren't coming from the user. They're embedded in documents, emails, web pages, and "
            "database records that the AI processes. The user never sees the attack. "
            "Every tool integration, email, file storage, databases, code execution, multiplies "
            "the impact of a successful attack by 3 to 5x. If an agent can read your email AND "
            "send email AND access your files, a single prompt injection can chain all three. "
            "On the supply chain side, researchers have shown that poisoning just one hundredth "
            "of a percent of training data is enough to install reliable backdoors. And because "
            "a small number of providers supply the foundation models for thousands of downstream "
            "applications, a single vulnerability has ecosystem-wide blast radius. "
            "The bottom line: prompt injection is the new SQL injection, but unlike SQL injection, "
            "there is no parameterized query equivalent. Every defense is probabilistic."
        ),
    },
    {
        "file": "slide-07.mp3",
        "title": "Divider: The Identity Crisis",
        "script": (
            "Now let's connect these model-level risks to the identity layer. "
            "Because this is where the operational impact really hits."
        ),
    },
    {
        "file": "slide-08.mp3",
        "title": "The NHI Explosion",
        "script": (
            "These four numbers frame the scale of the problem. "
            "Non-human identities now outnumber human identities by 50 to 500x in enterprise "
            "environments. Every AI agent creates a cluster of NHIs: API keys for the model "
            "provider, OAuth tokens for SaaS integrations, service accounts for data access, "
            "bearer tokens for inter-agent communication. "
            "97 percent of these NHIs have excessive privileges. They're created for a project, "
            "given broad access to get things working, and never scoped down, rotated, or revoked. "
            "Only 12 percent of organizations report high confidence in their ability to prevent "
            "NHI-related attacks. And fewer than one in four have formally documented policies "
            "for creating or removing AI identities. "
            "This is the governance gap. And it's growing faster than organizations can close it."
        ),
    },
    {
        "file": "slide-09.mp3",
        "title": "Why Traditional IAM Falls Short",
        "script": (
            "The natural question is: don't we already have IAM and PAM programs for this? "
            "The answer is no, and the gap is structural, not incremental. "
            "Traditional IAM was built for human users. Authentication events measured in minutes. "
            "Static role definitions mapped to job functions. Quarterly access reviews conducted "
            "by managers. 90-day credential rotation policies. "
            "AI agents operate in a completely different regime. They authenticate thousands of "
            "times per second across dozens of services. They need dynamic, context-dependent "
            "permissions that change with every task. When you have 50x more identities than "
            "humans, manual quarterly reviews are physically impossible. And agent credentials "
            "need sub-minute lifetimes with just-in-time provisioning. "
            "You cannot bolt AI identity governance onto a system designed for humans. "
            "You need a purpose-built approach."
        ),
    },
    {
        "file": "slide-10.mp3",
        "title": "The NHI Kill Chain",
        "script": (
            "Here's how these risks play out in practice. The NHI kill chain. "
            "It starts with credential compromise: a leaked API key in a code repository, "
            "a hardcoded token, a compromised OAuth integration. This is the initial access vector. "
            "From there, lateral movement happens at machine speed. A single compromised agent "
            "credential provides access to every tool and service that agent is connected to: "
            "email, file storage, databases, APIs, all at once, all instantly. "
            "Privilege escalation happens through delegation chains. AI agents act on behalf of "
            "users, inheriting their permissions. Compromise the agent, and you effectively gain "
            "the permissions of every user who delegates to it. "
            "Persistence is trivial because NHI credentials are long-lived. Zombie secrets, "
            "leaked credentials that were never rotated, remain valid for months or years. "
            "Finally, exfiltration happens at API speed. Gigabytes per minute, faster than any "
            "DLP system designed for human-paced data theft. "
            "The Salesloft-Drift incident in 2025 illustrated this perfectly. Compromised OAuth "
            "tokens connecting SaaS platforms gave attackers access to hundreds of downstream "
            "customer environments. Blast radius 10x greater than a typical human credential breach."
        ),
    },
    {
        "file": "slide-11.mp3",
        "title": "The Speed Asymmetry",
        "script": (
            "This is the fundamental problem we need to internalize. "
            "Attackers are operating at machine speed. Defenders are still operating at human speed. "
            "80 to 90 percent of attack campaigns now run autonomously. A SOC analyst takes "
            "15 minutes to triage an alert. In that time, an AI-powered attack has already "
            "completed its objective: enumerated systems, moved laterally, exfiltrated data, "
            "and covered its tracks. "
            "AI agents outnumber humans 82 to 1 in hybrid workforces. This isn't a future "
            "prediction. This is the current state. And it creates an unprecedented speed "
            "advantage for adversaries. "
            "The implication is clear: you cannot defend against machine-speed attacks with "
            "human-speed processes. The defense has to match the speed of the threat."
        ),
    },
    {
        "file": "slide-12.mp3",
        "title": "Divider: Our Point of View",
        "script": (
            "So what do we do about it? Here's our point of view."
        ),
    },
    {
        "file": "slide-13.mp3",
        "title": "Identity as the Control Plane",
        "script": (
            "Our point of view rests on four pillars. "
            "First, Zero Trust for AI agents. Never trust implicitly. Every agent action, not just "
            "the initial authentication, but every subsequent action, must be authenticated, "
            "authorized, and auditable. The CSA Agentic Trust Framework and NIST's AI Agent "
            "Standards Initiative both landed in early 2026 with exactly this guidance. "
            "Continuous verification at every action, not just session establishment. "
            "Second, machine-speed detection. We need behavioral baselines for every agent "
            "identity. When an agent starts accessing new services, making API calls at unusual "
            "volumes, or communicating with unexpected endpoints, automated systems need to "
            "detect and respond in seconds. Revoke credentials, isolate the agent, block further "
            "actions. Not minutes. Seconds. "
            "Third, dedicated NHI governance. AI agents are a distinct identity class that needs "
            "its own governance program. An AI identity registry with full lifecycle management. "
            "Just-in-time secret provisioning. Automated continuous access reviews replacing "
            "quarterly human reviews, because manual review at 50x scale is not feasible. "
            "Fourth, microsegmentation and blast radius containment. Confine every agent to the "
            "minimum tools and data required for its current task. Enforce those boundaries at "
            "the infrastructure level, not by relying on the agent's own instructions. "
            "Assume compromise. Design so that no single credential unlocks the environment."
        ),
    },
    {
        "file": "slide-14.mp3",
        "title": "The Path Forward",
        "script": (
            "Let me leave you with three concrete imperatives. "
            "First: treat AI as untrusted infrastructure. Conduct adversarial red-teaming against "
            "every AI deployment. Prompt injection testing, tool abuse scenarios, data exfiltration "
            "paths. Implement defense-in-depth. And critically, inventory your shadow AI. "
            "66 percent of enterprises have AI systems deployed by individual teams with no "
            "security oversight. You can't govern what you can't see. "
            "Second: build dedicated NHI governance. Establish an AI identity registry that "
            "catalogs every agent, every credential, every tool integration, every delegation "
            "chain. Mandate automated lifecycle management. No long-lived secrets, no orphaned "
            "service accounts. Define autonomy levels matched to risk, with human-in-the-loop "
            "gates for high-impact actions. "
            "Third: prepare for the regulatory wave. NIST is developing SP 800-53 control "
            "overlays specifically for AI agent use cases. The EU AI Act mandates governance for "
            "frontier models. Gartner predicts 70 percent of CISOs will deploy identity "
            "intelligence capabilities by 2028. The question isn't whether governance will be "
            "required. It's whether you build it proactively or retrofit it under regulatory pressure. "
            "The organizations that move now will lead. The ones that wait will be catching up."
        ),
    },
    {
        "file": "slide-15.mp3",
        "title": "Closing",
        "script": (
            "Thank you. We believe identity is the control plane for AI-era security, "
            "and the organizations that recognize this, and act on it, will be the resilient ones. "
            "I'm happy to take questions or discuss how any of this applies to your specific environment."
        ),
    },
]


async def generate_slide_audio(slide, output_dir):
    """Generate MP3 for a single slide."""
    path = os.path.join(output_dir, slide["file"])
    print(f"  Generating {slide['file']} — {slide['title']}...")
    communicate = edge_tts.Communicate(slide["script"], VOICE, rate="-5%", pitch="+0Hz")
    await communicate.save(path)
    return path


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Generating narration with voice: {VOICE}")
    print(f"Output: {OUTPUT_DIR}/\n")

    for slide in SLIDES:
        await generate_slide_audio(slide, OUTPUT_DIR)

    print(f"\nDone! {len(SLIDES)} audio files generated in {OUTPUT_DIR}/")
    print("\nTo play: open each MP3 as you advance slides,")
    print("or open the auto-player: presentations/narration/player.html")

    # Generate a simple HTML player
    player_html = """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Narration Player</title>
<style>
body { font-family: 'Open Sans', Arial, sans-serif; background: #1c1b1c; color: #fff; padding: 40px; max-width: 800px; margin: 0 auto; }
h1 { color: #86BC25; font-size: 1.4rem; margin-bottom: 24px; }
.slide-row { display: flex; align-items: center; gap: 16px; padding: 12px 16px; border-bottom: 1px solid rgba(255,255,255,0.08); }
.slide-row:hover { background: rgba(255,255,255,0.04); }
.slide-num { color: #86EB22; font-weight: bold; min-width: 36px; }
.slide-title { flex: 1; }
audio { height: 32px; }
.play-all { background: #86BC25; color: #000; border: none; padding: 10px 24px; font-weight: bold; cursor: pointer; border-radius: 4px; margin-bottom: 24px; font-size: 0.9rem; }
.play-all:hover { background: #86EB22; }
.now-playing { background: rgba(134,235,34,0.1); }
</style></head><body>
<h1>Presentation Narration Player</h1>
<button class="play-all" onclick="playAll()">Play All (Auto-Advance)</button>
<div id="slides">"""

    for i, slide in enumerate(SLIDES):
        player_html += f"""
  <div class="slide-row" id="row-{i}">
    <span class="slide-num">{i+1}</span>
    <span class="slide-title">{slide['title']}</span>
    <audio id="audio-{i}" src="{slide['file']}" preload="none" controls></audio>
  </div>"""

    player_html += """
</div>
<script>
let currentSlide = 0;
let autoPlaying = false;

function playAll() {
  autoPlaying = true;
  currentSlide = 0;
  playSlide(0);
}

function playSlide(n) {
  document.querySelectorAll('.slide-row').forEach(r => r.classList.remove('now-playing'));
  if (n >= """ + str(len(SLIDES)) + """) { autoPlaying = false; return; }
  const row = document.getElementById('row-' + n);
  const audio = document.getElementById('audio-' + n);
  row.classList.add('now-playing');
  row.scrollIntoView({ behavior: 'smooth', block: 'center' });
  audio.play();
  audio.onended = () => {
    if (autoPlaying) playSlide(n + 1);
  };
}
</script></body></html>"""

    player_path = os.path.join(OUTPUT_DIR, "player.html")
    with open(player_path, "w", encoding="utf-8") as f:
        f.write(player_html)
    print(f"Player generated: {player_path}")


if __name__ == "__main__":
    asyncio.run(main())
