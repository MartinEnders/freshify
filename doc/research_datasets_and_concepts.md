# Research 4 MVP:

## Concept Transfer Learning

<https://www.geeksforgeeks.org/machine-learning/ml-introduction-to-transfer-learning/>

Base-Layer:   
MobileNetV2 ist pre-trained und erkennt Brot als solches und kann damit universelle Features extrahieren.  
  
Fine-Tuning:   
Mit den Datasets von unten sollen Varianten, Texturen, Farben, Formen und auch eben Schimmelflecken erkannt werden, die Brotfrische hängt genau an solchen Features.   
//Tobias: Wie sinnvoll ist das? (siehe Learnings)

Latest-Layer (alias Label-Mapping):  
Wahrscheinlich nochmal dann ca. 300 selbst fotografierte Bilder für die drei Klassen (frisch, alt, verdoben).

## Learnings

Wie soll die Klassifizierung genau aussehen? Wir können ja nicht auf mikroskopischer Ebene eine Klassifizierung vornehmen. Ist unser Model dann wirklich "besser" als der Mensch? Was ist der größte Nutzen davon? Der offensichtliche Schlimmel wird ja bereits durch Menschen erkannt also was soll das Modell erkennen? 

//Tobias: Möglicherweise switchen wir auf Allgmeines Food-Freshness?  
Dataset: 

---

## Ressources

  
**Project**: ca. 3k microscopic images of bread with and without mold; Size=14GB <https://github.com/NawanolT/Bread-Mold-Datasets>

---

**Project**: Good and Bad Classification of Bread (Triticum Aestivum) Using Realme 11x 5G Mobile Camera; Size=4.05GB <https://data.mendeley.com/datasets/2cymbb4gt4/1>

---

**Project**: Food-101 – Mining Discriminative Components with Random Forests; Size=5.02GB <https://www.kaggle.com/datasets/dansbecker/food-101>

---

**Project**: Ensuring consistent bread quality is vital for maintaining industry standards, reducing waste, and keeping consumer satisfaction.  
<https://agdatacommons.nal.usda.gov/articles/dataset/Data_and_Code_From_AI-Based_bread_quality_assessment_using_image_processing_techniques_and_the_developed_BQe-CNN/29251832>

---

## ???

<https://universe.roboflow.com/bread-dxsbg/bread-m0zyj>

<https://universe.roboflow.com/meruuu/bread-model-o77fy>

<https://universe.roboflow.com/perman/bread-quality-v3/dataset/6>

<https://academic.oup.com/ijfst/article/61/1/vvag010/8439609?login=false#553758011>

<https://www.sciencedirect.com/science/article/pii/S2665927123001429?via%3Dihub>

---

## Allgemeines Food

**Project:** Standardized Fruit and Vegetable Images for Quality Detection Tasks; Size=6.41GB <https://www.kaggle.com/datasets/ulnnproject/food-freshness-dataset>