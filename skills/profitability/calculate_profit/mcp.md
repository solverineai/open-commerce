# Future MCP Support

Expose `calculate_profit` as an MCP tool with a JSON input schema matching `interface.json`.

## Tool Contract

- Tool name: `opencommerce.calculate_profit`
- Input: explicit monetary costs and quantity.
- Output: profitability metrics and cost breakdown.
- Safety: do not resolve starter dataset values as verified costs unless the tool response includes a confidence warning.
