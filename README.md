# Rasa Job Bot

Rasa Job Bot is an automated chat bot that lets applicants:
* Find jobs at Rasa
* Check their Rasa job application status

### Requirements

* [Python 3.6](https://www.python.org/)
* [rasa_core==0.13.6](https://legacy-docs.rasa.com/docs/core/0.13.6/)
* [rasa_nlu[spacy]==0.14.6](https://legacy-docs.rasa.com/docs/nlu/0.14.6/)

### Install

**1**. Install requirements
```
pip install -r requirements.txt
```

**2**. Install the spaCy English language model and link it
```
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

## How to run Rasa Job Bot

**1**. Run Rasa Job Bot in the command line

```
make run
```

## How to train Rasa Job Bot

**1**. Train the NLU model
```
make train-nlu
```

**2**. Train the Core model
```
make train-core
```

**3**. Run Rasa Job Bot in the command line 
```
make run
```

## Examples

```
Your input ->  Hi
Hi, I’m Rasa’s recruiting bot. How can I help?
Your input ->  I’d like to know which positions are open right now.
Are you looking for a technical or a business role?
Your input ->  A technical one.
ML Engineer and Solutions Engineer are the open positions.
```

```
Your input ->  Hi, my name is Ali Park. I applied for a job and would like to know when I’ll hear back.
Hi Ali! Let me check that for you.
Yes, your application has been received.
```

## Acknowledgments

* [Popular Baby Names](https://www.ssa.gov/oact/babynames/limits.html)