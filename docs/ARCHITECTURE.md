# Architecture

```text
GitHub public activity
        ↓
Daily collector / public events
        ↓
Normalized JSON state
        ↓
Analytics
        ↓
Widget renderers
        ↓
README / SVG / history JSON
```

Profile Signal intentionally separates two refresh paths:

- **Full refresh**: Search API metrics, operations/CI, history, SVG generation, and all enabled widgets every three hours.
- **Latest signals refresh**: public-event-driven LIVE SIGNAL, CURRENT FOCUS, and ACTIVITY STREAM every 30 minutes.

The lightweight stream refresh merges only dynamic public-event keys into the existing state so CI, repository health, and historical aggregates are not discarded or recomputed on every run.
