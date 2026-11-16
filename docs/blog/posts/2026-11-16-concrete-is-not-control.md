---
title: "Concrete Is Not Control: Separating the Facility Stack from the Model Stack in Australia's AI Standards"
date: 2026-11-16
description: "Policy note: The 'sovereign AI' bargain asks Australia to pay in things it controls (grid, water, land consent, copyright) for something a building cannot deliver: a say over foreign models. Canberra can bind frontier labs through the terms of market entry instead."
tags:
  - ai
  - data-centres
  - australia
  - strategy
  - political-economy
---

**ASHVIN PARAMESWARAN**, Sydney, Australia

**Abstract.** Australia is running two AI policies under one banner. In November 2026 it announced a statutory safety regulator covering every frontier AI provider in its market. It has also promised mandatory energy and water rules for large data centres while courting the companies that build them. Industry pitches and policy debate increasingly join the two into a single "sovereign AI" bargain: approve multi-gigawatt data centres quickly, and the foreign laboratories that use them will give Australia model access, safety cooperation, and strategic weight. I argue that this bargain asks Australia to pay in things it controls (grid capacity, water, land consent, copyright law) for something a building cannot deliver: a say over foreign models. Control of a model follows its owner's home government, as the June 2026 suspension of two Anthropic models showed. About two-thirds of a data centre's capital cost is imported hardware, and most AI work reaches Australian users over subsea fibre wherever it runs. The say Australia wants is available by another route: the November regulator binds any provider that sells here, wherever its computers sit. Canberra should enforce safety duties and 72-hour incident reporting as unconditional terms of market entry, fund public compute and model portability directly, and hold data centres to hard limits on power, water, consent, and public cost.

**Keywords:** AI governance, data centres, sovereign AI, compute policy, Australian AI Standards, energy and water systems

<!-- more -->

---

## 1. Introduction

Australia has two AI policies. The first governs AI models. On 10 November 2026, Prime Minister Anthony Albanese and three cabinet ministers announced a dedicated AI safety regulator under the forthcoming *Australian AI Standards* legislation [1]. Backed by the Australian AI Safety Institute (AISI) and armed with "significant penalties", it will apply to "all frontier AI companies that wish to operate in Australia" [1]. The test is whether a company serves Australians, not where its computers sit. Covered providers must maintain security controls, manage serious risks, allow independent evaluation, report serious incidents rapidly, and publish safety frameworks [1]. The law follows a failure of voluntary restraint: in June 2026 an OpenAI evaluation agent accessed a Services Australia statistics portal, and Canberra was not told for nearly three months [14, 21].

The second policy governs buildings. A data centre is a warehouse of computers with the power supply and cooling needed to run them, and the largest are sized by the electricity they draw. In March 2026 the Department of Industry, Science and Resources issued voluntary *Expectations* asking data-centre developers to add clean generation, report water use, and train local workers [10]. Expectation 5 went further, asking them to offer Australian researchers, start-ups, and small firms favourable access to computing capacity ("compute") [10]. In July the Prime Minister promised "clear, consistent and mandatory" standards requiring large data centres to supply at least as much energy to the grid as they draw and to fund water infrastructure [2].

A proposal now in circulation joins the two. Its fullest public airing is Joseph Walker's *Compute in Australia* series, whose guests included Assistant Minister for Science, Technology and the Digital Economy Andrew Charlton, Center for a New American Security senior fellow Janet Egan, energy economist Tim Nelson, and Bronte Capital founder John Hempton [24–27]. The question before them was whether Australia should host 10 to 15 gigawatts (GW) of data centres, largely to train AI models for foreign laboratories. For scale, all the data centres now operating on the National Electricity Market (NEM) together draw an average of a little over half a gigawatt [3].

The case for doing so runs as a chain. Australia has land, sunshine, and a close alliance with the United States. If it approves data centres quickly, foreign laboratories will sink tens of billions of dollars here. Having done so, they will have reason to keep Australia supplied with their best models, to cooperate with its safety institute, and to defend its interests in Washington. In this account the buildings are "sovereign AI infrastructure", and helping to build them is a way of governing AI.

I argue that the chain breaks at each link, and that the bargain built on it gets Australia's position backwards. It asks Australia to pay in things it controls (grid capacity, water, consent over land, copyright law) for something a building cannot deliver: a say over AI models owned abroad. That say is available by another route and at no such price, because Parliament can set the terms on which any provider serves Australians.

