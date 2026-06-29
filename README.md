# HuginnMuninn

HuginnMuninn is an event-driven, multithreaded background daemon that acts as an intelligent auditory assistant. Operating on a producer-consumer architecture, the system monitors enterprise email feeds in real time via Microsoft Graph, processes incoming events, and utilizes a local Speech-to-Text (STT) pipeline to provide seamless voice-driven notifications and context awareness.

Unlike single-execution scripts, HuginnMuninn is architected to run indefinitely in the background, managing thread-safe queues, external API authentications, and local model inference without blocking the core execution loop.

## 🛠️ Architectural Overview

The system is split into two primary concurrent modules (named after Odin's mythical ravens of thought and memory) that communicate over a thread-safe synchronized queue:

* **Huginn (The Producer / Information Gatherer):** Establishes a persistent connection to the Microsoft Graph API using OAuth2 authorization flows. It continuously polls or responds to webhooks for new email events, filters them based on user-defined priority layers, and pushes payloads onto the shared queue.
* **Muninn (The Consumer / Processing Engine):** Monitors the shared queue. Upon receiving a payload, it orchestrates the notification engine, managing local Whisper (STT) inference and audio endpoints to gracefully announce incoming alerts without starving system resources.

## ✨ Key Technical Showcases

* **Multithreaded Daemon Architecture:** Designed as a persistent background process with coordinated threads, robust lifecycle management, and clean signal handling (`SIGINT` / `SIGTERM`).
* **Producer-Consumer Concurrency Pattern:** Implements a strict, thread-safe queue between the data-ingestion layer (Huginn) and the audio / inference engine (Muninn) to eliminate race conditions and prevent API blocking.
* **OAuth2 & Rest API Integration:** Implements fully authenticated REST workflows with Token lifecycle management (refresh and access tokens) via Microsoft Graph API.
* **Local STT Pipeline:** Integrates OpenAI's Whisper locally for context-aware processing, keeping data entirely on-device and eliminating external cloud inference costs or latencies.
* **Event-Driven Design:** Moves away from static input processing, reacting dynamically to real-time external network and voice events.

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Microsoft Azure Developer Account (for Graph API credentials)
* Local audio drivers (PyAudio / SoundDevice dependencies)

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/HuginnMuninn.git](https://github.com/yourusername/HuginnMuninn.git)
   cd HuginnMuninn

### Install dependencies
pip install -r requirements.txt

### Configure variables
Configure your environment variables in a .env file:
Code snippet
CLIENT_ID=your_azure_client_id
CLIENT_SECRET=your_azure_client_secret
TENANT_ID=your_azure_tenant_id
REDIRECT_URI=http://localhost:8080

### Running it
python main.py --daemon
