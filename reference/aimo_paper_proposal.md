# AIMO Interpretability Challenge — proposal paper

- Source: [aimo_paper_proposal.pdf](aimo_paper_proposal.pdf), 13 pages.
- Paper version: arXiv:2607.13899v1 [cs.AI], 15 July 2026.
- Website: <https://aimo-interp.github.io/>.
- PDF SHA-256: `7f79aded0f928080335d83edbe99ee9e3f664dbddd4d1a8c0978f8e59c08c9f7`.
- Conversion: UTF-8 text extracted with Poppler `pdftotext`; paragraphs reflowed, section headings marked up, and the figure code, equation, and table reconstructed for readability. References, footnotes, and appendices are retained. Page markers refer to the source PDF. This is a transcription, not a summary; consult the PDF for exact typography and layout.

> Historical proposal: use the current challenge website for rules and this repository's README, harness, and Dockerfile for the submission interface and runtime. Proposal details about labels, data restrictions, hardware, deadlines, and prizes may have been superseded. The proposal's internal schedule inconsistencies are preserved here.

## Navigation

- Pages 1–5: motivation, data, task definition, metrics, and baselines (Section 1).
- Pages 6–8: organization, proposed rules, schedule, and resources (Sections 2–3).
- Pages 9–10: references.
- Pages 10–12: organizer biographies (Appendix A).
- Pages 12–13: perturbation types and adversarial evaluations (Appendix B).

---

## PDF page 1

AIMO Interpretability Challenge

Michal Štefánik1∗ Philipp Mondorf2∗ Andreas Waldis3∗ Qianying Liu1 Chuan Yang4 Michal Spiegel5 Josef Kuchař5 Marek Kadlčík5 Adam Vawda-Oomerjee6,1 Chaoran Liu1 Simon Frieder7,8 Barbara Plank2 Fazl Barez8,9 Pontus Stenetorp6,1 https://aimo-interp.github.io

arXiv:2607.13899v1 [cs.AI] 15 Jul 2026

### Abstract

We propose the AIMO Interpretability Challenge, a competition on distinguishing robust from spurious reasoning in frontier mathematical language models based on the models’ internal mechanisms. The challenge is motivated by a central limitation of standard reasoning benchmarks: strong final-answer accuracy does not reveal whether a model relies on stable reasoning mechanisms or exploits brittle reasoning shortcuts. Building on AI Mathematical Olympiad (AIMO) problems and submissions, together with resources from the Fields Model Initiative, the competition will provide (1) newly-published olympiad-level math reasoning problems and their symbolic representations, allowing generation of novel functional variants, (2) access to frontier reasoning models, and (3) assessments of models’ adversarial robustness on these problems. Participants will use these resources, along with our computing infrastructure support, to develop methods for identifying which models solve problems robustly. Our competition will also create a new, open robustness benchmark and baseline systems, aiming to provide a lasting foundation for standard benchmarking in mathematical reasoning and interpretability. Scientifically, the competition connects interpretability and generalization research around a central question in AI research: can we determine if, and to what extent, the decision-making of frontier AI models is generalizable and thus, reliable?

**Keywords:** interpretability, reasoning, robustness, language models, frontier AI capabilities.

### 1 Competition description

#### 1.1 Background and impact

Recent advances of large language models have sharpened a foundational disagreement in AI: whether frontier systems are beginning to exhibit generalized, frontier reasoning abilities, or whether they remain highly capable pattern matchers whose success often depends on spurious cues [Feng et al., 2024, Mondorf and Plank, 2024, Mirzadeh et al., 2025]. Standard benchmark scores alone can not resolve this disagreement, because they can not evidence how a system arrives at a correct answer. Interpretability offers a promising route forward: previous work uncovers robust mechanisms of internal representations [Štefánik et al., 2025] or identifies circuits claimed to implement meaningful functions decomposing the high-level problem into subproblems [Wang et al., 2023, Brinkmann et al., 2024] – implying that models’ underlying mechanisms are indeed vastly robust. However, much of current work is still dominated by compelling case studies and localized analyses that are difficult to compare and generalize [Bereska and Gavves, 2024, Templeton et al., 2024, Lindsey et al., 2025].

**Affiliations:** 1 National Institute of Informatics, Japan; 2 Munich Center for Machine Learning / MaiNLP LMU; 3 University of Tübingen; 4 Fuzhou University; 5 Masaryk University; 6 University College London; 7 AIMO Organization Team; 8 University of Oxford; 9 Martian. ∗ Core organizers.

Competition of the Conference on Neural Information Processing Systems (NeurIPS 2026)

## PDF page 2

The proposed competition targets this gap. Its scientific goal is to measure whether interpretability methods can identify mechanisms that generalize across problem instances and meaningfully distinguish robust models from brittle ones. This problem spans multiple NeurIPS-relevant areas, including interpretability, evaluation, generalization, reasoning, mathematical AI, and AI safety.

The submissions of this competition will be applicable in auditing high-stakes reasoning systems. In realistic deployment, a research lab, education provider, or scientific-assistance platform may choose among several models that achieve similar benchmark accuracy, yet differ substantially in reliability. The competition operationalizes this scenario by asking participants to infer robustness from behavior and internal model representations. Beyond the competition itself, the resulting symbolic robustness benchmark will also support future work focused on developing more robust frontier models.

We expect interest from both a general ML audience interested in models’ frontier capabilities, and the interpretability community interested in understanding the models’ internals. In 2026, AIMO 31 that was hosted Kaggle2 attracted more than 4,000 teams, indicating substantial upstream interest of the AI community in olympiad-level reasoning systems. In our challenge, we expect roughly 20–40 well-performing submissions from teams of researchers focused on interpretability and generalization.

