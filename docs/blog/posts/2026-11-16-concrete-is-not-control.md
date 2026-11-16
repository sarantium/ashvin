---
title: "Concrete Is Not Control: Separating the Facility Stack from the Model Stack in Australia's AI Standards"
date: 2026-11-16
description: "Policy note: Australia's forthcoming AI Standards span frontier model safety and physical data centres. Treating them as two distinct technical stacks lets Canberra regulate models at the market door while holding server halls to hard physical and fiscal gates."
tags:
  - ai
  - data-centres
  - australia
  - strategy
  - political-economy
---

**ASHVIN PARAMESWARAN**, Sydney, Australia

**Abstract.** On 10 November 2026, the Australian Government announced a statutory AI safety regulator under its forthcoming *Australian AI Standards* legislation, requiring every frontier AI provider operating in Australia to allow independent model evaluation, report serious incidents rapidly, and maintain security controls across development and deployment [1]. Earlier announcements under the same agenda foreshadowed mandatory net-energy and water rules for large data centres [2] alongside voluntary expectations that compute developers grant favourable access to local researchers and start-ups [10]. Public debate increasingly merges these two tracks into a single "sovereign AI" or "compute-for-access" bargain: facilitate gigawatts of domestic server halls so foreign frontier laboratories grant Australia model access, safety visibility, and sovereign capability. I argue that physical data centres and frontier AI services sit on separate technical and legal stacks, and that conflating them weakens both policies. Because roughly two-thirds of AI facility capital buys imported silicon [12], most inference workloads travel cleanly over fibre, and foreign export rules and cloud control planes follow parent-company nationality rather than server geography [5, 7], pouring domestic concrete buys data residency and low latency—not model control, guaranteed access, or safety assurance. Conversely, the November regulator demonstrates that Canberra can attach safety, evaluation, and transparency duties directly to *market operation* without underwriting server halls. I recommend splitting the *Australian AI Standards* into distinct service and facility schedules, funding public research compute and portability directly, and subjecting data-centre approvals to a sequential gate that enforces hourly grid firming, catchment water caps, and community consent ahead of economic trade-offs.

**Keywords:** AI governance, data centres, sovereign AI, compute policy, Australian AI Standards, energy and water systems

<!-- more -->

---

## 1. Introduction

On 10 November 2026, Prime Minister Anthony Albanese and three cabinet ministers announced that Australia's forthcoming *Australian AI Standards* legislation will create a dedicated AI safety regulator, backed by the technical capability of the Australian AI Safety Institute (AISI) and armed with "significant penalties" [1]. Its six statutory obligations—security controls across development and deployment, serious-risk management, independent model evaluation, rapid mandatory incident notification, published safety frameworks, and compliance with evolving standards—will apply to "all frontier AI companies that wish to operate in Australia" [1]. The announcement followed winter incidents in which offshore evaluation agents touched live third-party systems, including a Services Australia statistics portal accessed by an OpenAI evaluation agent in June and reported to Canberra nearly three months later [14, 21].

Under the same *AI in Australia's Interests* banner sits a second, physical track. In March 2026, the Department of Industry, Science and Resources issued *Expectations of data centres and AI infrastructure developers*, asking operators to bring additional clean generation, report water use, train local workers, and—under Expectation 5—offer favourable compute terms and engineering partnerships to Australian researchers, start-ups, and small firms [10]. In July, the Prime Minister promised "clear, consistent and mandatory" Australian Standards requiring large facilities to put at least as much energy into the grid as they draw and to pay for water infrastructure [2]. Meanwhile, prominent policy commentary—crystallised in Joe Walker's *Compute in Australia* series with Special Envoy Andrew Charlton, strategist Janet Egan, energy economist Tim Nelson, and investor John Hempton [24–27]—has debated whether Australia should court 10 to 15 gigawatts (GW) of hyperscale capacity to turn abundant land and solar resources into sovereign AI capability and geopolitical leverage.

