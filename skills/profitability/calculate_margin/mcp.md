# Future MCP Support

Expose `calculate_margin` as `opencommerce.calculate_margin`.

The MCP tool should require `revenue` and one of `total_costs` or `profit`. It should reject ambiguous payloads where both values conflict.