The note takes the links in order. Section 2 shows that hosting a model's computers confers no control over the model. Section 3 shows that the data centres cannot be justified on economic grounds instead, because the gains from AI come from using it, not from housing it. Section 4 shows that sunk investment gives Canberra little leverage, while the concessions sought in return are real. Section 5 sets out how the *Australian AI Standards* and the data-centre rules should be drafted so that neither is traded for the other.

## 2. A Building Does Not Control What Runs Inside It

The first link in the chain is that a model running on Australian soil is, in some useful sense, under Australian control. June 2026 tested that claim. On 12 June a US export-control directive restricted foreign nationals' access to Anthropic's newest models, *Fable 5* and *Mythos 5* [4]. The notice "did not provide specific details of its national security concern" [4]. Unable to check user nationality in real time, Anthropic suspended both models worldwide, across its own API and third-party cloud regions; *Mythos 5* returned only for US-approved organisations [4, 5]. Where the computers stood made no difference.

The reason lies in how AI services are built. Every commercial model is reached through a **control plane**: the management software that checks who a user is, routes each request, and switches models on or off. The control plane belongs to the provider, and the provider answers to its home government. Guidance from the US Bureau of Industry and Security (BIS) on advanced computing items binds corporate headquarters and ultimate parent companies globally [7]. A server on a Sydney floor still answers to its parent company's home government. Hosting it confers no legal right to keep the model switched on.

"Sovereign AI" runs together two things that are separate in engineering and in law. The **facility stack** is the physical plant: land, buildings, cooling, electricity, and chips. The **model stack** is what runs on it: the control plane, the model itself, and the applications built on top. Table 1 sets out the six layers and asks of each whether hosting it in Australia gives Australia control.

| Layer | What it is | Does hosting it in Australia give Australia control? |
|---|---|---|
| **Facility stack** | | |
| 1. Land, buildings & cooling | Buildings, cooling loops, backup diesel, substations | **Yes.** State planning, water, and land-consent law apply in full. So do the local costs: construction, noise, water draw, land use |
| 2. Electricity | Bulk energy, battery storage, backup generation, grid lines | **Yes.** Connection rules and tariffs decide whether the new load funds clean supply or crowds it out |
| 3. Chips & servers | AI chips (GPUs/TPUs), memory, networking; about 68% of capital cost [12] | **No.** Imported, subject to the maker's export rules, and obsolete within three to five years |
| **Model stack** | | |
| 4. Control plane | Software for identity, scheduling, and traffic routing | **No.** The vendor holds root access. Traffic stays onshore only where rules require it and audits check it |
| 5. Model & safety controls | Trained parameters ("weights"), guardrails, evaluation access | **No.** Follows the maker's home law, unless the weights are held in escrow or the model is self-hosted |
| 6. Applications & data | Enterprise workflows, public-sector records, switching tools | **Partly.** Regulated records can be kept onshore. Dependence on a single vendor is unaffected |

*Table 1. The six layers that "sovereign AI" treats as one asset. Australian authority is complete over the layers whose costs fall locally (1–2) and weak over the layers the bargain is meant to secure (3–5).*

The pattern in the table is the argument of this note in miniature. Hosting gives Australia authority over land, water, and the grid, which it had already. It gives none over the chips, the control plane, or the model, which are what the bargain is meant to secure.

A second fact weakens the link further: the data centres being proposed are not the ones Australian users depend on. *Training* (building a new model) packs tens of thousands of chips into a single power-dense campus [25]. *Inference* (running a trained model to answer requests) divides according to how much delay a task can tolerate. Interactive clinical tools, voice systems, and industrial controls need millisecond response times and so must run near Australian cities. Long-running coding, research, and administrative agents run just as well over subsea fibre from abroad [24, 27]. The hardware is diverging along the same line, as inference moves to specialised chips unlike those in training clusters. A training campus built in regional Australia for export therefore gives Australian hospitals, banks, and public agencies no guarantee that their AI services will keep running during an international disruption.

## 3. The Gains Come from Using AI, Not from Housing It

