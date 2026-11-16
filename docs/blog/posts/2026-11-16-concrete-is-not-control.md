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

**Abstract.** In November 2026, the Australian Government announced a statutory AI safety regulator under its forthcoming *Australian AI Standards* legislation. Every frontier AI provider operating in Australia will have to maintain security controls, open its models to independent evaluation, and report serious incidents rapidly. Under the same agenda, Canberra has promised mandatory energy and water rules for large data centres while asking developers to offer local researchers and start-ups favourable compute access. Public debate increasingly fuses these tracks into one "compute-for-access" bargain: approve gigawatts of domestic server halls so foreign labs grant Australia model access, safety visibility, and strategic weight. I argue that physical data centres and frontier AI services sit on separate technical and legal stacks, and that merging them weakens both policies. Pouring concrete onshore buys local data storage and low latency; it does not buy control over foreign models, guaranteed access, or safety assurance. Two-thirds of AI facility capital buys imported chips, most AI queries travel cleanly over subsea fibre, and cloud control software and export rules follow corporate nationality rather than server location. Conversely, the November regulator shows that Canberra can attach safety and transparency duties directly to *market entry* without underwriting server halls. I recommend splitting the *Australian AI Standards* into separate service and facility schedules, funding public compute and model portability directly, and enforcing local power, water, and consent gates ahead of economic trade-offs.

**Keywords:** AI governance, data centres, sovereign AI, compute policy, Australian AI Standards, energy and water systems

<!-- more -->

---

## 1. Introduction

On 10 November 2026, Prime Minister Anthony Albanese and three cabinet ministers announced a dedicated AI safety regulator under the forthcoming *Australian AI Standards* legislation [1]. Backed by the Australian AI Safety Institute (AISI) and armed with "significant penalties", the regulator will apply to "all frontier AI companies that wish to operate in Australia", regardless of where their servers sit [1]. Covered providers must maintain security controls across development and deployment, manage serious risks, allow independent evaluation, report serious incidents rapidly, publish safety frameworks, and meet evolving standards [1]. The reform followed mid-2026 incidents in which offshore evaluation agents touched live external systems. In one case, an OpenAI agent accessed a Services Australia statistics portal in June, and Canberra was notified nearly three months later [14, 21].

Under the same *AI in Australia's Interests* banner runs a second, physical track for data centres. In March 2026, the Department of Industry, Science and Resources issued voluntary *Expectations* asking developers to add clean generation, report water use, and train local workers [10]. Expectation 5 went further, asking operators to offer Australian researchers, start-ups, and small firms favourable compute access and engineering partnerships [10]. Four months later, the Prime Minister promised "clear, consistent and mandatory" standards requiring large halls to supply at least as much grid energy as they draw and to fund water infrastructure [2]. Prominent voices have meanwhile weighed an export-scale build-out across Joseph Walker's *Compute in Australia* series, featuring Special Envoy Andrew Charlton, strategist Janet Egan, energy economist Tim Nelson, and investor John Hempton [24–27]. One question sits at the centre of that debate: should Australia court 10 to 15 gigawatts (GW) of hyperscale capacity to turn abundant land and solar power into sovereign AI capability and strategic weight?

I argue that this debate conflates two distinct technical objects under one legislative banner: the **physical facility stack** and the **model-and-service stack**. Pouring concrete onshore secures local data storage and low network delay, yet it confers neither operational command over foreign-owned models nor immunity from foreign law. Equally, Canberra does not need to host server halls to govern the AI services Australians use. My subject is not whether AI adoption will lift Australian productivity, but how the *Australian AI Standards* should govern frontier models and physical server halls without mistaking one for the other.

## 2. Two Stacks Under One Banner

Calls for "sovereign AI infrastructure" routinely treat a data centre and the intelligence running inside it as one indivisible asset. In engineering and law, they divide into six layers across two separate stacks, each governed by different actors, bottlenecks, and policy instruments (Table 1).

