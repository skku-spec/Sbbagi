---
name: research-intelligence-workflows
description: "Use when gathering, monitoring, organizing, or writing research intelligence from arXiv, blogs/RSS, prediction markets, LLM wikis, or paper-writing pipelines."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, arxiv, literature, blogs, prediction-markets, papers, knowledge-base]
    related_skills: []
---

# Research Intelligence Workflows

## Overview

This umbrella covers research discovery, monitoring, knowledge organization, market/probability context, and paper production. These tasks are usually chained: discover sources, extract evidence, organize notes, synthesize, and write.

Former packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- Searching arXiv or building a literature review.
- Monitoring blogs/RSS for new posts.
- Querying Polymarket for market-implied probabilities or orderbook/history data.
- Building/querying an interlinked LLM wiki.
- Drafting or preparing ML research papers and conference templates.

## Workflow Map

1. **Discovery**: arXiv, blog feeds, web, and existing notes.
2. **Evidence capture**: preserve URLs, IDs, dates, abstracts, and quoted snippets.
3. **Knowledge organization**: write durable wiki/note structures when research spans sessions.
4. **Quantitative context**: use prediction markets carefully, reporting liquidity and timestamps.
5. **Paper writing**: follow conference/template constraints and keep claims tied to experiments/citations.

## Source Packages

- `references/source-packages/arxiv/`
- `references/source-packages/blogwatcher/`
- `references/source-packages/polymarket/`
- `references/source-packages/llm-wiki/`
- `references/source-packages/research-paper-writing/`

## Verification Checklist

- [ ] Sources and timestamps are cited.
- [ ] Search terms and filters are recorded.
- [ ] Market data includes uncertainty/liquidity caveats.
- [ ] Paper outputs preserve template and citation requirements.