#### 1.2 Novelty

With regard to prior competitions at ML conferences, the AIMO Interpretability Challenge is an entirely new competition. Its novelty lies in connecting interpretability with an objective that is increasingly relevant for the broader AI community, but standard benchmarks do not directly target: assessing whether frontier models that succeed on most complex reasoning tasks do so robustly. While this competition will not build the first interpretability benchmark available, the benchmark developed in this challenge will also make a valuable and lasting contribution to the field of interpretability. Existing interpretability benchmarks focus on evaluating interpretability methods in rudimentary and/or synthetic settings; Most aligned with us, the RAVEL benchmark tests whether methods can identify and disentangle attribute-value information [Huang et al., 2024], InterpBench tests whether methods recover planted internal algorithms from semi-synthetic transformers with known circuits [Gupta et al., 2024], and MIB advances standardized evaluation of circuit and causalvariable localization on synthetic, controlled tasks such as arithmetics [Mueller et al., 2025]. These benchmarks present valuable contributions for developing better interpretability methods, but their highly controlled settings limits their contribution in our understanding of the behaviour of frontier models. Our goal is not to validate recovery of known subcomponents, but to test whether interpretability can determine whether strong performance on hard reasoning problems reflects stable, generalizable reasoning mechanisms or brittle strategies that fail under structured variation. This goal is aligned with some recent work striving to identify generalization from internal circuitry [Huang et al., 2025] or attention patterns [Li et al., 2025, Spiegel et al., 2025]. To this line of work, the proposed competition brings both a standard benchmark and a reusable toolset for understanding the nature and limits in frontier reasoning capabilities and with the most advanced models.

#### 1.3 Data

The competition uses three main data components:

1. Original olympiad-level mathematical problems The core benchmark will be drawn from frontier mathematical problems included in AIMO 2, AIMO 3, JMO (Japanese Mathematical Olympiad), and two last years of AIME (American Invitational Mathematics Examination), totaling 180 problems. Thanks to the close involvement of mathematicians in our organizing team, we can guarantee that 50% of problems in both the train and test sets are new, i.e. not previously published on the Internet. We have confirmed that the licenses for these collections permit their use in the competition (public AIMO and AIME problems are both Apache 2.0-licensed, and we have received confirmation from the owners of the private AIMO and JMO problems).

2. Symbolic reasoning annotations For the original problems, we create new annotations of symbolic reasoning chains similar to the functional variation introduced by GSM-Symbolic [Mirzadeh

**Footnotes:**

- 1: https://aimoprize.com

- 2: https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-3

## PDF page 3

AIMO 2 Reference problem 480182 PROBLEM: Let ABC be a triangle with BC=[input1], CA=[input2], and AB=[input3]. Point X lies on segment AC such that BX bisects angle CBA. Let omega be the circumcircle of triangle ABX. Let Y be a point on omega different from X such that CX=CY. Line XY meets BC at E. The length of the segment BE can be written as m/n, where m and n are coprime positive integers. Find m+n. INPUT CONSTRAINTS: CA > BC >> AB (BC > AB * 2)

```python
def solution(bc, ca, ab):
    cx = (bc * ca) / (bc + ab)  # Step 1: Find CX by applying the Angle Bisector Theorem.
    power_c = cx * ca  # Step 2: Compute the power of C wrt the circumcircle of ABX.
    cb_prime = power_c / bc  # Step 3: Find the circle’s second intersection with line BC.
    x = (bc * cb_prime + cx * cx) / (bc + cb_prime)  # Step 4: Locate E on BC by equating powers.
    be = abs(bc - x)  # Step 5: Convert E’s coordinate into segment length BE.
    best_num, best_den = min(  # Step 6: Approximate BE as a fraction m/n.
        ((round(be * den), den) for den in range(1, 1000)),
        key=lambda t: abs(be - t[0] / t[1]),
    )
    a, b = best_num, best_den  # Step 7: Reduce m/n using the Euclidean algorithm.
    while b:
        a, b = b, a % b
    return best_num // a + best_den // a
```

Figure 1: Newly annotated symbolic template for AIMO 2 reference problem 480182.

et al., 2025] but centered on the frontier reasoning level: these chains capture the logical inference underlying valid solutions, allowing us to generate unconstrained volumes of adversarial problem variants following controlled distribution shifts (Fig. 1). We will use these to identify and annotate the interpreted models for their robustness. In this collection, we build on deep expertise in mathematics brought by a direct involvement of olympiad-level mathematicians in our organizational board, including mathematicians from Fuzhou university in the PRC, National Institute of Informatics in Japan and their network of frontier mathematicians at Peking university. By the submission date, we are close to completing the annotation process and will have the full collection ready within one month from the submission deadline.3 The full train split of problems with associated symbolic reasoning chains will be publicly released for any use under permissible Apache 2.0 license before the competition starts.

In Appendix B, we provide results of robustness to permutations with already-collected symbolic chains, evidencing that they indeed allow us to generate problem variants that can systematically mislead frontier AI models within and beyond AIMO, including Qwen, GPT 5.2, and Gemini-Pro.

3. Interpreted model set As the analysed models, the challenge will pick among the top-performing AIMO submissions and derive robust/spurious labels from their evaluation on the counterfactual evaluation set. Participation of AIMO organisers in this challenge provides competition participants and us with easy access to these models.

**Data splits**

The collected problems will be split into the train and test collections:

- Train split will include 150 problems from both published and not-yet-published sources (AIMO, AIME, JMO).