| Stack and layer | What sits here | What onshore concrete changes | Effective policy lever |
|---|---|---|---|
| **Facility stack** | | | |
| 1. Land, shells & cooling | Buildings, cooling loops, backup diesel, substations | Concentrates construction, noise, water draw, and land use in host postcodes | State planning gates, catchment water caps, Indigenous consent (FPIC), cleanup bonds |
| 2. Electricity, shaping & firming | Bulk megawatt-hours, battery storage, backup generation, grid lines | Adds flat 24/7 load at specific grid nodes; can fund or crowd out clean supply | Cost-reflective connection tariffs, siting in renewable-surplus zones, hourly firming rules |
| 3. Accelerators & racks | AI chips (GPUs/TPUs), memory, networking (~68% of capex [12]) | Physically onshore, yet imported; washes out of GDP and ages out in 3–5 years | Supply-chain security; realistic chip depreciation in fiscal audits |
| **Model & service stack** | | | |
| 4. Cloud control plane | Management software for scheduling, identity, and traffic routing | Keeps traffic onshore only if regional routing is enforced; vendor holds root access | Government cloud security rules (IRAP), routing audits, cybersecurity standards |
| 5. Model weights & safety controls | Trained parameters, guardrails, APIs, evaluation hooks | Unchanged unless weights are escrowed or self-hosted; follows maker's home law | AI Safety Regulator duties [1], AISI evaluation, open-weights procurement |
| 6. Applications, data & exit | Enterprise workflows, public-sector records, switching tools | Keeps regulated records onshore; does not prevent vendor lock-in | Privacy law, interoperability standards, multi-vendor procurement |

*Table 1. Six technical layers often collapsed into "sovereign AI". Onshore concrete governs the physical footprint of Layers 1–2 and supports data residency at Layer 6, while operational control over Layers 3–5 remains governed by hardware supply chains, cloud software, and corporate nationality.*

Two features of modern AI systems make the boundary between these stacks decisive for Australian law. First, **cloud control software and export licences follow parent-company nationality across borders**. Every commercial cloud or API relies on a control plane: the management software that authenticates users, routes prompts, and switches models on or off. On 12 June 2026, a US export-control directive restricted foreign nationals' access to Anthropic's newest models, *Fable 5* and *Mythos 5* [4]. The notice "did not provide specific details of its national security concern" [4]. Unable to check user nationality in real time, Anthropic suspended both models worldwide across its API and third-party cloud regions; *Mythos 5* returned only for US-approved organisations [4, 5]. Guidance from the US Bureau of Industry and Security (BIS) on advanced computing items likewise binds corporate headquarters and ultimate parent companies globally [7]. Even when a model runs on servers in Sydney, foreign law and vendor deployment switches decide whether Australians can call it.

Second, **training and inference have different physical footprints**. Frontier *training* (building a new model) packs tens of thousands of chips into a single power-dense campus, creating large sunk costs where it lands [25]. *Inference* (running a trained model to answer requests) splits according to how much delay a task can tolerate. Interactive clinical tools, voice systems, and industrial controls need millisecond response times near Australian cities. Long-running coding, research, and administrative agents, by contrast, run cleanly over subsea fibre from offshore halls [24, 27]. Hardware is diverging along the same line, as inference increasingly uses specialised silicon separate from training clusters. Hosting an export-oriented training hall in regional Australia therefore does not guarantee resilient local inference for Australian hospitals, banks, or public agencies during an international disruption.

## 3. The Arithmetic of Hosting Versus Using

Separating physical hosting from domestic AI use untangles three numbers routinely blurred in pitches for fast-tracked approvals: **gigawatt pipelines**, **headline capital billions**, and **economy-wide productivity gains**. Public debate often pairs the first two with the third as though pouring concrete is what produces the productivity dividend.

Start with electricity demand. In August 2026, the Australian Energy Market Operator (AEMO) counted 225 developing data-centre projects totalling **67 GW** [3]. Actual FY2026 consumption across the National Electricity Market (NEM) was far smaller: operating data centres drew roughly **5 terawatt-hours (TWh)**, or 3% of grid demand [3]. Average grid-connection utilisation sat near **27%**, facilities took five to ten years to reach full load, and **36%** of projects recorded in the 2025 forecast had already been cancelled [3]. Policy proposals to host 10 to 15 GW running at 75% utilisation imply 65.7 to 98.6 TWh a year. That represents **4.2 to 6.4 times** AEMO's FY2030 Step Change forecast (15.5 TWh), and up to nine times its central economic-outlook series (10.7 TWh) [3, 25, 26]. Those gigawatt figures do not measure domestic Australian demand; they describe a bid to build an export-scale training industry.

