# Project context

This checkout is `/workspace/getting-started`. Use `/workspace` for repositories,
virtual environments, model caches, and large outputs; the root filesystem is small.
Run Python with `uv run`. The project environment is `.venv`.
For existing cached models, use `HF_HOME=/workspace/getting-started/data/huggingface`.
Use `UV_CACHE_DIR=/workspace/.cache/uv` when installing dependencies.

`origin` is the user's fork, `https://github.com/agent-q1/aimo-interp-getting-started.git`.
`upstream` is `https://github.com/aimo-interp/getting-started.git`.
Do not include credentials or credential-store files in commits or tool output.

# Sources and precedence

- Current local README, ingestion/scoring programs, and Dockerfile specify the
  interface and runtime for this checkout. Check them before using historical guidance.
- `reference/aimo_paper_proposal.md` transcribes the July 2026 proposal. Its metrics,
  datasets, labeling, and infrastructure describe historical experiments and plans.
- The Discord history below was supplied by the user. It explains changes over time;
  it is not an independently verified statement of the current remote deployment.
- Official resources: https://aimo-interp.github.io/ and
  https://github.com/aimo-interp/getting-started#evaluation-environment.
- Leaderboard view: https://aimo-interp.github.io/#leaderboard.
- User clarification: `https://huggingface.co/datasets/aimo-interp/problems-public`
  is private and is not intended to be public, despite its repository name and
  its mention in the historical proposal. Do not describe it as a public release
  or assume its symbolic templates are available to participants.

# Useful Discord history (2026)

- August 3 and 11: warmup validation data changed repeatedly, including newly
  collected unpublished problems and verified robustness labels. Do not assume an
  older public sample matches the Codabench validation set.
- September 2: Main competition began with an expert-verified, rebalanced validation
  set. The announcement accidentally listed four models while saying five.
- September 14: organizers identified the omitted fifth model as Skywork-OR1-Math-7B
  and directed participants to the README for the exact model list.
- September 15: organizers reported that many leading submissions failed to
  generalize to unseen problems, often performing below random guessing. Their
  analysis attributed this to using problem features rather than model internals.
  They planned additional balancing so the same problem has both positive and
  negative labels across models, and a train release disjoint from validation.
- September 16: organizers announced replacement of the validation set with labels
  balanced per problem and per model, a cleared/repopulated leaderboard, and release
  of a complementary training set. Scores across leaderboard resets are not directly
  comparable. Reasoning-effort metadata was added to the submission interface.
- Undated clarification supplied by the user: runfme asked, "Hi! May
  self-generated mathematical perturbations and resulting model robustness labels
  be used only for validation or training?" Michael Stefanik replied:
  "Hi @runfme, you can use those for anything. Note that we have removed the rule
  on the training data from the official rules listed on the website, hoping to
  incentivize whitebox and light-weight methods with some constraints on the
  evaluation time. Just be careful not to overfit the existing validation sets as
  the final scoring will be done on the new problems."
  Self-generated mathematical perturbations and resulting model robustness labels
  are therefore permitted for both training and validation. Do not apply the
  proposal's historical restriction on extra labeled training data; evaluation
  time constraints still apply, and methods should generalize to new problems.

# Current model set and callable contract

The local README lists these exact Competition-phase model identifiers:

- `Qwen/Qwen3.5-4B`
- `Skywork/Skywork-OR1-Math-7B`
- `allenai/Olmo-3-7B-Think`
- `deepseek-ai/DeepSeek-R1-0528-Qwen3-8B`
- `openai/gpt-oss-120b` (Main Track only)

Use Olmo **Think**, not the older warmup **Instruct** checkpoint.
Competition-phase IDs are passed verbatim; historical public datasets may use aliases.

The September 16 Discord message showed `reasoning_effort: list[str]` after
`problems`. That conflicts with this checkout. The local supported interface is:

```python
def are_robust(model_id: str, reasoning_effort: str, problems: list[str]) -> list[bool]:
    ...
```

Ingestion groups cases by model and effort and calls with keyword arguments
`reasoning_effort=effort, problems=problems`. Effort is one string per group and defaults
to `"default"` when absent. The legacy `(model_id, problems)` interface is supported.
Return one native Python boolean per input problem in the original order.

# Baseline evaluation guidance

- Robustness labels belong to a model/problem/effort configuration. Do not apply a
  model-specific probe to other models and report the result as its baseline accuracy.
- Evaluate on unseen problems, keeping repeated problem statements together across
  train/validation/test splits. Stratification alone does not prevent prompt leakage.
- Report per-model and per-effort results alongside aggregate accuracy; check whether
  problem-only and model-only shortcuts explain performance. Inspect label balance and
  compare with a majority-class baseline. Balanced accuracy and ordinary accuracy are
  different metrics; identify which is being reported.
- Pin dataset revisions and record artifact provenance and evaluation scope. Public
  training-set evaluation of an exported ensemble is not an out-of-fold estimate.
- In this checkout, the pinned `val-sample` import has 24 cases across seven historical
  model IDs and eight problems. Only one case is named `qwen3-8b:low`; this is not a
  sufficient matching evaluation set for the bundled DeepSeek probe.
- The initial 62.5% local score used the DeepSeek artifact for all 24 cases because the
  generic artifact fallback does not enforce model matching. Do not cite it as a valid
  DeepSeek baseline reproduction.
- The bundled probe artifact selects layer 31 and contains both normal (`NONE`) and
  shuffled-label (`RANDOMIZATION`) control groups. The current inference scorer averages
  all groups. Keep randomized-label controls separate when implementing a scientific
  baseline; establish the intended scoring policy before changing submission behavior.
- The proposal reports probing accuracy 58.37% +/- 7.5 and uncertainty accuracy
  69.23% +/- 10.13, from stratified 10-fold CV on DeepSeek. It does not define the
  +/- statistic or provide enough configuration to reproduce these figures exactly.
- The upstream baseline code inspected at commit
  `7e8839966750059b6b1d247a12ab56552c79b342` is cloned at
  `/workspace/aimo-interp-baselines`. Its current defaults use four folds and five
  seeds, and metric summaries prefer balanced accuracy. Its aggregate CSV contains
  141 rows / 137 unique prompts for `qwen3-8b:low`; do not conflate this dataset or
  protocol with the 24-case sample or proposal's ten-fold experiment.
- `aimo-interp/train-main-v2` is a separate main-track public training release. At the
  inspected revision `23791d9b120132087877b0459f953d5959fc8455`, it contains 82 rows
  across the five models, with 71 labeled and 11 unlabeled cases. Its fields are
  `model_id`, `reasoning_effort`, `problem`, `is_robust`, and `max_drop`; it requires
  adaptation rather than passing directly through the historical sample importer.
  Preserve null labels; exclude them from supervised accuracy computation.
