# Cardiotoxicity Classifier

Prediction of drug-induced cardiotoxicity as a binary classification of cardiotoxicity risk along with a probability score depicting the confidence level of the prediction. Classification is based on the chemical data such as SMILES representations of compounds and a variety of descriptors such as Morgan fingerprints and Mordred physicochemical descriptors that describe the molecular structure of the drug interactions. Biological data is also used including gene expression and cellular paintings after drug interactions. The DICTrank (Drug-Induced Cardiotoxicity Rank) dataset provides the ground truth labels for the training data.

## Identifiers

* EOS model ID: `eos1pu1`
* Slug: `cardiotox-dictrank`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability, Boolean`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: The model provides a probability score indicating the likelihood of a compound being cardiotoxic

## References

* [Publication](https://doi.org/10.1021/acs.jcim.3c01834)
* [Source Code](https://github.com/srijitseal/DICTrank)
* Ersilia contributor: [kurysauce](https://github.com/kurysauce)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos1pu1)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1pu1.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos1pu1) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://doi.org/10.1021/acs.jcim.3c01834) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!