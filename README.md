# Cardiotoxicity Classifier

Prediction of drug-induced cardiotoxicity as a binary classification of cardiotoxicity risk. The probability score depicts risk of the compound being cardiotoxic. Classification is based on the chemical data such as SMILES representations of compounds and a variety of descriptors such as Morgan fingerprints and Mordred physicochemical descriptors that describe the molecular structure of the drug interactions. Biological data is also used including gene expression and cellular paintings after drug interactions. The DICTrank (Drug-Induced Cardiotoxicity Rank) dataset provides the ground truth labels for the training data.

This model was incorporated on 2024-06-29.

## Information
### Identifiers
- **Ersilia Identifier:** `eos1pu1`
- **Slug:** `cardiotox-dictrank`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Cardiotoxicity`, `DrugBank`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** The model provides a probability score indicating the likelihood of a compound being cardiotoxic

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| cardiotoxicity_risk | float | low | Cardiotoxicity risk score (0-1) based on a binary classification model. The recommended threshold by the authors is 0.641338  |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Replicated`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos1pu1](https://hub.docker.com/r/ersiliaos/eos1pu1)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1pu1.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1pu1.zip)

### Resource Consumption
- **Model Size (Mb):** `4`
- **Environment Size (Mb):** `817`
- **Image Size (Mb):** `770.41`

**Computational Performance (seconds):**
- 4 inputs: `35.99`
- 20 inputs: `376.34`
- 100 inputs: `516.5`

### References
- **Source Code**: [https://github.com/srijitseal/DICTrank](https://github.com/srijitseal/DICTrank)
- **Publication**: [https://doi.org/10.1021/acs.jcim.3c01834](https://doi.org/10.1021/acs.jcim.3c01834)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [kurysauce](https://github.com/kurysauce)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos1pu1
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos1pu1
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
