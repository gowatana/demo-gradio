# demo-gradio

Environment

```
# cat /etc/redhat-release
Red Hat Enterprise Linux release 8.9 (Ootpa)
# python -V
Python 3.11.5
```

Install RPMs.
```
dnf install -y git python3.11
```

Install Python Module.
```
pip3.11 install gradio
pip3.11 install openai==0.28
```

Edit app.py

example:

* aoai_instance = "demo-aoia-01"
* deployment_id = "gpt35-tarbo-01"

```
vi app.py
```

set OPENAI_API_KEY

```
export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

Run script
```
python3 ./app.py
```
