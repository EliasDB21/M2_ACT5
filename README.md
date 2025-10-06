# Advanced Large Language Models & Visualization Tools for Data Analytics Learning

This repository accompanies an applied study with **59 participants** (students and professionals, mostly from **non‑computing** backgrounds). It introduces concrete, classroom‑ready materials that help educators and learners **incorporate visualization and generative AI tools into educational practice**. The emphasis here is practical: a curated gallery of figures (source files in EPS) and short, reproducible examples that show how to use them in lessons, workshops, or self‑study.

Throughout this README, we use the term **non‑computing backgrounds** to refer to participants without formal training in computer science or software engineering.

The study compares three approaches to complete the same analytics tasks:
- **Approach 1 — Traditional**: Python with standard packages such as pandas, seaborn, and scikit‑learn.
- **Approach 2 — ChatGPT**: conversational assistance to generate and revise code.
- **Approach 3 — LIDA + GPT**: programmatic orchestration that summarizes data, proposes goals, and generates visualizations.

Across settings, participants rated ChatGPT highest on **ease** and **speed**, and LIDA+GPT highest on **appropriateness** and **correctness**. These results support our central aim: to **introduce innovative, classroom‑ready ways to incorporate visualization and GenAI into educational practice**, balancing rapid iteration with rigor so that learners master both the pipeline and the judgment required to use AI responsibly.

---

## Project Overview

This project, grounded in two complementary studies, demonstrates how advanced Large Language Models (LLMs) and visualization tools can improve data‑analytics learning for students and professionals from **non‑computing** backgrounds. We provide concrete methods and outcomes showing how **Generative AI (GenAI)**—from chat‑based assistance to API‑driven orchestration—helps learners build end‑to‑end pipelines faster **while preserving appropriateness and correctness**. The materials in this repository are classroom‑ready and designed to be reused, adapted, and extended in lessons, workshops, and self‑study.

### Project Objectives

- Promote a comprehensive understanding of data‑based project pipelines.
- Enhance programming and other computational thinking‑related skills through interactive AI assistance.
- Enable wider adoption of GenAI tools in educational contexts.
- Improve the efficiency and effectiveness of data‑related project development.

### Who this is for

- **Instructors** who want to integrate visual analytics and GenAI in their courses with evidence‑based, ready‑to‑use artifacts.
- **Students and professionals** who want to experience three workflows for the same project and reflect on trade‑offs.
- **Training teams** that need concrete materials for hands‑on sessions and quick wins.

---

## What is inside

- `Data_processing.ipynb`: the main notebook used to process survey responses and generate figures.
- `materials/`: supporting documents (for example, the open‑access article and the conference presentation).
- `images/`: the **figure sources** in **EPS** exactly as used in the study and teaching materials.

> GitHub does not render EPS inline. Keep the EPS files as sources and generate PNG or SVG with the same base names to embed the images in Markdown or slides.

---