- Test split will contain 30 problems provided by the AIMO 3 organizers at varying levels of difficulty. These problems are and will not be made public and will only be accessible by the participants’ submissions through automated evaluation on our servers.

The data volume is sufficient for training and a meaningful evaluation because the effective size of robustness labels (Sec 1.4) comes from the cross-product of original problems and models. We aim to include at least 8 top-performing models in our evaluations, resulting in roughly 1200 training and 240 test instances. Nevertheless, to support more data-demanding methods, we will additionally release an LLM-based codebase to generate adversarial training data from generic perturbations not requiring symbolic chains. Our new benchmarks will not involve personal or sensitive user data. New symbolic chains are created directly by the organizers rather than collected from human subjects. 3

A sample of public problems with our newly annotated, verified symbolic chains allowing perturbations is available on: https://huggingface.co/datasets/aimo-interp/problems-public

## PDF page 4

Challenge summary Given a mathematical problem and a model providing a correct solution to this problem, the task is to decide if the model responds to the given problem robustly w.r.t. to a pre-defined set of distribution shifts.

#### 1.4 Tasks and application scenarios

The central task of the AIMO Interpretability Challenge is to determine which model provides a correct answer to a given problem robustly. Formally, given a triple of (Problem X, Model M, Distribution shift ∆) where M (P ) is correct (i.e. M (X) = ytrue ), the task is to determine whether M (∆X) will also be correct for all perturbations under ∆. The participants will be asked to create a submission system S that assigns one of two categories to each triple (X, M, ∆):

$$
S(X,M,\Delta) =
\begin{cases}
0 & \text{if for a majority of } \Delta X \in \Delta:
    M(X)=y_{\mathrm{true}} \text{ and } M(\Delta X)\ne y_{\mathrm{true}},\\
1 & \text{otherwise.}
\end{cases}
$$

*Transcription note: the preceding sentence uses `M(P)` where the surrounding discussion uses `M(X)`; this source notation is retained. This proposal equation is not the current competition labeling criterion.*

While determining a general robustness of M across all possible distribution shifts is intractable, annotations of symbolic chains (Fig. 1) offering an unconstrained number of perturbed problems ∆X will allow us to generate a sufficiently large and broad set to uncover a systematic robustness or fragility of M under ∆. This abundance will also allow us to leave out from evaluation sets the samples that are not clear-cut; i.e. where either the original model is not robustly correct (e.g. in a repeated sampled generation) or the evaluated perturbations ∆X do not cause a consistent deterioration to the M ’s prediction.

The distribution shifts ∆ will be instantiated by applying one or more perturbation types on the original problem using its symbolic representation. A non-exhaustive list of perturbations that can be instantiated using our symbolic chains and that we already tested can be found in Appendix B together with examples of their corresponding performance drops.

The challenge is offered in two tracks differing in the scale of analyzed models:

- Main track including a full scale of top-performing models from AIMO 3;

- Small models track subsetting the evaluation to best-performing models below the 10-billionparameter scale, providing a comparable setup for methods that are more compute-heavy to train, such as Sparse Autoencoders or Transcoders.

**Application** The competition task corresponds to a concrete real-world need: selecting and auditing the robustness of strong reasoning models before deployment. In industry, this matters for systems that support scientific work, quantitative analysis, or educational tutoring, where a model that appears strong on a benchmark but fails under innocuous reformulations may have costly or harmful consequences. Nevertheless, our competition is primarily aimed at contributing to support a central, open research goal: understanding whether, and to what extent, models’ successes in tasks of frontier complexity stand upon robust reasoning mechanisms or brittle shortcut following.

**Feasibility** The presented challenge is scientifically challenging but tractable; It is challenging because models’ black-box behaviour on the original problem will in most cases likely not be sufficient for dissecting robust and non-robust inference mechanisms,4 reducing the usefulness of standard evaluation and making the distinction to benefit from deeper behavioural or mechanistic evidence. At the same time, it is tractable because the competition provides a clear extrinsic signal of success – providing labelled datasets that support experimentation with a wide range of possible methods and strategies.

**Code of Ethics** The competition is aligned with the NeurIPS Code of Ethics; its primary aim is to improve reliability assessment of AI systems, it does not target or profile people and it supports safer deployment by helping practitioners identify brittle systems before they are used in consequential 4

While this is just an assumption, we note that showing the contrary would have significant implications for a reliability of deployments, itself being a valuable contribution.

## PDF page 5

settings. Potential risks include overclaiming the strength of interpretability methods based on the competition results. We will mitigate these risks through shaping the submission rules against overfitting, maintaining a private test set, and open-sourcing the full scope of our evaluations.

#### 1.5 Metrics

The primary metric will be accuracy on the held-out test set, i.e., the fraction of examples for which a submission correctly classifies the model as robust or non-robust. This metric directly reflects upon our main research question of whether we can dissect the robustness of LLMs decision-making mechanisms by their internal behaviour. Together with the global accuracy, in our final report, we will also provide evaluations dissecting performance: (1) for public and private sets; (2) for each perturbation type; (3) for each model; (4) for the previously published and unpublished problems. For the final report, we will use nonparametric bootstrap confidence intervals over test examples and paired significance testing (e.g., McNemar’s test on per-example decisions) for the comparisons of the final submissions. Both in-competition and final evaluations will be run on the isolated infrastructure of organizers, with 32 CPU cores, 512GB of RAM and eight large-scale N GPUs for both in-competition and the final evaluation. We will use the submission bundle interface predefined by the Codabench competition platform5 , assuring reproducibility of valid submissions in docker containers.

#### 1.6 Baselines, code, and material provided

