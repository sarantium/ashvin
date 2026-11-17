---
title: "Build the Data Centres, Govern the Models"
slug: concrete-is-not-control
date: 2026-11-16
description: "Policy note: Approving a data centre and governing an AI model are separate decisions. Data centres that pay their own costs get a fast, published path to approval. AI providers owe safety duties as a condition of market entry. Neither is traded for the other."
tags:
  - ai
  - data-centres
  - australia
  - strategy
  - political-economy
---

**ASHVIN PARAMESWARAN**, Sydney, Australia

**Abstract.** Approving a data centre and governing an AI model are separate decisions, and Australia should make them separately. The "sovereign AI" proposal joins them. It holds that if Australia approves very large data centres quickly, the foreign laboratories that use them will repay it with model access, safety cooperation, and strategic weight.

This note argues that the trade fails. A building confers no authority over the model that runs inside it: a model answers to its owner's home government wherever its computers sit. The economic gains from AI come from using it, not from housing it. Australia's authority over models has a different source, the terms it sets on entry to its market, and linking those terms to investment weakens them.

Each decision should be made on its own terms. Data centres that meet clear limits on power, water, consent, and public cost should be approved quickly, through a published path. AI providers should owe safety duties and 72-hour incident reporting as unconditional terms of market entry. Research compute should be funded directly.

**Keywords:** AI governance, data centres, sovereign AI, compute policy, Australian AI Standards, energy and water systems

<!-- more -->

---

## 1. Introduction

AI runs on data centres, and Australia is a good place to build them. It has land, sun and wind, stable institutions, and a close alliance with the United States. Investors have noticed. The Australian Energy Market Operator (AEMO) counts 225 data-centre projects in development [3], and Commonwealth Bank describes a $150 billion investment opportunity [9]. Projects that pay their own costs should be built, and approved quickly. The question for policy is what Australia gains from them, what they cost, and who sets the terms.

That question has become tangled with a second one, because Australia now has two AI policies.

**The first governs AI models.** On 10 November 2026, Prime Minister Anthony Albanese and three cabinet ministers announced a dedicated AI safety regulator under the forthcoming *Australian AI Standards* legislation [1]. Backed by the Australian AI Safety Institute (AISI) and armed with "significant penalties", it will apply to "all frontier AI companies that wish to operate in Australia" [1]. The test is whether a company serves Australians, not where its computers sit. Covered providers must maintain security controls, manage serious risks, allow independent evaluation, report serious incidents rapidly, and publish safety frameworks [1]. The law follows a failure of voluntary restraint: in June 2026 an OpenAI evaluation agent accessed a Services Australia statistics portal, and Canberra was not told for nearly three months [14, 21].

**The second governs buildings.** A data centre is a warehouse of computers with the power supply and cooling needed to run them, and the largest are sized by the electricity they draw. In March 2026 the Department of Industry, Science and Resources issued voluntary *Expectations* asking data-centre developers to add clean generation, report water use, and train local workers [10]. Expectation 5 went further, asking them to offer Australian researchers, start-ups, and small firms favourable access to computing capacity ("compute") [10]. In July the Prime Minister promised "clear, consistent and mandatory" standards requiring large data centres to supply at least as much energy to the grid as they draw and to fund water infrastructure [2].

**A proposal now in circulation joins the two.** Its fullest public airing is Joseph Walker's *Compute in Australia* series, whose guests included Assistant Minister for Science, Technology and the Digital Economy Andrew Charlton, Center for a New American Security senior fellow Janet Egan, energy economist Tim Nelson, and Bronte Capital founder John Hempton [24–27]. The question before them was whether Australia should host 10 to 15 gigawatts (GW) of data centres, largely to train AI models for foreign laboratories. For scale, all the data centres now operating on the National Electricity Market (NEM) together draw an average of a little over half a gigawatt [3].

The case for linking the policies runs as a chain. If Australia approves data centres quickly, foreign laboratories will sink tens of billions of dollars here. Having done so, they will have reason to keep Australia supplied with their best models, to cooperate with its safety institute, and to defend its interests in Washington. In this account the buildings are "sovereign AI infrastructure", and helping to build them is a way of governing AI.

I argue that the two policies must be kept apart. A data centre confers no authority over the models that run inside it. The joined deal therefore asks Australia to pay in things it controls (grid capacity, water, consent over land, copyright law) for something a building cannot deliver. Australia already holds authority over models through the terms of market entry. Data centres should be approved on clear commercial terms, AI providers should owe safety duties as a condition of serving Australians, and neither should be traded for the other.

