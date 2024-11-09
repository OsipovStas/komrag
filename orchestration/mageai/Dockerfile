FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

# Note: this overwrites the requirements.txt file in your new project on first run.
# You can delete this line for the second run :)
COPY ../../requirements.txt /home/src/requirements.txt

RUN pip install -r /home/src/requirements.txt
