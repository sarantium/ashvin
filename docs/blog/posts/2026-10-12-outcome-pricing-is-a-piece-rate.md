---
title: "Outcome pricing is a piece rate"
date: 2026-10-12
description: "Per seat, per token and per outcome are a salary, an hourly wage and a piece rate. Labour economics knows when piece rates work, and that decides where outcome pricing will hold."
tags:
  - ai
  - economics
  - business-models
  - future-of-work
---

Metronome's [pricing levers page](https://metronome.com/pricing-levers) sets out the choices a software company makes when it prices a product. There are five levers: the metric it charges for, the structure of its tiers, the commercial model, the incentives, and how it charges for support. Most of the argument about AI pricing is about the first lever, and its options sound new: per seat, per token, per outcome. They are three old ways of paying for work. A seat is a salary, a token is an hourly wage, and an outcome is a piece rate.

![A table pairing three ways people are paid with three ways software is priced: salary with per seat (Jira), hourly wage with per token (OpenAI API), and piece rate with per outcome (Intercom Fin). Below it, who carries the risk. If the job takes longer, the seller pays under a salary or a piece rate and the buyer pays under an hourly wage. If the job fails, the buyer pays under a salary or an hourly wage, and the seller pays only under a piece rate.](../blog_assets/outcome_pricing_pay_forms.png)

The bottom rows of the figure show what each form does with risk. A salary and a piece rate both leave the seller to absorb a job that runs long, but only a piece rate also leaves the seller to absorb a job that fails. Labour economics has studied all three forms for decades, and it knows when piece rates work: when the job can be counted, when bad work can be seen, and when the worker has a floor under the slow weeks. Those conditions will decide where outcome pricing holds. One more lever, the commercial model, comes back at the end, where it turns out to manage the risk the metric creates; tiers, incentives and support pricing stay out of this post.

<!-- more -->

## Seats are salaries, and inference cost broke them

A salary pays for being there. The employer pays the same in a quiet week as in a frantic one, so the worker absorbs the long weeks and the employer absorbs the risk that little gets done. Seat pricing makes the same trade. The customer pays per user per month, and the vendor absorbs whatever that user does.