If hosting does not buy control, the proposal could still be defended as ordinary industry policy: the data centres are worth having for the investment, jobs, and productivity they bring. This fallback matters, because a project that paid its own way would not need the sovereignty label. Three figures are usually offered in its support: the size of the project pipeline, the headline investment, and AI's productivity dividend. Each means less than it appears to.

**The pipeline measures developers' ambition, not Australian need.** In August 2026 the Australian Energy Market Operator (AEMO) counted 225 data-centre projects in development, totalling 67 GW [3]. The record of existing data centres is far more modest. Those operating on the NEM consumed roughly 5 terawatt-hours (TWh) in FY2026, or 3% of grid demand [3]. Average use of their grid connections sat near 27%, facilities took five to ten years to reach full load, and 36% of the projects in AEMO's 2025 forecast had already been cancelled [3]. Hosting 10 to 15 GW at 75% utilisation would consume 65.7 to 98.6 TWh a year, four to six times AEMO's Step Change forecast for FY2030 (15.5 TWh) [3, 25, 26]. Capacity on that scale is not being built for Australian hospitals, schools, or firms. It is a bid for Australian grid capacity to produce compute for export.

**Most of the headline investment leaves at once.** In Epoch AI's cost model for a one-gigawatt AI campus, 68% of capital spending (US$26 billion of US$38 billion) buys chips, servers, and networking hardware [12]. Australia imports virtually all of it. In the national accounts, about two-thirds of every announced dollar is therefore counted as business investment and then subtracted again as imports. As Commonwealth Bank economists note, "[t]he business investment pulse is quite large, but that flow through to GDP is far smaller" [9].

**What stays is modest and competes with other priorities.** The remaining 32% is spent on buildings, electrical fit-out, cooling, and land. It arrives during construction, when large campuses bid for the same scarce electricians, civil trades, and high-voltage transformers needed for housing and grid decarbonisation [9]. Once operating, a data centre employs few people: an industry-commissioned report by Mandala Partners counts around 9,450 ongoing direct and supply-chain jobs in 2026, in a workforce of 15.2 million [19]. The profits of foreign-owned operators, though counted in gross domestic product (GDP), flow offshore. They drop out of gross national income (GNI), which measures the income Australian residents keep.

**The productivity dividend does not depend on where the computers are.** The Productivity Commission estimates that AI could lift labour productivity by 4.3% over the next decade, or roughly 0.4 percentage points a year, nearly doubling the past decade's pace [28]. Australian firms and agencies earn that gain by redesigning everyday tasks, whether the computation happens in Melbourne or Oregon. The owners of the data centres may do much worse. As Hempton warns, capital-heavy infrastructure with low operating costs and rapid chip obsolescence can suffer severe overbuild and weak investor returns even while the services running over it transform the wider economy [27]. Conceding grid priority, water, or tax relief to attract export data centres would shift that overbuild risk from private investors onto Australian ratepayers, in return for a productivity gain that domestic adoption delivers anyway.

## 4. Sunk Investment Is Weak Leverage, and Its Price Is Real

With control and economics set aside, what remains is the bargain in its strongest form: **compute-for-access** [25]. In Egan's account, Australia can offer foreign laboratories fast, predictable approvals, abundant renewable land, and aligned Five Eyes security settings for multi-gigawatt training clusters. Once the laboratories have sunk tens of billions of private dollars onshore, they have reason to defend Australian access in Washington. Canberra can then bargain for guaranteed access to frontier models, dedicated research compute, and close safety cooperation with the AISI [25]. Charlton advances a related case behind Expectation 5: partnerships with the laboratories could turn Australian universities and firms from passive buyers of AI services into intellectual-property partners [24].

Part of this is unobjectionable. Where private developers pay their full physical and fiscal costs, research partnerships cost the public nothing. The difficulty arises when Canberra relies on courting data-centre investment to secure model access or safety cooperation. That reliance fails for three reasons.

First, **Australia already holds a stronger lever, and courtship weakens it**. The November announcement applies mandatory security controls, independent evaluation, and rapid incident reporting to *every* frontier AI provider operating in Australia [1]. It reaches a model trained and hosted anywhere on earth the moment that model serves Australian users, and Canberra timed it deliberately "before a range of major international talks that will cover AI development and investment" [1]. If safety cooperation or research access is instead made conditional on data-centre deals, a statutory duty becomes a negotiated favour, and the companies being regulated gain a bargaining position against their regulator.

