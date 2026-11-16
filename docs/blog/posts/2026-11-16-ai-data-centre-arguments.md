---
title: "How to read the fight over AI data centres"
date: 2026-11-16
description: "Six contested links sit between pouring concrete for a server hall and achieving public value. Mapping the case for and against at each link, its nuances, and how to weigh the evidence."
tags:
  - ai
  - data-centres
  - strategy
  - political-economy
---

When a developer proposes a multibillion-dollar AI data centre, two camps form immediately. Supporters see indispensable infrastructure that brings investment, raises productivity, and secures national sovereignty. Critics see a warehouse of imported chips that claims scarce electricity, water, and land while leaving few lasting jobs behind.

Smart people look at the same building and reach opposite verdicts because **AI facility** capacity and **Public value** sit at opposite ends of a long causal chain. Headline arguments skip the middle of that chain. One camp treats announced megawatts and capital spending as proof of national gain; the other treats resource draw as proof of net harm.

![An AI facility on the left and public value on the right. Boosters draw a dashed shortcut across the top claiming capacity equals prosperity and control; critics draw a dashed shortcut across the bottom claiming capacity equals a power and water drain, skipping six faint boxes in the middle.](../blog_assets/ai_data_centres_shortcut.png)

Before weighing competing studies, it helps to see the whole map of the debate. Six contested links sit between pouring concrete for a server hall and achieving a good public outcome: onshore need, retained money and skills, power and water systems, host communities, sovereign control, and subsidy politics. Walking through the strongest case for and against at each link, the nuances inside it, and the measurement traps to check when evidence arrives gives policy readers a clear framework before a single number is cited.

<!-- more -->

## Demand and location

The first dispute is whether new facilities are needed at all, and whether domestic AI use requires domestic buildings.

**The case for building** starts with physical scale. Training frontier AI models and running them reliably for millions of users requires dense, specialised computing clusters that scattered office servers cannot provide. Even when software improvements cut the computing needed for a single query, cheaper and better AI can expand total usage fast enough to push overall demand higher. Falling short of capacity risks higher prices, slower domestic adoption, and reliance on whichever firms and countries built ahead. Public research, health systems, defence, and emergency services may also need dedicated capacity they can count on when commercial queues tighten.

**The case against** separates market demand from social need, and global demand from local siting. Anticipated commercial demand can reflect speculative land-banking, rival firms duplicating clusters, or low-value uses, while universities and civic projects remain priced out. Better model design, workload scheduling, and fuller use of existing halls can meet part of projected growth without pouring as much concrete. Above all, a country can consume AI services produced abroad over undersea fibre cables, just as most countries import software or phones without hosting semiconductor fabs. Domestic appetite for AI tools does not by itself prove a need for domestic server halls.

**Where the nuance sits** is in the type of computing task, known as the **workload**, and in the **counterfactual** (what happens if this specific project is not built). **Training** builds or updates a model and can often run wherever power and chips are cheapest, though the largest runs prize single massive campuses. **Inference** uses a trained model to answer requests: real-time voice, clinical, or industrial control needs low response delay near users, whereas overnight coding agents or batch analysis can run almost anywhere. Sensitive government, health, or financial workloads may stay onshore for legal rather than technical reasons. Meanwhile, the realistic alternative to a greenfield campus is rarely doing nothing. It may be expanding an existing site, phasing construction, importing compute for mobile tasks, or putting public effort into helping local firms use AI rather than hosting it.

**How to weigh the evidence:** Never treat an announced development pipeline as proof of needed capacity. Separate four different quantities: **announced pipeline**, **contracted grid connections**, **installed IT power**, and **actual utilisation**. In Australia, the electricity market operator counted 67 gigawatts of data-centre projects in its 2026 pipeline, yet average grid-connection utilisation across operating sites sat near 27%, and 36% of developing projects from the previous year's forecast had been cancelled ([AEMO, 2026](https://www.aemo.com.au/-/media/files/electricity/nem/planning_and_forecasting/nem_esoo/2026/2026-esoo-data-centre-forecasting-overview.pdf)). Pipeline totals measure developer option-taking rather than verified social need.