Headline investment figures similarly overstate what stays in the local economy. In Epoch AI's cost model for a one-gigawatt AI campus, **68%** of capital spending (US$26 billion of US$38 billion) buys chips, servers, and networking hardware [12]. Because Australia imports virtually all advanced semiconductors, two-thirds of every announced dollar enters **gross domestic product (GDP)** as business investment and subtracts straight back out as imports. As Commonwealth Bank economists note, "[t]he business investment pulse is quite large, but that flow through to GDP is far smaller" [9].

Domestic value added sits mainly in the remaining 32% spent on buildings, electrical fit-out, cooling, and land. Those gains arrive during construction, when mega-campuses bid for the same scarce electricians, civil trades, and high-voltage transformers needed for housing and grid decarbonisation [9]. Once operating, permanent employment is modest: an industry-commissioned report by Mandala Partners counts 9,450 direct, indirect, and part-time roles in 2026 across a workforce of 15.2 million [19]. Furthermore, profits earned by foreign-owned operators count in Australian GDP yet flow offshore, dropping out of **gross national income (GNI)**, which tracks the income Australian residents actually keep.

Finally, three economic outcomes merged in public pitches move independently: **gains to Australian AI adopters**, **returns to facility investors**, and **net value retained by the public**. Australia's Productivity Commission estimates AI could add roughly 0.4 percentage points a year to labour productivity over the next decade, compared with 0.3% annual growth over the past decade [24]. Australian firms and agencies capture that gain by redesigning everyday tasks, whether the underlying tokens are processed in Melbourne or Oregon. Meanwhile, as Hempton warns, capital-heavy infrastructure with low operating costs and rapid chip obsolescence can suffer severe overbuild and weak investor returns even while the services running over it transform the wider economy [27]. Subsidising private capacity risk with public concessions is doubly costly when domestic productivity gains come from adopting AI rather than hosting servers.

## 4. Why Compute-for-Access Cannot Govern Models

Because direct job counts and domestic demand cannot carry the case for rapid multi-gigawatt approvals, the sharpest Australian argument for hyperscale expansion turns to geostrategic bargaining: **compute-for-access** [25]. In Egan's account, Australia can offer foreign laboratories fast, predictable approvals, abundant renewable land, and aligned Five Eyes security settings for multi-gigawatt training clusters. Once laboratories sink tens of billions of private dollars onshore, that commercial stake gives them reason to defend Australian access in Washington. Canberra, the argument runs, can bargain in return for guaranteed frontier model access, dedicated research compute, and close safety cooperation with the Australian AISI [25]. Charlton advances a related ecosystem case behind Expectation 5, aiming to turn local universities and firms from passive API buyers into intellectual-property partners [24].

Where private capital pays its own physical and fiscal costs, seeking local research partnerships makes commercial sense. Relying on server halls to secure model governance or sovereign access, however, fails on three structural counts.

First, **market access is a cleaner and broader legal hook than physical hosting**. Canberra's 10 November 2026 announcement applies mandatory safety controls, independent evaluation, and rapid incident reporting to *every* frontier AI provider operating in Australia [1]. That rule reaches models trained and hosted anywhere on earth the moment they serve Australian users. Canberra timed it deliberately "before a range of major international talks that will cover AI development and investment" [1]. Tying safety visibility to onshore server halls would leave offshore-hosted services untouched while giving domestic landlords bargaining power over their own regulator.

