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

## 🧰 Tools I've built

| Tool | What it does |
|---|---|
| 🗓️ **[TimePilot](https://github.com/shanemc92/TimePilot)** | Self-hosted task board, day planner, single timer, and timesheet exporter for multiple users |
| 🛡️ **[security-assessment](https://github.com/shanemc92/security-assessment)** | Static HTML toolkit for running security maturity assessments (NIST CSF / CIS) and generating a client-ready report — no backend required |
| 📋 **[change-manager](https://github.com/shanemc92/change-manager)** | In-browser tool for building and reusing IT change request templates (reason, steps, test plan, risks, backup plan, expected results) |
| 🔐 **[cert-tool](https://github.com/shanemc92/cert-tool)** | Single-file certificate/key toolkit, fully client-side, no server or dependencies |
| 🔑 **[password-generator](https://github.com/shanemc92/password-generator)** | Client-side password generator with theming and secure one-time sharing via scrt.link |
| 🔔 **[ntfy-reminders](https://github.com/shanemc92/ntfy-reminders)** | Self-hosted notification scheduler for [ntfy](https://ntfy.sh), with one-time and recurring reminders dispatched via cron |
| 🧽 **[scrub-adub](https://github.com/shanemc92/scrub-adub)** | Reversible PII redaction that runs entirely client-side — strip PII/secrets before pasting into an LLM, then decode the response back to real values |
| 💰 **[finance-ledger](https://github.com/shanemc92/finance-ledger)** | Personal finance workbook that runs entirely in the browser — budgeting, loan amortisation, statement categoriser, savings projections, historical bill logs |
| 📊 **[budget-tracker](https://github.com/shanemc92/budget-tracker)** | Budget tracker for projects — plan what each line item should cost, log what it actually cost, see how far ahead or behind you are |
| ⛩️ **[gate-remote](https://github.com/shanemc92/gate-remote)** | Flask app that triggers a Raspberry Pi GPIO relay to toggle a physical gate remote — daily schedule, optional RTSP camera view, ntfy push on each toggle |

## 🖥️ Server scripts

| Script | What it does |
|---|---|
| 🔒 **[debian-harden](https://github.com/shanemc92/debian-harden)** | Interactive hardening script for Debian-based systems — sudo user/SSH key setup, sshd hardening, UFW + fail2ban, optional sysctl network hardening, unattended-upgrades and automatic cleanup, all from a handful of prompts |
| 📈 **[motd-stats](https://github.com/shanemc92/motd-stats)** | Login banner showing server stats at a glance: failed systemd units, reboot-required flag, fail2ban bans, last apt update, swap usage |

## 📚 Study tooling

**[mcq-portal](https://github.com/shanemc92/mcq-portal)** and **[markdown-portal](https://github.com/shanemc92/markdown-portal)** grew out of wanting a better way to study my own notes while working toward various certifications — an offline flashcard player and a single-file Markdown viewer, so revision material stays usable without a network connection or a bloated app.

## 🕰️ Older work

🎓 **[remobix-v2](https://github.com/shanemc92/remobix-v2)** — a rebuild of an old college thesis project: an emoji-grid graphical password scheme that reshuffles and re-tokenises on every request.

---

## 🚀 Demos

Live demos of most of these apps are available at **[sws.gltch.pro](https://sws.gltch.pro)**, and via GitHub Pages on each individual repo.

## 🐛 Feedback

Found a bug or have a feature idea? Open an issue on the relevant repo's Issues tab.

## ☕ Support

I'm posting everything here for free, but if you like these tools and want to help with development and hosting costs:

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=☕&slug=01fsslj4kk&button_colour=FFDD00&font_colour=000000&font_family=Comic&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/01fsslj4kk)