**Baselines** For the competition, we will implement at least three baselines provided as starting bundles: (1) a simple probing classifier [Belinkov, 2022, Waldis et al., 2024] predicting robustness label from the internal representations of last input token on the best-performing layer, (2) a classifier based on model-internal confidence signals during chain-of-thought generation [Grünefeld et al., 2026], and (3) a data attribution method [Park et al., 2024] assessing robustness as the impact and scale of memorization. We have already implemented the first two of the baselines using different types of classifiers and evaluated them with DeepSeek-R1-0528-Qwen3-8B6 on our sample validation set in stratified 10-fold cross-validation. We found that (1) the probing classifier and uncertainty-based classifier achieves up to 58.37 (±7.5) and 69.23% (±10.13) of accuracy, respectively. As such, both baselines outperform the random-guessing baseline (50%), showing that our newly proposed task is both feasible as models’ internals exhibit an informative signal, and challenging as the results leave plenty of room for improvements.

All these baselines will be provided as implementations on the competition GitHub7 with instructions how to build them into a ready-to-submit Codabench submission bundle. As such, participants will start their implementations from functional prototypes, minimising their time spent in familiarizing with the formatting of submissions.

Each baseline will publish its full lifecycle codebase, including reusable competition data loaders, training code, local evaluation, submission bundle build, and submission interface. We will provide all implementations, together with a high-level walkthrough of these steps, as a starting guide in this GitHub’s README by the announcement of the competition (July 1, 2026). The Starter kit is already referenced from the header of the competition website.

Beyond this Starter kit, we already make available:

1. Public, human-readable sample of train and validation sets8 with examples in a format defined in Section 1.4, i.e. containing a collection of samples with (1) a math word problem, (2) a model (i.e. a HuggingFace model ID) and (3) a label of the tested distribution shift;

2. A ready-to-run implementation of a baseline competition systems9 ;

**Footnotes:**

- 5: https://codabench.org

- 6: DeepSeek-R1-0528-Qwen3-8B was among the three highest-ranked models in AIMO 3.

- 7: https://github.com/aimo-interp/baselines

- 8: https://huggingface.co/datasets/aimo-interp/val-sample

- 9: https://github.com/aimo-interp/baselines

## PDF page 6

3. Evaluation codebase that will exactly match the one ran on a private test set on our servers through Codabench10 ; All model types included in the private test set will be covered in the public validation set;

4. A convenient Codabench competition interface, including a leaderboard presenting the results of evaluations of participants’ submissions on the private test set in real time.11

All these resources will be linked from the competition’s Starter kit. Possible rough edges will be refined via testing submissions before the competition opens and in the Warmup competition phase.

#### 1.7 Website, tutorial and documentation

The public challenge website, https://aimo-interp.github.io, already presents the challenge motivation, task, tracks, environment, a concise “How to participate” guide, FAQ covering tracks, data usage, hardware access, and submission format, a dedicated organiser contact address, and a timeline overview with key competition dates.

### 2 Organizational aspects

#### 2.1 Protocol

The competition will run fully online before the conference. Each team will complete these steps:

1. Register on Codabench, read the rules, and download the submission bundle with a baseline. Full public split of validation data will be publicly available and referenced from the website;

2. (optional) Apply for the compute resources provided by the organisers via the Fields Model Initiative12 by completing the online form;

3. Submit executable containers on Codabench. These will be evaluated on the private test set on our servers with no Internet connection and fixed compute budget (1 hour per problem on 8-GPU nodes);

4. After the competition deadline, participants will be required to submit a 1–2-page technical report, summarizing the methods applied in their submission. Cheating and overfitting will be limited through hidden tests, limits on the number of submissions, offline execution, and compliance checks after the deadline. Before the competition start, the submission interface and leaderboards will be tested with the organisers’ baselines.

We support the openness of the competition to underresourced communities not only by an open call for application for compute resources (§3.2), but also by introducing a dedicated small-model track (§1.4) and a standardised evaluation pipeline running on our hardware.

#### 2.2 Rules and Engagement

Submission rules.

Submissions must follow the following data rules to prevent overfitting:

1. Data: teams may not use extra labeled data for the same perturbation types as in our final validation set; however, unlabeled data and labeled data for other perturbations are allowed.

2. Signals: teams can use weights, activations, token probabilities, or any other black-box statistics as inputs for their methods.

3. Tracks: teams may submit to the Main or Small models track, but each submission will count only for the chosel submission track.

4. Report: ranked teams must submit a technical report within one week for compliance checks.

**Footnotes:**

- 10: https://github.com/aimo-interp/evaluation

- 11: Codabench interface of the competition is now privately available at this url.

- 12: https://www.fieldsmodel.org

## PDF page 7

These rules discourage overfitting to our robustness-labeling mechanism, reward methods’ generalization, and keep participation open across affiliations, geographies, career and technical levels.

**Communication** All official competition updates will be communicated via email to all participants enrolled in the competition in Codabench and in the competition’s Discord server on the announcements channel. Participants can always reach out to organizers by using the official email (aimo-interp@gmail.com) or by tagging one of the organizers in the Discord channel. The official competition website will maintain and update a dedicated FAQ section with participants’ questions.

#### 2.3 Schedule and readiness

**Schedule** 1) By July 15: finalize splits, baselines, and Codabench setup; 2) Late July: competition announcement, release of validation data and Starter bundles with baselines; 3) By Aug. 2026: submissions warm-up phase permitting minor changes in the interface; 4) Aug. 1–Nov. 1: main competition phase; 5) Oct. 1: final submission deadline; 6) Nov. 15: technical reports due; 7) Nov. 15: results validation and analysis; 8) Dec. 1: final leaderboard and organizers report publications, workshop materials and schedule finalized; 9) Dec. 11/12: competition workshop. The schedule gives participants at least three months from the announcement to final evaluation, which is suitable for training or designing potentially complex interpretability methods.

