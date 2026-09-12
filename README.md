<div align="center">

# 🛠️ Shane's Toolbox

**IT & cybersecurity tools built to automate repetitive tasks and streamline daily workflows.**

</div>

Working in IT and cybersecurity, mostly hands-on with security operations, infrastructure, and automation. What's here is a combination of scripts and apps I've built along the way to cut down on manual work and keep my daily routine moving.

> Common thread across most of these: no build step, minimal dependencies, everything running from a single file where possible.

<div align="center">

[![Static Badge](https://img.shields.io/badge/no%20build%20step-brightgreen)](#)
[![Static Badge](https://img.shields.io/badge/single%20file-blue)](#)
[![Static Badge](https://img.shields.io/badge/minimal%20deps-lightgrey)](#)
[![Demos](https://img.shields.io/badge/demos-sws.gltch.pro-orange)](https://sws.gltch.pro)

</div>

---

## 🧰 Tools

| Tool | What it does |
|---|---|
| 🗓️ **[TimePilot](https://github.com/shanemc92/TimePilot)** | Self-hosted task board, day planner, single timer, and timesheet exporter for multiple users |
| 🔃 [**flow-state**](https://github.com/shanemc92/flow-state) | Build a process as a flowchart, get a runbook out of it, then follow it step by step when it matters. Plus a plain incident timeline for the days nothing goes to plan |
| 📋 **[change-manager](https://github.com/shanemc92/change-manager)** | In-browser tool for building and reusing IT change request templates (reason, steps, test plan, risks, backup plan, expected results) |
| 🔔 **[ntfy-reminders](https://github.com/shanemc92/ntfy-reminders)** | Self-hosted notification scheduler for [ntfy](https://ntfy.sh), with one-time and recurring reminders dispatched via cron |
| ☕ **[cyber-barista](https://github.com/shanemc92/cyber-barista)** | Minimal client-side text encoding/decoding tool, zero dependencies - build recipes, export/import them, basic encryption functions |
| 🗃️ [**data-wrangler**](https://github.com/shanemc92/data-wrangler) | Paste or drop CSV, TSV, any delimiter, fixed width columns, JSON or JSON lines, Markdown tables or key=value log lines, run them through a list of steps, and export |
| ⛩️ **[gate-remote](https://github.com/shanemc92/gate-remote)** | Flask app that triggers a Raspberry Pi GPIO relay to toggle a physical gate remote - daily schedule, optional RTSP camera view, ntfy push on each toggle |

## 🛡️ Security

| Tool | What it does |
|---|---|
| 🔑 **[password-generator](https://github.com/shanemc92/password-generator)** | Client-side password generator with theming and secure one-time sharing via scrt.link |
| 🛡️ **[security-assessment](https://github.com/shanemc92/security-assessment)** | Static HTML toolkit for running security maturity assessments (NIST CSF / CIS) and generating a client-ready report - no backend required |
| 🔐 **[cert-tool](https://github.com/shanemc92/cert-tool)** | Single-file certificate/key toolkit, fully client-side, no server or dependencies |
| 🧽 **[scrub-adub](https://github.com/shanemc92/scrub-adub)** | Reversible PII redaction that runs entirely client-side - strip PII/secrets before pasting into an LLM, then decode the response back to real values |
| 🖼️ **[steg-lab](https://github.com/shanemc92/steg-lab)** | Tool to hide a message in the pixels of a PNG image. You can share the image and the recipient can use the decode tab to pull the message back out. |

## 🎮 Games

| Game | What it does |
|---|---|
| ⚖️ **[thirteen-clauses](https://github.com/shanemc92/thirteen-clauses)** | A text-based dungeon crawler about binding arbitration. Thirteen floors, a clause for every one. Plays in a terminal or in a browser - the browser version runs the same Python as the terminal version, compiled to WebAssembly, entirely in your tab. |
| 🚩 **[ninefold-ctf](https://github.com/shanemc92/ninefold-ctf)** | Nine compartments stand between you and the flag. Each one is a different physical trick - nothing is explained up front, and nothing about how a compartment works is visible in the page source until you've opened it. |
| 🚨 **[break-glass](https://github.com/shanemc92/break-glass)** | A cyber incident response tabletop simulator. You're the lead responder - choose the right actions to resolve the incident while minimising damage. |

## 📚 Study tooling

| Tool | What it does |
|---|---|
| 🗂️ **[mcq-portal](https://github.com/shanemc92/mcq-portal)** | Offline MCQ flashcard player for exam prep - load your own question banks in JSON, shuffle questions and answer order, track scores per attempt, flag weak topics for review, and revise without needing a network connection or an app store |
| 📖 **[markdown-portal](https://github.com/shanemc92/markdown-portal)** | Single-file Markdown viewer with custom theming, collapsible sidebar navigation, full-text search across all loaded notes, syntax-highlighted code blocks and table rendering, so revision notes and study guides stay usable and readable fully offline |

## 💰 Finance

| Tool | What it does |
|---|---|
| 💰 **[finance-ledger](https://github.com/shanemc92/finance-ledger)** | Personal finance workbook that runs entirely in your browser. Budgeting, loan amortisation, bank statement vs budget tracking, savings projections, maternity calculator electricity cost comparison and historical bill logs. |
| 📊 **[budget-tracker](https://github.com/shanemc92/budget-tracker)** | Budget tracker for projects - plan what each line item should cost, log what it actually cost, see how far ahead or behind you are |

## 🖥️ Server scripts

| Script | What it does |
|---|---|
| 🔒 **[debian-harden](https://github.com/shanemc92/debian-harden)** | Interactive hardening script for Debian-based systems - sudo user/SSH key setup, sshd hardening, UFW + fail2ban, optional sysctl network hardening, unattended-upgrades and automatic clean-up, all from a handful of prompts |
| 📈 **[motd-stats](https://github.com/shanemc92/motd-stats)** | Login banner showing server stats at a glance: failed systemd units, reboot-required flag, fail2ban bans, last apt update, swap usage |
| 🪟 **[powershell-automate](https://github.com/shanemc92/powershell-automate)** | Windows script scheduler platform with a central shared function library - email notifications, full transcript logging, log rotation, daily health check emails, script integrity monitoring, task scheduler management, and centralised credential management for AD and EntraID cert scripts |

## 🕰️ Older work

🎓 **[remobix-v2](https://github.com/shanemc92/remobix-v2)** - a rebuild of an old college thesis project: an emoji-grid graphical password scheme that reshuffles and re-tokenises on every request.

---

## 🚀 Demos

Live demos of most of these apps are available at **[sws.gltch.pro](https://sws.gltch.pro)**, and via GitHub Pages on each individual repo.

## 🐛 Feedback

Found a bug or have a feature idea? Open an issue on the relevant repo's Issues tab.

## ☕ Support

I'm posting everything here for free, but if you like these tools and want to help with development and hosting costs:

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=☕&slug=01fsslj4kk&button_colour=FFDD00&font_colour=000000&font_family=Comic&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/01fsslj4kk)