The note proceeds in four steps:

- **Section 2** shows that hosting a model's computers confers no control over the model.
- **Section 3** shows that the economic case for data centres is real, but that it is a commercial case, to be met on commercial terms.
- **Section 4** shows that joining the two deals weakens Australia's hand in both.
- **Section 5** recommends rules that give developers speed and certainty, communities protection, and government authority over models.

## 2. Hosting a Model Is Not Controlling It

The first link in the chain is that a model running on Australian soil is, in some useful sense, under Australian control. June 2026 tested that claim.

On 12 June a US export-control directive restricted foreign nationals' access to Anthropic's newest models, *Fable 5* and *Mythos 5* [4]. The notice "did not provide specific details of its national security concern" [4]. Unable to check user nationality in real time, Anthropic suspended both models worldwide, across its own API and third-party cloud regions; *Mythos 5* returned only for US-approved organisations [4, 5]. Where the computers stood made no difference.

The reason lies in how AI services are built. Every commercial model is reached through a **control plane**: the management software that checks who a user is, routes each request, and switches models on or off. The control plane belongs to the provider, and the provider answers to its home government. Guidance from the US Bureau of Industry and Security (BIS) on advanced computing items binds corporate headquarters and ultimate parent companies globally [7]. A server on a Sydney floor still answers to its parent company's home government. Hosting it confers no legal right to keep the model switched on.

"Sovereign AI" runs together two things that are separate in engineering and in law:

- The **facility stack** is the physical plant: land, buildings, cooling, electricity, and chips.
- The **model stack** is what runs on it: the control plane, the model itself, and the applications built on top.

Table 1 sets out the six layers and asks of each whether hosting it in Australia gives Australia control.

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

*Table 1. The six layers that "sovereign AI" treats as one asset. Australian authority is complete over the layers whose costs fall locally (1–2) and weak over the layers the joined deal is meant to secure (3–5).*

The table shows the pattern on which the rest of this note depends. Hosting gives Australia authority over land, water, and the grid, which it had already. It gives none over the chips, the control plane, or the model.

A second fact points the same way: the data centres proposed for export are not the ones Australian users depend on. AI computing comes in two kinds.

- ***Training*** (building a new model) packs tens of thousands of chips into a single power-dense campus [25]. It can be done anywhere with enough power.
- ***Inference*** (running a trained model to answer requests) divides according to how much delay a task can tolerate. Interactive clinical tools, voice systems, and industrial controls need millisecond response times and so must run near Australian cities. Long-running coding, research, and administrative agents run just as well over subsea fibre from abroad [24, 27].

The hardware is diverging along the same line, as inference moves to specialised chips unlike those in training clusters. Whatever its commercial merits, a training campus built in regional Australia for export gives Australian hospitals, banks, and public agencies no guarantee that their AI services will keep running during an international disruption.

## 3. The Economic Case Is Real, and It Is Commercial

If hosting does not buy control, data centres must be judged as industry policy. On that footing they have genuine merits, and three deserve plain statement:

- Construction spending is large, and it is spent locally [9].
- Services that need fast responses or onshore data must be hosted near their Australian users, so some new capacity is needed on any view [24].
- A large electricity customer can lower power prices for everyone. If it puts more energy through the existing network without adding to the peak, the network's fixed costs are spread more thinly [26].

These are good reasons to build. They are also ordinary commercial reasons, which a sound project can meet on ordinary commercial terms. Productivity Commission chair Danielle Wood makes the same point: there is "pretty strong commercial incentive to build these things", and she expects Australia to "end up with a lot of capacity in any case" [28].

**How to count the benefit.** Headline investment is the wrong measure, and so is gross domestic product (GDP). GDP counts everything produced on Australian soil, including profits that belong to foreign owners. The right measure is gross national income (GNI): what Australian residents keep. For a single project, the calculation has three terms:

> **Net benefit to residents = income residents keep + spillovers − costs left with residents**

Table 2 sets out what belongs in each term and what does not.