**What is already ready** We have a near-final version of the public website, including task specifications, contacts, and FAQs. Further, we already have implementations of evaluations, a competition dataset sample, Codabench competition and implementations of baselines. We also have agreements on data and resource sharing within AIMO and the Fields Model Initiative allowing us to immediately provide the compute resources to interested participants. An outstanding task that we are working on now is a further extension of our datasets with the non-public problems from AIMO and JMO.

**Contingency plan** In the case that fewer than 3 participating teams will submit by the deadline, we will implement further baselines from the prior work and include them in the reports, delivering on our scientific goals. In the case that the allocated compute resources for our evaluations and participants become unexpectedly unavailable, we may restrain the Small models track towards even smaller models and provide the resources for evaluation, including GPUs, from commercial sources.

Our competition will involve a private sets of problems from AIMO that are not publicly available. In the unlikely case that AIMO organisers withdraw from this agreement, we will replace the test set with unpublished problems of comparable complexity from JMO. We will move forward with the competition according to the schedule, regardless of these externalities.

#### 2.4 Competition promotion and incentives

We will promote the competition through the organizers’ research networks, including both AI and less-represented pure mathematics networks. We will also advertise the call for participation through official competition social-media accounts and reposts by organisers on Bluesky, LinkedIn, and X. We will also use our networks to promote the challenge through online channels and in-person presentations at closely related venues taking place during the competition, including the GEM workshop at ACL 2026, the Mechanistic Interpretability and AI4Math workshops at ICML 2026, and the BlackboxNLP workshop at EMNLP 2026. These venues will help us reach a broad range of researchers interested in evaluation, interpretability, reasoning, and mathematical problem solving.

**Incentives** All participants will be invited to submit a non-archival technical report after the competition deadline. Submissions with strong empirical results or broadly impactful methodological lessons documented in their report will be invited to present at the in-person competition venue. As of today, we are awaiting confirmation of industrial sponsorship for a 500 USD award for the best-ranked method in each track.

#### 2.5 Competition track workshop and dissemination

We will create and maintain a dedicated Discord server where we will encourage team formation, discussion of ideas and preliminary results, and allow participants to reach out to us directly with any questions. The competition workshop will allow submitting a non-archival one-page technical report for each submission.

## PDF page 8

Based on the reports, we will invite selected participants to present their methods on site at the workshop, highlighting strong results and generalizable methodological lessons. The workshop will include the overview presentation with the final results, general takeaways, summarizing what worked and what did not. The program will also include 2–3 invited talks from invitees or members of the advisory board, featuring experts in evaluation, interpretability and generalization.

With the participants’ permission, we will also promote the findings documented in the reports on the competition’s social media accounts. We will release the pre-print with the competition findings before the workshop’s in-person event.

### 3 Resources

#### 3.1 Organizing team

The organizing team combines expertise in evaluation, interpretability and data collection with top-tier mathematicians, setting us to a unique position for curating a high-quality data collection that our competition builds upon. Close involvement of organizers of AIMO, ranking among the 30 largest competition in the history of Kaggle, also brings to our team a unique expertise with competition organization at scale. In overview, our team consists of the following experts and their roles:

- Michal Štefánik (National Institute of Informatics, Japan) – Competition coordination, website maintenance and communication

- Philipp Mondorf (MCML / MaiNLP LMU) – Competition coordination, baseline implementations, leaderboard

- Andreas Waldis (University of Tübingen) – Baseline implementations and beta testing

- Qianying Liu (National Institute of Informatics, Japan) – Olympiad math expert: validation of robustness evaluations

- Chuan Yang (Fuzhou University) – Olympiad math expert (top-100 in Chinese National Olympiads): supervision and coordination of data collection with mathematical communities

- Michal Spiegel (Masaryk University) – Data: robustness labels collection

- Josef Kuchař (Masaryk University) – Codabench & infrastructure development

- Marek Kadlčík (Masaryk University) – Data: Symbolic chains and permutations design

- Adam Vawda-Oomerjee (National Institute of Informatics / University College London) – Infrastructure support, Codabench administration, beta testing

- Chaoran Liu (National Institute of Informatics, Japan) – Infrastructure: participants’ support

- Simon Frieder (AIMO Manager / University of Oxford / Benchmarks & Baselines) – Advisory board: Competition infrastructure design, coordination on accessing AIMO models and data

- Barbara Plank (MCML / MaiNLP LMU) – Advisory board: evaluation and data collection

- Fazl Barez (University of Oxford) – Advisory board: Interpretability methods

- Pontus Stenetorp (University College London / National Institute of Informatics, Japan) – Advisory board: evaluation and adversarial data collection, initiative promotion

#### 3.2 Resources provided by organizers

The competition will provide resources and infrastructure, opening the abilities of frontier industrial labs to the broader community:

- Large-scale compute: participating teams may request an access to up to 10,000 H200 GPUhours of compute, justified in the submitted proposal;

- Frontier reasoning models: we will provide unrestricted access to best-performing AI systems from AIMO in standalone, fully reproducible containers;

- Standardized evaluation infrastructure: official submissions will be evaluated on our infrastructure with access to eight large-scale GPUs, supporting even cost-heavy inference methods;

## PDF page 9

#### 3.3 Support requested

