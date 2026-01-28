#!/bin/bash

echo "Making repository professional..."

# Remove emojis from all markdown files
find . -name "*.md" -type f -exec sed -i '' 's/[😀-🙏🌀-🗿🚀-🛿🇦-🇿✂-➰Ⓜ-🉑]//' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/✅//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/🎉//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/🚀//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/📊//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/🔥//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/💪//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/🎯//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/📝//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/⚡//g' {} \;
find . -name "*.md" -type f -exec sed -i '' 's/🛡️//g' {} \;

# Clean up Python files
find . -name "*.py" -type f -exec sed -i '' 's/[😀-🙏🌀-🗿🚀-🛿🇦-🇿✂-➰Ⓜ-🉑]//' {} \;

echo "✓ Emojis removed"
echo "✓ Repository professionalized"
