# pwn_ctf_workshop

This repository contains my **personal solutions** to the CTF challenges from the
**m0leCon workshops**, organized by **pwnthem0le**, the CTF team of Politecnico di Torino.

The original challenges are available here: <https://workshop.m0lecon.it/challenges>

> These are my own solutions, written while learning. They are not official
> solutions and may not be the cleanest or the intended way to solve each challenge.

## Repository structure

Each folder matches one workshop:

| Folder | Workshop |
| --- | --- |
| `w1_surviving_the_shell/` | Surviving the Shell |
| `w2_hacking_ai_chatbots/` | Hacking AI Chatbots |
| `w3_reverse_engineering/` | Reverse Engineering |
| `w4_crypto/` | Cryptography |

Inside each workshop folder:

- `challenges/` – one subfolder per challenge. It usually contains the original
  challenge files (e.g. `chall.py`, `output.txt`) and my solution script (`solve.py`).
- `notes/` – slides or cheatsheets from the workshop.

## Running the solutions

Most solutions are Python scripts. Many use [pwntools](https://github.com/Gallopsled/pwntools)
and/or [PyCryptodome](https://pypi.org/project/pycryptodome/):

```bash
pip install pwntools pycryptodome
python solve.py
```

## Disclaimer

This repository is for educational purposes only. All challenges belong to their
authors (pwnthem0le / m0leCon).