We would appreciate standard support from the NeurIPS 2026 Competition Track organizers, especially inclusion in official promotion channels to help us reach relevant communities, as well as appropriately sized on-site meeting space for the competition session. We would also welcome any additional guidance from the Competition Track organizers to support the smooth and successful execution of the competition.

### References

Yonatan Belinkov. Probing classifiers: Promises, shortcomings, and advances. Computational Linguistics, 48(1):207–219, 04 2022. ISSN 0891-2017. doi: 10.1162/coli_a_00422. URL https://doi.org/10.1162/coli_a_00422.

Leonard Bereska and Stratis Gavves. Mechanistic interpretability for AI safety - a review. Transactions on Machine Learning Research, 2024. ISSN 2835-8856. URL https://openreview.net/forum?id=ePUVetPKu6. Survey Certification, Expert Certification.

Jannik Brinkmann, Abhay Sheshadri, Victor Levoso, Paul Swoboda, and Christian Bartelt. A mechanistic analysis of a transformer trained on a symbolic multi-step reasoning task. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Findings of the Association for Computational Linguistics: ACL 2024, pages 4082–4102, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.findings-acl.242. URL https://aclanthology.org/2024.findings-acl.242/.

Tao Feng, Chuanyang Jin, Jingyu Liu, Kunlun Zhu, Haoqin Tu, Zirui Cheng, Guanyu Lin, and Jiaxuan You. How far are we from AGI: Are LLMs all we need? Transactions on Machine Learning Research, 2024. ISSN 2835-8856. URL https://openreview.net/forum?id=H2ZKqfNd0U. Survey Certification.

Nils Grünefeld, Bertram Højer, Philipp Mondorf, Barbara Plank, Anna Rogers, Christian Hardmeier, Stefan Heinrich, and Jes Frellsen. Tracing uncertainty in language model "reasoning", 2026. URL https://arxiv.org/abs/2605.07776.

Rohan Gupta, Iván Arcuschin, Thomas Kwa, and Adrià Garriga-Alonso. Interpbench: Semi-synthetic transformers for evaluating mechanistic interpretability techniques. In ICML 2024 Workshop on Mechanistic Interpretability, 2024. URL https://openreview.net/forum?id=YXhVojPivQ.

Jing Huang, Zhengxuan Wu, Christopher Potts, Mor Geva, and Atticus Geiger. RAVEL: Evaluating interpretability methods on disentangling language model representations. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8669–8687, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.470. URL https://aclanthology.org/2024.acl-long.470/.

Jing Huang, Junyi Tao, Thomas Icard, Diyi Yang, and Christopher Potts. Internal causal mechanisms robustly predict language model out-of-distribution behaviors. In Forty-second International Conference on Machine Learning, 2025. URL https://openreview.net/forum?id=Ofa1cspTrv.

Victoria R. Li, Jenny Kaufmann, Martin Wattenberg, David Alvarez-Melis, and Naomi Saphra. Can interpretation predict behavior on unseen data?, 2025. URL https://arxiv.org/abs/2507.06445.

Jack Lindsey, Wes Gurnee, Emmanuel Ameisen, Brian Chen, Adam Pearce, Nicholas L. Turner, Craig Citro, David Abrahams, Shan Carter, Basil Hosmer, Jonathan Marcus, Michael Sklar, Adly Templeton, Trenton Bricken, Callum McDougall, Hoagy Cunningham, Thomas Henighan, Adam Jermyn, Andy Jones, Andrew Persic, Zhenyi Qi, T. Ben Thompson, Sam Zimmerman, Kelley Rivoire, Thomas Conerly, Chris Olah, and Joshua Batson. On the biology of a large language model. Transformer Circuits Thread, 2025. URL https://transformer-circuits.pub/2025/attribution-graphs/biology.html.

## PDF page 10

Seyed Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar. GSM-symbolic: Understanding the limitations of mathematical reasoning in large language models. In The Thirteenth International Conference on Learning Representations,

2025. URL https://openreview.net/forum?id=AjXkRZIvjB.

Philipp Mondorf and Barbara Plank. Beyond accuracy: Evaluating the reasoning behavior of large language models - a survey. In First Conference on Language Modeling, 2024. URL https://openreview.net/forum?id=Lmjgl2n11u.

Philipp Mondorf, Samuel J. Bell, Jesse Dodge, and Dieuwke Hupkes. Lpds: Evaluating llm robustness through logic-preserving difficulty scaling, 2026. URL https://arxiv.org/abs/2605.15393.

Aaron Mueller, Atticus Geiger, Sarah Wiegreffe, Dana Arad, Iván Arcuschin, Adam Belfki, Yik Siu Chan, Jaden Fried Fiotto-Kaufman, Tal Haklay, Michael Hanna, Jing Huang, Rohan Gupta, Yaniv Nikankin, Hadas Orgad, Nikhil Prakash, Anja Reusch, Aruna Sankaranarayanan, Shun Shao, Alessandro Stolfo, Martin Tutek, Amir Zur, David Bau, and Yonatan Belinkov. MIB: A mechanistic interpretability benchmark. In Aarti Singh, Maryam Fazel, Daniel Hsu, Simon LacosteJulien, Felix Berkenkamp, Tegan Maharaj, Kiri Wagstaff, and Jerry Zhu, editors, Proceedings of the 42nd International Conference on Machine Learning, volume 267 of Proceedings of Machine Learning Research, pages 45069–45108. PMLR, 13–19 Jul 2025. URL https://proceedings.mlr.press/v267/mueller25a.html.