## Materials
- Journal article published at Frontiers in Education [open access here](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1418006/full)
- Data from Case Study used to obtain results for our journal article [available here](https://www.frontiersin.org/api/v3/articles/1418006/file/Data_Sheet_1.csv/1418006_supplementary-materials_datasheets_1_csv/1?isPublishedV2=false)
- Conference extended abstract published at proceedings of IACEE 2024 [free access here](https://www.researchgate.net/publication/382695760_Empowering_Data_Analytics_Learning_Leveraging_Advanced_Large_Language_Models_and_Visualization_Tools)
- Conference presentation [access here](https://github.com/jvalverr/data-analytics-education/blob/main/materials/session7-JorgeValverde-IACEE-24.pdf)

---

## Getting started

### 1) Environment (Python 3.10+)
```bash
pip install -U pandas numpy matplotlib seaborn plotly scipy dython
```

### 2) Data
Download the CSV from the article’s **Supplementary material** and place it where you prefer (recommendation: `materials/`).  
Link: https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1418006/full#supplementary-material

In the examples below we assume `materials/Data Sheet 1.csv`. If you use a different path, adjust it in the notebook or code snippets.

### 3) Run
```bash
jupyter notebook Data_processing.ipynb
```
The notebook will generate or update figures under `images/`. Keep the `.eps` as sources and add `.png` or `.svg` with the same base names if you need inline rendering.

---

## Figure map (repository file names and how to use them)

Each file below is the **authoritative source** for the corresponding image used in the paper and slides. Create `figX.png` or `figX.svg` next to the EPS to embed it in Markdown.

- `images/fig1.eps` — Number of participants by **current role and gender** (bar).  
  *Use:* discuss cohort composition and why role matters for tool adoption.

- `images/fig2.eps` — Number of participants by **affiliation** (bar).  
  *Use:* motivate visual scaffolding and GenAI prompts that lower entry barriers for non‑computing cohorts.

- `images/fig3.eps` — Number of participants by **age range** (bar).  
  *Use:* connect age distributions with prior exposure to notebooks and APIs.

- `images/fig4-c.eps` — **Programming experience** by role (two pies: Students and Professionals).  
  *Use:* form mixed teams and assign tasks that promote peer instruction.

- `images/fig6-c.eps` — **Data analytics experience** by role (two pies).  
  *Use:* decide whether to start with EDA templates or with guided prompting.

- `images/fig8.eps` — Experience using **Python/Colab** and similar tools (pie).  
  *Use:* confirm that the audience can run notebooks before introducing APIs.

- `images/fig9.eps` — **Programming experience by age range × role × gender** (stacked horizontal bars).  
  *Use:* illustrate intersectional patterns and how they inform pacing and scaffolding.

- `images/fig13.eps` — **Time required to finish activities** by approach and role (stacked bars).  
  *Use:* analyze time distributions and debate trade‑offs between speed and understanding; connect results to assessment rubrics.

- `images/fig14.eps` — **GenAI experience** (four pies: general ChatGPT use, use for programming, use for analytics, and use of generative APIs).  
  *Use:* introduce API‑based orchestration and why it differs from chat‑only workflows.

- `images/fig15.eps` — Composite/supporting visual used in teaching materials.  
  *Use:* reference when creating narrative slides or posters.

- `images/fig16-2.eps` — **Metrics by role** (lollipop): Ease of use, Speed of result, Appropriateness, Correctness.  
  *Use:* discuss why ChatGPT scores higher on ease and speed, while LIDA+GPT scores higher on appropriateness and correctness.

- `images/fig17-2.eps` — **Metrics by gender** (lollipop) with the same four criteria.  
  *Use:* verify that the pattern persists across subgroups.

---

## Make the images visible in GitHub

Keep EPS as your sources and create PNG or SVG for embedding:

**ImageMagick to PNG**
```bash
# macOS: brew install imagemagick ghostscript
# Ubuntu/Debian: sudo apt-get install imagemagick ghostscript

magick mogrify -density 300 -format png images/*.eps
# Produces: images/fig1.png, images/fig2.png, …
```

**Inkscape to SVG**
```bash
inkscape images/fig1.eps --export-type=svg --export-filename=images/fig1.svg
```

After conversion you can embed, for example: `![Fig. 1 — Role × Gender](images/fig1.png)`.

---

## Reproducible mini‑examples

The intent of the examples is to help you **reuse** the figures with your own cohorts or datasets while keeping the same analytical questions.

### A) Replicate `fig2.eps` (Affiliation) with your CSV
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("materials/Data Sheet 1.csv")  # adapt if needed
order = df["Affiliation"].value_counts().index

ax = df["Affiliation"].value_counts()[order].plot(kind="bar", rot=45)
ax.set_title("Number of participants by affiliation")
ax.set_xlabel("")
ax.set_ylabel("Count")
plt.tight_layout()
plt.savefig("images/fig2.png", dpi=300)  # keep same base name as fig2.eps
plt.show()
```

**What to discuss:** Why business and social sciences dominate in many classrooms and how this influences the design of prompts and scaffolds.

> Tip: if your CSV stores categorical labels with inconsistent capitalization or trailing spaces, normalize them before counting (e.g., `df["Affiliation"] = df["Affiliation"].str.strip().str.title()`).

### B) Replicate `fig13.eps` (Time to finish) by approach and role
```python
import pandas as pd
import matplotlib.pyplot as plt

# Expected columns (rename to match your CSV):
# Role ∈ {Student, Professional}
# Approach ∈ {Approach 1, Approach 2, Approach 3}
# TimeBin ∈ {"Less than 5 minutes","5 to 10 minutes","10 to 15 minutes","15 to 30 minutes","More than 30 minutes"}

df = pd.read_csv("materials/Data Sheet 1.csv")
order_time = ["Less than 5 minutes","5 to 10 minutes","10 to 15 minutes","15 to 30 minutes","More than 30 minutes"]
df["TimeBin"] = pd.Categorical(df["TimeBin"], order_time, ordered=True)

tab = (df.groupby(["Role","Approach","TimeBin"])
         .size()
         .groupby(level=[0,1]).apply(lambda s: 100*s/s.sum())
         .unstack(fill_value=0))

for role, subset in tab.groupby(level=0):
    ax = (subset.droplevel(0)
             .reindex(["Approach 1","Approach 2","Approach 3"])
             [order_time]
             .plot(kind="barh", stacked=True, figsize=(8,2.6)))
    ax.set_title(f"Time required — {role}")
    ax.set_xlabel("Percentage of participants")
    ax.set_ylabel("")
    plt.legend(loc="lower right", ncol=3, fontsize=8)
    plt.tight_layout()
    plt.show()
```

**What to discuss:** Where the distributions concentrate, how speed relates to cognitive load, and when orchestration improves appropriateness and correctness.

### C) Build a lollipop chart like `fig16-2.eps` (metrics by role)
```python
# Sketch: counts of choices per metric and approach (adapt column names)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("materials/Data Sheet 1.csv")

# Example layout: one row per (Role, Metric), columns = approaches
counts = (df.groupby(["Role","Metric","Choice"]).size()
            .rename("n").reset_index())
pivot = counts.pivot_table(index=["Role","Metric"], columns="Choice", values="n", fill_value=0)

# Plot a lollipop per metric (pseudocode; adapt to your column names)
for (role, metric), row in pivot.iterrows():
    xs = row.values
    labels = list(row.index)
    plt.hlines(y=0, xmin=0, xmax=max(xs))
    for v in xs:
        plt.plot([0, v], [0, 0], linewidth=2)
        plt.scatter([v], [0], s=60)
    plt.title(f"{metric} — {role}")
    plt.yticks([])
    plt.xlabel("Number of participants")
    plt.tight_layout()
    plt.show()
```

**What to discuss:** Why learners value ease and speed in early stages and why correctness and appropriateness become decisive for assessment and transfer.

---

## Teaching ideas and prompts

**1) Ten-minute briefing (read the room, set expectations)**  
Use `fig1.eps`–`fig3.eps` to discuss roles, affiliations, and age ranges. Link these distributions to prior exposure (e.g., notebooks vs. APIs) and likely scaffolding needs. State an explicit learning goal: Complete a compact pipeline from *business understanding* to *data understanding* and *initial evaluation* while comparing three workflows (Traditional, ChatGPT, LIDA+GPT).

**2) Three hands-on segments that build on each other**

- **Traditional segment (pipeline foundations).**  
  Each team produces a minimal yet complete EDA: (a) A tidy missing-values table, (b) At least one well-labeled distribution per key variable, and (c) A comparative chart that answers a concrete question. Require a brief note under every figure that explains how it answers the stated question. Capture elapsed time for later reflection (to be compared with `fig13.eps`).

- **ChatGPT segment (computational thinking with interactive AI)**  
  Shift from code recall to reasoning about design choices. Students should request runnable code, explanations, and a quick test—and verify outputs locally. Use a high-leverage, auditable prompt:
  ```
  Act as my pair programmer. Given CSV <X>, propose a minimal EDA that answers <question>.
  Return: (1) runnable code, (2) reasoning for each plot, (3) a tiny synthetic test to validate the logic.
  Make assumptions explicit and highlight any data cleaning you recommend.
  ```
  Require students to annotate the generated code with what they kept, what they changed, and why.

- **LIDA+GPT segment**  
  Move from ad-hoc prompting to a structured workflow: summary → candidate goals → visualization specs. Then apply *human curation* (titles, axes, ordering, annotations) to align outputs with the learning objective.
  ```
  Given dataset <X> and objective <Y>, produce:
  (a) a concise data summary,
  (b) 3 concrete analysis goals (each phrased as a question),
  (c) 1 visualization spec per goal (library-agnostic).
  Optimize for clarity and instructional value. I will edit labels and add notes for the final audience.
  ```
  Provide a short curation checklist: “Does the title answer the question? Are axes readable? Is ordering meaningful? Is there an annotation that states the main finding?”

**3) Structured reflection**  
Use `fig16-2.eps` and `fig17-2.eps` to interpret why **ease** and **speed** often favor ChatGPT, while **appropriateness** and **correctness** tend to favor LIDA+GPT across roles and genders. Reproduce `fig13.eps` with your own timing logs to compare distributions by approach and role. Conclude with an exit conclusion:
- *One practice I will keep for efficiency is…*  
- *One safeguard I will add for correctness is…*

---

## Contributing

Pull requests and issues with classroom examples, datasets, or evaluation rubrics are welcome.  
If you generate `figX.png` or `figX.svg`, keep the **same base names** as the EPS so the README and slides remain consistent.

---

## License and citation

The article and figures are released under **Creative Commons BY 4.0** (reuse with attribution).

When referencing this project, please use the following citation formats:

**Journal Article:**

Valverde-Rebaza, J., González, A., Navarro-Hinojosa, O., & Noguez, J. (2024). *Advanced large language models and visualization tools for data analytics learning*. Front. Educ. 9:1418006. DOI: [10.3389/feduc.2024.1418006](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2024.1418006/abstract).

```bibtex
@article{valverde:frontiers:24,
  title={Advanced large language models and visualization tools for data analytics learning},
  author={Valverde-Rebaza, J. and González, A. and Navarro-Hinojosa, O. and Noguez, J.},
  journal={Front. Educ.},
  volume={9},
  pages={1418006},
  year={2024},
  doi={10.3389/feduc.2024.1418006}
}
```

**Conference Extended-Abstract:**

Valverde-Rebaza, J., González, A., Navarro-Hinojosa, O., & Noguez, J. (2024). Empowering Data Analytics Learning: Leveraging Advanced Large Language Models and Visualization Tools. Proceedings of the 19th World Conference on Continuing Engineering Education, IACEE 2024, pp. 47-49. ISBN: 978-1-7327114-3-3.

```bibtex
@inproceedings{Valverde:iacee:24b, 
 author = {Valverde-Rebaza, J. and González, A. and Navarro-Hinojosa, O. and Noguez, J.},
 title = {{Empowering Data Analytics Learning: Leveraging Advanced Large Language Models and Visualization Tools}},
 booktitle = {Proceedings of The 19th World Conference on Continuing Engineering Education},
 series = {IACEE 2024},
 pages = {47--49},
 isbn = {978-1-7327114-3-3},
 publisher = {IACEE},
 year = {2024}
}
```
