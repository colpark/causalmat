## Overview

The **MatMech Dataset** is a large-scale collection of **61,200+ materials science papers**, each represented by a structured JSON file and associated figure images.

This dataset provides both the **full raw collection (compressed)** and **sample cases** for quick exploration.

---

## Data Composition

The dataset contains:

| Component              | Description                                                                                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `matmech.zip`          | Full dataset (\~19 GB) containing all papers, organized by DOI folders. Each folder includes:<br>• `paper.json`: parsed paper metadata and text content<br>• `images/`: figures extracted from the PDF |
| `case/`                | A curated set of small example cases for quick testing and inspection                                                                                                                                  |
| `dataset_summary.json` | Machine-readable dataset metadata                                                                                                                                                                      |
| `README.md`            | Human-readable dataset description and usage instructions                                                                                                                                              |

---

## Directory Structure

```
matshare_dataset/
│
├── README.md
├── matshare_full.zip
├── case/
│   ├── doi_001/
│   ├── doi_002/
│   └── ...
└── data_summary.json
```

---

## Data Format

Each paper folder in the full dataset contains:

```
<DOI>/
   ├── data.json
   └── images/
       ├── fig1.jpg
       ├── fig2.jpg
       └── ...
```

### Example JSON Structure

```json
{
  "doi": "https://doi.org/xxxxxx",
  "journal": "Journal Name",
  "title": "Article Title",
  "year": 2025,
  "material_object": "Material or compound studied",
  "material_element": ["Element1", "Element2"],
  "material_category": ["Material category A", "Material category B"],
  "tetrahedron_element": {
    "Processing": "Brief description of processing method",
    "Structure": "Key structural features",
    "Properties": "Key material properties",
    "Performance": "Observed performance outcome"
  },
  "casual_chain": "Processing → Structure → Properties → Performance",
  "image_info": [
    {
      "image_path": "images/fig1.jpg",
      "image_caption": ["Figure 1. Caption text here."],
      "image_description": ["Brief description of what is shown in the image."],
      "image_function": "Experimental setup / Microstructure / Others",
      "microscopic_image": true
    }
  ],
  "mechanism": [
    {
      "link": "Structure → Property",
      "cause": "Cause description.",
      "effect": "Effect description.",
      "description": "Concise explanation of the causal relationship.",

      "experiment": {
        "name": "Experiment name.",
        "type": "Experiment type.",
        "parameters": "Key experimental parameters.",
        "result": "Observed experimental finding.",
        "confidence": "Consistency score from hallucination detection module."
      },

      "images": [
        {
          "image description": "Description of the image content.",
          "microscopic": false,
          "confidence": "Consistency score for this image description.",
          "image_path": "images/example.jpg"
        }
      ],

      "mechanism": {
        "description": "Underlying mechanism explanation.",
        "reasoning_chain": [
          {
            "statement": "Reasoning step.",
            "type": "experimental result / image description / external knowledge / deductive reasoning"
          }
        ],
        "confidence": "Overall consistency score for the mechanism."
      },

      "external_knowledge": [
        {
          "content": "External knowledge supporting the mechanism.",
          "reference": ["Optional citation list"],
          "confidence": "Consistency score for this knowledge.",
          "type": "referenced_knowledge or non-referenced_knowledge",
          "conflict_detection": {
            "conflict_sentence": "Conflicting or inconsistent retrieved evidence.",
            "conflict_doi": "DOI of conflicting source.",
            "reason": "Explanation of the potential contradiction."
          }
        }
      ]
    }
  ]
}
```

---

## Usage Instructions

The MatMech Dataset is designed to be machine-readable and easy to integrate into computational materials science workflows. This section provides detailed steps on how to access, parse, and utilize the data.

#### 1\. Dataset Preparation

- **Sample Cases (Quick Inspection):**
  The `case/` directory contains a small, pre-selected set of papers for quick testing.

  ```bash
  ls case/
  # Example: Accessing the JSON file for a sample case
  cat case/doi_001/paper.json | less
  ```

