import os


def compose_prompt(base_idea: str, style: str | None = None, color_scheme: str | None = None) -> str:
    parts = [base_idea.strip()]
    if style:
        parts.append(f"in {style} style")
    if color_scheme:
        parts.append(f"using {color_scheme} colors")
    return ", ".join(parts)


def generate_image(prompt: str, size: str = "1024x1024") -> str:
    """Generate an image using OpenAI's image API and return the URL."""
    import openai  # imported lazily so tests can run without the package

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")

    response = openai.Image.create(prompt=prompt, n=1, size=size)
    return response["data"][0]["url"]


def interactive_session() -> None:
    base = input("Describe the board game artwork you want to create: ")
    style = input("Optional - specify an art style (or leave blank): ")
    color = input("Optional - specify a color scheme (or leave blank): ")
    prompt = compose_prompt(base, style or None, color or None)
    print(f"Using prompt: {prompt}")
    confirm = input("Generate image with this prompt? [y/N]: ")
    if confirm.lower().startswith("y"):
        try:
            url = generate_image(prompt)
        except Exception as exc:
            print(f"Failed to generate image: {exc}")
            return
        print(f"Image created: {url}")
    else:
        print("Aborted.")


if __name__ == "__main__":
    interactive_session()
