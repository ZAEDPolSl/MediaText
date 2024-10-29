# MediaText
MediaText: a media industry-based dataset for scene text detection.

Dataset:
https://zenodo.org/records/12796380

## Dataset description

- 400 images
- 7 744 annotated text instances
- 973 annotations have been marked as illegible for the task of text recognition
- 659 texts have been markes as do not care (###) for scene text detection.
- Images are represented by 193 unique resolutions.
- Annotation Format - Each image has corresponding  gt_*.txt file, which contains annotations in bounding box format (defined by 4 courners), transcription, and bool flag which determines that text is illegible for OCR. Proposed format is similar to ICDAR15 annotations.
<br>
x1, x2, ..., x4, y4, transcription, OCR Flag 
<br>
Example:
<br>
37,68,198,49,214,181,52,200,LADIES,False
<br>

## Citing the related works

Please cite the related works in your publications if it helps your research:

``` 
@inproceedings{inproceedings,
author = {Kalisz, Seweryn and Marczyk, Michał and Fagas, Rafał and Polanska, Joanna},
booktitle = {Modelling and simulation 2024. The 2024 European Simulation and Modelling Conference}
editor = {Manuel Graña; J. David Nuñez-Gonzalez}
year = {2024},
month = {10},
pages = {138-144},
publisher = {EUROSIS-ETI},
title = {Media-Text: a Media Industry-Based Dataset for Scene Text Detection}
}
  ``` 