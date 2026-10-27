# ADR-0001: Capstone Framing — Indian Stock Market Knowledge Assistant

- **Status:** Draft v1
- **Date:** 2026-10-28
- **Author:** Laxmi Hima Nutulapati

## Context

Retail participation in Indian equities has grown fast, but new investors struggle to make sense of dense, scattered sources — SEBI rules, NSE/BSE circulars, and company annual reports and quarterly results. General-purpose chatbots answer these questions confidently but often with outdated or invented facts and no sources. This capstone builds a Q&A assistant that answers Indian stock market questions grounded only in a curated document corpus, with citations, so beginners get answers they can verify.

## Decision — Solution Framing Canvas

| Box | Your answer |
|-----|-------------|
| **Inputs** | A natural-language question in English (e.g. "What is a circuit breaker on NSE?", "What were Infosys's main risks in its last annual report?"), plus an optional filter for company or document type. |
| **Outputs** | A short text answer, a citation list (document name + page/section) for every claim, and a fixed disclaimer that this is educational information, not investment advice. If the corpus doesn't cover the question, it says so instead of guessing. |
| **Tools** | OpenAI (`gpt-4o-mini` via the Vocareum proxy) for generation and embeddings; a retriever over a local vector store built from the corpus — SEBI investor-education material, NSE/BSE market rules, and annual reports / quarterly results for a small set of NIFTY 50 companies. |
| **Memory** | Last few turns of the current conversation only, so follow-ups like "and what about TCS?" work. No durable user history and no personal financial data stored. |
| **Autonomy level** | Near the chatbot end: a retrieval-augmented Q&A assistant. It retrieves and answers, but takes no actions (no trading, no alerts, no portfolio access). Low autonomy keeps it safe and testable in a regulated domain. |
| **Decision boundaries** | **On its own:** pick which documents to retrieve, summarise and compare what they say, refuse questions outside the corpus. **Needs a human:** any buy/sell/hold recommendation, price targets or personalised advice (these are refused and the user is pointed to a SEBI-registered adviser); adding new documents to the corpus. |

## Consequences

- **Positive:**
  - Answers are grounded and cited, so users can check them and hallucinations are easier to catch.
  - A small, fixed corpus makes retrieval quality measurable with a hand-written test set of questions.
  - Staying informational (no advice, no actions) keeps the project clear of SEBI investment-adviser rules.
- **Negative / risks:**
  - No live prices: answers are only as current as the corpus, which will go stale (new results, new circulars).
  - Annual reports are long PDFs full of tables; chunking and extracting numbers accurately will be hard.
  - Users may still read answers as advice despite the disclaimer.
- **Things we'll re-visit:**
  - Whether to add a live market-data tool (prices, index levels), which would move the system towards an agent.
  - Chunking and embedding strategy for financial PDFs and tables.
