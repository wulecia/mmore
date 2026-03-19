# 🏗️ Architecture

This page gives a high-level view of MMORE and explains how the main components fit together.

It is meant to help readers understand the system before diving into implementation details.

## Overview

MMORE is designed as a multimodal ingestion and retrieval framework for heterogeneous document collections.

At a high level, the system follows a pipeline like this:

```text
Data sources
    ↓
Ingestion and processing
    ↓
Structured representations
    ↓
Indexing
    ↓
Retrieval / reranking
    ↓
Optional RAG generation
    ↓
Evaluation / profiling / production deployment
```

## Main components

### 1. Ingestion and processing

This stage takes raw inputs and transforms them into normalized, usable representations.

Depending on the document type and workflow, this may involve:

- loading files from one or more sources
- extracting text, metadata, or layout information
- chunking long documents
- preparing multimodal content representations
- organizing outputs for downstream indexing

This part of the pipeline is documented in [Processing pipeline](process.md).

### 2. Indexing

The indexing stage converts processed content into searchable artifacts.

Typical responsibilities include:

- selecting what unit to index, such as full documents or chunks
- generating representations used for retrieval
- storing indexes in a format suitable for fast search
- managing index lifecycle and updates

This stage is documented in [Indexing](indexing.md).

### 3. Retrieval

Retrieval is responsible for finding relevant content for a query.

Depending on the setup, this can include:

- lexical or semantic retrieval
- multimodal retrieval
- hybrid retrieval strategies
- reranking or score refinement

The retrieved outputs can be returned directly to the user or passed into a downstream generation system.

### 4. RAG workflows

When MMORE is used in a retrieval-augmented generation setting, retrieval outputs are passed into a generative layer.

The quality of the final result then depends on:

- document processing quality
- chunking choices
- index quality
- retrieval relevance
- prompt and generation design

See [RAG](rag.md) for more details.

### 5. Multimodal support

A key aspect of MMORE is support for heterogeneous and multimodal collections.

That means the framework may work with:

- plain text documents
- structured metadata
- images or layout-aware representations
- multimodal retrieval models such as ColPali-related components

See [ColPali](../core_features/colpali.md) for the multimodal retrieval side.

### 6. Distributed execution

For larger workloads, MMORE can scale through distributed processing.

This is useful when:

- the collection is large
- processing is computationally expensive
- indexing or retrieval must be parallelized
- experiments need to run over multiple jobs or nodes

See [Distributed processing](../advanced_usage/distributed_processing.md).

### 7. Evaluation and profiling

MMORE also includes tooling to inspect and improve system quality and performance.

Two complementary concerns matter here:

- **evaluation**, which measures retrieval or pipeline quality
- **profiling**, which measures runtime behavior and performance bottlenecks

See [Evaluation](../core_features/evaluation.md) and [Profiler](../advanced_usage/profiler.md).

## Reader-oriented map

Depending on what you want to do, start in different places:

- to **use MMORE**, start with [Quickstart](quickstart.md) and [Installation](installation.md)
- to **understand the pipeline**, read [Processing pipeline](process.md), [Indexing](indexing.md), and [RAG](rag.md)
- to **work on multimodal retrieval**, read [ColPali](../core_features/colpali.md)
- to **run at scale**, read [Distributed processing](../advanced_usage/distributed_processing.md)
- to **contribute to the codebase**, read [For developers](../developer_documentation/for_devs.md)

## Design principles

MMORE is organized around a few simple principles:

- clear separation between stages of the pipeline
- modularity between processing, indexing, retrieval, and evaluation
- support for heterogeneous and multimodal data
- scalability from local experiments to larger deployments
- readability for both users and contributors