Even when a workload genuinely belongs onshore, physical necessity settles only the first link. The next question is how much economic value stays behind.

## Money and capability

A facility with a ten-billion-dollar price tag sounds like a ten-billion-dollar boost to the host economy, which is why headline capital spending dominates political announcements.

**The case for economic value** runs through three channels. Construction creates work for civil contractors, electricians, cooling specialists, and engineers. Operation generates corporate taxes, land rates, and ongoing demand for maintenance and energy services; judging a capital-intensive asset solely by permanent headcount inside the fence would dismiss ports, wind farms, and telecommunications networks too. Most importantly, accessible computing is an enabling input: its main economic payoff comes when businesses, hospitals, and agencies redesign everyday tasks to raise output per hour worked across the wider economy.

**The case against** follows where the money actually goes. In [Epoch AI's cost breakdown](https://epoch.ai/data-insights/ai-datacenter-cost-breakdown), roughly two-thirds of capital spending per gigawatt of IT power (US$26 billion of US$38 billion) buys specialised chips, servers, and networking hardware. Outside a handful of hardware-exporting economies, almost all of that equipment is imported. In national accounting, imported machines enter **gross domestic product (GDP)** as business investment and subtract straight back out as imports, leaving domestic value added mostly in the building shell, electrical fit-out, and local services. Once running, foreign-owned halls record their output in domestic GDP, yet profits sent to overseas shareholders drop out of **gross national income (GNI)**, which measures what residents actually keep. During construction booms, giant campuses can also bid scarce electricians, transformers, and builders away from housing and grid upgrades. And a turnkey hall filled with imported racks and managed by offshore software can depreciate fast as chips age, leaving little lasting domestic technical capability.

**Where the nuance sits** is in keeping three tests apart: **whether AI is useful to adopters**, **whether data centres are profitable for private investors**, and **whether hosting creates net public value**. Fierce competition, heavy upfront capital, and rapid chip obsolescence can crush investor returns even while AI transforms industries, or generate private rents while shifting infrastructure costs onto the public. Analysts must also avoid double-counting. One local building cannot claim credit for the productivity gains of domestic AI adoption if local firms could have accessed the same models from existing or overseas servers; only the facility's *additional* contribution counts.

**How to weigh the evidence:** Check four distinctions in any economic-impact study:

1. **Gross spending versus domestic value added** after subtracting direct and indirect hardware imports.
2. **GDP versus resident income (GNI)** after foreign profit repatriation and tax concessions.
3. **Direct full-time-equivalent jobs versus multiplier counts.** Industry reports frequently bundle direct staff, supplier roles, and part-time work through input-output multipliers (for instance, [Mandala's Australian industry report](https://datacentres.org.au/wp-content/uploads/2026/08/2026-08_DCA-Mandala-The-Economic-Contribution-of-the-Data-Centre-Industry-in-Australia-digital.pdf)), which national statistical agencies warn overstate net employment when labour markets are tight.
4. **Facility activity versus enabled downstream output.** As [Ireland's enterprise assessment](https://enterprise.gov.ie/en/publications/publication-files/the-value-of-data-centres-to-ireland.pdf) illustrates, cumulative upstream value added and annual enabled-sector value added are different quantities that cannot simply be added together.

Tracing demand and money fills in the upper half of our map, yet every server hall also plugs into local wires, pipes, and land.

## Power, water, and land

While commercial revenues travel across borders through contracts, physical resource claims land in a specific grid zone and river basin at a specific hour. Adding **1. Demand & site** and **2. Money & skills** along the top of our drawing, and **3. Power & water** alongside **4. Host places** below them, shows why the debate splits into two parallel chains.

![The middle of the map splits into two bands. Claimed benefits and control on top now hold 1. Demand & site and 2. Money & skills, with a third slot still faint. Physical, local and political risks below hold 3. Power & water and 4. Host places, with a third risk slot and the bottom policy band still faint.](../blog_assets/ai_data_centres_two_chains.png)

**The case that data centres help physical transitions** rests on scale and creditworthiness. Large, solvent operators can sign long-term power-purchase contracts that underwrite new wind, solar, battery, and transmission projects. Sited behind transmission bottlenecks, a campus can buy renewable electricity that would otherwise go to waste. If some AI workloads can pause or shift during evening peaks, spread-out power consumption could even spread fixed grid costs across more megawatt-hours. On water and land, proponents point out that consolidating workloads into modern halls beats running thousands of inefficient corporate closets, and that closed-loop or air cooling, recycled industrial water, and brownfield industrial land can keep local environmental footprints small.

**The case that expansion strains grids and ecosystems** focuses on speed, timing, and concentration. Large, flat round-the-clock loads can arrive years faster than new generation and high-voltage lines. When they do, grids keep coal or gas plants running longer to cover the extra load, raising **marginal emissions** (the pollution from the extra generator turned on) even if average grid power looks clean. Network upgrades built to serve new campuses can spill onto household and business electricity bills. Efficiency gains per computation do not guarantee lower total energy or water use if falling unit costs spur a larger jump in total computing. In hot, dry regions, evaporative cooling competes directly with towns, farms, and river ecosystems during summer droughts. Looking only inside the site fence also misses upstream mineral mining and chip fabrication, diesel backup generators, new transmission corridors, and electronic waste at the end of chip life.

**Where the nuance sits** is in matching physical engineering rather than annual averages. An electricity system needs three distinct things: **bulk energy** over the year, **shaping** (storage to shift solar and wind across hours), and **firming** (dispatchable supply through multi-day wind and solar lulls). Buying annual renewable certificates equal to yearly consumption does not supply local hourly shaping and firming. Paying today's regulated power tariff also differs from covering tomorrow's system build. Virginia's legislative auditor found that data centres paid their full cost of service under existing tariffs, yet projected that extra generation and transmission demand could still add US$14–37 a month in real dollars to a typical Dominion residential bill by 2040 ([JLARC, 2024](https://jlarc.virginia.gov/landing-2024-data-centers-in-virginia.asp)). Cooling carries engineering trade-offs too: dry cooling saves local water at the price of higher electricity draw. And refusing a project in a clean, wet region can shift rather than reduce global emissions if the workload moves to a coal-heavy, water-stressed grid instead.

**How to weigh the evidence:** Put five checks on any energy or environmental claim:

1. **Scenario ranges, not single destiny lines.** Treat projections like the [International Energy Agency's 2026](https://www.iea.org/reports/key-questions-on-energy-and-ai) global central case (around 950 terawatt-hours by 2030) or [Lawrence Berkeley National Laboratory's 2025](https://escholarship.org/uc/item/33m6w3x0) US bounds (521–843 terawatt-hours) as assumption-sensitive scenarios rather than meter readings.
2. **Regional concentration, not just global share.** Data centres used about 1.5% of global electricity in 2024 ([IEA, 2025](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)), yet reached 23% of all metered electricity in Ireland in 2025 ([CSO, 2026](https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2025/keyfindings/)). Grids fail locally, not globally.
3. **Physical additionality and hourly delivery** rather than annual certificate matching alone, and system-wide auction or bill effects (such as [PJM's market monitor](https://www.monitoringanalytics.com/reports/Reports/2025/IMM_Analysis_of_the_20262027_RPM_Base_Residual_Auction_Part_A_20251001.pdf) modelling capacity-cost jumps) alongside current retail rates.
4. **Water withdrawal versus consumption, and direct versus indirect water.** **Withdrawal** returns to the river or pipe; **consumption** evaporates. [LBNL's 2024 study](https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report) also estimated indirect US water consumed generating electricity for data centres at roughly twelve times direct on-site cooling water in 2023. Both must be judged against local seasonal scarcity rather than global company-wide replenishment totals.
5. **Lifecycle boundaries** that include enabling transmission lines, backup generators, hardware supply chains, and decommissioning ([UNCTAD, 2024](https://unctad.org/publication/digital-economy-report-2024)).

Because physical burdens concentrate in specific postcodes while AI services spread worldwide, technical system analysis leads straight into fairness.

## Host communities

Even when a project passes a national cost-benefit test, gains and burdens rarely fall on the same people.

**The case that projects help host communities** points to local council rates, civil construction contracts, technical apprenticeships, and shared road or substation upgrades, alongside negotiated community benefit funds. Supporters also argue that every national network, from railways to high-voltage lines, places concentrated infrastructure in a few towns so millions of citizens can use the service, and that fair compensation is the right way to handle local disruption.

**The case against** highlights a sharp mismatch of power and permanence. Revenues flow to global technology shareholders and urban enterprise users, while construction traffic, transformer hum, visual bulk, diesel backup testing, and pressure on local land, water, and grid queues remain permanently with host residents. Specialist operational staff often commute in from outside, and state or municipal tax breaks can strip away the promised fiscal windfall. Fast-tracked planning pathways can also reduce community involvement to box-ticking after site deals are already signed, an acute risk on Indigenous estates where representative bodies such as Australia's [Northern Land Council](https://www.aph.gov.au/DocumentStore.ashx?id=64091ae6-dec5-47ec-a083-b32aa60fc35b&subId=803365) have pressed for free, prior, and informed consent, cumulative precinct assessment, and funded end-of-life cleanup.

**Where the nuance sits** is in separating **compensable inconvenience** from **non-negotiable thresholds and rights**. Benefit-sharing payments or lower council rates can fairly offset temporary disruption or lost amenity; they cannot justify breaching safe drinking-water limits, grid reliability floors, or legal consent rights. Labour effects also span four distinct groups that should never be collapsed into one job number: temporary local tradespeople (who gain work, though sometimes pulled from housing builds), small permanent site crews, overseas mineral and hardware workers, and domestic workers whose own jobs AI tools reshape.

**How to weigh the evidence:** Check net local public revenue *after* subtracting tax exemptions and publicly funded enabling infrastructure, verify who carries financial liability if a campus closes early, and distinguish genuine early decision rights from post-announcement consultation sessions.

If local economics and resource pressures were the whole story, many governments would treat data centres like any other large industrial warehouse. What elevates them into cabinet rooms is the promise of national sovereignty.

## Sovereignty and leverage

Governments increasingly back AI campuses less for local jobs than for national security, resilience, and geopolitical bargaining power.

**The case for domestic sovereignty** begins with legal reach and physical continuity. Keeping sensitive health, tax, defence, and critical-infrastructure workloads onshore ensures domestic privacy and security laws apply and protects essential services if foreign links are disrupted. Operating advanced clusters locally can also build domestic engineering talent and supplier networks. Going a step further, strategists in energy-rich allies such as Australia argue for **compute-for-access**: if global AI labs sink tens of billions of private dollars into local gigawatt training clusters, their dependence on host-country sites and power could give the host government leverage for guaranteed frontier model access, safety transparency, or allied standing ([Compute Coalition, 2026](https://carnegieendowment.org/research/2026/06/the-compute-coalition-how-to-build-the-future-of-ai-in-the-free-world); [Walker Compute Series, 2026](https://josephnoelwalker.com/janet-egan/)).

**The case against** warns that **physical location is routinely mistaken for sovereign control**. A server hall on domestic soil can be owned by a foreign parent company, run imported chips governed by extraterritorial export licences (such as [US Bureau of Industry and Security rules](https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf) that follow parent nationality across borders), depend on proprietary offshore software, and serve mostly foreign customers. In a diplomatic or commercial crunch, the host country owns the concrete while foreign executives and foreign law control the switch. Concentrating critical public services into two or three giant cloud campuses can also create single points of cyber, power, and vendor-lock-in failure. As for compute-for-access leverage, bargaining power erodes if workloads are portable inference jobs that reroute overnight, if global overbuilding leaves operators with spare sites elsewhere, or if a lab's home government overrides commercial promises.

**Where the nuance sits** is that sovereignty is a bundle of **eight separable rights**, not a binary badge earned by pouring domestic concrete:

- **Residency:** where data and computation physically sit.
- **Jurisdiction:** whose laws apply and can actually be enforced.
- **Ownership:** who owns the assets and collects the returns.
- **Operational control:** who can direct, inspect, or halt computing runs.
- **Access:** who is guaranteed capacity in normal markets and during crises.
- **Capability:** what domestic workers and institutions know how to build and run.
- **Exit:** whether users can move data and workloads to another provider without prohibitive cost.
- **Resilience:** whether critical services keep running through technical or geopolitical shocks.

Different public goals need different slices of that bundle. Pooled cross-border research clusters like Europe's [EuroHPC AI Factories](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en) or dedicated public funds like [Canada's Sovereign AI Compute Strategy](https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy) can secure research and small-business access directly without underwriting gigawatts of private commercial halls ([OECD, 2026](https://www.oecd.org/en/publications/securing-ai-compute_7f96dc99-en/full-report.html)).

**How to weigh the evidence:** Whenever a proposal invokes "sovereign AI", ask which of the eight rights is written into binding contracts and technical architecture, whether the workload is sticky frontier training or mobile inference, and what domestic users can still run if a foreign vendor or foreign regulator withdraws support.

Once governments decide to court, steer, or bargain with operators for these strategic goals, one final link enters the map: the politics of public intervention itself.

## Subsidies and power

Markets left alone can misprice shared grids and water, yet active government backing introduces its own predictable failures.

**The case for active government involvement** is coordination. No single private developer can align multi-year transmission planning, regional water caps, skills pipelines, and security standards on its own. Proactive governments can steer campuses toward strong grid nodes, resolve permitting bottlenecks that stall clean-energy builds alongside compute, and attach public-interest conditions before approvals are granted. Standing completely aside while rival jurisdictions court mobile capital can also leave a country with weaker infrastructure and less voice in technical standards.

**The case against** centres on **subsidy races, asymmetric information, and political lock-in**. Because hyperscale capital is mobile across states and countries, developers can play jurisdictions against one another to extract sales-tax exemptions, discounted land, or priority grid access for facilities they would have built anyway. Virginia's legislative auditor estimated that state data-centre tax exemptions totalled US$4.06 billion over FY2016–FY2025 and returned just 22 cents of state revenue per dollar foregone once realistic location assumptions were applied ([JLARC, 2026](https://jlarc.virginia.gov/pdfs/reports/Rpt623.pdf)). Operators also know far more than local planners about actual load curves, cooling needs, chip lifespans, and contract cancellation risks. Concentrated developer, property, and construction interests organise more easily than millions of households bearing diffuse grid costs. And once a government commits public transmission upgrades and political prestige to an AI hub, **power feedback** sets in: enforcing conditions or refusing later expansion stages becomes politically harder because the project has built its own constituency.

**Where the nuance sits** is in separating **project additionality** (what the facility adds compared with realistic alternatives) from **support additionality** (what a tax break or fast-track approval actually changed), and separating **voluntary expectations** from **enforceable obligations**. Non-binding policy signals, such as [Chile's monitored regional agreements](https://www.minciencia.gob.cl/uploads/filer_public/29/c7/29c71595-69d1-4b1f-be58-b6946a1967f2/national_data_centers_plan.pdf) or [Australia's federal developer expectations](https://www.industry.gov.au/publications/expectations-data-centres-and-ai-infrastructure-developers), can clarify government priorities early, yet promises without metered baselines, public disclosure, decommissioning bonds, and transferable penalties rarely survive changes in ownership or market pressure.

**How to weigh the evidence:** Look for independent ex-post audits of whether concessions changed siting decisions, check whether resource reporting is publicly metered rather than hidden behind commercial confidentiality, and verify which regulator holds power over cumulative regional load rather than isolated site permits.

## Three policy decisions

Placing **5. Sovereignty** and **6. Subsidies** into the map completes the argument structure and reveals why a blanket "accelerate" or "block" posture fails. Governments are never making one big decision about data centres; as the bottom band shows, they face **National strategy**, **Policy levers**, and a **Project gate** as three distinct choices.

![The completed map connects an AI facility to public value across all six contested links: 1. Demand & site, 2. Money & skills, and 5. Sovereignty along the top benefit-and-control band; 3. Power & water, 4. Host places, and 6. Subsidies along the middle risk band; and three separate policy decisions across the bottom: National strategy, Policy levers, and Project gate.](../blog_assets/ai_data_centres_map.png)

Keeping those three levels separate prevents a sound national ambition from rubber-stamping a bad local site, or a good single facility from masquerading as a national AI strategy:

| Decision level | Question it answers | What good policy looks like |
|---|---|---|
| **National strategy** | What public outcomes is the country seeking from AI infrastructure? | Targets for AI adoption, retained resident income, domestic skills, grid reliability, and named sovereign rights rather than a raw gigawatt target |
| **Policy levers** | Which rule or price addresses each system risk, and who runs it? | Separate instruments matched to each link: connection tariffs and firming rules for power; basin caps for water; skills, competition, and public compute pools for capability; security and portability law for sovereignty; strict additionality tests for subsidies |
| **Project gate** | Should this specific facility proceed here, now, and on what terms? | A sequential test: define workload and counterfactuals; enforce hard thresholds on water, power reliability, environment, and local consent before trade-offs; check net capture; bind monitoring and cleanup into enforceable obligations |

At the **Project gate**, keeping thresholds ahead of trade-offs is decisive: promised construction spending or national AI prestige should never cancel out a breached drinking-water limit, an unfinanced household bill hike, or overridden community consent. And every outcome must stay genuinely live: **approve**, **approve with binding conditions**, **phase capacity**, **relocate or redesign**, **defer until grid prerequisites exist**, and **reject** (as [Singapore's shift](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/four-data-centre-proposals-selected-as-part-of-second-data-centre-call-for-application) from a building pause to selective, efficiency-bound capacity allocation illustrates under tight land and energy limits).

Finally, this structure clarifies what empirical research can settle and what remains a political value choice. Studies can measure import shares, hourly marginal grid emissions, aquifer drawdown, contract portability, and subsidy additionality. Depending on what that evidence shows in a given country, rational policy shifts accordingly:

- **If ordinary electricity tariffs, water caps, and planning rules already internalise system costs**, governments need less bespoke data-centre intervention.
- **If most valuable AI tasks can run cleanly across borders while local halls retain little income or capability**, policy effort should shift from courting server buildings toward funding domestic AI skills and adoption.
- **If sticky workloads deliver genuine sovereign resilience, research access, and net resident income within hard power and water limits**, conditional facilitation is well earned.
- **If local resource limits or governance capacity cannot protect host communities and bill-payers**, restraint or refusal is the right call.

Even with perfect data, however, evidence alone cannot decide how much local disruption is worth trading for national growth, how high a premium citizens should pay to keep computing onshore, or how precautionary to be when demand forecasts could prove wrong. Laying out the full map pro and against does not erase those value choices; it puts them in plain sight where democratic policy can argue them honestly.

## Sources

- Australian Energy Market Operator, [*2026 ESOO Data Centre Forecasting Overview*](https://www.aemo.com.au/-/media/files/electricity/nem/planning_and_forecasting/nem_esoo/2026/2026-esoo-data-centre-forecasting-overview.pdf), August 2026.
- Bureau of Industry and Security, [*Guidance Regarding Enforcement of License Requirements for Advanced Computing Items*](https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf), May 2026.
- Central Statistics Office Ireland, [*Data Centres Metered Electricity Consumption 2025*](https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2025/keyfindings/), July 2026.
- Department of Industry, Science and Resources Australia, [*Expectations of data centres and AI infrastructure developers*](https://www.industry.gov.au/publications/expectations-data-centres-and-ai-infrastructure-developers), March 2026.
- Epoch AI, [*Total Cost of Ownership of a One-Gigawatt AI Data Center*](https://epoch.ai/data-insights/ai-datacenter-cost-breakdown), May 2026.
- EuroHPC Joint Undertaking, [*AI Factories Access Modes*](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en), 2025.
- Infocomm Media Development Authority Singapore, [*Four Data Centre Proposals Selected as Part of Second Data Centre Call for Application*](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/four-data-centre-proposals-selected-as-part-of-second-data-centre-call-for-application), August 2026.
- Innovation, Science and Economic Development Canada, [*Canadian Sovereign AI Compute Strategy*](https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy), June 2026.
- International Energy Agency, [*Energy and AI*](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai), 2025, and [*Key Questions on Energy and AI*](https://www.iea.org/reports/key-questions-on-energy-and-ai), 2026.
- Joint Legislative Audit and Review Commission Virginia, [*Data Centers in Virginia*](https://jlarc.virginia.gov/landing-2024-data-centers-in-virginia.asp), 2024, and [*Economic Development Incentives 2026*](https://jlarc.virginia.gov/pdfs/reports/Rpt623.pdf), 2026.
- Joseph Walker, [*The Geostrategic Case for Compute in Australia (Janet Egan)*](https://josephnoelwalker.com/janet-egan/), August 2026.
- KPMG for Department of Enterprise, Tourism and Employment Ireland, [*The Value of Data Centres to Ireland*](https://enterprise.gov.ie/en/publications/publication-files/the-value-of-data-centres-to-ireland.pdf), March 2026.
- Lawrence Berkeley National Laboratory, [*2024 United States Data Center Energy Usage Report*](https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report), 2024, and [*2025 Update*](https://escholarship.org/uc/item/33m6w3x0), June 2026.
- Mandala Partners for Data Centres Australia, [*The Economic Contribution of the Data Centre Industry in Australia*](https://datacentres.org.au/wp-content/uploads/2026/08/2026-08_DCA-Mandala-The-Economic-Contribution-of-the-Data-Centre-Industry-in-Australia-digital.pdf), August 2026.
- Ministry of Science, Technology, Knowledge and Innovation Chile, [*National Data Centers Plan*](https://www.minciencia.gob.cl/uploads/filer_public/29/c7/29c71595-69d1-4b1f-be58-b6946a1967f2/national_data_centers_plan.pdf), 2024.
- Monitoring Analytics, [*Analysis of the 2026/2027 RPM Base Residual Auction, Part A*](https://www.monitoringanalytics.com/reports/Reports/2025/IMM_Analysis_of_the_20262027_RPM_Base_Residual_Auction_Part_A_20251001.pdf), October 2025.
- Northern Land Council, [*Submission 207 to the Senate Inquiry into AI and Data Centres*](https://www.aph.gov.au/DocumentStore.ashx?id=64091ae6-dec5-47ec-a083-b32aa60fc35b&subId=803365), September 2026.
- OECD, [*Securing AI Compute: Government Policy Approaches*](https://www.oecd.org/en/publications/securing-ai-compute_7f96dc99-en/full-report.html), October 2026.
- Phillips-Robins, A., Tawil, T. and Winter-Levy, S., [*The Compute Coalition*](https://carnegieendowment.org/research/2026/06/the-compute-coalition-how-to-build-the-future-of-ai-in-the-free-world), Carnegie Endowment, June 2026.
- UN Trade and Development, [*Digital Economy Report 2024*](https://unctad.org/publication/digital-economy-report-2024), July 2024.
