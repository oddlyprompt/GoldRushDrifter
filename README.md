# Gold Rush Drifter (Web)
A Western MUD-lite **text RPG** with **real-time (tick-based)** combat. Built with **Vite + React + TypeScript**. Deployed on **Vercel**; packaged for **itch.io**.

## Quick Start
```bash
npm i
npm run dev
```

## Commands

* `bounty easy|std|hard|deadly`
* `attack` (optionally `attack bandit_grunt_1`)
* `reload`
* `flee`
* `help`, `map`

## Deploy to Vercel

1. Push this repo to GitHub.
2. In Vercel, **New Project** → Import repo → Framework preset **Vite** → Build `npm run build` → Output `dist`.
3. `vercel.json` is provided.

## Ship to itch.io

* Manual: `npm run build` then zip `dist/` and upload as **HTML5**.
* CI (recommended): Add repo secret `ITCH_API_KEY` (butler API key). Tag `release-0.1.0` to trigger workflow. Edit the workflow slug to your game page.

## Game Features

- **Real-time Combat**: Tick-based combat system with cast times and cooldowns
- **Western Setting**: Gold-rush boomtown with unlockable buildings
- **Multiple Encounters**: Bounty hunting, escort missions, prospecting, duels, and more
- **Deterministic RNG**: Consistent gameplay experience with seeded randomness
- **Progress System**: Build town prosperity to unlock new buildings and opportunities

## Building & Deployment

The game builds to a static `dist/` folder that can be deployed anywhere:

```bash
npm run build
```

For itch.io, simply zip the contents of `dist/` and upload as an HTML5 game.