- **Full Dataset Download and Extraction:**
  The full dataset is approximately 19 GB compressed.

  ```bash
  # 1. Download the file: matmech_full.zip
  # 2. Extract the contents:
  unzip matmech_full.zip -d matmech_data
  ```

  This will create the directory `matmech_data/` containing a folder for every paper (named by DOI).

#### 2\. Working with the Structured Data (`paper.json`)

The core information for each paper is contained in the structured JSON file. The data is organized around the fundamental **Materials Science Tetrahedron (Processing $\to$ Structure $\to$ Properties $\to$ Performance)** and detailed **Causal Mechanisms**.

**Example Python Script for Loading and Analyzing Data:**

```python
import json
import os

DATA_DIR = 'matmech_data' # or 'case' for samples

def load_paper_data(doi_folder):
    """Loads and returns the structured data for a single paper."""
    json_path = os.path.join(DATA_DIR, doi_folder, 'paper.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

# --- Main Usage Example ---
example_doi = 'doi_001' # Replace with an actual DOI folder name
paper_data = load_paper_data(example_doi)

if paper_data:
    print(f"--- Paper: {paper_data.get('title')}")

    # A. Accessing the Materials Science Tetrahedron summary
    print("\n[A] Materials Science Tetrahedron Summary:")
    tetra = paper_data.get('tetrahedron_element', {})
    for key, value in tetra.items():
        print(f"  - {key}: {value}")

    # B. Extracting detailed causal mechanisms
    print("\n[B] Detailed Causal Mechanisms:")
    mechanisms = paper_data.get('mechanism', [])
    print(f"  Found {len(mechanisms)} distinct mechanisms.")

    # Iterate over the first mechanism found
    if mechanisms:
        mechanism = mechanisms[0]
        print(f"  Causal Link: {mechanism.get('link')}")
        print(f"  Mechanism Description: {mechanism.get('mechanism', {}).get('description')}")

        # Accessing the reasoning chain and confidence scores
        print(f"  Confidence Score: {mechanism.get('mechanism', {}).get('confidence')}")
        print("  Key Reasoning Steps:")
        for step in mechanism.get('mechanism', {}).get('reasoning_chain', []):
            print(f"    -> {step.get('type')}: {step.get('statement')[:50]}...")

# ---
```

#### 3\. Analyzing Causal Chains and Mechanisms

The most valuable structured fields are for advanced analysis:

- **`casual_chain` (String):** Provides the high-level relationship extracted from the text, usually in the format: `Processing → Structure → Properties → Performance`.
- **`mechanism` (List of Objects):** The core of the dataset, providing detailed, grounded explanations for specific causal links (e.g., `Structure → Property`). Each entry includes:
  - **`link`**: The specific causal relationship being explained (e.g., `Structure → Property`).
  - **`experiment`**: Details about the supporting experiment (name, type, parameters, result).
  - **`mechanism`**: A detailed, step-by-step **`reasoning_chain`** that justifies the causal link, categorized by its source (`experimental result`, `image description`, `external knowledge`, etc.).
  - **`external_knowledge`**: References to external facts or conflicting evidence (`conflict_detection`) used by the extractor.

#### 4\. Linking Data to Figures

The `image_info` array connects the textual data to the figure files in the `images/` subfolder.

```python
if paper_data and paper_data.get('image_info'):
    print("\n[C] Figure Information:")
    for img in paper_data['image_info']:
        print(f"  - Path: {img.get('image_path')}")
        print(f"  - Function: {img.get('image_function')}")
        print(f"  - Caption: {img.get('image_caption', ['N/A'])[0]}")
        # Use a library like Pillow or Matplotlib to load and display the image
        # image_path_full = os.path.join(DATA_DIR, example_doi, img['image_path'])
        # # Display the image...
```

---

## License

This dataset is shared under the **CC BY 4.0 License**.
You are free to use, share, and adapt the dataset with proper attribution.
