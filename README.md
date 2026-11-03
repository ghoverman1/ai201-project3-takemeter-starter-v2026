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

**Base model:**

`distilbert-base-uncased` — a pretrained DistilBERT language model fine-tuned to classify Reddit investment discussions into my four argument-quality categories.

**Settings:**

- **Epochs:** 3
- **Learning rate:** 2e-5 (0.00002)
- **Batch size:** 16
- **Maximum sequence length:** 128 tokens
- **Random seed:** 42

**Anything I changed from the defaults, and why:**

I kept all the default training hyperparameters unchanged to establish an initial benchmark before experimenting with adjustments.

I configured the model to predict my four dataset labels: `no_argument`, `unsupported`, `partial`, and `well_supported`.

**Split sizes:**

| Label | Train | Validation | Test |
|---|---:|---:|---:|
| `no_argument` | 58 | 13 | 13 |
| `unsupported` | 4 | 1 | 1 |
| `partial` | 31 | 6 | 6 |
| `well_supported` | 18 | 4 | 4 |
| **Total** | **111** | **24** | **24** |

The dataset was divided approximately 70%/15%/15% into training, validation, and held-out test sets.

Three labels had fewer than eight examples in the test set: `unsupported` (1), `partial` (6), and `well_supported` (4). Their evaluation metrics may vary substantially between random seeds because each individual prediction has a large effect on the scores.

In particular, the model had only four `unsupported` examples available during training, which limits its opportunity to learn that category.

---

## How I Used AI

**Moment 1 — Collecting and cleaning Reddit data**

- **What I asked for:** I asked AI to help collect real posts from r/stocks after Reddit's JSON endpoint returned a 403 error.
- **What came back:** AI suggested using Reddit's RSS feeds and provided Python code to extract post titles and bodies, remove HTML formatting, and deduplicate entries.
- **What I changed:** I switched to the RSS approach and reviewed the collected data. The initial collection contained 166 unique posts. I removed seven recurring moderator discussion threads, leaving 159 posts for classification.

**Moment 2 — Preparing and reviewing labels**

- **What I asked for:** After independently labeling my first 20 posts, I asked AI to suggest classifications for the remaining posts using my four-label taxonomy and to help create a review script.
- **What came back:** AI provided 139 suggested labels and a Python script that displayed each post individually so I could accept or change its classification.
- **What I changed:** I reviewed all 139 posts individually against my definitions rather than treating the AI-generated labels as automatically correct. I preserved my original 20 independent classifications and recorded the remaining posts separately as AI-reviewed.

**Pre-labelling disclosure:**

I labeled **20 posts independently without AI assistance**. I then used AI to pre-label the remaining **139 posts** according to my taxonomy: `no_argument`, `unsupported`, `partial`, and `well_supported`.

I read and reviewed every AI-suggested classification before finalizing the dataset. The `note` column distinguishes my independently labeled posts (`cold`) from the AI-assisted, human-reviewed posts (`ai_reviewed_accepted` or `ai_reviewed_changed`).

I also used AI to help write and troubleshoot data-processing scripts, understand the training process, and organize portions of my README. I ran the code and used the notebook's actual outputs when reporting results.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.250 | 0.542 | +0.292 |
| Macro F1 | 0.127 | 0.176 | +0.048 |
| F1 — `no_argument` | 0.125 | 0.703 | +0.578 |
| F1 — `partial` | 0.385 | 0.000 | -0.385 |
| F1 — `unsupported` | 0.000 | 0.000 | +0.000 |
| F1 — `well_supported` | 0.000 | 0.000 | +0.000 |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

The baseline will do worse because it hasn't practiced on my examples.

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->
The overall accuracy increased by approximately 29 percentage points after fine-tuning, from 25.0% to 54.2%. However, the fine-tuned model appeared to predict only `no_argument`, the most common label. Although fine-tuning improved overall accuracy, the model did not learn to distinguish all four categories effectively. Its macro F1 remained low at 0.176.


---

## Run Log — Before

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥80% on every seed | 54.2% | 54.2% | 54.2% | **Missed** |
| 2. Per-label F1 | ≥0.70 for every label on every seed | 0.703 / 0 / 0 / 0 | Per-label values to confirm | Per-label values to confirm | **Missed** |
| 3. Class balance | No label exceeds 50% | 52.8% | 52.8% | 52.8% | **Missed** |
| 4. Human annotation agreement | ≥80% agreement on 50 independently labeled posts | Not tested | Not tested | Not tested | **Pending** |
| 5. High-confidence accuracy | ≥85% accuracy when confidence ≥0.80 | Not tested | Not tested | Not tested | **Pending** |

