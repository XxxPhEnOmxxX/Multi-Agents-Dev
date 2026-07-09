# Code Analysis

## Goal

Use the best available code-search tool without assuming a specific local environment.

## Tool priority

1. `sg` / ast-grep for structural search.
2. `rg` / ripgrep for fast text search.
3. `grep` as a universal fallback.

## Detection

```bash
if command -v sg >/dev/null 2>&1; then
  echo "use ast-grep"
elif command -v rg >/dev/null 2>&1; then
  echo "use ripgrep"
else
  echo "use grep"
fi
```

## Scope control

Exclude generated and dependency directories:

```txt
.git
node_modules
vendor
dist
build
coverage
.tmp
```

Prefer source directories:

```txt
src
lib
app
packages
services
modules
```

## Usage guidance

Use code search to answer:

- how existing features are structured;
- where similar validation is implemented;
- which commands exist for test/build/lint;
- which modules own a concept;
- which files a task actually needs to touch.

Do not replace reasoning with broad searches. Search specifically, inspect relevant files, then decide.