I argue that Australian policy risks conflating two distinct technical objects—the **physical facility stack** and the **model-and-service stack**—under one legislative programme. Domestic concrete secures physical data residency and local routing; it confers neither operational command over foreign-owned model weights nor immunity from foreign legal directives. My subject is not whether AI adoption will lift Australian productivity, but how the *Australian AI Standards* should govern frontier services and physical server halls without mistaking one for the other.

## 2. Two Stacks Under One Banner

Debates over "sovereign AI infrastructure" routinely treat a data centre and the intelligence running inside it as one indivisible asset. In engineering practice, they divide into six layers across two separate stacks, each governed by different actors, bottlenecks, and legal instruments (Table 1).

| Stack and layer | What sits here | What onshore concrete changes | Effective policy lever |
|---|---|---|---|
| **Facility stack** | | | |
| 1. Land, shells & cooling | Buildings, cooling loops, backup diesel, substations | Concentrates construction work, noise, water draw, and land use in host postcodes | State planning gates, catchment water caps, FPIC consent, cleanup bonds |
| 2. Electricity, shaping & firming | Bulk MWh, battery shifting, multi-day firming, transmission | Adds flat 24/7 load at specific grid nodes; can fund or crowd out clean supply | Cost-reflective connection tariffs, curtailment siting, hourly firming rules |
| 3. Accelerators & racks | GPUs/TPUs, high-bandwidth memory, networking (~68% of capex [12]) | Almost wholly imported; washes out of GDP and depreciates in 3–5 years | Hardware supply-chain security; realistic depreciation in fiscal audits |
| **Model & service stack** | | | |
| 4. Cloud & cluster control plane | Hypervisors, scheduling, identity, deployment tiers | Region residency only if local routing is enforced; vendor holds administrative root | IRAP cloud rules, regional-routing audits, cybersecurity standards |
| 5. Model weights & safety controls | Trained parameters, guardrails, APIs, evaluation hooks | Unchanged unless weights are escrowed or self-hosted; follows maker's jurisdiction | AI Safety Regulator duties [1], AISI evaluation, open-weights procurement |
| 6. Applications, data & exit | Enterprise workflows, public-sector records, switching tools | Keeps regulated records onshore; does not prevent vendor lock-in | Privacy law, interoperability mandates, multi-model procurement |

*Table 1. Six technical layers often collapsed into "sovereign AI". Onshore server halls govern the physical footprint of Layers 1–2 and support data residency at Layer 6, while operational control of Layers 3–5 remains governed by supply chains, software architecture, and corporate jurisdiction.*

Two features of 2026 AI systems make this separation decisive for Australian law. First, **control planes and export licences follow parent nationality across borders**. On 12 June 2026, Anthropic received a US export-control directive restricting foreign nationals' access to its newest models, *Fable 5* and *Mythos 5*, in a notice that "did not provide specific details of its national security concern" [4]. Unable to verify user nationality in real time, Anthropic suspended both models globally—across third-party cloud regions as well as its own API—and *Mythos 5* returned only for US-approved organisations [4, 5]. Guidance from the US Bureau of Industry and Security (BIS) on advanced computing items likewise attaches compliance duties to corporate headquarters and ultimate-parent jurisdiction worldwide [7]. Even when a model runs inside a Sydney cloud hall, foreign parent obligations and proprietary deployment switches continue to govern whether Australian users can call it.

Second, **training and inference have diverging physical footprints**. Frontier *training* concentrates tens of thousands of accelerators into single power-dense campuses, creating high sunk costs where it lands [25]. *Inference*—running trained models in production—splits by response-time tolerance. Interactive clinical, voice, or industrial systems need millisecond latency near Australian cities, whereas long-running coding, research, and administrative agents tolerate offshore routing over subsea fibre [24, 27]. Specialised inference silicon is also diverging from training clusters. Hosting an export-oriented training hall in regional Australia therefore provides no automatic guarantee of resilient domestic inference for Australian hospitals, banks, or agencies during an international disruption.

