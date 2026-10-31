
# NBA Analytics

A growing collection of basketball analytics projects exploring NBA performance, strategy, and decision-making through data.

## Overview

NBA Analytics is an evolving Python-based project focused on using basketball data to investigate questions about player performance, team dynamics, game strategy, and other aspects of the NBA.

The repository serves as both a research workspace and a collection of reusable analytical tools. Projects may involve statistical analysis, data visualization, predictive modeling, and other computational approaches.

Rather than focusing on a single research question, the goal is to continuously develop new analyses and expand the project's technical capabilities.

## Current Research

### Project 01 — Five-Man Lineup Performance Analysis

**Status: In Development**

The first project focuses on reconstructing NBA on-court lineups from play-by-play data and evaluating the performance of different five-man combinations.

The initial case study uses data from the Dallas Mavericks' 2026 preseason.

**Research Questions**
- Which five-man lineups perform most effectively?
- How do lineup combinations influence offensive and defensive efficiency?
- How does lineup performance vary with playing time and sample size?

**Current Progress**
- NBA play-by-play and box score data retrieval
- Starting lineup identification
- Substitution event parsing
- Player ID mapping and name normalization
- Initial lineup tracking implementation

**Currently Working On**
- Reconstructing lineups across quarter boundaries
- Validating on-court player combinations

**Next Steps**
- Generating lineup stints
- Calculating lineup-level efficiency metrics
- Visualizing and interpreting results

## Future Directions

Potential areas of exploration include:

- **Player Analytics:** Individual performance, efficiency, and development
- **Team & Lineup Analytics:** Player combinations, rotations, and on/off impact
- **Tactical Analysis:** Shot selection, defensive schemes, and play types
- **Predictive Modeling:** Machine learning applications to basketball data
- **Data Visualization:** Interactive and exploratory basketball analytics

These are potential research directions rather than a fixed development roadmap.

## Tools & Technologies

Current tools include:
- Python
- pandas
- nba_api
- Git and GitHub

Additional tools and libraries will be introduced as new projects develop.

## Repository Organization

- `src/` — Reusable analytics code
- `scripts/` — Development and testing scripts

The repository structure will evolve as additional research projects are introduced.

## Development Philosophy

This repository emphasizes reproducible analysis, transparent assumptions, and careful data validation.

New projects and research questions will be added over time, with an emphasis on building reusable tools rather than isolated one-off scripts.