| Term | What counts | What does not count |
|---|---|---|
| **Income residents keep** | Wages paid to Australian workers; margins earned by Australian suppliers of construction, land, and energy; taxes and charges paid to Australian governments; profits to any Australian owners | Imported chips and servers, which enter as investment and leave as imports; profits to foreign owners |
| **Spillovers** | Lower network charges, if the load does not add to the peak; compute and skills passed on to local researchers and firms | The productivity gain from using AI, which arrives wherever the model is hosted |
| **Costs left with residents** | Grid upgrades and higher bills the project does not pay for; water drawn from stressed catchments; trades diverted from housing and the energy transition; tax relief and other concessions | Costs the project pays for itself |

*Table 2. How to count a data centre's benefit to Australian residents.*

Four findings fill in these terms. They show that the first term is much smaller than the headline, that the second is conditional, and that the third is within government's control.

**The pipeline is far larger than Australian demand.** In August 2026 AEMO's 225 projects in development totalled 67 GW [3]. The record of existing data centres is more modest. Those operating on the NEM consumed roughly 5 terawatt-hours (TWh) in FY2026, or 3% of grid demand [3]. Average use of their grid connections sat near 27%, facilities took five to ten years to reach full load, and 36% of the projects in AEMO's 2025 forecast had already been cancelled [3]. Hosting 10 to 15 GW at 75% utilisation would consume 65.7 to 98.6 TWh a year, four to six times AEMO's Step Change forecast for FY2030 (15.5 TWh) [3, 25, 26]. Capacity on that scale would serve export markets, not Australian hospitals, schools, or firms. Export is a legitimate business. It should be assessed as one.

**Most of the headline investment is imported equipment.** In Epoch AI's cost model for a one-gigawatt AI campus, 68% of capital spending (US$26 billion of US$38 billion) buys chips, servers, and networking hardware [12]. Australia imports virtually all of it. In the national accounts, about two-thirds of every announced dollar is therefore counted as business investment and then subtracted again as imports. As Commonwealth Bank economists note, "[t]he business investment pulse is quite large, but that flow through to GDP is far smaller" [9].

The same pattern holds once a data centre is running. Charlton estimates that of each dollar spent on AI services, energy takes about 5 to 10 cents and infrastructure less than 10. Chips take 20 to 30 cents, and most of the remainder goes to the model's developer [24]. Australia would supply the smaller parts. Whether those parts earn more than a commodity return depends on whether Australia can supply them below the global marginal cost, which Charlton calls an "[i]mportant unanswered question" [24].

**The local share arrives during construction and competes for scarce trades.** The remaining 32%, about US$12 billion per gigawatt in Epoch's model, is spent on buildings, electrical fit-out, cooling, and land [12]. Large campuses bid for the same electricians, civil trades, and high-voltage transformers needed for housing and grid decarbonisation [9]. Once operating, a data centre employs few people: an industry-commissioned report by Mandala Partners counts around 9,450 ongoing direct and supply-chain jobs in 2026, in a workforce of 15.2 million [19]. The profits of foreign-owned operators, though counted in GDP, flow offshore and so drop out of GNI.

**The productivity gain comes from using AI, wherever it is hosted.** The Productivity Commission estimates that AI could lift labour productivity by 4.3% over the next decade, or roughly 0.4 percentage points a year, nearly doubling the past decade's pace [28]. Australian firms and agencies earn that gain by redesigning everyday tasks, whether the computation happens in Melbourne or Oregon. The owners of the data centres carry a separate risk. As Hempton warns, capital-heavy infrastructure with low operating costs and rapid chip obsolescence can suffer severe overbuild and weak investor returns even while the services running over it transform the wider economy [27].

None of the sources reviewed here puts numbers on all three terms for an Australian project. Governments should calculate that figure and publish it, because approvals should turn on it and not on headline investment (Recommendation 1).

The formula also yields a simple rule: approve, but do not subsidise. When a project pays its own costs, the third term falls to zero, and whatever income and spillovers it brings are a net gain. A project that pays for its own grid connection, water, and site remediation leaves the overbuild risk with its investors, and is welcome at any size. A project that needs grid priority, cheap water, or tax relief asks ratepayers to carry that risk, in return for a productivity gain they would receive anyway. On this the proposal's advocates agree. In Egan's version, "[t]he Australian government is not spending money on these" [25].

## 4. Joining the Deals Weakens Both

What remains is the joined deal in its strongest form: **compute-for-access** [25]. Its advocates state it with care, and it deserves the same care in reply.