## 3. The Arithmetic of Hosting Versus Using

Separating the two stacks clarifies the economic numbers now invoked to justify fast-tracked approvals. Australian public debate frequently pairs headline pipeline totals with economy-wide AI productivity estimates as though the first causes the second.

On the demand side, the Australian Energy Market Operator (AEMO) counted 225 developing data-centre projects totalling **67 GW** in August 2026 [3]. Yet realised FY2026 data-centre consumption across the National Electricity Market (NEM) was roughly **5 terawatt-hours (TWh)**, or 3% of operational demand; average grid-connection utilisation across operating facilities sat near **27%**; projects took five to ten years to reach full load; and **36%** of developing projects recorded in the 2025 forecast had already been cancelled [3]. Stipulated policy scenarios of 10 to 15 GW running at 75% utilisation imply 65.7 to 98.6 TWh a year—**4.2 to 6.4 times** AEMO's FY2030 Step Change forecast (15.5 TWh) and up to nine times its economic-outlook series (10.7 TWh) [3, 25, 26]. Those gigawatt figures do not describe organic Australian demand; they describe a bid to build an export-scale training industry.

On the expenditure side, headline capital figures overstate domestic capture. In Epoch AI's cost model for a one-gigawatt-IT AI facility, **68%** of capital spending (US$26 billion of US$38 billion) purchases chips, servers, and networking [12]. Because Australia imports virtually all advanced semiconductors, two-thirds of every announced dollar enters gross domestic product (GDP) as business investment and subtracts straight back out as imports—why Commonwealth Bank economists note that "[t]he business investment pulse is quite large, but that flow through to GDP is far smaller" [9]. Of the remaining 32% spent on shells, electrical fit-out, cooling, and land, local value added accrues during construction, where mega-campuses bid for the same scarce electricians, civil trades, and high-voltage transformers required for housing and grid decarbonisation [9]. Once operating, ongoing employment is modest—an industry-commissioned Mandala report estimates 9,450 direct, indirect, and part-time roles in 2026 across a workforce of 15.2 million [19]—and profits earned by foreign-owned operators count in Australian GDP without remaining in Australian gross national income (GNI).

Meanwhile, three economic outcomes routinely merged in public pitches move independently: **AI's usefulness to Australian adopters**, **private returns to facility investors**, and **net public value retained by residents**. Australia's Productivity Commission estimates AI could add roughly 0.4 percentage points a year to labour productivity over the coming decade, compared with 0.3% over the past decade [24]. That gain arises from Australian firms and public agencies redesigning tasks, whether the underlying tokens are processed in Melbourne or Oregon. Conversely, as Hempton warns, capital-heavy infrastructure with low marginal operating costs and rapid chip obsolescence can suffer severe overbuild and weak investor returns even while the services running over it transform the wider economy [27]. Underwriting private capacity risk with public concessions is doubly costly when domestic productivity gains depend primarily on diffusion and skills.

## 4. Why Compute-for-Access Cannot Carry Model Governance

Recognising weak direct job numbers, the most sophisticated Australian case for rapid hyperscale expansion shifts from construction multipliers to geostrategic bargaining: **compute-for-access** [25]. In Egan's formulation, if Australia offers fast, predictable approvals, abundant renewable land, and aligned Five Eyes security settings for multi-gigawatt training clusters, frontier laboratories will sink tens of billions of private dollars onshore. That sunk dependence, the argument runs, turns hosting labs into internal champions for Australia in Washington and lets Canberra bargain for guaranteed frontier model access, dedicated research compute, and deep safety collaboration between labs and the Australian AISI [25]. Charlton advances a related ecosystem logic behind Expectation 5, aiming to turn Australian universities and firms from passive API buyers into intellectual-property partners [24].

As a commercial negotiation strategy where private capital bears its own cost, seeking ecosystem commitments makes sense. As the primary foundation for Australian safety governance or sovereign access, however, facility leverage has three structural flaws.

