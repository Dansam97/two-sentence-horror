"""Two-Sentence Horror entry.

Writes the story to entry.txt in the output directory.
"""

import os

TEXT = (
    "The sleep clinic pays me to dream on camera, "
    "and every morning the doctors ask me what I dreamed. "
    "This morning they said nothing, because the camera had recorded me "
    "standing over each of their beds, asking them the same question."
)


def validated_text():
    """Enforce the bounty gate: exactly two sentences, 1-400 chars, UTF-8."""
    encoded = TEXT.encode("utf-8")
    assert 1 <= len(TEXT) <= 400, f"text must be 1..400 chars, got {len(TEXT)}"
    assert TEXT.strip(), "text must not be only whitespace"
    sentences = [s for s in TEXT.split(".") if s.strip()]
    assert len(sentences) == 2, f"expected exactly 2 sentences, got {len(sentences)}"
    return encoded


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = validated_text()
    with open(path, "wb") as f:
        f.write(data + b"\n")
    with open(path, "rb") as f:
        assert f.read() == data + b"\n", "written bytes differ from validated text"


if __name__ == "__main__":
    main()
