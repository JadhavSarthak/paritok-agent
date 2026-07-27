[![Built with Paritok](https://img.shields.io/badge/Built%20with-Paritok-1f2d3d)](https://github.com/Paritok-official/paritok-4b-v1)

# TokenLean Agent

A coding agent that uses Paritok to prune irrelevant context before every LLM call, keeping token usage flat instead of growing with each step — with a live dashboard showing real, measured savings against a naive baseline.

Built with [Paritok](https://github.com/Paritok-official/paritok-4b-v1).

> ⚠️ **Status: Work in progress.** This README is a placeholder and will be updated as the project develops for the Paritok Token-Efficiency Hackathon (deadline Aug 5, 2026).

---

## What it does

TokenLean Agent reads files, greps a codebase, edits code, and runs tests in a real repo — a genuine agentic loop, not a demo wrapper. Before every LLM call, it routes accumulated context through Paritok's hosted GPU to prune out what's irrelevant to the current step.

It also ships a **naive baseline mode** (pruning off) so results can be directly compared, and a **live dashboard** showing tokens sent vs. tokens that would've been sent without Paritok.

## Status / Roadmap

- [ ] Core agent loop (naive mode)
- [ ] Tool executors (read, grep, edit, run_shell)
- [ ] Paritok pruning integration
- [ ] Live CLI dashboard
- [ ] Sample buggy repo + demo task
- [ ] Demo video
- [ ] Final polish & submission

## Setup

```bash
git clone <this-repo-url>
cd tokenlean-agent
pip install -r requirements.txt
cp .env.example .env   # add your PARITOK_API_KEY
```

## Usage

```bash
python scripts/run_lean.py    # run agent with Paritok pruning
python scripts/run_naive.py   # run agent without pruning (baseline)
python scripts/compare_results.py   # generate savings report
```

*(commands above are the intended interface — subject to change as the project is built)*

## Project Structure

```
tokenlean-agent/
├── agent/          # core loop, context store, Paritok pruner, tools
├── dashboard/      # live token dashboard
├── examples/       # sample buggy repo + demo task + sample outputs
├── scripts/        # run_lean.py, run_naive.py, compare_results.py
├── docs/           # architecture & Paritok integration notes
└── tests/
```

## License

Apache 2.0 — see [LICENSE](./LICENSE)

## Credit

Built with [Paritok](https://github.com/Paritok-official/paritok-4b-v1) for the Build with Paritok Token-Efficiency Hackathon.
