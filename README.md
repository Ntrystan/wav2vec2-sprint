This repo is deprecated in favor of https://github.com/jonatasgrosman/huggingsound

# Wav2Vec Trainer

This repository is based on https://github.com/jqueguiner/wav2vec2-sprint

## Building docker image

Dockerhub available at https://hub.docker.com/r/patilsuraj/hf-wav2vec

to build the docker :

```
$ docker build -t hf-wav2vec-sprint -f Dockerfile .
```

to push it to dockerhub
First create a repository on dockerhub
```
$ docker tag hf-wav2vec-sprint your-dockerhub-user/hf-wav2vec-sprint
```

to push it to dockerhub

```
$ docker push your-dockerhub-user/hf-wav2vec-sprint
```

## Running WandB sweep

Initialize your sweep from any machine...

```
$ export WANDB_API_KEY=YOUR_WANDB_API_KEY
$ export WANDB_ENTITY=YOUR_WANDB_ENTITY
$ export WANDB_PROJECT=YOUR_WANDB_PROJECT

$ wandb sweep sweep.yaml
```
... the execution above will give you a sweep id, save it and on the training machine run:

```
$ export WANDB_API_KEY=YOUR_WANDB_API_KEY
$ export WANDB_ENTITY=YOUR_WANDB_ENTITY
$ export WANDB_PROJECT=YOUR_WANDB_PROJECT

$ wandb agent YOUR_SWEEP_ID
```

## Uploading model to HF

You need to upload the following files to the HF repository

- preprocessor_config.json
- special_tokens_map.json
- tokenizer_config.json
- vocab.json
- config.json
- pytorch_model.bin
- README.md (create this file based on the MODEL_CARD.md)

```
$ git config --global user.email "email@example.com"

$ git config --global user.name "Your name"

$ transformers-cli login

$ transformers-cli repo create your-model-name

$ git clone https://username:password_or_token@huggingface.co/username/your-model-name

$ git add .

$ git commit -m "Initial commit"

$ git push

```

## Troubleshooting

- audioread.exceptions.NoBackendError: `$ sudo apt-get install ffmpeg sox libsox-fmt-mp3`


## Finetuned models

### Wav2Vec2-XLSR-53

- [Arabic](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-arabic)
- [Chinese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn)
- [Dutch](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-dutch)
- [Finnish](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-finnish)
- [French](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-french)
- [German](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-german)
- [Greek](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-greek)
- [Hungarian](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-hungarian)
- [Italian](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-italian)
- [Japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese)
- [Persian](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-persian)
- [Polish](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-polish)
- [Portuguese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-portuguese)
- [Russian](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-russian)
- [Spanish](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish)