Second, **hosting leverage fails in both gluts and crises**. If global compute overbuilds or frontier leads stay narrow, sunk training halls confer little bargaining power because substitutes are plentiful. In May 2026, leading open-weights models trailed top closed models by roughly four months on capability benchmarks [11]. Conversely, in an acute geopolitical crisis where frontier compute is scarce, a provider's home government holds statutory authority over parent companies, chip replacements, and software updates [5, 7]. Those legal powers override host-country memoranda of understanding. Hosting allied compute builds real diplomatic voice, as Carnegie's *Compute Coalition* report argues [23], yet physical concrete cannot compel a foreign sovereign.

Third, **trading domestic rules to court laboratories surrenders certain public value for uncertain returns**. Contributors to the *Compute in Australia* series noted that foreign labs worried about US fair-use litigation might treat Australian copyright licensing as a red line [25]. Yet US courts have already separated lawful training copies from retained pirated libraries (*Bartz v Anthropic* [6]), and Australia's Attorney-General's Department has ruled out a text-and-data-mining exception in favour of licensing certainty [8]. Weakening Australian creator rights, compressing environmental and Indigenous land-consent processes [20], or entering state tax-exemption races gives away permanent domestic assets for non-binding promises. Virginia's legislative auditor offers a clear benchmark: US$4.06 billion in data-centre tax exemptions returned just 22 cents of state revenue per dollar foregone [17].

## 5. Recommendations for the Australian AI Standards

Because the *Australian AI Standards* Bill is still being drafted [1], Parliament and regulators can match each policy goal to the technical layer that actually controls it (Table 2).

| Public objective | Stack layer | Instrument and responsible authority |
|---|---|---|
| Frontier model safety, evaluation & incident notice | Layer 5 (Models & APIs) | Statutory market-access duties on all frontier providers serving Australia; enforced by AI Safety Regulator and AISI [1] |
| Sovereign data residency & switching resilience | Layers 4 & 6 (Control plane & apps) | Audited domestic routing, open-weights fallbacks, and multi-vendor portability under federal digital and cyber rules (DTA / ASD) |
| Public research & start-up compute capability | Layer 5 (Compute access) | Direct national compute pool (CSIRO / ARC / Industry), plus contracted, audited GPU quotas where grid priority is granted |
| Grid reliability, clean supply & bill protection | Layer 2 (Electricity system) | Hourly storage and firming rules, siting in renewable-surplus zones, and full connection cost recovery (AEMO / AER / states) |
| Water security, local consent & site remediation | Layer 1 (Land & catchments) | Hard catchment consumption caps, upfront Indigenous consent (FPIC), and transferable cleanup bonds (states / federal environment law) |

*Table 2. A decoupled governance design for the Australian AI Standards: regulate models and operational resilience at the market and procurement layers, while holding physical facilities to metered local limits.*

**Commonwealth legislators: enact separate statutory schedules for frontier services and physical facilities.** The *Australian AI Standards* Bill should keep model governance strictly separate from infrastructure attraction. Every frontier provider serving Australians, hosted onshore or offshore, should face the same AISI evaluation access, security rules, and incident-reporting duties [1]. Notification should fall due within 72 hours, matching European breach rules after multi-month reporting delays in 2026 [14, 21]. Regulatory, copyright, and safety standards should never be offered as sweeteners in siting deals.

**Energy and water regulators: define "net-positive" rules in local hours and catchments, not annual averages.** The Prime Minister's July pledge that large facilities return at least as much energy as they draw and fund water infrastructure [2] will fail if measured by annual accounting certificates alone. A flat 24/7 server load requires **bulk energy** over the year, **hourly shaping** via batteries to cover evening peaks, and **multi-day firming** during wind and solar lulls [26]. Matching round-the-clock draw with annual renewable certificates can still push coal or gas plants harder at peak hours and shift grid-upgrade costs onto households. In Virginia, data-centre demand is projected to add US$14–37 a month to typical residential bills by 2040 [16]. AEMO, the Australian Energy Regulator (AER), and state governments should require project-funded connections and steer flexible training loads toward grid zones with surplus solar and wind [26]. Water standards should likewise cap both on-site *evaporative loss* and upstream power-station water use against seasonal local catchment limits [18].

