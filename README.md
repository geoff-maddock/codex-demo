# codex-demo

Demo project for testing out codex

## Board Game Art Generator

This small application helps you craft prompts for an image generation API to create artwork for tabletop board games. It uses the `openai` package to generate images via the DALL·E API.

### Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key in the environment:

   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

### Running the App

Execute the interactive script:

```bash
python -m boardgame_art.app
```

The script will ask for a description of the art you want, optional style and color scheme, and then attempt to generate an image. The resulting URL from the API is printed to the console.

### Tests

Unit tests are located in the `tests/` directory and can be run with `python -m unittest`:

```bash
python -m unittest discover -v
```
