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

<table>
<tr><th width="220">Tool</th><th>What it does</th></tr>
<tr><td>🗓️ <b><a href="https://github.com/shanemc92/TimePilot">TimePilot</a></b></td><td>Self-hosted task board, day planner, single timer, and timesheet exporter for multiple users</td></tr>
<tr><td>🔃 <b><a href="https://github.com/shanemc92/flow-state">flow&#8209;state</a></b></td><td>Build a process as a flowchart, get a runbook out of it, then follow it step by step when it matters. Plus a plain incident timeline for the days nothing goes to plan</td></tr>
<tr><td>📋 <b><a href="https://github.com/shanemc92/change-manager">change&#8209;manager</a></b></td><td>In-browser tool for building and reusing IT change request templates (reason, steps, test plan, risks, backup plan, expected results)</td></tr>
<tr><td>🔔 <b><a href="https://github.com/shanemc92/ntfy-reminders">ntfy&#8209;reminders</a></b></td><td>Self-hosted notification scheduler for <a href="https://ntfy.sh">ntfy</a>, with one-time and recurring reminders dispatched via cron</td></tr>
<tr><td>☕ <b><a href="https://github.com/shanemc92/cyber-barista">cyber&#8209;barista</a></b></td><td>Minimal client-side text encoding/decoding tool, zero dependencies - build recipes, export/import them, basic encryption functions</td></tr>
<tr><td>🗃️ <b><a href="https://github.com/shanemc92/data-wrangler">data&#8209;wrangler</a></b></td><td>Paste or drop CSV, TSV, any delimiter, fixed width columns, JSON or JSON lines, Markdown tables or key=value log lines, run them through a list of steps, and export</td></tr>
<tr><td>🧭 <b><a href="https://github.com/shanemc92/way-point">way&#8209;point</a></b></td><td>Single-file, client-side holiday itinerary builder - build a trip day by day, save it as JSON, load it back to edit, and export a themed, script-free HTML page or Markdown file for printing</td></tr>
<tr><td>⛩️ <b><a href="https://github.com/shanemc92/gate-remote">gate&#8209;remote</a></b></td><td>Flask app that triggers a Raspberry Pi GPIO relay to toggle a physical gate remote - daily schedule, optional RTSP camera view, ntfy push on each toggle</td></tr>
</table>

## 🛡️ Security

<table>
<tr><th width="220">Tool</th><th>What it does</th></tr>
<tr><td>🔑 <b><a href="https://github.com/shanemc92/password-generator">password&#8209;generator</a></b></td><td>Client-side password generator with theming and secure one-time sharing via scrt.link</td></tr>
<tr><td>🗝️ <b><a href="https://github.com/shanemc92/back-stop">back&#8209;stop</a></b></td><td>Single-file browser vault for account recovery codes - AES-256-GCM under a PBKDF2 passphrase, exports an encrypted file, and prints a plain code sheet, an encrypted QR backup and a break-glass key card. Offline Python recovery script included</td></tr>
<tr><td>🛡️ <b><a href="https://github.com/shanemc92/security-assessment">security&#8209;assessment</a></b></td><td>Static HTML toolkit for running security maturity assessments (NIST CSF / CIS) and generating a client-ready report - no backend required</td></tr>
<tr><td>🔐 <b><a href="https://github.com/shanemc92/cert-tool">cert&#8209;tool</a></b></td><td>Single-file certificate/key toolkit, fully client-side, no server or dependencies</td></tr>
<tr><td>🧽 <b><a href="https://github.com/shanemc92/scrub-adub">scrub&#8209;adub</a></b></td><td>Reversible PII redaction that runs entirely client-side - strip PII/secrets before pasting into an LLM, then decode the response back to real values</td></tr>
<tr><td>🖼️ <b><a href="https://github.com/shanemc92/steg-lab">steg&#8209;lab</a></b></td><td>Tool to hide a message in the pixels of a PNG image. You can share the image and the recipient can use the decode tab to pull the message back out.</td></tr>
</table>

## 🎮 Games

<table>
<tr><th width="220">Game</th><th>What it does</th></tr>
<tr><td>⚖️ <b><a href="https://github.com/shanemc92/thirteen-clauses">thirteen&#8209;clauses</a></b></td><td>A text-based dungeon crawler about binding arbitration. Thirteen floors, a clause for every one. Plays in a terminal or in a browser - the browser version runs the same Python as the terminal version, compiled to WebAssembly, entirely in your tab.</td></tr>
<tr><td>🚩 <b><a href="https://github.com/shanemc92/ninefold-ctf">ninefold&#8209;ctf</a></b></td><td>Nine compartments stand between you and the flag. Each one is a different physical trick - nothing is explained up front, and nothing about how a compartment works is visible in the page source until you've opened it.</td></tr>
<tr><td>🚨 <b><a href="https://github.com/shanemc92/break-glass">break&#8209;glass</a></b></td><td>A cyber incident response tabletop simulator. You're the lead responder - choose the right actions to resolve the incident while minimising damage.</td></tr>
</table>

## 📚 Study tooling

<table>
<tr><th width="220">Tool</th><th>What it does</th></tr>
<tr><td>🗂️ <b><a href="https://github.com/shanemc92/mcq-portal">mcq&#8209;portal</a></b></td><td>Offline MCQ flashcard player for exam prep - load your own question banks in JSON, shuffle questions and answer order, track scores per attempt, flag weak topics for review, and revise without needing a network connection or an app store</td></tr>
<tr><td>📖 <b><a href="https://github.com/shanemc92/markdown-portal">markdown&#8209;portal</a></b></td><td>Single-file Markdown viewer with custom theming, collapsible sidebar navigation, full-text search across all loaded notes, syntax-highlighted code blocks and table rendering, so revision notes and study guides stay usable and readable fully offline</td></tr>
</table>

## 💰 Finance

<table>
<tr><th width="220">Tool</th><th>What it does</th></tr>
<tr><td>💰 <b><a href="https://github.com/shanemc92/finance-ledger">finance&#8209;ledger</a></b></td><td>Personal finance workbook that runs entirely in your browser. Budgeting, loan amortisation, bank statement vs budget tracking, savings projections, maternity calculator electricity cost comparison and historical bill logs.</td></tr>
<tr><td>📊 <b><a href="https://github.com/shanemc92/budget-tracker">budget&#8209;tracker</a></b></td><td>Budget tracker for projects - plan what each line item should cost, log what it actually cost, see how far ahead or behind you are</td></tr>
</table>

## 🖥️ Server scripts

<table>
<tr><th width="220">Script</th><th>What it does</th></tr>
<tr><td>🔒 <b><a href="https://github.com/shanemc92/debian-harden">debian&#8209;harden</a></b></td><td>Interactive hardening script for Debian-based systems - sudo user/SSH key setup, sshd hardening, UFW + fail2ban, optional sysctl network hardening, unattended-upgrades and automatic clean-up, all from a handful of prompts</td></tr>
<tr><td>📈 <b><a href="https://github.com/shanemc92/motd-stats">motd&#8209;stats</a></b></td><td>Login banner showing server stats at a glance: failed systemd units, reboot-required flag, fail2ban bans, last apt update, swap usage</td></tr>
<tr><td>🪟 <b><a href="https://github.com/shanemc92/powershell-automate">powershell&#8209;automate</a></b></td><td>Windows script scheduler platform with a central shared function library - email notifications, full transcript logging, log rotation, daily health check emails, script integrity monitoring, task scheduler management, and centralised credential management for AD and EntraID cert scripts</td></tr>
</table>

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