In Egan's account, Australia offers foreign laboratories fast, predictable approvals, abundant renewable land, and aligned Five Eyes security settings for multi-gigawatt training clusters. In return it asks for three kinds of access: frontier models for Australians, a share of compute for public research, and close cooperation between the laboratories and the AISI [25]. Enforcement could include financial penalties, or making a data centre's power supply conditional on the agreement [25]. Egan is clear that this is soft leverage. A US company remains "at the behest of the US government"; the aim is to create "an internal champion" that argues for Australia in Washington [25]. Charlton advances a related case behind Expectation 5: partnerships with the laboratories could turn Australian universities and firms from customers into partners in developing intellectual property [24].

Two parts of this account are right. Fast, predictable approvals are worth offering for their own sake. And goodwill has value: a laboratory with a large Australian investment is a useful friend. The third part is the error: making model access or safety oversight depend on that goodwill. It fails for three reasons.

**First, Australia already holds a stronger lever, and linkage weakens it.** The November announcement applies mandatory security controls, independent evaluation, and rapid incident reporting to *every* frontier AI provider operating in Australia [1]. It reaches a model trained and hosted anywhere on earth the moment that model serves Australian users. Canberra timed it deliberately "before a range of major international talks that will cover AI development and investment" [1]. If safety cooperation or research access is instead made conditional on data-centre deals, a statutory duty becomes a negotiated favour, and the companies being regulated gain a bargaining position against their regulator.

**Second, the leverage is weak, as advocates and sceptics both accept.** Hard bargaining is not on offer. Egan observes that if the Netherlands used its hold over chip-making equipment against the United States, a trade war would follow that the United States would probably win, and she rejects hard bargaining for Australia on the same ground [25]. A clause letting Australia cut a data centre's power is real, because Australia does control the grid (Table 1, Layer 2). But a dark data centre restores no model access, and using the clause is the escalation Egan warns against.

The soft version depends on scale and on market conditions. Egan's benchmark is hosting half of a leading laboratory's training compute [25]. Wood calls the leverage case for government-backed data centres "a fairly long bow" [28]. If the world overbuilds, or the leading models stay close together, a laboratory has many substitutes and owes its host little: in May 2026, leading open-weights models trailed the top closed models by roughly four months on capability benchmarks [11]. If instead a crisis makes frontier compute scarce, the provider's home government holds statutory authority over parent companies, replacement chips, and software updates [5, 7]. Allied hosting can earn a seat in diplomatic consultations, as Carnegie's *Compute Coalition* report argues [23], and that seat is worth having. It is not a legal right.

**Third, the price is paid in permanent rights for revocable promises.** Egan identifies copyright as "the key barrier": laboratories will not pay for Australian licences while they argue fair use in US courts, so the deal requires a change to Australian copyright law [25]. The government has taken the opposite position. The Attorney-General's Department has ruled out a text-and-data-mining exception in favour of licensing certainty [8], and Charlton describes the aim as ensuring that Australian creative work "isn't given away for free" [24]. US courts, for their part, have already separated lawful training copies from retained pirated libraries (*Bartz v Anthropic* [6]). Weakening creators' rights, compressing environmental and Indigenous land-consent processes [20], or entering a tax-exemption race among the states would each give up a lasting domestic protection for a commercial pledge that binds no one. Virginia's legislative auditor offers a warning: US$4.06 billion in data-centre tax exemptions returned just 22 cents of state revenue per dollar forgone [17].

Linkage also serves developers poorly. An approval won by concession lasts only as long as the political mood that granted it. Wood warns that if data centres push up power or water prices, "you're going to see that social licence degrade pretty quickly" [28]. An approval granted under published rules is far harder to reopen. Singapore shows that strict rules and strong demand can coexist: its latest capacity round, run under tight efficiency limits, was oversubscribed [15].

## 5. Recommendations: Two Deals, Each on Clear Terms

Each deal should be made on its own terms, so that neither can be traded for the other. Table 3 sets out what each party gains. Four recommendations follow, each tied to the layers in Table 1.

| Party | What it gains from separate deals |
|---|---|
| Data-centre developers | Published conditions, a fixed decision time, freedom to comply by contract, and approvals that survive a change of government |
| Host communities | No added cost on power bills, metered water limits, consent before construction, and offsets that land locally |
| Researchers and start-ups | Compute that is funded or contracted, not merely promised |
| AI providers | One set of safety duties, the same wherever they host |
| Government | Authority over models that depends on no investor's goodwill |

*Table 3. What each party gains when data-centre approval and model governance are kept apart.*