The model achieved identical accuracy (54.2%) and macro F1 (0.176) across all three seeds. This suggests consistent performance, but not effective classification. The model achieved these scores while failing to distinguish the minority categories in the confirmed seed-42 results.

For Criterion 2, the seed-42 F1 values are listed in this order: `no_argument`, `unsupported`, `partial`, `well_supported`. The individual F1 values for seeds 7 and 2024 still need to be confirmed from the saved results.

Criterion 3 evaluates the same dataset for all three seeds, so its 52.8% value does not change.

Criterion 4 requires independent labeling of 50 posts under my own taxonomy. The separate 30-post staff agreement exercise uses different definitions and does not directly satisfy this criterion.

Criterion 5 requires measuring accuracy specifically for predictions with confidence at least 0.80. The notebook's most-confident-third metric is not equivalent to that threshold.

### Confusion Matrix

| True \ Predicted | no_argument | unsupported | partial | well_supported |
|---|---:|---:|---:|---:|
| **no_argument** | 13 | 0 | 0 | 0 |
| **unsupported** | 1 | 0 | 0 | 0 |
| **partial** | 6 | 0 | 0 | 0 |
| **well_supported** | 4 | 0 | 0 | 0 |

**My biggest off-diagonal number, and what it means:**

The largest off-diagonal value is 6: all six actual `partial` posts were incorrectly predicted as `no_argument`, while zero actual `no_argument` posts were predicted as `partial`.

This indicates a one-directional failure. The model consistently predicts the majority class rather than distinguishing different levels of argument quality. Class imbalance is a plausible contributing factor, although the confusion matrix alone cannot prove the underlying cause.

---

## Verdicts and Diagnoses

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Overall accuracy | ≥80% on all three seeds | **MISSED** | Accuracy was 54.2% for seeds 42, 7, and 2024, below my 80% target. |
| 2 | Per-label F1 | ≥0.70 for every label on all three seeds | **MISSED** | The original seed-42 run had F1 scores of 0 for `unsupported`, `partial`, and `well_supported`. Macro F1 was only 0.176 across all three seeds. |
| 3 | Class balance | No label exceeds 50% of the dataset | **MISSED** | `no_argument` represented 84 of 159 posts (52.8%). |
| 4 | Human annotation agreement | ≥80% agreement on 50 independently labeled posts using my taxonomy | **NOT ESTABLISHED** | The staff comparison returned 30/30 matches, but it used a different taxonomy and only 30 posts. It does not measure my original criterion. |
| 5 | High-confidence accuracy | ≥85% accuracy among predictions with confidence ≥0.80 | **NOT ESTABLISHED** | The evaluation reported accuracy for the most-confident third, but not specifically for predictions at or above 0.80 confidence. |

### Diagnoses

**Criterion 1 — Overall accuracy**

The fine-tuned model achieved only 54.2% accuracy on all three seeds. The confusion matrix shows that it predicted `no_argument` for every test post in the original evaluation.

This suggests majority-class collapse. The model learned a strategy that performed reasonably on the largest category but failed to distinguish argument quality across all four labels.

**Criterion 2 — Per-label F1**

The original model achieved an F1 score of zero on three categories. In the seed-42 test set, all six `partial` posts, the single `unsupported` post, and all four `well_supported` posts were incorrectly classified as `no_argument`.

A likely contributor is insufficient data for minority classes. The dataset contained only six `unsupported` examples, with four used for training and one for testing in the reported splits.

Additionally, classifying investment arguments requires distinguishing subtle differences between evidence, reasoning, and unsupported assertions. The model may not have received enough diverse examples to learn these distinctions.

**Criterion 3 — Class balance**

My largest category, `no_argument`, represented 52.8% of the dataset, exceeding my original 50% target.

This imbalance creates an incentive for the model to favor the majority class. However, class imbalance alone does not prove why the model collapsed. Small sample size, training configuration, and possible annotation inconsistencies could also contribute.

**Criterion 4 — Human agreement**

My original criterion required 80% agreement on 50 posts independently labeled under my own taxonomy. I did not conduct that exact experiment.

The separate staff agreement comparison returned 30/30 matching classifications, but it used the staff's three-label taxonomy. Therefore, it cannot establish whether my original four-label TakeMeter taxonomy was applied consistently.

**Criterion 5 — Confidence accuracy**

My acceptance criterion required at least 85% accuracy when the model's prediction confidence was 0.80 or higher.