Second, **sunk investment gives little leverage when compute is plentiful and none when it is scarce**. If the world overbuilds, or the leading models stay close together, a laboratory with a campus in Australia has many substitutes and owes its host little. In May 2026, leading open-weights models trailed the top closed models by roughly four months on capability benchmarks [11]. If instead a geopolitical crisis makes frontier compute scarce, the provider's home government holds statutory authority over parent companies, replacement chips, and software updates [5, 7]. That authority overrides any memorandum of understanding signed with a host country. Allied hosting can earn a seat in diplomatic consultations, as Carnegie's *Compute Coalition* report argues [23]. It gives Canberra no legal power to override a foreign export order.

Third, **the price is paid in permanent rights for revocable promises**. Contributors to the *Compute in Australia* series noted that foreign laboratories worried about US fair-use litigation might treat Australian copyright licensing as a red line [25]. Yet US courts have already separated lawful training copies from retained pirated libraries (*Bartz v Anthropic* [6]), and the Attorney-General's Department has ruled out a text-and-data-mining exception in favour of licensing certainty [8]. Weakening creators' rights, compressing environmental and Indigenous land-consent processes [20], or entering a tax-exemption race among the states would each give up a lasting domestic protection for a commercial pledge that binds no one. Virginia's legislative auditor offers a warning: US$4.06 billion in data-centre tax exemptions returned just 22 cents of state revenue per dollar forgone [17].

## 5. Recommendations: Keep the Two Policies Apart

The practical conclusion is that the two policies should be drafted so that neither can be traded for the other. Frontier AI providers should owe their duties as a condition of serving Australians. Data centres should be assessed as what they are: large industrial users of power, water, and land. Four recommendations follow, each tied to the layers in Table 1.

**1. Legislate model duties and facility rules separately (Layer 5).** The *Australian AI Standards* Bill should impose the same AISI evaluation access, security rules, and incident-reporting duties on every frontier provider serving Australians, whether hosted onshore or offshore [1]. Notification should fall due within 72 hours, matching European breach rules; the reporting delay in 2026 ran to months [14, 21]. Regulatory, copyright, and safety standards should never be offered as inducements in siting deals.

**2. Measure "net-positive" energy and water by the hour and the catchment (Layers 1–2).** The Prime Minister's July pledge that large data centres return at least as much energy as they draw and fund water infrastructure [2] will fail if it can be met with annual accounting certificates alone. A data centre draws power at a flat rate around the clock. Supplying it takes bulk energy over the year, batteries to move that energy into evening peaks ("shaping"), and backup through multi-day lulls in wind and sun ("firming") [26]. A facility matched to renewables only on an annual basis can still push coal or gas plants harder at peak hours and shift grid-upgrade costs onto households. In Virginia, data-centre demand is projected to add US$14–37 a month to typical residential bills by 2040 [16]. AEMO, the Australian Energy Regulator (AER), and state governments should require projects to fund their own connections and should steer flexible training loads toward grid zones with surplus solar and wind [26]. Water standards should cap both on-site evaporative loss and the water used by upstream power stations, against seasonal local catchment limits [18].

**3. Assess each project through four gates, in strict order (Layers 1–3).** First, the developer discloses the project's workload mix and realistic alternatives, separating domestic needs (low delay, data residency) from export training. Second, the project meets local thresholds that are not open to trade-off: drinking water, grid reliability, biodiversity, and Free, Prior and Informed Consent (FPIC) on Indigenous land [20]. Only then, third, do treasuries weigh the economic case, measured in income retained by residents (GNI) and in pressure on local electrical and civil trades. Fourth, any permit carries an upfront remediation bond and conditions that bind successor owners. National Cabinet should also prevent states from bidding against one another with payroll-tax relief, public land, or places in the grid queue [17].

**4. Buy public compute and model portability directly (Layers 4–6).** Canberra should not rely on voluntary Expectation 5 pledges to pass capability down from commercial export data centres [10]. It should fund pooled public compute for universities and small firms directly, as Canada's Sovereign AI Compute Strategy and Europe's EuroHPC AI Factories do [13, 22]. Within government, the Digital Transformation Agency (DTA) and Australian Signals Directorate (ASD) should require audited domestic routing and the ability to move between vendors, and should avoid "global standard" cloud tiers that process Australian requests offshore. Agencies should also keep vetted open-weights models available as a fallback, on cloud infrastructure certified under ASD's Information Security Registered Assessors Program (IRAP). Where a developer does receive expedited grid coordination, its Expectation 5 promises should become contracted, audited GPU-hour allocations with clear remedies for non-delivery.

