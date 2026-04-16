# IFU Analysis of NGC1510: Balmer Maps, Common Spaxels, and Composite Spectrum

This repository contains a preliminary IFU-based analysis of the DGIS galaxy **NGC1510**, carried out as part of my research training on integral-field spectroscopy and galaxy evolution.

## Project Background

Integral-field spectroscopy (IFS) allows us to obtain a full spectrum at each spatial position in a galaxy, making it possible to study spatially resolved emission-line properties, ionized gas structure, and internal physical variation.

This project is motivated by:
- the DGIS survey framework for nearby dwarf galaxies
- the use of IFU datacubes for spatially resolved analysis
- the multi-Balmer methodology discussed in Reddy et al. (2020)

## Current Goal

After my second progress report, the next task assigned by my advisor was:

- identify the **common reliable spaxels** shared by **Hα, Hβ, and Hγ**
- construct a **composite spectrum** from those common spaxels
- plot the **Balmer spectral panels** for each selected spaxel

## What I Have Completed

### 1. Datacube reading and wavelength-axis inspection
I read the NGC1510 IFU datacube and extracted the key data structures required for spectral analysis.

### 2. Emission-line flux maps
I generated 2D flux maps for several important emission lines, including:
- Hα
- Hβ
- Hγ
- Hδ
- Hη
- [OIII]5007
- [NII]6583

### 3. Central-spaxel identification
Using the Hα flux map, I located the brightest reliable Hα spaxel and used it as the central spaxel for spectral inspection.

### 4. Central-spaxel spectrum check
I plotted the observed spectrum, total fit, and continuum fit for the central spaxel to verify the quality of the emission-line fitting.

### 5. Common-spaxel selection for Hα/Hβ/Hγ
Following the logic of multi-Balmer analysis, I selected the spaxels that are simultaneously reliable in Hα, Hβ, and Hγ.

### 6. Composite spectrum and Balmer panels
For the shared spaxels, I completed the first-stage products:
- a composite spectrum constructed from the common sample
- Balmer spectral panels for individual selected spaxels

## Repository Structure

```text
ifu-ngc1510-balmer-analysis/
├── docs/      # reports and project notes
├── figures/   # maps, spectra, and selected Balmer panels
├── results/   # selected spaxel lists and stage summaries
├── src/       # notebooks and scripts
