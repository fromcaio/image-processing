Perfect — that’s a great next step. Making the repository self-guided, with clear entry points and standardized English naming, will make it much easier for students or developers to follow.

Below is the **improved and polished version** of your `README.md`, incorporating:
✅ A clear “Getting Started” guide
✅ Consistent English naming (`Exercise01.pdf`, etc.)
✅ A new `practices/` folder
✅ Updated `images/` folder structure with subdirectories
✅ Improved organization and readability for GitHub presentation

---

```markdown
# 🧠 Image Processing

This repository contains educational **Jupyter Notebooks** focused on **Digital Image Processing**, combining **theory**, **visual examples**, and **Python implementations**.

The content is inspired by:

- The course *“Processamento Digital de Imagens”* taught by **Prof. Dr. Jesuliana N. Ulysses**, which I attended during my undergraduate studies in Computer Science.  
- The book *“A Computational Introduction to Digital Image Processing”* by **Alasdair McAndrew**.

---

## 🎯 Objectives

This project aims to provide a **practical and structured introduction** to digital image processing through:

1. **Interactive notebooks** that mix explanations, mathematics, and code.  
2. **Hands-on exercises** that reinforce theoretical understanding.  
3. **Real examples and images** demonstrating key operations.  
4. **A clean file structure** separating code, exercises, and visual resources.

---

## 🚀 Getting Started

Start by exploring the notebooks inside the [`notebooks/`](./notebooks) folder.  
Each notebook introduces a new topic and builds on previous concepts.

👉 **Recommended path:**
1. Open `01-introduction.ipynb` to understand the basics.  
2. Continue sequentially through the next notebooks (`02-fundamentals.ipynb`, `03-pixel-relationships.ipynb`, etc.).  
3. Refer to the corresponding **Exercises** in [`exercises/`](./exercises) for additional practice.  
4. Explore the **Practice** activities in [`practices/`](./practices) for real-world or experimental challenges.

Each notebook contains:
- Explanations and equations  
- Visual examples using sample images  
- Python implementations with comments  
- References to related exercises and practices

---

## 📂 Repository Structure

```bash
image-processing/
│
├── notebooks/
│   ├── 01-introduction.ipynb
│   ├── 02-fundamentals.ipynb
│   ├── 03-pixel-relationships.ipynb
│   ├── 04-intensity-transformations.ipynb
│   ├── 05-histogram-processing.ipynb
│   ├── 06-smoothing-filters.ipynb
│   ├── 07-sharpening-filters.ipynb
│   ├── 08-frequency-domain.ipynb
│   ├── 09-edge-detection.ipynb
│   ├── 10-thresholding.ipynb
│   └── 11-region-growing.ipynb
│   └── ...
│
├── exercises/
│   ├── Exercise01.ipynb
│   ├── Exercise02.ipynb
│   ├── Exercise03.ipynb
│   ├── Exercise04.ipynb
│   ├── Exercise05.ipynb
│   ├── Exercise06.ipynb
│   └── Exercise07.ipynb
│
├── practices/
│   ├── Practice01.ipynb
│   ├── Practice02.ipynb
│   └── ...
│
├── images/
│   ├── notebook01/
│   │   ├── lena_gray.png
│   │   ├── cameraman.png
│   │   └── sample_01.png
│   ├── notebook02/
│   │   └── ...
│   ├── exercise01/
│   │   └── ...
│   ├── practice01/
│   │   └── ...
│   └── ...
│
└── README.md
```

## 🧰 Technologies and Tools

- **Python 3**
- **NumPy** – numerical computations  
- **Matplotlib** – plotting and visualization  
- **OpenCV** – image manipulation and processing  
- **scikit-image** – advanced image analysis tools  
- **Jupyter Notebook** – interactive learning environment

---

## 🧑‍🏫 Writing and Style

All materials are written in **English**, focusing on clarity and learning.  
Each notebook includes:

- Mathematical foundations and formulas  
- Step-by-step Python implementations  
- Visual examples and explanations  
- Links to related exercises and practices  

---

## 🪶 References and Attribution

> Based on course materials created by **Prof. Dr. Jesuliana N. Ulysses**,  
> and on concepts from *A Computational Introduction to Digital Image Processing* by **Alasdair McAndrew**.

---

## 📬 Author

**Caio Fromm**  
👩‍💻 [github.com/fromcaio](https://github.com/fromcaio)