First, **Canberra's 10 November 2026 announcement establishes a cleaner, broader hook: market access**. By legislating mandatory safety controls, independent model evaluation, and rapid incident notification for *every* frontier AI provider operating in Australia—explicitly sequenced "before a range of major international talks that will cover AI development and investment" [1]—the Commonwealth reaches models trained and hosted anywhere on earth the moment they serve Australian customers. Conditioning safety visibility on onshore server halls would leave offshore-hosted frontier services untouched while giving domestic developers leverage over their regulator.

Second, **facility leverage is brittle at both extremes of the market**. If global compute overbuilds or frontier advantages narrow—with leading open-weights models trailing top closed models by roughly four months on independent capability indices in 2026 [11]—sunk training halls confer little bargaining power. Conversely, in an acute geopolitical crisis where frontier compute is genuinely scarce, a provider's home government holds statutory authority over parent companies, chip replacements, and software updates that overrides host-country commercial MOUs [5, 7]. Soft influence is real among allies, as Carnegie's *Compute Coalition* argues [23], yet physical hosting cannot compel a foreign sovereign.

Third, **trading domestic regulatory settings to attract labs imposes certain public costs for uncertain returns**. In the *Compute Series*, copyright licensing sensitivity was flagged as a potential red line for foreign labs concerned about US fair-use litigation [25]. Yet US courts have already drawn fine distinctions between lawful training copies and retained pirated libraries (*Bartz v Anthropic* [6]), and Australia's Attorney-General's Department confirmed via its Copyright and AI Reference Group that a text-and-data-mining exception is off the table in favour of licensing certainty [8]. Weakening Australian creator rights, compressing environmental and Indigenous land-consent processes [20], or entering subnational tax-exemption races—where Virginia's legislative auditor found US$4.06 billion in data-centre exemptions returned just 22 cents of state revenue per dollar foregone [17]—trades permanent domestic assets for non-binding promises.

## 5. Recommendations for the Australian AI Standards

Because the *Australian AI Standards* legislation is still being drafted [1], Parliament and portfolio agencies have a rare chance to align each policy objective with the technical layer that actually controls it (Table 2).

| Public objective | Stack layer | Instrument and responsible authority |
|---|---|---|
| Frontier model safety, evaluation & incident notice | Layer 5 (Models & APIs) | Statutory market-access duties on all frontier providers serving Australia; enforced by AI Safety Regulator + AISI [1] |
| Sovereign data residency & switching resilience | Layers 4 & 6 (Control plane & apps) | Enforced domestic routing tiers, open-weights self-hosting options, and multi-vendor portability under DTA / ASD rules |
| Public research & SME compute capability | Layer 5 (Compute access) | Direct national compute pool (CSIRO / ARC / Industry) plus SLA-bound, audited GPU quotas where grid priority is granted |
| Grid reliability, decarbonisation & bill protection | Layer 2 (Electricity system) | Hourly shaping/firming obligations, curtailment-zone siting, and full connection cost recovery (AEMO / AER / states) |
| Water security, local consent & site remediation | Layer 1 (Land & catchments) | Hard catchment consumption caps, upfront FPIC consent on Indigenous land, and transferable cleanup bonds (states / EPBC) |

*Table 2. A decoupled governance design for Australia's AI agenda: governing models and operational resilience at the service and procurement layers while holding physical facilities to metered local thresholds.*

**Commonwealth legislators: enact separate statutory schedules for frontier services and physical facilities.** The *Australian AI Standards* Bill should keep model governance strictly decoupled from infrastructure attraction. Every frontier provider serving Australian users—hosted onshore or offshore—should face the same mandatory AISI evaluation access, 72-hour incident-reporting clock (matching European breach-notification practice after multi-month delays in 2026 [14, 21]), and security standards [1]. Regulatory, copyright, or safety concessions should never be offered as sweeteners in facility siting deals.

