# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## Label Taxonomy

**Community:** r/stocks (Reddit)

**Purpose:** Classify how well investment arguments are supported, rather than whether their predictions ultimately turn out correct.

### `no_argument`

**Definition:** News, genuine questions, or discussions without an identifiable investment position or market prediction.

**Example 1:** [Tesla beats on earnings and sales even as auto revenue declines](https://www.reddit.com/r/stocks/comments/1xby6j8/tesla_beats_on_earnings_and_sales_even_as_auto/)

The post reports Tesla's quarterly earnings and revenue compared with expectations, without making an investment recommendation or price prediction.

**Example 2:** [How Can I Beat FOMO In This Market And Stop Buying The Peak/Ceiling?](https://www.reddit.com/r/stocks/comments/1qj1f8n/how_can_i_beat_fomo_in_this_market_and_stop/)

The author describes past trading mistakes and asks for advice, rather than advancing an investment thesis.

### `unsupported`

**Definition:** An investment claim or market prediction without meaningful supporting evidence or reasoning.

**Example 1:** [RDDT undervalued?](https://www.reddit.com/r/stocks/comments/1qxpnuj/rddt_undervalued/)

The author suggests Reddit stock is undervalued based mainly on its recent price history and personal impression, without explaining its fundamental valuation.

**Example 2:** [Apparently buying the dip makes me a gambler](https://www.reddit.com/r/stocks/comments/1x8h76i/apparently_buying_the_dip_makes_me_a_gambler/)

The author argues for buying fallen technology stocks largely on the expectation that they will eventually recover, without establishing why those investments should deliver positive returns.

### `partial`

**Definition:** An investment claim supported by relevant evidence or reasoning, but with an incomplete connection between the support and the conclusion.

**Example 1:** [Feels like a relief rally… not convinced it's the bottom](https://www.reddit.com/r/stocks/comments/1s91sfp/feels_like_a_relief_rally_not_convinced_its_the/)

The author argues that a market rebound may be temporary, citing oil prices, persistent inflation, and Federal Reserve policy. The reasoning is relevant but lacks detailed evidence about expected market returns.

**Example 2:** [Which stocks do you think are mispriced despite strong fundamentals?](https://www.reddit.com/r/stocks/comments/1wm8zd5/which_stocks_do_you_think_are_mispriced_despite/)

The author argues that APP and CRDO may be undervalued because their prices have fallen despite continuing growth, but does not provide a detailed valuation analysis.

### `well_supported`

**Definition:** An investment claim supported by relevant, checkable evidence and a clear explanation connecting that evidence to the investment conclusion.

**Example 1:** [GME 5-Year DCF: The Transformation Climax](https://www.reddit.com/r/stocks/comments/1pgxr3v/gme_5year_dcf_the_transformation_climax/)

The author develops a discounted cash-flow valuation with bear, neutral, and bull cases, explaining how assumptions about revenue, margins, and future cash flows affect the estimated stock value.

**Example 2:** [My take on RDDT and future catalysts](https://www.reddit.com/r/stocks/comments/1uf9y1v/my_take_on_rddt_and_future_catalysts/)

The author uses P/E ratios, growth assumptions, and a PEG calculation to explain a valuation argument for Reddit stock.

### The hardest boundary

**Which two labels:** `unsupported` and `partial`

**The decision rule I used every time:**

An investment prediction is `unsupported` when it merely asserts an outcome without meaningful justification. It becomes `partial` when the author provides relevant evidence or a plausible causal explanation, even if the evidence is incomplete or not independently quantified.

To qualify as `well_supported`, the post must contain relevant, checkable evidence and explain how it supports the investment conclusion. Multiple numbers alone are not sufficient.

Posts are classified according to what the author communicates, not their punctuation. Genuine information-seeking questions are `no_argument`; rhetorical questions implying investment positions are evaluated using the other labels.git add README.md
git commit -m "Define TakeMeter label taxonomy"
---

## The Dataset

**Where the posts came from:**

I collected posts from the public r/stocks subreddit using Reddit's RSS feeds, including recent posts and popular posts from the past month. A Python script extracted the titles and body text, removed HTML formatting, and eliminated duplicate post IDs.

The initial collection contained 166 unique posts. I excluded seven recurring moderator discussion threads because they mainly contained standardized instructions and links rather than individual investment discussions.

My final dataset contains **159 unique posts**. I stopped below the original 200-post target because of time constraints and an unsuccessful additional RSS collection. This follows the assignment's documented fallback for a dataset of at least 150 posts.

**How I labelled them:**

I independently labeled the first 20 posts without AI assistance, marking them `cold`.

For the remaining 139 posts, I used AI to suggest classifications based on my four-label taxonomy. I then read and reviewed every suggested classification, accepting or correcting labels according to my definitions.

The four labels assess the strength of an investment argument, not whether its prediction ultimately proves correct.

**Counts per label:**

| Label | Count | Share |
|---|---:|---:|
| `no_argument` | 84 | 52.8% |
| `unsupported` | 6 | 3.8% |
| `partial` | 43 | 27.0% |
| `well_supported` | 26 | 16.4% |
| **Total** | **159** | **100%** |

No label exceeds the assignment's 70% class-balance limit. However, `no_argument` exceeds my stricter 50% acceptance criterion, and `unsupported` has only six examples. Both are limitations I will examine during evaluation.

### Three hard cases

**1.**

> **The post:** "Relief rally after midterms"
>
> **Could have been:** `no_argument` or `partial`
>
> **I chose, because:** `partial`. Although the author asks a question, the post implicitly argues that a market rally is unjustified. It cites concerns about AI spending, inflation, oil prices, and debt, but does not fully demonstrate how those concerns should affect market prices.

**2.**

> **The post:** "Reddit stock — the market is pricing in something that may not even happen"
>
> **Could have been:** `partial` or `well_supported`
>
> **I chose, because:** `partial`. The author distinguishes a conditional management warning from an actual forecast and explains why investors might have overreacted. However, the breakdown attributing portions of the stock's decline to different causes is largely an estimate rather than a demonstrated calculation.

**3.**

> **The post:** "Google was even lower than it is now last March and then hit over $400"
>
> **Could have been:** `unsupported` or `partial`
>
> **I chose, because:** `unsupported`. The author uses an earlier price recovery to support buying Google now, but does not establish why that historical rebound predicts another one. The investment recommendation lacks meaningful current valuation evidence.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
