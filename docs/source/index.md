# MMORE Documentation

MMORE is an open-source multimodal ingestion and retrieval framework designed for heterogeneous document collections.

It provides tools to process documents, build indexes, run retrieval pipelines, support multimodal workflows, and scale execution for larger collections and production-oriented settings.

## Overview

This documentation is organized to help different types of users:

- **New users** who want to install MMORE and run a first workflow
- **Practitioners** who want to process, index, and retrieve from document collections
- **Advanced users** who need distributed processing, profiling, evaluation, or production-related guidance
- **Developers** who want to understand the codebase and extend the framework

## What is MMORE?

MMORE helps you build retrieval systems over complex document collections by combining:

- document ingestion and processing
- indexing pipelines
- retrieval and RAG workflows
- multimodal retrieval support
- distributed execution for large-scale workloads
- evaluation and profiling tools

## Recommended reading path

If you are new to MMORE, start here:

1. [Installation](installation.md)
2. [Quickstart](quickstart.md)
3. [Architecture](architecture.md)
4. [Processing pipeline](process.md)
5. [Indexing](indexing.md)
6. [RAG](rag.md)

If you already know the basics, continue with evaluation, multimodal retrieval, distributed execution, or developer-oriented pages.

## Documentation map

```{toctree}
:maxdepth: 1
:caption: Getting started

getting_started/installation
getting_started/quickstart
getting_started/architecture
getting_started/process
getting_started/indexing
getting_started/rag
```

```{toctree}
:maxdepth: 1
:caption: Core features

core_features/colpali
core_features/websearch
core_features/evaluation
core_features/dashboard
```

```{toctree}
:maxdepth: 1
:caption: Advanced usage

advanced_usage/distributed_processing
advanced_usage/profiler
advanced_usage/uv
advanced_usage/rcp_and_production
```

```{toctree}
:maxdepth: 1
:caption: Developer documentation

developer_documentation/for_devs
developer_documentation/index_api
```

## Page guide

Here is a quick overview of the main pages:

- [Installation](installation.md): set up MMORE and prepare your environment
- [Quickstart](quickstart.md): run a first minimal workflow end to end
- [Architecture](architecture.md): understand the main system components and how they interact
- [Processing pipeline](process.md): understand how documents are ingested and transformed
- [Indexing](indexing.md): build and manage indexes
- [RAG](rag.md): structure retrieval-augmented generation workflows
- [ColPali](colpali.md): multimodal retrieval-related documentation
- [Websearch](websearch.md): web search integration and related workflows
- [Evaluation](evaluation.md): assess system performance
- [Dashboard](dashboard.md): monitoring and interface-related documentation
- [Distributed processing](distributed_processing.md): scale execution across larger workloads
- [Profiler](profiler.md): profile and analyze performance
- [uv](uv.md): environment and dependency workflow
- [RCP and production](rcp_and_production.md): deployment and production-oriented guidance
- [For developers](for_devs.md): contributor and internal development documentation
- [Index API](index_api.md): API-oriented reference for indexing-related functionality


