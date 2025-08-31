import argparse
import os
import ast
import inspect

def generate_docs():
    """Generates documentation from the source code."""
    print("Generating documentation...")
    
    source_path = "src/code_to_content_demo/main.py"
    output_path = "generated_docs.md"
    
    if not os.path.exists(source_path):
        print(f"Error: Source file not found at {source_path}")
        return

    with open(source_path, "r") as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    
    docs_content = "# Documentation\n\n## API Reference\n\n"

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            docstring = ast.get_docstring(node)
            
            # Get signature
            # This is a bit tricky as we don't have the live object
            # We'll reconstruct it from the AST
            args = [a.arg for a in node.args.args]
            signature = f"{func_name}({', '.join(args)})"
            
            docs_content += f"### `{signature}`\n\n"
            if docstring:
                docs_content += f"{docstring.strip()}\n\n"

    with open(output_path, "w") as f:
        f.write(docs_content)
        
    print(f"Documentation successfully generated at {output_path}")


def generate_changelog(since=None):
    """Generates a changelog by comparing the current code to a previous state."""
    print(f"Generating changelog since {since}...")

    source_path = "src/code_to_content_demo/main.py"
    output_path = "generated_changelog.md"

    # Simulate a "previous" version of the code for comparison
    previous_code_state = {
        "greet",
    }

    if not os.path.exists(source_path):
        print(f"Error: Source file not found at {source_path}")
        return

    with open(source_path, "r") as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    
    current_functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    
    new_functions = current_functions - previous_code_state

    changelog_content = "## Changelog\n\n"

    if new_functions:
        changelog_content += "### Added\n"
        for func in new_functions:
            changelog_content += f"- New `{func}()` function.\n"

    with open(output_path, "w") as f:
        f.write(changelog_content)

    print(f"Changelog successfully generated at {output_path}")


def generate_blog(style=None):
    """Generates a blog post about new features."""
    print(f"Generating blog post with style {style}...")

    source_path = "src/code_to_content_demo/main.py"
    output_path = "generated_blog.md"

    # Simulate a "previous" version of the code for comparison
    previous_code_state = {
        "greet",
    }

    if not os.path.exists(source_path):
        print(f"Error: Source file not found at {source_path}")
        return

    with open(source_path, "r") as f:
        source_code = f.read()

    tree = ast.parse(source_code)
    
    current_functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    
    new_functions = current_functions - previous_code_state

    if not new_functions:
        print("No new features to write about.")
        return

    blog_content = "# New Features in Our Project!\n\n"

    if style == "casual":
        blog_content += "We've been hard at work on some exciting new updates. Here's a look at what's new:\n\n"
    else: # technical
        blog_content += "This post outlines the recent additions to the codebase.\n\n"

    for func_name in new_functions:
        if style == "casual":
            blog_content += f"## Say Hello to `{func_name}`!\n\n"
            blog_content += f"We've just added the `{func_name}` function. It's a great new way to interact with our application. Here's how you can use it:\n\n"
        else: # technical
            blog_content += f"### New Function: `{func_name}`\n\n"
            blog_content += f"The `{func_name}` function has been added to the API. Below is a usage example:\n\n"

        # Extract the function's source code for the snippet
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                # This is a simplified way to get the source; a more robust solution
                # would use inspect.getsource or similar on a live object.
                snippet = ast.get_source_segment(source_code, node)
                blog_content += f"```python\n{snippet}\n```\n\n"
                break

    with open(output_path, "w") as f:
        f.write(blog_content)

    print(f"Blog post successfully generated at {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Code-to-Content Generator")
    subparsers = parser.add_subparsers(dest="command")

    # 'generate' command
    gen_parser = subparsers.add_parser("generate", help="Generate content from the repository")
    gen_subparsers = gen_parser.add_subparsers(dest="content_type")

    # 'generate docs' command
    docs_parser = gen_subparsers.add_parser("docs", help="Generate documentation")
    docs_parser.set_defaults(func=generate_docs)

    # 'generate changelog' command
    changelog_parser = gen_subparsers.add_parser("changelog", help="Generate a changelog")
    changelog_parser.add_argument("--since", help="The git tag or commit to generate the changelog from")
    changelog_parser.set_defaults(func=lambda args: generate_changelog(since=args.since))

    # 'generate blog' command
    blog_parser = gen_subparsers.add_parser("blog", help="Generate a blog post")
    blog_parser.add_argument("--style", choices=["technical", "casual"], default="casual", help="The style of the blog post")
    blog_parser.set_defaults(func=lambda args: generate_blog(style=args.style))

    args = parser.parse_args()
    if hasattr(args, "func"):
        if "since" in args or "style" in args:
            args.func(args)
        else:
            args.func()

if __name__ == "__main__":
    main()