**1. Give data centres a fast, published path to approval (Layers 1–3).** Developers need speed and certainty more than they need concessions, and on this the debate agrees. Egan's first priority is that Australia "demonstrate that we can build data centres quickly and we can do it well, with certainty" [25]. Wood wants approval processes streamlined without protections being removed [28]. Commonwealth and state governments should publish one set of conditions and commit to a fixed decision time for any project that meets them. A project should pass four gates, in strict order:

1. **Disclosure.** The developer states the project's workload mix and realistic alternatives, separating domestic needs (low delay, data residency) from export training.
2. **Local thresholds.** The project meets limits that are not open to trade-off: drinking water, grid reliability, biodiversity, and Free, Prior and Informed Consent (FPIC) on Indigenous land [20].
3. **Economic case.** Only then do treasuries weigh the benefits, measured in income retained by residents (GNI) and in pressure on local electrical and civil trades, and publish the estimate.
4. **Exit.** Any permit carries an upfront remediation bond and conditions that bind successor owners.

National Cabinet should also prevent states from bidding against one another with payroll-tax relief, public land, or places in the grid queue [17]. States should compete on how quickly they decide, not on how much they give away.

**2. Make data centres pay their way on the grid and in the catchment (Layers 1–2).** The Prime Minister's July pledge that large data centres return at least as much energy as they draw and fund water infrastructure [2] is the right standard. Met well, it does more than protect households. Nelson shows that a data centre which adds energy to the network without adding to its peak spreads fixed network costs more thinly and can lower prices for everyone [26]. Met badly, it does the reverse: in Virginia, data-centre demand is projected to add US$14–37 a month to typical residential bills by 2040 [16]. Three conditions separate the two outcomes.

- **Connection.** Projects should fund their own grid connections, so that network costs do not fall on households if forecast loads disappoint [16].
- **Peak.** A data centre draws power at a flat rate around the clock. Supplying it takes bulk energy over the year, batteries to move that energy into evening peaks ("shaping"), and backup through multi-day lulls in wind and sun ("firming") [26]. Projects should bring enough storage or flexibility that they do not raise the peak, and flexible training loads should be steered toward grid zones with surplus solar and wind [26].
- **Clean supply.** How to match consumption with renewable certificates is contested. Nelson argues that annual certificates suffice, because the wholesale market already prices energy by time of day; others favour hourly matching [26]. The Australian Energy Market Commission's advice to energy ministers includes a middle option, matching within broad blocks of the day [26]. That option is the sensible default. It ties clean supply to the hours of demand without duplicating the market, and existing certificates can serve as a bridge while new generation is built [26].

Water standards should cap both on-site evaporative loss and the water used by upstream power stations, against seasonal local catchment limits [18]. Nelson reports that some operators run closed-loop cooling systems that use no water at all [26]. A project of that kind meets the cap without effort.

None of this rules out paying to comply. Developers should be free to meet these standards by contract instead of by construction: buying firmed clean power, paying for storage, or funding water recycling. The test is that the remedy must arrive where the cost falls. For carbon, a tonne avoided anywhere counts, so a verified credit can do the job. Power and water are different, because their costs are local. A certificate for solar energy generated at noon in another state does not supply a Sydney substation at 6 pm, and a water offset in another catchment does not refill this one. An instrument should therefore count only if it delivers in the same part of the day and the same region, or the same catchment, as the demand it covers. Under that test developers keep their flexibility, and host communities receive the benefit that was paid for.

**3. Make safety duties a condition of market entry, whatever a provider builds (Layer 5).** The *Australian AI Standards* Bill should impose the same AISI evaluation access, security rules, and incident-reporting duties on every frontier provider serving Australians, whether hosted onshore or offshore [1]. Notification should fall due within 72 hours, matching European breach rules; the reporting delay in 2026 ran to months [14, 21]. Regulatory, copyright, and safety standards should never be offered as inducements in siting deals. Providers gain from this too, because their duties no longer depend on where they host or what they have built.

The duties should also stay narrow. Wood cautions that a general AI Act would duplicate existing law [28]; the regulator's remit should be frontier providers and the specific risks they pose. Statute sets the floor. Partnerships with laboratories that build here can add to it, for example through early information on unreleased models and exchanges of researchers, both of which Egan rightly values [25]. They should not replace it.