**Energy and water regulators (AEMO, AER, and states): define "net-positive" infrastructure rules in hourly and catchment units.** The Prime Minister's July pledge that large facilities put back at least as much energy as they draw and fund water infrastructure [2] will fail if measured by annual accounting certificates alone. A flat 24/7 load requires **bulk energy**, **hourly shaping** via storage, and **multi-day firming** during renewable lulls [26]; annual renewable certificates matched against round-the-clock draw can still increase marginal gas or coal dispatch and leave long-run network augmentations on household bills, as Virginia's projected US$14–37 monthly residential cost increase by 2040 illustrates [16]. Standards should require project-funded network connections, steer flexible or training loads toward curtailed renewable zones [26], and meter *evaporative water consumption* alongside indirect power-station water against seasonal local catchment caps [18].

**Commonwealth and state planning ministers: enforce a sequential project gate and bar interstate subsidy races.** Individual campuses should clear four tests in strict order before receiving permits or public coordination: (1) workload and counterfactual disclosure separating domestic latency/residency needs from export training; (2) **non-tradable local thresholds** on drinking water, grid reliability, biodiversity, and Free, Prior and Informed Consent on Indigenous estates [20] *before* economic benefits are weighed; (3) net resident-income (GNI) and trade-crowding scrutiny; and (4) decommissioning bonds and conditions that bind successor owners. National cabinet coordination should prevent states from bidding away payroll taxes, land, or grid queues against one another [17].

**Department of Industry, DTA, and research agencies: purchase sovereign access and portability directly.** Rather than relying on commercial export halls to trickle capability down through voluntary *Expectation 5* pledges [10], Canberra should fund pooled public research and SME compute directly—following Canada's Sovereign AI Compute Strategy and Europe's EuroHPC access modes [13, 22]—and require government agencies to maintain model portability, audited regional routing (avoiding "global standard" cloud tiers that process Australian prompts offshore), and vetted open-weights fallbacks on IRAP-assessed infrastructure. Where developers do seek expedited grid coordination under Expectation 5, soft promises should convert into contracted, AISI- and Industry-audited GPU-hour allocations with explicit remedies for non-delivery.

## 6. Objections and Limitations

*“Hard physical and fiscal gates will drive hyperscale investment to Southeast Asia or the United States.”* Workloads that require Australian data residency or low local latency must locate near Australian users regardless, as Singapore's oversubscribed selective capacity allocation under strict efficiency rules demonstrates [15]. Conversely, if an offshore-bound training hall is viable in Australia only when households cross-subsidise its firming or communities waive water thresholds, declining to subsidise it protects national welfare.

*“Without gigawatt training clusters onshore, Australia will be rationed out of frontier AI in an international crisis.”* Sunk hardware without sovereign legal authority did not prevent US export directives from suspending frontier models across cloud regions in June 2026 [4, 5]. Where allied compute hosting genuinely advances defence or intelligence resilience, Canberra should negotiate binding intergovernmental carve-outs, local weight escrow, and emergency priority rights explicitly, and evaluate that campus on its defence budget merits rather than disguising it as general economic policy.

*“Wholesale spot prices plus annual renewable certificates already reward storage without hourly matching rules.”* Time-varying wholesale prices signal storage investment where locational constraints and retail tariffs pass peak costs through cleanly [26]. Because regulated network charges and long-lived transmission builds still socialise expansion risks across captive residential customers [16], physical connection and firming conditions remain a necessary backstop.

**Limitations.** Project-level Australian power contracts, cooling designs, and foreign-ownership shares remain largely commercial-in-confidence; March 2026's *Developer Expectations* have not yet undergone a public compliance audit [10]; and the full legislative text of the *Australian AI Standards* Bill remained unreleased at the time of writing [1]. Standardized public metering of facility energy, water, and contracted research compute would make every link in this policy note empirically testable.

## 7. Conclusion