Sangdon Park, Bernhard Schölkopf, Andrew Ilyas, Logan Engstrom, and Aleksander Madry. Data attribution at scale. ICML Tutorial, 2024. URL https://ml-data-tutorial.org/. Presented at the International Conference on Machine Learning (ICML 2024).

Michal Spiegel, Michal Štefánik, Marek Kadlčík, and Josef Kuchař. Attend or perish: Benchmarking attention in algorithmic reasoning, 2025. URL https://arxiv.org/abs/2503.01909.

Adly Templeton, Tom Conerly, Jonathan Marcus, Jack Lindsey, Trenton Bricken, Brian Chen, Adam Pearce, Craig Citro, Emmanuel Ameisen, Andy Jones, Hoagy Cunningham, Nicholas L Turner, Callum McDougall, Monte MacDiarmid, C. Daniel Freeman, Theodore R. Sumers, Edward Rees, Joshua Batson, Adam Jermyn, Shan Carter, Chris Olah, and Tom Henighan. Scaling monosemanticity: Extracting interpretable features from claude 3 sonnet. Transformer Circuits Thread,

2024. URL https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html.

Andreas Waldis, Yotam Perlitz, Leshem Choshen, Yufang Hou, and Iryna Gurevych. Holmes: A benchmark to assess the linguistic competence of language models. Transactions of the Association for Computational Linguistics, 12:1616–1647, 2024. doi: 10.1162/tacl_a_00718. URL https://aclanthology.org/2024.tacl-1.88/.

Kevin Ro Wang, Alexandre Variengien, Arthur Conmy, Buck Shlegeris, and Jacob Steinhardt. Interpretability in the wild: a circuit for indirect object identification in GPT-2 small. In The Eleventh International Conference on Learning Representations, 2023. URL https://openreview.net/forum?id=NpsVSN6o4ul.

Michal Štefánik, Timothee Mickus, Marek Kadlčík, Bertram Højer, Michal Spiegel, Raúl Vázquez, Aman Sinha, Josef Kuchař, and Philipp Mondorf. Unravelling the mechanisms of manipulating numbers in language models, 2025. URL https://arxiv.org/abs/2510.26285.

### A Biography of all team members

Michal Štefánik (Lead organizer) is a Specially Appointed Researcher at the National Institute of Informatics, Japan (NII) with a track record in evaluation, interpretability and generalization of large language models. Prior to NII, he was a Postdoctoral Research Associate at the University of Helsinki, Finland and a PhD Researcher at Masaryk University, Czechia. He has a track record of first-authored publications at *ACL and EMNLP conferences focused on the robustness of neural language models. His research in this area was awarded several prizes and awards, including two Best Paper awards and a Dean’s Award (top 10%) for his dissertation studying covariates of robustness of neural language models. Beyond research, Michal holds over 8 years of AI research experience across startups and corporates.

## PDF page 11

Philipp Mondorf (Core organizer) is a third-year PhD student at LMU Munich specializing in reasoning, evaluation, interpretability, and generalization in language models. He has an established publication record at leading AI and NLP venues, including ICLR, ICML, ACL, EMNLP, EACL, and COLM. During his time at Meta FAIR, he worked on improving the reasoning robustness of LLMs in collaboration with leading experts in the field, including Dieuwke Hupkes and Jesse Dodge. He is currently a visiting researcher at NYU and Princeton University, where he conducts research on compositional generalization with Brenden Lake and Todd Gureckis. Andreas Waldis (Core organizer) is a PostDoc and Junior Group Lead at the University of Tübingen. His research focuses on understanding and improving the reliability of language models, with an emphasis on methods that integrate internal and behavioral perspectives. His work spans evaluation, interpretability, and generalization, with applications to computational argumentation and societal alignment. He co-organized the first shared task on Perspective Argument Retrieval (ArgMining@ACL2024), the previous iteration of INTERPLAY in 2025, and KnitTogether25, a European summit supporting early-career researchers in computational linguistics, and regularly serves as an Area Chair at ARR.

Qianying Liu is a Specially Appointed Researcher at the Large Language Model Research and Development Center of National Institute of Informatics, Japan (NII). Her research focuses on multilingualism, reasoning, and interpretability of large language models, with publications in major venues including ACL, EMNLP, TASLP, and AAAI. Prior to joining NII, She completed PhD studies at Kyoto University under the supervision of Professor Sadao Kurohashi. She has also regularly served as a Senior Area Chair for ARR and various other major conferences.

Chuan Yang is an Associate Professor in the School of Mathematics and Statistics at Fuzhou University. Her research focuses on discrete modeling, combinatorial, and continuous optimization. Her research works have been accepted or published in SIMAX, Sci. China Math., and Commun. Math. Sci. Prior to joining Fuzhou University, she received her PhD in Computational Mathematics from Peking University.

Adam Vawda-Oomerjee is a Visiting Researcher at the Large Languge Model Research and Development Center at the National Institute of Informatics, Japan (NII), and a Research Assistant in the Natural Language Processing Group (NLP) at University College London (UCL). His work focuses on understanding reasoning, reinforcement learning, and world models.

Michal Spiegel is a student researcher at Masaryk University, Czechia, and a Machine Learning Engineer at Filevine. Previously, he served as an NLP researcher at the Kempelen Institute of Intelligent Technologies. Specializing in mechanistic interpretability, his research focuses on algorithmic reasoning and length generalization within large language models. He has an established early-career track record with publications at major NLP venues, including ACL and EMNLP. Recently, he served as a visiting researcher at the National Institute of Informatics (NII), Japan, where he focused on robustness evaluations in mathematical reasoning.