The original evaluation reported 87.5% accuracy for the most-confident third of predictions. However, the most-confident third is not necessarily the same group as predictions exceeding 0.80 confidence.

I therefore cannot establish whether the criterion was met without an additional threshold-specific evaluation.

**What the agreement report contributes to my diagnosis:**

The staff comparison showed 30 matching labels out of 30. If those classifications were completed independently before viewing the staff answers, that supports consistent application of the staff taxonomy on those examples.

However, the comparison cannot rule out inconsistent labeling in my TakeMeter dataset because it used different definitions and different posts.

As a result, the evidence more directly supports class imbalance and limited training examples as plausible explanations than it supports a demonstrated labeling-consistency problem.

---

## Agreement Report

**Agreement rate:** 30 / 30 = **100% matching labels**

**Disagreements:**

The comparison script reported zero disagreements between `my_staff_labels.csv` and the staff reference file.

There were therefore no disagreements to adjudicate or sort into the three diagnostic categories.

**What the pattern in my disagreements tells me:**

The two files matched on all 30 examples. If the labels were assigned independently before seeing the answer key, this suggests that the staff taxonomy was sufficiently clear for these particular examples.

However, matching labels alone does not verify that the comparison was blind, and the result cannot establish consistency in my separate TakeMeter taxonomy.

---

## The Improvement

**What I changed:**

I increased the number of training epochs from 3 to 6.

I kept the labeled dataset, learning rate (2e-5), batch size (16), maximum sequence length (128), and three random seeds (42, 7, and 2024) unchanged.

This allowed me to isolate the effect of additional training.

**Which diagnosis pointed at it:**

The original model predicted only `no_argument`, suggesting majority-class collapse. Its training and validation losses were still decreasing near the end of the initial three epochs.

I wanted to test whether the model needed more opportunities to update its weights before it could distinguish the minority categories.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥80% | 54.2% | 54.2% | 54.2% | **MISSED** |
| 2. Every label F1 | ≥0.70 each | Macro F1: 0.176 | Macro F1: 0.176 | Macro F1: 0.176 | **MISSED** |
| 3. Class balance | No label over 50% | 52.8% | 52.8% | 52.8% | **MISSED** |
| 4. Human agreement | ≥80% on 50 posts | Not measured | Not measured | Not measured | **NOT ESTABLISHED** |
| 5. High-confidence accuracy | ≥85% at confidence ≥0.80 | Not measured | Not measured | Not measured | **NOT ESTABLISHED** |

For Criterion 2, the notebook's run summary reports macro F1 rather than each individual label's F1. Because the macro F1 remains substantially below 0.70, the requirement that every label achieve at least 0.70 was not met.

**Did it help, and how do I know?**

No. Increasing the training duration from three to six epochs did not improve the classification metrics.

Before and after the change, all three seeds produced:

- Overall accuracy: 54.2%
- Macro F1: 0.176

For seed 42, final validation loss decreased from approximately 1.152 to 1.104. This indicates that additional training changed the model's optimization results, but did not improve its measured classification accuracy or macro F1.

The experiment suggests that simply increasing training duration is insufficient to resolve the observed classification problem.

---

## What's Still Broken

**Overall accuracy:** The model remains below my original 80% target. I would investigate whether more balanced and diverse training examples improve its ability to generalize.

**Per-label F1:** The original model did not correctly identify any examples of three categories in the held-out test set. My next experiment would focus on adding carefully labeled examples of the underrepresented categories, especially `unsupported`, and evaluating performance again across three seeds.

**Class balance:** My dataset still exceeds my stricter 50% maximum for any single label. I would collect additional genuine posts belonging to the less common categories, rather than artificially changing labels.

**Human annotation agreement:** I would arrange for another annotator to independently label 50 posts using my original TakeMeter definitions, then measure agreement and investigate every disagreement.

**High-confidence accuracy:** I would add an evaluation that selects predictions with confidence at least 0.80 and calculates accuracy within that subset. If too few predictions meet the threshold, I would report the sample size rather than claim reliable confidence performance.

I stopped after one controlled improvement experiment to preserve a clear before-and-after comparison and complete the project. The results did not meet most of my original targets, but they identified specific weaknesses for future work.

**The gap between what I meant my labels to capture and what the model learned:**

I intended TakeMeter to distinguish between posts with no investment argument, unsupported claims, partially supported arguments, and well-supported arguments. Instead, the original model predicted the most common category for every test post, showing that it had not learned the distinctions my taxonomy was designed to measure.

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
