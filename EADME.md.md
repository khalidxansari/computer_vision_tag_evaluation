# 🧠 AI-Driven Metadata Tagging for Image Collections

This project evaluates the effectiveness of three AI-based computer vision platforms — **Google Cloud Vision**, **Microsoft Azure Computer Vision**, and **Amazon Rekognition** — in generating metadata tags for culturally diverse image categories. It combines **quantitative metrics** with **qualitative observations** to measure accuracy, sensitivity, and contextual relevance.

> 📘 Based on my MA dissertation at King's College London, Department of Digital Humanities.

---

## 📂 Repository Structure

```
dissertation-code/
├── notebooks/                   # Jupyter notebooks per service
├── data/                        # Sample images + vocabularies
│   ├── image_dataset/           # Subfolders by category
│   └── ground_truth_controlled_vocabularies/
├── results/                     # Tag outputs & visualisations
│   ├── graphs/                  # Heatmaps, network graphs
│   └── *.csv                    # Performance metrics
├── utils/
│   └── metrics.py               # Reusable evaluation functions
├── requirements.txt             # Python environment
├── LICENSE                      # Open source license (MIT)
└── README.md                    # This file
```

---

## 🧪 Platforms Evaluated

- 🟦 **Microsoft Azure Computer Vision**
- 🟩 **Amazon Rekognition**
- 🟥 **Google Cloud Vision**

---

## 🧵 Image Categories

1. People  
2. Art & Creative Craft  
3. Nature  
4. Daily Life  
5. Objects  
6. Text & Documents  
7. Urban & Rural Settings

Each category has a dedicated folder with images and a **controlled vocabulary** sourced from:
- Getty AAT
- Library of Congress Subject Headings (LCSH)
- UK Archival Thesaurus (UKAT)

---

## 📊 Evaluation Metrics

- Precision
- Recall
- F1 Score
- Accuracy

All performance metrics are calculated using scikit-learn and visualised using:
- Seaborn (heatmaps)
- Matplotlib (bar charts)
- NetworkX (tag co-occurrence graphs)

---

## 🛠️ Usage

You can run the notebooks directly in Jupyter or JupyterLab:

```bash
cd notebooks/
jupyter notebook amazon_rekognition.ipynb
```

To use evaluation functions:

```python
from utils.metrics import calculate_metrics, plot_performance_heatmap
```

---

## 📈 Sample Visualisation

<img src="results/graphs/heatmap.png" alt="Heatmap Example" width="500">

---

## 🧠 Key Insight

While all three platforms demonstrate decent object recognition performance, only Google Cloud Vision shows some cultural sensitivity. All models perform weakest in abstract or context-heavy categories like **Art** and **Daily Life**.

---

## 📎 Citation

If you reference this work, please cite as:

```
Ansari, Khalid. "Effectiveness of AI for Metadata Tagging in Image-Based Digital Asset Management Systems." MA Dissertation, King’s College London, 2025.
```

---
# 📄 Full Dissertation Report

The full academic report that informed this project is available here:

📘 [`docs/computer_vision_tag_dissertation.pdf`](docs/computer_vision_tag_dissertation.pdf)

It details the research questions, methodology, evaluation framework, and key findings regarding the effectiveness of AI-generated metadata tags across culturally diverse image categories.

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).

---

👨‍💻 Created by [Khalid Ansari](https://www.khalidansare.com)
