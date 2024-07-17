FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia


RUN pip install rdkit==2024.3.1
RUN pip install pandas==2.0.3
RUN pip install pandarallel==1.6.5
RUN pip install mordred==1.2.0
RUN pip install dimorphite_dl==1.3.2
RUN pip install scikit-learn==1.1.1


WORKDIR /repo
COPY . /repo