For two decades that trade cost software vendors very little, because serving one more click on a web app cost almost nothing. AI ended that: every request now runs a model, and what a request costs depends on how hard it is. When Cursor changed its pricing in 2025, it said that "the hardest requests cost an order of magnitude more than simple ones" ([Cursor](https://cursor.com/blog/june-2025-pricing)). A seat priced for the average user loses money on the heaviest one. In July 2025 Anthropic announced weekly limits for its Claude subscriptions, because some subscribers were running Claude Code "continuously in the background, 24/7" ([TechCrunch](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/)).

A vendor in that position has the choices an employer has with a salaried worker who costs too much: ration the work, or start paying for it by the unit. Anthropic's limits are the first. GitHub chose the second. From 1 June 2026 every Copilot plan includes a monthly allowance of AI credits, consumed by tokens at the published API rates ([GitHub](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)). The seat survives, but as an allowance of credit that the user draws down, which Metronome's map files under the commercial model (prepaid credits) rather than the metric. Cost explains why the salary broke, but it leaves open what should replace it.

## Tokens are hourly wages, so the buyer carries both risks

An hourly wage pays for time worked. The worker is safe, since a job that runs long pays more, and the employer carries both risks: the long job and the failed one. Per-token pricing makes the same trade. The OpenAI API bills for input and output tokens whether or not the answer was any good, and a task that takes ten times the tokens costs ten times as much.

Hourly pay rewards time spent, so a contractor who finds a faster way to do a job earns less for doing it. Token pricing carries the same incentive. A vendor whose agent learns to finish a task in 20,000 tokens instead of 100,000 has done better work and now earns a fifth as much for it. The buyer, looking at the bill, can't tell whether a long run was a hard problem or a wasteful agent.

## Piece rates work where the job can be counted and checked

A piece rate pays per finished job. It is the only form in the figure that moves both risks to the seller, because a slow job and a failed job both cost the seller, and only finished work gets paid. Buyers like that, and vendors who offer it call it [the future of software business models](https://sierra.ai/resources/podcasts/bret-taylor-of-sierra-on-ai-agents-outcome-based-pricing-and-the-openai-board). Intercom's Fin agent charges $0.99 per outcome, where an outcome is mostly a resolved conversation ([Fin](https://fin.ai/pricing/)).

The best-known study of a piece rate comes from Safelite, an American auto-glass company. In the mid-1990s it stopped paying its windshield installers by the hour and started paying them by the windshield. The economist Edward Lazear measured what happened: output per worker rose 44 percent ([Lazear 2000](https://www.aeaweb.org/articles?id=10.1257/aer.90.5.1346)). About half of the rise came from installers working faster. The rest came from the company attracting and keeping faster installers.

Safelite could pay this way because windshields are easy to count and a bad installation is easy to see. An installer who did a poor job had to fix it on his own time or pay for the repair ([Christian Science Monitor](https://www.csmonitor.com/1996/1223/122396.econ.econ.1.html)). Where quality is harder to see, piece rates go wrong. In the same article the economist Claudia Goldin pointed to packers of glass items, who aren't paid by the piece because their care drops as their speed rises, and said: "Piece rates are frequently a disaster." Bengt Holmström and Paul Milgrom had given the general reason in 1991: when the volume of output is easy to measure and its quality is not, a piece rate pushes the worker to raise volume at the expense of quality ([Holmström and Milgrom](https://ideas.repec.org/a/oup/jleorg/v7y1991i0p24-52.html)).

So the hard part of any outcome price is deciding what counts as a finished job, and who checks it. Here the vendors disagree. Fin counts a resolution when the customer confirms the answer helped, or when the customer leaves without asking for more help, and a customer who goes quiet for 24 hours after Fin's last answer counts as resolved ([Fin help](https://fin.ai/help/en/articles/13975800-fin-pricing-outcomes)). Zendesk doesn't bill that case. It charges only for a "verified resolution", where an LLM reads the conversation after it ends and confirms that the request was resolved ([Zendesk](https://support.zendesk.com/hc/en-us/articles/9570369117338)). Fin does guard quality the way Safelite did, by taking the charge back if the customer returns to the same conversation for more help. A customer who gave up in silence, though, still counts as a finished job.

## Commits and minimums are the floor under a piece rate

Even at Safelite the piece rate didn't stand alone. Installers earned about $20 a windshield, but the plan guaranteed about $11 an hour whenever a week's piece pay fell below that, and "many end up in the guarantee range" ([Christian Science Monitor](https://www.csmonitor.com/1996/1223/122396.econ.econ.1.html)). A floor like that makes sense when output depends partly on something the worker doesn't control, and no installer controlled how many broken windshields came in each week. The figure below sketches that pay plan, with pay against jobs finished; it isn't drawn to scale.

![A line chart of pay against jobs finished. In a slow period, pay is held flat at a floor (Safelite: about $11 an hour; software: a minimum commit), above the dashed line the piece rate alone would pay, and the gap between them is what the floor tops up. Past the point where the two meet, in a busy period, pay rises with each job (Safelite: $20 a windshield; Fin: $0.99 an outcome).](../blog_assets/outcome_pricing_floor.png)

In a slow period the floor tops up what the piece rate alone would pay, and in a busy period the piece rate takes over. An AI agent's outcomes also depend on things its vendor doesn't control: how many tickets arrive, how good the customer's help articles are, which questions get routed to the agent. So outcome prices often come wrapped in the commercial levers from Metronome's map. Fin's $0.99 per outcome sits on a $49 monthly minimum that includes 50 outcomes ([Fin](https://fin.ai/pricing/)). Zendesk sells automated resolutions as an allowance included with each plan, as a committed block, or pay as you go ([Zendesk pricing](https://www.zendesk.com/pricing/)). A minimum or a commit works the way Safelite's guarantee did. It protects the seller in a slow month, and in return the buyer gets a known budget.

The pricing map of the next few years is therefore a sorting rather than a march from seats to outcomes. ICONIQ's 2026 survey of AI companies found outcome-based pricing rising from 18 to 23 percent in six months, yet the same companies blend 1.7 pricing models on average ([ICONIQ](https://www.iconiq.com/growth/reports/state-of-ai-2026)). Countable work with a visible result, like a resolved ticket, will move to piece rates with a floor under them. Work whose value is diffuse or slow to show, like an agent that helps an analyst think, will stay on salaries and hourly wages, increasingly drawn from a prepaid allowance. Many products will mix the two, as the map's "hybrid" metric already does: dbt charges per developer seat and per successful model built, which is a base salary plus a commission, a salary for the part of the job nobody can count and a commission for the part they can. Labour markets made the same sort long ago, and piece rates stayed where the work arrives in units someone can count and inspect.

## Sources

- Metronome, [Pricing levers](https://metronome.com/pricing-levers)
- Cursor, [June 2025 pricing post](https://cursor.com/blog/june-2025-pricing), 4 July 2025
- TechCrunch, [Anthropic unveils new rate limits to curb Claude Code power users](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/), 28 July 2025
- GitHub, [GitHub Copilot is moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/), 27 April 2026
- Sierra, [Bret Taylor of Sierra on AI agents, outcome-based pricing, and the OpenAI board](https://sierra.ai/resources/podcasts/bret-taylor-of-sierra-on-ai-agents-outcome-based-pricing-and-the-openai-board)
- Fin, [Pricing](https://fin.ai/pricing/) and [Fin pricing: outcomes](https://fin.ai/help/en/articles/13975800-fin-pricing-outcomes)
- Zendesk, [About automated resolution tiers](https://support.zendesk.com/hc/en-us/articles/9570369117338) and [Pricing](https://www.zendesk.com/pricing/)
- Edward P. Lazear, [Performance Pay and Productivity](https://www.aeaweb.org/articles?id=10.1257/aer.90.5.1346), *American Economic Review* 90(5), 2000
- Christian Science Monitor, [Incentive Pay Boosts Output On Shop Floor](https://www.csmonitor.com/1996/1223/122396.econ.econ.1.html), 23 December 1996
- Bengt Holmström and Paul Milgrom, [Multitask Principal-Agent Analyses](https://ideas.repec.org/a/oup/jleorg/v7y1991i0p24-52.html), *Journal of Law, Economics and Organization* 7, 1991
- ICONIQ, [State of AI 2026](https://www.iconiq.com/growth/reports/state-of-ai-2026)