**Commonwealth and state planning ministers: enforce a four-step sequential gate and bar interstate subsidy races.** Proposed campuses should clear four tests in strict order before receiving permits or public coordination. First, developers should disclose the project's workload mix and realistic alternatives, separating domestic latency or residency needs from export training. Second, campuses must clear **non-tradable local thresholds** on drinking water, grid reliability, biodiversity, and Free, Prior and Informed Consent (FPIC) on Indigenous land [20] *before* economic benefits are weighed. Third, treasuries should audit net resident income (GNI) and crowding of local electrical and civil trades. Fourth, permits should require upfront remediation bonds and conditions that bind successor owners. National Cabinet should also prevent states from bidding away payroll taxes, public land, or grid queues against one another [17].

**Industry, digital, and research agencies: buy public compute and model portability directly.** Canberra should not rely on commercial export halls to trickle capability down through voluntary *Expectation 5* pledges [10]. Instead, it should fund pooled public compute for universities and small firms directly, following Canada's Sovereign AI Compute Strategy and Europe's EuroHPC AI Factories [13, 22]. Within government, the Digital Transformation Agency (DTA) and Australian Signals Directorate (ASD) should require multi-vendor portability and audited domestic routing, avoiding "global standard" cloud tiers that process Australian prompts offshore. Agencies should also maintain vetted open-weights fallbacks on cloud infrastructure certified under ASD's Information Security Registered Assessors Program (IRAP). Where developers do seek expedited grid coordination under Expectation 5, soft promises should become contracted, audited GPU-hour allocations with clear remedies for non-delivery.

## 6. Objections and Limitations

*“Hard physical and fiscal gates will drive hyperscale investment to Southeast Asia or the United States.”* Some export-oriented training halls may go elsewhere; domestic service capacity will not. Workloads that need Australian data residency or millisecond latency must locate near Australian users regardless, as Singapore's oversubscribed capacity allocations under strict efficiency limits demonstrate [15]. Conversely, if an offshore-bound training campus pencils out in Australia only when households cross-subsidise its grid firming or communities waive water limits, declining to subsidise it protects national welfare.

*“Without gigawatt training clusters onshore, Australia will be rationed out of frontier AI in an international crisis.”* Crisis rationing is a real risk, yet commercial server halls do not prevent it. Onshore hardware did not stop US export directives from suspending *Fable 5* and *Mythos 5* across global cloud regions in June 2026 [4, 5]. Where allied hosting genuinely strengthens defence or intelligence continuity, Canberra should negotiate binding intergovernmental carve-outs, local weight escrow, and emergency priority rights. Any such campus should be funded and judged against the defence budget rather than disguised as general economic policy.

*“Wholesale spot prices plus annual renewable certificates already reward storage without hourly matching rules.”* Spot prices do reward batteries when wholesale supply tightens [26]. What they do not ring-fence are regulated transmission lines and substations, whose multi-decade costs still spill onto captive residential customers if forecast loads disappoint or network tariffs lag [16]. Upfront connection funding and firming conditions remain a necessary backstop.

**Limitations.** Project-level Australian power contracts, cooling designs, and foreign-ownership shares remain largely commercial-in-confidence. March 2026's *Developer Expectations* have not yet undergone a public compliance audit [10], and the full legislative text of the *Australian AI Standards* Bill remained unreleased at the time of writing [1]. Standardised public metering of facility power draw, water consumption, and contracted research compute would make every link in this policy note empirically testable.

## 7. Conclusion

Canberra's decision to legislate a statutory AI safety regulator ahead of international investment talks quietly resolves the confusion at the heart of Australia's compute debate [1]. A middle power does not need to underwrite gigawatts of imported silicon to govern the frontier models operating in its market. Equally, pouring concrete onshore does not transfer legal command over foreign-owned model weights, cloud control software, or export licences. Splitting the *Australian AI Standards* into two schedules pairs each policy tool with the stack it actually reaches. Market-entry duties and portable procurement govern frontier AI services; hard local power, water, consent, and fiscal gates discipline physical server halls. Australia can then capture the productivity gains of adopting AI while welcoming only the facilities that earn their claim on shared grids, catchments, and land.

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