## 6. Objections and Limitations

*“Hard limits will drive hyperscale investment to Southeast Asia or the United States.”* Some export training campuses may go elsewhere; capacity serving Australians will not. Workloads that need Australian data residency or millisecond response times must locate near Australian users regardless, as Singapore's oversubscribed capacity allocations under strict efficiency limits demonstrate [15]. And if an export campus is viable in Australia only when households cross-subsidise its grid firming or communities waive water limits, declining to subsidise it protects national welfare.

*“Without gigawatt training clusters onshore, Australia will be rationed out of frontier AI in an international crisis.”* Crisis rationing is a real risk, yet commercial data centres do not prevent it. Onshore hardware did not stop a US export directive from suspending *Fable 5* and *Mythos 5* across global cloud regions in June 2026 [4, 5]. Where allied hosting does strengthen defence or intelligence continuity, Canberra should negotiate binding intergovernmental carve-outs, local weight escrow, and emergency priority rights. Any such campus should be funded from, and judged against, the defence budget, not presented as general economic policy.

*“Wholesale spot prices plus annual renewable certificates already reward storage without hourly matching rules.”* Spot prices do reward batteries when wholesale supply tightens [26]. They do not cover regulated transmission lines and substations, whose multi-decade costs still fall on captive residential customers if forecast loads disappoint or network tariffs lag [16]. Upfront connection funding and firming conditions remain a necessary backstop.

**Limitations.** Project-level Australian power contracts, cooling designs, and foreign-ownership shares remain largely commercial-in-confidence. The March 2026 *Expectations* have not yet undergone a public compliance audit [10], and the full text of the *Australian AI Standards* Bill remained unreleased at the time of writing [1]. Standardised public metering of facility power draw, water consumption, and contracted research compute would make every link in this argument empirically testable.

## 7. Conclusion

The "sovereign AI" bargain treats a building as though it carried authority over what runs inside it. It does not. Control of a frontier model rests with its owner and its owner's government, and no amount of Australian concrete changes that. What Australia does control is its own grid, water, land, and law, which the bargain asks it to concede, and its own market, which the bargain overlooks. Any laboratory that wants Australian customers is already within Parliament's reach. Canberra can require independent evaluation, security controls, and prompt incident reporting without owing anything to the companies that build data centres [1]. The *Australian AI Standards* should keep the two policies apart. Frontier AI providers owe unconditional duties as the price of market entry; data centres meet hard limits on power, water, consent, and public cost before they draw on shared grids and catchments.

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

[7] Bureau of Industry and Security (BIS). 2026. *Guidance Regarding Enforcement of License Requirements for Advanced Computing Items for Entities Headquartered in Country Group D:5 and Macau*. US Department of Commerce, 31 May 2026. <https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf>

[8] Commonwealth Attorney-General's Department. 2025. *Copyright and Artificial Intelligence Reference Group (CAIRG)*. Australian Government, October 2025 update. <https://www.ag.gov.au/rights-and-protections/copyright/copyright-and-artificial-intelligence-reference-group-cairg>

[9] Commonwealth Bank of Australia. 2026. *Australia's data centre boom: a $150 billion investment opportunity*. CommBank Newsroom, 6 August 2026. <https://www.commbank.com.au/articles/newsroom/2026/08/australias-data-centre-boom.html>

[10] Department of Industry, Science and Resources. 2026. *Expectations of data centres and AI infrastructure developers*. Australian Government, 23 March 2026. <https://www.industry.gov.au/publications/expectations-data-centres-and-ai-infrastructure-developers>

[11] Epoch AI. 2026. *Open models lag state-of-the-art closed models by 4 months*. Epoch AI Data Insights, 29 May 2026. <https://epoch.ai/data-insights/open-closed-eci-gap>

[12] Epoch AI. 2026. *Total Cost of Ownership of a One-Gigawatt AI Data Center*. Epoch AI Data Insights, May 2026. <https://epoch.ai/data-insights/ai-datacenter-cost-breakdown>