Announcing a statutory AI safety regulator ahead of international investment talks quietly resolves a confusion at the heart of Australia's compute debate [1]. A middle power does not need to underwrite gigawatts of imported silicon to govern the frontier models operating in its market, and pouring domestic concrete does not by itself transfer control over foreign-owned weights, software, or export licences. By splitting the *Australian AI Standards* into two clear engineering schedules—statutory market-access governance and portable procurement for the model stack, paired with hard local physical, consent, and fiscal gates for the facility stack—Australia can capture the productivity gains of AI adoption while welcoming only the server halls that earn their claim on shared grids, water, and land.

---

### Acknowledgments and Disclosure

**Acknowledgments.** Claude (Anthropic) and Gemini (Google) assisted with source verification, structural synthesis, and editing; every empirical claim, quotation, and reference was verified against primary documents on file, and the author takes sole responsibility for the analysis and positions expressed.

**Competing interests and funding.** The author works in the Australian enterprise software and AI sector; this note is written solely in a personal capacity and received no external funding.

---

### References

[1] Anthony Albanese, Richard Marles, Tony Burke, and Tim Ayres. 2026. *New Australian AI safety and security protections*. Media release, Office of the Prime Minister of Australia, 10 November 2026. <https://www.pm.gov.au/media/new-australian-ai-safety-and-security-protections>

[2] Anthony Albanese. 2026. *AI in Australia's Interests*. Speech, Office of the Prime Minister of Australia, 15 July 2026. <https://www.pm.gov.au/media/ai-australias-interests-0>

[3] Australian Energy Market Operator (AEMO). 2026. *2026 ESOO Data Centre Forecasting Overview*. AEMO, 25 August 2026. <https://www.aemo.com.au/-/media/files/electricity/nem/planning_and_forecasting/nem_esoo/2026/2026-esoo-data-centre-forecasting-overview.pdf>

[4] Anthropic. 2026. *Statement on the US government directive to suspend access to Fable 5 and Mythos 5*. Anthropic, 12 June 2026. <https://www.anthropic.com/news/fable-mythos-access>

[5] Anthropic. 2026. *Redeploying Fable 5*. Anthropic, 30 June 2026. <https://www.anthropic.com/news/redeploying-fable-5>

[6] *Bartz v Anthropic PBC*. 2025. Order on Fair Use, US District Court for the Northern District of California, Case No. 3:24-cv-05417, 23 June 2025. <https://storage.courtlistener.com/recap/gov.uscourts.cand.434709/gov.uscourts.cand.434709.231.0_5.pdf>

[7] Bureau of Industry and Security (BIS). 2026. *Guidance Regarding Enforcement of License Requirements for Advanced Computing Items*. US Department of Commerce, 31 May 2026. <https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf>

[8] Commonwealth Attorney-General's Department. 2025. *Copyright and Artificial Intelligence Reference Group (CAIRG)*. Australian Government, October 2025 update. <https://www.ag.gov.au/rights-and-protections/copyright/copyright-and-artificial-intelligence-reference-group-cairg>

[9] Commonwealth Bank of Australia. 2026. *Australia's data centre boom*. CommBank Newsroom, 6 August 2026. <https://www.commbank.com.au/articles/newsroom/2026/08/australias-data-centre-boom.html>

[10] Department of Industry, Science and Resources. 2026. *Expectations of data centres and AI infrastructure developers*. Australian Government, 23 March 2026. <https://www.industry.gov.au/publications/expectations-data-centres-and-ai-infrastructure-developers>

[11] Epoch AI. 2026. *Open models lag state-of-the-art closed models by 4 months*. Epoch AI Data Insights, 29 May 2026. <https://epoch.ai/data-insights/open-closed-eci-gap>

[12] Epoch AI. 2026. *Total Cost of Ownership of a One-Gigawatt AI Data Center*. Epoch AI Data Insights, May 2026. <https://epoch.ai/data-insights/ai-datacenter-cost-breakdown>

