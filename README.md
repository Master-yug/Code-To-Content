# Code-to-Content Demo

This is a sample project to demonstrate the capabilities of the Code-to-Content Generator.

It includes:
- A simple Python application.
- Project metadata in `pyproject.toml`.
- A command-line tool, `roo.py`, for generating content.

## Usage

The `roo.py` tool can be used to generate documentation, changelogs, and blog posts from the source code.

### Generate Documentation

To generate documentation, run the following command:

```bash
python roo.py generate docs
```

This will create a `generated_docs.md` file containing the API documentation.

### Generate a Changelog

To generate a changelog, run:

```bash
python roo.py generate changelog
```

This will create a `generated_changelog.md` file, which will list any new functions added to the project.

### Generate a Blog Post

To generate a blog post, you can use the following command:

```bash
python roo.py generate blog
```

You can also specify a style for the blog post:

```bash
python roo.py generate blog --style technical
```

This will create a `generated_blog.md` file with a blog post about the new features.