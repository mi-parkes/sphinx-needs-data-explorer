# v0.93.0 - 2024-11-17

### Added
- Table export support for JSON and PDF formats.
- Node types filter: control which node types are visible or hidden in the network.
- Keyboard shortcuts for `dragView` and `zoomView`.

### Fixed
- Resolved GUI issues, including improper focus behavior after help or select-type operations.
- Fixed multiple `keydown` events being triggered when re-entering network mode.
- Fixed exiting the filter input window in table and file modes.

### Changed
- Applied `dropdownAutoWidth` for `select-type` dropdown, improving usability.
- Updated the format of displayed information about the number of nodes matching active filter(s). 
  - The format `x/y` now indicates the current position (`x`) of an item in the Sphinx-Needs listbox relative to the total number of items (`y`) that match the active filter(s). 
  - `NDV` stands for Neighborhood Depth View.

# v0.92.0 - 2024-11-14

### Added
- Support for filtering both incoming and outgoing link types (e.g., `satisfies`, `satisfies_back`).

# v0.91.0 - 2024-11-13

### Fixed
- References to non-existing IDs in table view are now handled properly.

# v0.90.0 - 2024-10-11

### Added
- Support to negate the content of a single bracket.
- Added `devcontainer` for development environment setup.
- Included `.vscode` configuration for streamlined development.
- Enabled `README.md` to be used by PyPI and Sphinx, including all image rendering.

### Changed
- Moved the package build process to Poetry for managing dependencies and packaging.
- Defining poetry tasks: black, clean, doc, doc-clean,..
- Set image URLs in `README.md`to frozen revision for stability.
- Updated documentation.
- Reformatted codebase using Black.

### Fixed
- Resolved issues with viewing node attributes.
- Ensured `GNU Makefile` exits on the first error during execution.

### Removed
- Removed manually generated documentation from version control in favor of automated alternatives using GitHub Actions.

### Miscellaneous
- Minor changes and optimizations.