Josef Kuchař is a student researcher at Masaryk University, Czechia. He is interested in artificial intelligence agents and software engineering, with a particular focus on alternative LLM architectures. He co-authored or first-authored four publications presented at ACL, EMNLP, and LREC conferences. His work combines practical software engineering with machine learning research. In this competition, he will contribute his engineering expertise to design and develop a suitable Codabench interface.

Marek Kadlčík is a second-year PhD student at Masaryk University, Czechia, specialized in reasoning, reinforcement learning, and the generalization of neural models. He has an established publication record at leading NLP venues such as ACL and EMNLP, and his prior work in reinforcement learning have been honored with two Dean’s Awards and one Rector’s Award. Beyond academia, Marek has several years of practical experience in R&D spanning applications in NLP, computer vision, and reinforcement learning.

Chaoran Liu is currently a Project Associate Professor at the National Institute of Informatics (NII), Japan. Previously, he was a Research Scientist at RIKEN and a Specially Appointed Assistant

## PDF page 12

Professor at Osaka University. His recent work centers on large language models, with a focus on pretraining analysis, data attribution, training dynamics, and formal mathematical reasoning using LLM-based agents. His broader research background includes signal processing, robotics, and human–robot interaction. In this competition, he contributes infrastructure expertise and participant support.

Simon Frieder is the AIMO Prize Manager and founder of Benchmarks & Baselines the non-profit, dedicated to benchmarks LLMs on reasoning tasks. Previously, he studied toward a PhD at the University of Oxford, UK. He holds separate degrees in mathematics and computer science, and his research has been featured in popular science and technology outlets such as Ars Technica and ZDNet, as well as cited in AI-related reports by the German government. He has published at leading machine learning conferences, including NeurIPS, ICML, and ICLR. He will advise on organizational aspects and assist with coordination in sharing findings and resources with the AIMO competition.

Barbara Plank is a Full Professor and Chair for AI and Computational Linguistics at LMU Munich, where she leads the Munich AI & NLP Lab (MaiNLP) and co-directs the Center for Information and Language Processing (CIS). Her research focuses on natural language processing, especially robust and inclusive models that account for domain shift, language variation, limited supervision, and human label variation, with broader interests in interpretability, reasoning, and trustworthy evaluation. In this competition, she will advise on robust NLP evaluation and methods for handling data variation and annotation uncertainty.

Fazl Barez is a Senior Researcher at the University of Oxford, where he is Principal Investigator of the Technical Safety & Governance (TSG) Lab and Technical Director of the AI Governance Initiative. His group works across AI safety, interpretability, and technical governance. At Oxford, he teaches the AI Safety and Alignment course, and alongside his academic work, he is Principal Scientist at Martian, where they work on understanding machine intelligence. His research is supported by OpenAI, Anthropic, Schmidt Sciences, NVIDIA, and others. In this competition, he will advise on support for interpretability methods.

Pontus Stenetorp is a Professor of Natural Language Processing (NLP) at University College London (UCL), Deputy Director of the UCL Centre for Artificial Intelligence and Specially Appointed Professor at National Institute of Informatics, Japan. He leads the UCL NLP group and his primary research contributions and interests lie in the areas of model and system development, evaluation, and analysis. His research has received awards at leading conferences in his field: outstanding paper at EACL 2017, best paper at EACL 2021, outstanding paper at ACL 2022, and best paper ACL 2023. To date he has published more than 100 publications, which have been cited more than 9,000 times. In this competition, he will advise on adversarial data collection methodologies.

### B Perturbation types and adversarial evaluations

Following GSM-Symbolic [Mirzadeh et al., 2025] and related symbolic-template approaches [Mondorf et al., 2026], we evaluate robustness under answer-preserving and adversarial perturbations of annotated reasoning-chain examples. The open list of perturbations that we implemented to date of submission is:

- Rephrase: semantic-preserving rewrites of the original problem.

- Rename: renaming of variables or entities while preserving the underlying structure.

- Domain: transfer of the same mathematical structure to a different surface domain.

- Distract: insertion of irrelevant but plausible information.

- Typos: introduction of harmless typographical or formatting noise.

- Expert perturbations: answer-preserving adversarial edits making use of the expert knowledge of the problem (mathematical conventions, unstated premises or assumptions).

- Expert no-solution: unanswerable variants of the problems (e.g. missing some of the problem premises) intended to test unsolvability detection.

## PDF page 13

| AIMO ref. problem | Model | Perturbation type | Accuracy drop |
| --- | --- | --- | --- |
| bbd91e | Qwen3.5 | expert no-solution | 100% → 10% (90%) |
| a1d40b | Qwen3-8B | expert no-solution | 100% → 10% (90%) |
| 71beb6 | GPT-OSS-120B | expert perturbations | 70% → 20% (50%) |
| 057f8a | Qwen3.5 | distract | 60% → 20% (40%) |
| 057f8a | Qwen3.5 | domain | 60% → 10% (50%) |
| 057f8a | Qwen3.5 | rename | 60% → 20% (40%) |
| 480182 | GPT-5.2 | rephrase | 100% → 60% (40%) |
| 057f8a | Qwen3.5 | typos | 60% → 30% (30%) |
| 349493 | Gemini-3.1 Pro | typos | 60% → 30% (30%) |

Table 1: Examples of paired accuracy drops between original problems and perturbed variants generated from symbolic chains. Problems from the AIMO public reference set.

Table 1 shows performance drops of frontier AI models on permutations of AIMO 2 problems obtained using the annotations of symbolic reasoning chains collected for the purpose of this competition. These evaluations show that our symbolic chains allow for generating perturbations able to disrupt models’ predictions and identify their non-robust reasoning scenarios.

