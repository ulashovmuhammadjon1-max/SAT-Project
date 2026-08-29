# AP Microeconomics topic-fit audit — pass A

Independent audit of all 36 Micro question modules (1,800 questions: `t11`–`t16`,
`u2_1`–`u2_9`, `u3_1`–`u3_7`, `u4_1`–`u4_5`, `u5_1`–`u5_4`, `u6_1`–`u6_5`). Every
question stem in every module was read; answer choices and rationales were read for
every candidate before a verdict was recorded. Topic titles are taken from
`MICRO_UNITS` in `src/lib/ap/courses.ts` and treated as authoritative.

The regex pre-screen at `/tmp/micro_cand.txt` was consulted and is largely noise —
of its ~215 entries, roughly 12 survive judgement. It flagged whole modules on
ordinary shared vocabulary ("elastic" in a monopsony question, "demand" in a factor
market question, cost-table arithmetic inside a perfect-competition problem). It also
**missed** the two largest real clusters found here (2.6's comparative-statics block
and 6.1's tax-incidence block), because those questions use exactly the vocabulary
their host topic owns.

**Headline:** the bank is in good shape. Units 3, 4 and 5 are clean of real misfiles.
The genuine problems are concentrated in two places — Unit 6 topic 6.1 absorbing
Unit 2 topic 2.8's tax-incidence and price-control material, and Unit 2 topics 2.6
and 2.7 leaking into each other and into 2.8.

## Findings

| module | q# | stem (first 80 chars) | current topic | belongs to | verdict |
|---|---|---|---|---|---|
| u6_1 | 17 | Rent control is an example of | 6.1 Socially Efficient and Inefficient Market Outcomes | 2.8 Effects of Government Intervention in Markets | MISFILED |
| u6_1 | 18 | The minimum wage is an example of | 6.1 Socially Efficient and Inefficient Market Outcomes | 2.8 Effects of Government Intervention in Markets | MISFILED |
| u6_1 | 23 | Tax incidence describes | 6.1 Socially Efficient and Inefficient Market Outcomes | 2.8 Effects of Government Intervention in Markets | MISFILED |
| u6_1 | 24 | The side of the market with the more inelastic curve bears | 6.1 Socially Efficient and Inefficient Market Outcomes | 2.8 Effects of Government Intervention in Markets | MISFILED |
| u6_1 | 25 | If demand is perfectly inelastic and supply is upward sloping, a per-unit tax is | 6.1 Socially Efficient and Inefficient Market Outcomes | 2.8 Effects of Government Intervention in Markets | MISFILED |
| u6_1 | 26 | If supply is perfectly elastic and demand is downward sloping, a per-unit tax is | 6.1 Socially Efficient and Inefficient Market Outcomes | 2.8 Effects of Government Intervention in Markets | MISFILED |
| u2_6 | 36 | Both demand and supply increase simultaneously. The effect on equilibrium quanti | 2.6 Market Equilibrium and Consumer and Producer Surplus | 2.7 Market Disequilibrium and Changes in Equilibrium | MISFILED |
| u2_6 | 37 | Both demand and supply increase simultaneously. The effect on equilibrium PRICE  | 2.6 Market Equilibrium and Consumer and Producer Surplus | 2.7 Market Disequilibrium and Changes in Equilibrium | MISFILED |
| u2_6 | 38 | Demand increases while supply decreases. The effect on equilibrium price is | 2.6 Market Equilibrium and Consumer and Producer Surplus | 2.7 Market Disequilibrium and Changes in Equilibrium | MISFILED |
| u2_6 | 39 | Demand increases while supply decreases. The effect on equilibrium quantity is | 2.6 Market Equilibrium and Consumer and Producer Surplus | 2.7 Market Disequilibrium and Changes in Equilibrium | MISFILED |
| u2_7 | 41 | Which of the following best describes what happens to consumer surplus under a b | 2.7 Market Disequilibrium and Changes in Equilibrium | 2.8 (with 2.6 surplus analysis) | MISFILED |
| u2_7 | 42 | Producer surplus under a binding price ceiling | 2.7 Market Disequilibrium and Changes in Equilibrium | 2.8 (with 2.6 surplus analysis) | MISFILED |
| u2_2 | 38 | Which of the following describes the relationship between the supply curve and m | 2.2 Supply | 3.5 Profit Maximization / 3.7 Perfect Competition | MISFILED |
| u2_6 | 26 | An increase in demand with supply unchanged will | 2.6 Market Equilibrium and Consumer and Producer Surplus | 2.7 Market Disequilibrium and Changes in Equilibrium | UNSURE |
| u2_6 | 27 | A decrease in supply with demand unchanged will | 2.6 Market Equilibrium and Consumer and Producer Surplus | 2.7 Market Disequilibrium and Changes in Equilibrium | UNSURE |
| u2_7 | 26 | Why do binding price ceilings often lead to long queues or rationing? | 2.7 Market Disequilibrium and Changes in Equilibrium | 2.8 Effects of Government Intervention in Markets | UNSURE |
| u2_7 | 27 | Rent control is a classic example of | 2.7 Market Disequilibrium and Changes in Equilibrium | 2.8 Effects of Government Intervention in Markets | UNSURE |
| u2_7 | 28 | A minimum wage set above the equilibrium wage is an example of | 2.7 Market Disequilibrium and Changes in Equilibrium | 2.8 Effects of Government Intervention in Markets | UNSURE |
| u2_7 | 40 | If a government wants to eliminate a shortage caused by a price ceiling without  | 2.7 Market Disequilibrium and Changes in Equilibrium | 2.8 Effects of Government Intervention in Markets | UNSURE |
| u2_7 | 43 | Black markets often emerge alongside binding price ceilings because | 2.7 Market Disequilibrium and Changes in Equilibrium | 2.8 Effects of Government Intervention in Markets | UNSURE |
| u2_2 | 22 | The main reason a firm's marginal cost rises as output expands in the short run  | 2.2 Supply | 3.1 The Production Function / 3.2 Short-Run Production Costs | UNSURE |
| u2_2 | 37 | Firms in a competitive market decide how much to supply by comparing | 2.2 Supply | 3.5 Profit Maximization | UNSURE |
| u2_1 | 21 | A market system is best described as one in which | 2.1 Demand | 1.2 Resource Allocation and Economic Systems | UNSURE |
| u2_1 | 22 | Clearly defined property rights are essential to a market system because they | 2.1 Demand | 1.2 Resource Allocation and Economic Systems | UNSURE |
| u2_1 | 23 | Economic agents in a market system include | 2.1 Demand | 1.2 Resource Allocation and Economic Systems | UNSURE |
| u2_1 | 24 | An economic incentive is best described as | 2.1 Demand | 1.1 Scarcity / 1.2 Resource Allocation | UNSURE |
| u2_1 | 25 | Economic constraints are | 2.1 Demand | 1.1 Scarcity | UNSURE |
| u2_1 | 46 | A well-functioning market system relies on prices to | 2.1 Demand | 1.2 Resource Allocation and Economic Systems | UNSURE |
| u2_1 | 35 | Marginal utility is | 2.1 Demand | 1.6 Marginal Analysis and Consumer Choice | UNSURE |
| t15 | 23 | A firm's accounting profit equals total revenue minus | 1.5 Cost-Benefit Analysis | 3.4 Types of Profit | UNSURE |
| t15 | 24 | Economic profit equals total revenue minus | 1.5 Cost-Benefit Analysis | 3.4 Types of Profit | UNSURE |
| t15 | 25 | A shop earns $100,000 in revenue with $60,000 of explicit costs. The owner gave  | 1.5 Cost-Benefit Analysis | 3.4 Types of Profit | UNSURE |
| t15 | 26 | A negative economic profit alongside a positive accounting profit tells the owne | 1.5 Cost-Benefit Analysis | 3.4 Types of Profit | UNSURE |
| t15 | 27 | Total economic cost is defined as | 1.5 Cost-Benefit Analysis | 3.4 Types of Profit | UNSURE |
| t15 | 11 | The Law of Diminishing Marginal Utility states that as a person consumes more of | 1.5 Cost-Benefit Analysis | 1.6 Marginal Analysis and Consumer Choice | UNSURE |
| t15 | 21 | The table shows total utility from pizza slices. The marginal utility of the THI | 1.5 Cost-Benefit Analysis | 1.6 Marginal Analysis and Consumer Choice | UNSURE |
| t15 | 22 | The total utility figures in the table illustrate | 1.5 Cost-Benefit Analysis | 1.6 Marginal Analysis and Consumer Choice | UNSURE |
| u3_1 | 21 | Returns to scale describe what happens to output when | 3.1 The Production Function | 3.3 Long-Run Production Costs | UNSURE |
| u3_1 | 22 | If a firm doubles all inputs and output MORE than doubles, the firm experiences | 3.1 The Production Function | 3.3 Long-Run Production Costs | UNSURE |
| u3_1 | 23 | If a firm doubles all inputs and output exactly doubles, the firm experiences | 3.1 The Production Function | 3.3 Long-Run Production Costs | UNSURE |
| u3_1 | 24 | If a firm doubles all inputs and output LESS than doubles, the firm experiences | 3.1 The Production Function | 3.3 Long-Run Production Costs | UNSURE |
| u3_1 | 42 | A production function exhibiting constant returns to scale means that doubling i | 3.1 The Production Function | 3.3 Long-Run Production Costs | UNSURE |
| u3_1 | 46 | Returns to scale become relevant only in the long run because | 3.1 The Production Function | 3.3 Long-Run Production Costs | UNSURE |
| u3_1 | 47 | Decreasing returns to scale often arise from | 3.1 The Production Function | 3.3 Long-Run Production Costs | UNSURE |
| u3_2 | 42 | The rent a shop owner gives up by using a building she owns is an example of | 3.2 Short-Run Production Costs | 3.4 Types of Profit | UNSURE |
| u3_2 | 43 | An owner who gives up a $60,000 salary to run her own shop has incurred | 3.2 Short-Run Production Costs | 3.4 Types of Profit | UNSURE |
| u3_3 | 33 | In the long run, if a competitive firm cannot cover its total costs, it will | 3.3 Long-Run Production Costs | 3.6 Firms' Entry and Exit Decisions | UNSURE |
| u5_1 | 38 | The least-cost combination of two inputs requires that | 5.1 Introduction to Factor Markets | 5.3 Profit-Maximizing Behavior in Perfectly Competitive Factor Markets | UNSURE |
| u5_1 | 39 | If MP of labor divided by the wage exceeds MP of capital divided by the rental r | 5.1 Introduction to Factor Markets | 5.3 Profit-Maximizing Behavior in Perfectly Competitive Factor Markets | UNSURE |
| u5_1 | 40 | The profit-maximizing combination of inputs requires that | 5.1 Introduction to Factor Markets | 5.3 Profit-Maximizing Behavior in Perfectly Competitive Factor Markets | UNSURE |
| u6_2 | 45 | The tragedy of the commons arises when | 6.2 Externalities | 6.3 Public and Private Goods | UNSURE |
| u6_2 | 46 | Overfishing in international waters is an example of | 6.2 Externalities | 6.3 Public and Private Goods | UNSURE |
| u6_2 | 47 | A solution to the tragedy of the commons is to | 6.2 Externalities | 6.3 Public and Private Goods | UNSURE |
| u6_4 | 37 | Government provision of a public good addresses market failure by | 6.4 Effects of Government Intervention in Different Market Structures | 6.3 Public and Private Goods | UNSURE |

**13 MISFILED, 41 UNSURE, out of 1,800 questions (0.7% / 2.3%).**

## Clean results, stated plainly

- **Unit 1 (t11–t16)** — `t11` (1.1 Scarcity), `t12` (1.2 Resource Allocation),
  `t13` (1.3 PPC), `t14` (1.4 Comparative Advantage), `t16` (1.6 Marginal Analysis
  and Consumer Choice) are **clean**: no misfiles found, no UNSURE entries. Every
  one of the pre-screen's 23 hits in `t14` and its 20 hits in `t15`/`t13` are false
  positives (it read PPC opportunity-cost tables as 1.1 content, and read
  comparative-advantage opportunity-cost arithmetic as 1.1 content). Only `t15`
  (1.5 Cost-Benefit Analysis) carries entries, all UNSURE.
- **Unit 3 (u3_1–u3_7)** — **no MISFILED questions.** All seven modules sit inside
  their own topic. `u3_4` (Types of Profit), `u3_5` (Profit Maximization),
  `u3_6` (Entry and Exit), `u3_7` (Perfect Competition) are entirely clean, including
  `u3_7` q45, the one monopoly-comparison question, which is a legitimate benchmark
  contrast rather than a monopoly calculation.
- **Unit 4 (u4_1–u4_5)** — **completely clean.** No MISFILED and no UNSURE entries in
  any of the five modules. `u4_1` (Introduction to Imperfectly Competitive Markets)
  legitimately previews monopoly, monopolistic competition, oligopoly and cartels
  because that is what an introduction to market structures is; `u4_3`'s heavy use of
  "elastic" is intrinsic to third-degree price discrimination.
- **Unit 5 (u5_1–u5_4)** — **no MISFILED questions.** `u5_2` (Changes in Factor Demand
  and Factor Supply) and `u5_4` (Monopsonistic Markets) are entirely clean; the
  pre-screen's 21 hits on `u5_2` are all false positives caused by labor-market
  questions using the words "demand", "supply" and "equilibrium". `u5_4`'s
  minimum-wage questions (q23–q25) are correctly filed — the monopsony minimum-wage
  result is 5.4's signature content, not 2.8's.
- **Unit 6** — `u6_3` (Public and Private Goods) and `u6_5` (Income and Wealth
  Inequality) are **clean**.

## Patterns

**1. Topic 6.1 has absorbed topic 2.8's tax-incidence material.** This is the single
clearest defect and the only cluster I would act on without further discussion.
`u6_1` q14–q29 is a sixteen-question run on price ceilings, floors, taxes, subsidies
and quotas. Most of it survives on its efficiency framing — "a per-unit tax causes
quantity to fall below the efficient level, creating a deadweight loss" is genuinely
6.1 material. But six questions in that run have no efficiency content at all: q17
and q18 merely ask a student to *identify* rent control and the minimum wage as price
controls, and q23–q26 are a pure tax-incidence sequence (who bears the burden, the
inelastic side bears more, perfectly-inelastic-demand and perfectly-elastic-supply
limiting cases). Every one of those six has a near-twin in `u2_8` (q1–q3, q7–q10,
q42, q50). A student practising "socially efficient and inefficient market outcomes"
is being asked to split a tax burden between buyers and sellers, which is Unit 2 work.

**2. 2.6 / 2.7 / 2.8 form a leaky chain, each spilling forward into the next.**
- `u2_6` (Equilibrium and Surplus) carries the four-question double-shift block
  (q36–q39) whose whole point is that one equilibrium variable is *indeterminate*.
  That is the signature content of 2.7, and `u2_7` q8–q13 already teaches it — the
  two sets are near-duplicates of each other. Neither question mentions surplus.
- `u2_7` (Disequilibrium and Changes in Equilibrium) carries roughly twenty
  price-control questions (q14–q20, q26–q31, q38–q43). Most are defensible — a
  binding control is the canonical cause of persistent disequilibrium — but q41 and
  q42 ask for consumer and producer *surplus* under a ceiling, which needs 2.6's
  surplus geometry plus 2.8's policy analysis, and touches nothing 2.7 owns.
- Net effect: rent control and the minimum wage are each identified as a price control
  in three separate topics (`u2_7` q27–28, `u2_8` q1–q3/q23–q25, `u6_1` q17–18).

**3. The pre-screen's biggest blind spot is same-vocabulary misfiling.** Both real
clusters above (`u2_6` q36–39, `u6_1` q23–26) use only the words their host topic
owns — "equilibrium", "surplus", "deadweight loss", "elastic" — so a vocabulary
matcher cannot see them. Conversely it produced its largest false-positive blocks
(`u2_4` 21 hits, `u5_2` 21 hits, `u2_2` 15 hits) exactly where a topic's own subject
matter forces it to use a neighbour's words. Any future automated pass should score a
question against the *centre* of its topic, not against foreign keywords.

**4. Foundational concepts are taught two or three times over rather than being
misfiled.** Several UNSURE clusters are of this kind and may well be deliberate:
explicit/implicit cost and economic profit appear in 1.5, 3.2 and 3.4; returns to
scale in 3.1 and 3.3; diminishing marginal utility in 1.5, 1.6 and 2.1; the
MP-per-dollar least-cost rule in 5.1 and 5.3; the tragedy of the commons in 6.2 and
6.3. In every case the host module defines its own prerequisites first, so a student
practising that topic alone can still answer. I have flagged them so a human can
decide whether the repetition is intentional reinforcement or drift, but none of them
would leave a student stranded.

**5. `u2_1` q21–q25 and q46 are a block that reads as Unit 1.** Six questions on the
market system, property rights, economic agents, incentives and constraints sit in
the middle of a topic titled "Demand", and q21–q25 are contiguous, which is what an
imported block looks like. I have left all six UNSURE rather than MISFILED because
the CED plausibly opens Unit 2 with market-system framing under 2.1, and because none
of them is *wrong* for a student to see early in Unit 2 — but if the intent was a
pure demand topic, this is the block to move.