[13] EuroHPC Joint Undertaking. 2025. *AI Factories Access Modes*. European Union, 2025. <https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en>

[14] Erin Handley. 2026. *OpenAI hacked Medicare portal, Prime Minister Anthony Albanese says*. ABC News, 24 September 2026. <https://www.abc.net.au/news/2026-09-24/ai-agent-accessed-australian-government-site-pm-says/107189078>

[15] Infocomm Media Development Authority (IMDA) and Economic Development Board, Singapore. 2026. *Four Data Centre Proposals Selected as Part of Second Data Centre Call for Application*. Singapore Government, 21 August 2026. <https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/four-data-centre-proposals-selected-as-part-of-second-data-centre-call-for-application>

[16] Joint Legislative Audit and Review Commission (JLARC). 2024. *Data Centers in Virginia*. Commonwealth of Virginia, December 2024. <https://jlarc.virginia.gov/landing-2024-data-centers-in-virginia.asp>

[17] Joint Legislative Audit and Review Commission (JLARC). 2026. *Economic Development Incentives 2026*. Report 623, Commonwealth of Virginia, November 2026. <https://jlarc.virginia.gov/pdfs/reports/Rpt623.pdf>

[18] Arman Shehabi et al. 2024. *2024 United States Data Center Energy Usage Report*. Lawrence Berkeley National Laboratory, December 2024. <https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report>

[19] Mandala Partners. 2026. *The Economic Contribution of the Data Centre Industry in Australia*. Commissioned by Data Centres Australia, August 2026. <https://datacentres.org.au/wp-content/uploads/2026/08/2026-08_DCA-Mandala-The-Economic-Contribution-of-the-Data-Centre-Industry-in-Australia-digital.pdf>

[20] Northern Land Council. 2026. *Submission 207 to the Senate Environment and Communications References Committee Inquiry into Artificial Intelligence and Data Centres*. Parliament of Australia, September 2026. <https://www.aph.gov.au/DocumentStore.ashx?id=64091ae6-dec5-47ec-a083-b32aa60fc35b&subId=803365>

[21] OpenAI. 2026. *How we will do better for Australia*. OpenAI, 28 September 2026 (updated 4 October 2026). <https://openai.com/index/how-we-will-do-better-for-australia/>

[22] OECD. 2026. *Securing AI Compute: Government Policy Approaches*, 13 October 2026 (<https://www.oecd.org/en/publications/securing-ai-compute_7f96dc99-en/full-report.html>); Innovation, Science and Economic Development Canada, *Canadian Sovereign AI Compute Strategy*, launched December 2024 (updated 4 June 2026) (<https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy>).

[23] Alasdair Phillips-Robins, Teddy Tawil, and Sam Winter-Levy. 2026. *The Compute Coalition: How to Build the Future of AI in the Free World*. Carnegie Endowment for International Peace, 8 June 2026. <https://carnegieendowment.org/research/2026/06/the-compute-coalition-how-to-build-the-future-of-ai-in-the-free-world>

[24] Joseph Walker. 2026. *Australia's Plan to Turn Compute Into Sovereign AI — Dr Andrew Charlton MP*. The Joe Walker Podcast, 16 August 2026. <https://josephnoelwalker.com/andrew-charlton/>

[25] Joseph Walker. 2026. *The Geostrategic Case for Compute in Australia — Janet Egan*. The Joe Walker Podcast, 27 August 2026. <https://josephnoelwalker.com/janet-egan/>

[26] Joseph Walker. 2026. *AI Factories in the Outback — Tim Nelson*. The Joe Walker Podcast, 14 October 2026. <https://josephnoelwalker.com/tim-nelson/>

[27] Joseph Walker. 2026. *"Fibre Optics Mark II": Why Data Centres Will Change the World and Bankrupt Their Builders — John Hempton*. The Joe Walker Podcast, 4 November 2026. <https://josephnoelwalker.com/john-hempton/>

[28] Productivity Commission. 2025. *Harnessing data and digital technology*. Inquiry Report, Australian Government, 19 December 2025 (<https://www.pc.gov.au/inquiries-and-research/data-digital/>); see also Joseph Walker, *How Can Australia Get a Piece of the AI Action? — Danielle Wood*, The Joe Walker Podcast, 4 June 2026 (<https://josephnoelwalker.com/danielle-wood/>).