**4. Buy public compute and model portability directly (Layers 4–6).** Canberra should not rely on voluntary Expectation 5 pledges to pass capability down from commercial data centres [10]. It should fund pooled public compute for universities and small firms directly, as Canada's Sovereign AI Compute Strategy and Europe's EuroHPC AI Factories do [13, 22]. Where a developer does receive expedited grid coordination, its Expectation 5 promises should become contracted, audited GPU-hour allocations with clear remedies for non-delivery.

Within government, the Digital Transformation Agency (DTA) and Australian Signals Directorate (ASD) should require audited domestic routing and the ability to move between vendors, and should avoid "global standard" cloud tiers that process Australian requests offshore. Agencies should also keep vetted open-weights models available as a fallback, on cloud infrastructure certified under ASD's Information Security Registered Assessors Program (IRAP). Charlton names the same routes to reducing dependence: using a diversity of models across critical systems, and running open-weights models in Australia under Australian control [24].

## 6. Objections and Limitations

*“Hard limits will drive investment to Southeast Asia or the United States.”* Capacity serving Australians will stay, because workloads that need Australian data residency or millisecond response times must locate near their users. Singapore's oversubscribed allocations under strict efficiency limits show that firm rules do not deter demand [15]. Some export training campuses may go elsewhere. If such a campus is viable in Australia only when households cross-subsidise its grid firming or communities waive water limits, the country loses nothing by declining to subsidise it.

*“Australia is too small a market for its rules to bind; laboratories cooperate only because they hope to build here.”* This is Egan's strongest point: Australia has no "Brussels effect" [25]. There are three answers. The duties proposed are narrow and resemble the testing that providers already accept from the UK and US safety institutes [25], so compliance costs little beside the cost of leaving a wealthy market. Providers have also shown that they respond to Australian pressure: after the 2026 portal incident, OpenAI made public commitments to Australia [21]. And where statute cannot reach, as with unreleased internal models, partnership can add to the floor (Recommendation 3). The floor itself should not depend on investment that may go elsewhere.

*“Modern data centres use very little water, so water rules solve a problem that does not exist.”* Some designs do use little, and closed-loop systems can use none [26]. Water use varies widely with the cooling system, the climate, and the source of the electricity [18]. That variation is the reason to meter it. A cap measured at the site and the catchment costs a low-water project almost nothing and gives its neighbours proof in place of assurance. It binds only the projects that would otherwise draw heavily on a stressed catchment.

*“Without gigawatt training clusters onshore, Australia will be rationed out of frontier AI in an international crisis.”* Crisis rationing is a real risk, yet commercial data centres do not prevent it. Onshore hardware did not stop a US export directive from suspending *Fable 5* and *Mythos 5* across global cloud regions in June 2026 [4, 5]. Where allied hosting does strengthen defence or intelligence continuity, Canberra should negotiate binding intergovernmental carve-outs, local weight escrow, and emergency priority rights. Any such campus should be funded from, and judged against, the defence budget.

*“The wholesale market already rewards storage, so time-matching rules duplicate it.”* This is Nelson's view, and on energy it has force [26]. For that reason Recommendation 2 adopts the broad time-of-day blocks in the AEMC's advice, not strict hourly matching. The wholesale market does not, however, cover regulated transmission lines and substations, whose multi-decade costs still fall on captive residential customers if forecast loads disappoint or network tariffs lag [16]. Upfront connection funding remains a necessary backstop.

**Limitations.** Project-level Australian power contracts, cooling designs, and foreign-ownership shares remain largely commercial-in-confidence. The March 2026 *Expectations* have not yet undergone a public compliance audit [10], and the full text of the *Australian AI Standards* Bill remained unreleased at the time of writing [1]. Standardised public metering of facility power draw, water consumption, and contracted research compute would make every link in this argument empirically testable.

## 7. Conclusion

Approving a data centre and governing an AI model are different acts, and they rest on different sources of authority. Australia's authority over data centres comes from its land, grid, and water. Its authority over models comes from its market: any laboratory that wants Australian customers is within Parliament's reach, and Canberra can require independent evaluation, security controls, and prompt incident reporting without owing anything to the companies that build data centres [1].

The "sovereign AI" proposal confuses the two. It treats a building as though it carried authority over what runs inside it, and asks Australia to pay for that authority with its grid, water, land, and law. Concrete is not control. Australia should make each decision on its own terms: approve quickly the data centres that meet published limits on power, water, consent, and public cost, and hold every AI provider to the same safety duties wherever its computers sit.

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
