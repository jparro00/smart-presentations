"""
Generate narrated audio for each slide — v2 with SSML prosody.
Uses AndrewMultilingualNeural with strategic pauses and pacing.
"""

import asyncio
import os
import edge_tts

VOICE = "en-US-AndrewMultilingualNeural"
RATE = "-8%"
PITCH = "-2Hz"
OUTPUT_DIR = "presentations/narration"

# SSML-enhanced scripts with natural pauses and emphasis
# Use ... for sentence breaks, and structure phrases for natural delivery
SLIDES = [
    {
        "file": "slide-01.mp3",
        "script": (
            "Thank you for joining. "
            "Today I want to talk about something that's reshaping the cybersecurity landscape, "
            "in ways most organizations aren't prepared for. "
            "... "
            "We're seeing three forces converge at the same time. "
            "The rapid deployment of frontier AI models. "
            "An explosion of non-human identities driven by AI agents. "
            "And a shift to attacks that move at machine speed. "
            "... "
            "Each of these is significant on its own. "
            "But together? They're creating a threat landscape that our traditional "
            "security models were never designed to handle. "
            "... "
            "This is our point of view on what's happening, why it matters, "
            "and what organizations need to do about it."
        ),
    },
    {
        "file": "slide-02.mp3",
        "script": (
            "Let me frame the three forces we're tracking. "
            "... "
            "First, frontier model risks. "
            "These are the most capable AI systems — GPT-4, Claude, Gemini — "
            "and they bring a fundamentally new category of security risk. "
            "They're non-deterministic. They're opaque. "
            "And they have structural vulnerabilities like prompt injection "
            "that cannot be patched in the traditional sense. "
            "... "
            "Second, the NHI explosion. "
            "Every AI agent an organization deploys creates new non-human identities. "
            "API keys. OAuth tokens. Service accounts. "
            "These now outnumber human identities by fifty to five hundred x "
            "in modern enterprises. "
            "And ninety-seven percent of them have excessive privileges, "
            "with almost no governance. "
            "... "
            "Third, machine-speed threats. "
            "AI-powered attacks are compressing kill chains from hours to seconds. "
            "We saw the first confirmed cases of fully autonomous attack campaigns in 2025, "
            "with eighty to ninety percent running without human intervention. "
            "... "
            "Our core thesis, and the red thread through this entire deck, "
            "is that identity is now the primary control plane for AI-era security. "
            "... "
            "Not the network perimeter. Not the endpoint. "
            "Identity."
        ),
    },
    {
        "file": "slide-03.mp3",
        "script": (
            "Let's start by understanding the threat landscape. "
            "... "
            "What makes this moment different from anything we've seen before."
        ),
    },
    {
        "file": "slide-04.mp3",
        "script": (
            "This comparison is critical. "
            "Because it explains why our existing security playbooks "
            "don't work for AI systems. "
            "... "
            "Traditional software is deterministic. Same input, same output. "
            "You can audit the source code. "
            "When you find a vulnerability, you write a patch, and it's fixed. "
            "There are clear boundaries between what's an instruction and what's data. "
            "... "
            "Frontier AI models break every one of those assumptions. "
            "... "
            "Outputs vary unpredictably. "
            "The reasoning is embedded in billions of parameters that can't be "
            "meaningfully inspected. There's no source code to review. "
            "When you find a vulnerability like a jailbreak technique, "
            "the fix is retraining, or adding guardrails. "
            "Both of which are probabilistic. "
            "They reduce the problem. They don't eliminate it. "
            "... "
            "And crucially, instructions and data share the same channel. "
            "Which is what makes prompt injection a structural problem. "
            "Not just a bug. "
            "... "
            "This isn't an incremental change. "
            "It's a paradigm shift in what securing software means."
        ),
    },
    {
        "file": "slide-05.mp3",
        "script": (
            "Here's the slide I want everyone to sit with for a moment. "
            "... "
            "... "
            "The biggest security risk with frontier models "
            "isn't a technical vulnerability. "
            "It's the assumption, that the AI knows what it's doing. "
            "... "
            "That's the mythos. "
            "... "
            "Organizations anthropomorphize these systems. "
            "They name them. They call them assistants. "
            "They treat them like trusted colleagues. "
            "Users share sensitive data without thinking twice. "
            "Teams deploy models without consulting security, because, "
            "quote, it's just an API call. "
            "Vendor claims about safety training are accepted at face value. "
            "... "
            "The data tells the story. "
            "Only thirty-four percent of enterprises have AI-specific "
            "security controls in place. "
            "... "
            "That means two-thirds of organizations are deploying frontier models "
            "with no adversarial testing. No threat model. No governance. "
            "They're flying blind. And confident about it. "
            "... "
            "Closing this gap between perceived and actual security posture "
            "is foundational to everything else we'll discuss."
        ),
    },
    {
        "file": "slide-06.mp3",
        "script": (
            "Let me put numbers to the attack surface. "
            "... "
            "Prompt injection attacks surged three hundred and forty percent "
            "year over year in Q4 2025. "
            "And critically, over eighty percent of those attacks are now indirect. "
            "Meaning the malicious instructions aren't coming from the user. "
            "They're embedded in documents, emails, web pages, and database records "
            "that the AI processes. "
            "The user never sees the attack. "
            "... "
            "Every tool integration, email, file storage, databases, code execution, "
            "multiplies the impact of a successful attack by three to five x. "
            "If an agent can read your email, and send email, and access your files, "
            "a single prompt injection can chain all three. "
            "... "
            "On the supply chain side, researchers have shown that poisoning "
            "just one hundredth of a percent of training data "
            "is enough to install reliable backdoors. "
            "And because a small number of providers supply the foundation models "
            "for thousands of downstream applications, "
            "a single vulnerability has ecosystem-wide blast radius. "
            "... "
            "The bottom line. "
            "Prompt injection is the new SQL injection. "
            "But unlike SQL injection, there is no parameterized query equivalent. "
            "Every defense is probabilistic."
        ),
    },
    {
        "file": "slide-07.mp3",
        "script": (
            "Now let's connect these model-level risks to the identity layer. "
            "... "
            "Because this is where the operational impact really hits."
        ),
    },
    {
        "file": "slide-08.mp3",
        "script": (
            "These four numbers frame the scale of the problem. "
            "... "
            "Non-human identities now outnumber human identities "
            "by fifty to five hundred x in enterprise environments. "
            "Every AI agent creates a cluster of NHIs. "
            "API keys for the model provider. OAuth tokens for SaaS integrations. "
            "Service accounts for data access. Bearer tokens for inter-agent communication. "
            "... "
            "Ninety-seven percent of these NHIs have excessive privileges. "
            "They're created for a project, given broad access to get things working, "
            "and never scoped down. Never rotated. Never revoked. "
            "... "
            "Only twelve percent of organizations report high confidence "
            "in their ability to prevent NHI-related attacks. "
            "And fewer than one in four have formally documented policies "
            "for creating or removing AI identities. "
            "... "
            "This is the governance gap. "
            "And it's growing faster than organizations can close it."
        ),
    },
    {
        "file": "slide-09.mp3",
        "script": (
            "The natural question is, "
            "don't we already have IAM and PAM programs for this? "
            "... "
            "The answer is no. "
            "And the gap is structural, not incremental. "
            "... "
            "Traditional IAM was built for human users. "
            "Authentication events measured in minutes. "
            "Static role definitions mapped to job functions. "
            "Quarterly access reviews conducted by managers. "
            "Ninety-day credential rotation policies. "
            "... "
            "AI agents operate in a completely different regime. "
            "They authenticate thousands of times per second across dozens of services. "
            "They need dynamic, context-dependent permissions that change with every task. "
            "When you have fifty x more identities than humans, "
            "manual quarterly reviews are physically impossible. "
            "And agent credentials need sub-minute lifetimes "
            "with just-in-time provisioning. "
            "... "
            "You cannot bolt AI identity governance onto a system designed for humans. "
            "You need a purpose-built approach."
        ),
    },
    {
        "file": "slide-10.mp3",
        "script": (
            "Here's how these risks play out in practice. The NHI kill chain. "
            "... "
            "It starts with credential compromise. "
            "A leaked API key in a code repository. A hardcoded token. "
            "A compromised OAuth integration. "
            "... "
            "From there, lateral movement happens at machine speed. "
            "A single compromised agent credential provides access "
            "to every tool and service that agent is connected to. "
            "Email. File storage. Databases. APIs. "
            "All at once. All instantly. "
            "... "
            "Privilege escalation happens through delegation chains. "
            "AI agents act on behalf of users, inheriting their permissions. "
            "Compromise the agent, and you effectively gain the permissions "
            "of every user who delegates to it. "
            "... "
            "Persistence is trivial, because NHI credentials are long-lived. "
            "Zombie secrets, leaked credentials that were never rotated, "
            "remain valid for months. Or years. "
            "... "
            "And finally, exfiltration happens at API speed. "
            "Gigabytes per minute. "
            "Faster than any DLP system designed for human-paced data theft. "
            "... "
            "The Salesloft Drift incident in 2025 illustrated this perfectly. "
            "Compromised OAuth tokens connecting SaaS platforms "
            "gave attackers access to hundreds of downstream customer environments. "
            "Blast radius, ten x greater than a typical human credential breach."
        ),
    },
    {
        "file": "slide-11.mp3",
        "script": (
            "This is the fundamental problem we need to internalize. "
            "... "
            "... "
            "Attackers are operating at machine speed. "
            "Defenders are still operating at human speed. "
            "... "
            "Eighty to ninety percent of attack campaigns now run autonomously. "
            "A SOC analyst takes fifteen minutes to triage an alert. "
            "In that time, an AI-powered attack has already completed its objective. "
            "Enumerated systems. Moved laterally. Exfiltrated data. "
            "And covered its tracks. "
            "... "
            "AI agents outnumber humans eighty-two to one in hybrid workforces. "
            "This isn't a future prediction. This is the current state. "
            "And it creates an unprecedented speed advantage for adversaries. "
            "... "
            "The implication is clear. "
            "You cannot defend against machine-speed attacks "
            "with human-speed processes. "
            "The defense has to match the speed of the threat."
        ),
    },
    {
        "file": "slide-12.mp3",
        "script": (
            "So, what do we do about it? "
            "... "
            "Here's our point of view."
        ),
    },
    {
        "file": "slide-13.mp3",
        "script": (
            "Our point of view rests on four pillars. "
            "... "
            "First. Zero Trust for AI agents. "
            "Never trust implicitly. "
            "Every agent action, not just the initial authentication, "
            "but every subsequent action, "
            "must be authenticated, authorized, and auditable. "
            "The CSA Agentic Trust Framework and NIST's AI Agent Standards Initiative "
            "both landed in early 2026 with exactly this guidance. "
            "Continuous verification at every action. Not just session establishment. "
            "... "
            "Second. Machine-speed detection. "
            "We need behavioral baselines for every agent identity. "
            "When an agent starts accessing new services, "
            "making API calls at unusual volumes, "
            "or communicating with unexpected endpoints, "
            "automated systems need to detect and respond in seconds. "
            "Revoke credentials. Isolate the agent. Block further actions. "
            "Not minutes. Seconds. "
            "... "
            "Third. Dedicated NHI governance. "
            "AI agents are a distinct identity class that needs its own governance program. "
            "An AI identity registry with full lifecycle management. "
            "Just-in-time secret provisioning. "
            "Automated continuous access reviews, "
            "replacing quarterly human reviews. "
            "Because manual review at fifty x scale is simply not feasible. "
            "... "
            "And fourth. Microsegmentation and blast radius containment. "
            "Confine every agent to the minimum tools and data "
            "required for its current task. "
            "Enforce those boundaries at the infrastructure level. "
            "Not by relying on the agent's own instructions. "
            "Assume compromise. "
            "Design so that no single credential unlocks the environment."
        ),
    },
    {
        "file": "slide-14.mp3",
        "script": (
            "Let me leave you with three concrete imperatives. "
            "... "
            "First. Treat AI as untrusted infrastructure. "
            "Conduct adversarial red-teaming against every AI deployment. "
            "Prompt injection testing. Tool abuse scenarios. "
            "Data exfiltration paths. "
            "Implement defense-in-depth. "
            "And critically, inventory your shadow AI. "
            "Sixty-six percent of enterprises have AI systems deployed "
            "by individual teams, with no security oversight. "
            "You can't govern what you can't see. "
            "... "
            "Second. Build dedicated NHI governance. "
            "Establish an AI identity registry that catalogs every agent, "
            "every credential, every tool integration, every delegation chain. "
            "Mandate automated lifecycle management. "
            "No long-lived secrets. No orphaned service accounts. "
            "Define autonomy levels matched to risk, "
            "with human-in-the-loop gates for high-impact actions. "
            "... "
            "And third. Prepare for the regulatory wave. "
            "NIST is developing SP 800-53 control overlays "
            "specifically for AI agent use cases. "
            "The EU AI Act mandates governance for frontier models. "
            "Gartner predicts seventy percent of CISOs "
            "will deploy identity intelligence capabilities by 2028. "
            "The question isn't whether governance will be required. "
            "It's whether you build it proactively, "
            "or retrofit it under regulatory pressure. "
            "... "
            "The organizations that move now will lead. "
            "The ones that wait, will be catching up."
        ),
    },
    {
        "file": "slide-15.mp3",
        "script": (
            "Thank you. "
            "... "
            "We believe identity is the control plane for AI-era security. "
            "And the organizations that recognize this, and act on it, "
            "will be the resilient ones. "
            "... "
            "I'm happy to take questions, "
            "or discuss how any of this applies to your specific environment."
        ),
    },
]


async def generate_slide_audio(slide, output_dir):
    """Generate MP3 for a single slide using SSML-style pacing."""
    path = os.path.join(output_dir, slide["file"])
    print(f"  Generating {slide['file']}...")
    communicate = edge_tts.Communicate(
        slide["script"],
        VOICE,
        rate=RATE,
        pitch=PITCH,
    )
    await communicate.save(path)
    return path


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Voice: {VOICE} | Rate: {RATE} | Pitch: {PITCH}\n")

    for slide in SLIDES:
        await generate_slide_audio(slide, OUTPUT_DIR)

    print(f"\nDone! {len(SLIDES)} files regenerated in {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
