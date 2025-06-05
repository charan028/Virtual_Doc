# 🩺 Virtual Doctor – AI-Powered Health Assistant

![Virtual Doctor Banner](https://your-image-link-here.com/banner.png)

**Virtual Doctor** is an AI-powered healthcare assistant that allows users to upload medical images (like rashes, scans), describe symptoms, and receive intelligent diagnosis and voice responses. It combines the power of **OpenAI (via GroqCloud)** for natural language understanding and **ElevenLabs** for lifelike voice synthesis. Built with **Gradio** for an interactive web interface.

---

## 🚀 Features

- 🖼️ Upload medical images (e.g., skin rash, eye redness, etc.)
- ✍️ Optionally describe symptoms in plain text
- 🤖 LLM-based diagnosis using OpenAI GPT via GroqCloud
- 🔊 Speaks diagnosis using ElevenLabs' TTS API
- 🧑‍⚕️ Mimics a friendly virtual doctor conversation
- 🌐 Clean Gradio interface, works locally or can be hosted

---

## 🧰 Tech Stack

| Layer            | Tools Used                     |
|------------------|-------------------------------|
| UI               | Gradio                        |
| Backend          | Python (FastAPI optional)     |
| Inference Engine | OpenAI GPT via GroqCloud      |
| Voice Synthesis  | ElevenLabs TTS (v2)           |
| Image Processing | PIL, base64                   |
| Deployment       | Uvicorn, Docker (optional)    |

---


### Create a `.env` file in the root:
```
```env
OPENAI_API_KEY=your_groqcloud_key
GROQ_API_BASE=https://api.groq.com/openai/v1
ELEVENLABS_API_KEY=your_elevenlabs_key
ELEVENLABS_VOICE_ID=your_voice_id
```# Virtual_Doc
