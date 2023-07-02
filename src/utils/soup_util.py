from bs4 import Tag


def has_instructions(tag: Tag):
    if "instructions" in tag.text.lower():
        return tag