[13] EuroHPC Joint Undertaking. 2025. *AI Factories Access Modes*. European Union, 2025. <https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en>

[14] Erin Handley. 2026. *OpenAI hacked Medicare portal, Prime Minister Anthony Albanese says*. ABC News, 24 September 2026. <https://www.abc.net.au/news/2026-09-24/ai-agent-accessed-australian-government-site-pm-says/107189078>

[15] Infocomm Media Development Authority (IMDA) and Economic Development Board, Singapore. 2026. *Four Data Centre Proposals Selected as Part of Second Data Centre Call for Application*. Singapore Government, 21 August 2026. <https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/four-data-centre-proposals-selected-as-part-of-second-data-centre-call-for-application>

[16] Joint Legislative Audit and Review Commission (JLARC). 2024. *Data Centers in Virginia*. Commonwealth of Virginia, December 2024. <https://jlarc.virginia.gov/landing-2024-data-centers-in-virginia.asp>

[17] Joint Legislative Audit and Review Commission (JLARC). 2026. *Economic Development Incentives 2026*. Report 623, Commonwealth of Virginia, 2026. <https://jlarc.virginia.gov/pdfs/reports/Rpt623.pdf>

[18] Arman Shehabi et al. 2024. *2024 United States Data Center Energy Usage Report*. Lawrence Berkeley National Laboratory, December 2024. <https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report>

[19] Mandala Partners. 2026. *The Economic Contribution of the Data Centre Industry in Australia*. Commissioned by Data Centres Australia, August 2026. <https://datacentres.org.au/wp-content/uploads/2026/08/2026-08_DCA-Mandala-The-Economic-Contribution-of-the-Data-Centre-Industry-in-Australia-digital.pdf>

[20] Northern Land Council. 2026. *Submission 207 to the Senate Inquiry into Artificial Intelligence and Data Centres*. Parliament of Australia, September 2026. <https://www.aph.gov.au/DocumentStore.ashx?id=64091ae6-dec5-47ec-a083-b32aa60fc35b&subId=803365>

[21] OpenAI. 2026. *How we will do better for Australia*. OpenAI, 28 September 2026 (updated 4 October 2026). <https://openai.com/index/how-we-will-do-better-for-australia/>

[22] OECD. 2026. *Securing AI Compute: Government Policy Approaches*, 13 October 2026 (<https://www.oecd.org/en/publications/securing-ai-compute_7f96dc99-en/full-report.html>); Innovation, Science and Economic Development Canada, *Canadian Sovereign AI Compute Strategy*, 4 June 2026 (<https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy>).

[23] Alexandra Phillips-Robins, Tarek Tawil, and Sam Winter-Levy. 2026. *The Compute Coalition: How to Build the Future of AI in the Free World*. Carnegie Endowment for International Peace, June 2026. <https://carnegieendowment.org/research/2026/06/the-compute-coalition-how-to-build-the-future-of-ai-in-the-free-world>

[24] Joseph Walker. 2026. *Australia's Plan to Turn Compute Into Sovereign AI — Dr Andrew Charlton MP*. The Joe Walker Podcast, 16 August 2026 (Productivity Commission 0.4% labour-productivity estimate: Danielle Wood, 25 June 2026). <https://josephnoelwalker.com/andrew-charlton/>

[25] Joseph Walker. 2026. *The Geostrategic Case for Compute in Australia — Janet Egan*. The Joe Walker Podcast, 27 August 2026. <https://josephnoelwalker.com/janet-egan/>

[26] Joseph Walker. 2026. *AI Factories in the Outback — Tim Nelson*. The Joe Walker Podcast, 14 October 2026. <https://josephnoelwalker.com/tim-nelson/>

[27] Joseph Walker. 2026. *"Fibre Optics Mark II": Why Data Centres Will Change the World and Bankrupt Their Builders — John Hempton*. The Joe Walker Podcast, 4 November 2026. <https://josephnoelwalker.com/john-hempton/>
