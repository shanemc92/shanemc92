Working in IT and cybersecurity, mostly hands-on with security operations, infrastructure, and automation. What's uploaded here is a combination of scripts and apps that I've created to automate repetitive tasks and streamline my daily workflow.

## Tools I've built

**[TimePilot](https://github.com/shanemc92/TimePilot)** -- self-hosted task board, day planner, single timer, and timesheet exporter for multiple users.

**[security-assessment](https://github.com/shanemc92/security-assessment)** -- static HTML toolkit for running security maturity assessments against an industry framework (NIST CSF / CIS), then turning the result into a client-ready report. No backend required.

**[change-manager](https://github.com/shanemc92/change-manager)** -- browser-based tool for building and reusing IT change request templates (reason, steps, test plan, risks, backup plan, expected results).

**[cert-tool](https://github.com/shanemc92/cert-tool)** -- single-file certificate/key toolkit, fully client-side, no server or dependencies.

**[password-generator](https://github.com/shanemc92/password-generator)** -- client-side password generator with theming and secure one-time sharing via scrt.link.

**[ntfy-reminders](https://github.com/shanemc92/ntfy-reminders)** -- self-hosted notification scheduler for [ntfy](https://ntfy.sh), with one-time and recurring reminders dispatched via cron.

**[scrub-adub](https://github.com/shanemc92/scrub-adub)** -- reversible PII redaction, entirely in your browser. Strip PII, secrets and anything else you don't want leaving the  building out of a file, paste the redacted version into an LLM, then decode the model's response back to the real values.

**[finance-ledger](https://github.com/shanemc92/finance-ledger)** -- personal finance workbook that runs entirely in your  browser. Budgeting, loan amortisation, bank statement categoriser,  savings projections and historical bill logs.

**[budget-tracker](https://github.com/shanemc92/budget-tracker)** --  budget tracker for projects. Plan what each line item should cost, log what it actually cost, and see how far ahead or behind you are.

**[gate-remote](https://github.com/shanemc92/gate-remote)** -- self-hosted flask web app that triggers a Raspberry Pi GPIO relay to toggle a physical gate remote. Daily on/off schedule, optional RSTP camera view and ntfy push notification on each toggle. 

## Server scripts

**[debian-harden](https://github.com/shanemc92/debian-harden)** -- interactive hardening script for Debian-based systems. Sets up a sudo user/SSH key, hardens sshd, configures UFW and fail2ban, applies optional sysctl network hardening, and sets up unattended-upgrades and automatic cleanup -- all from a handful of prompts.

**[motd-stats](https://github.com/shanemc92/motd-stats)** -- login banner script showing server stats at a glance: failed systemd units, reboot-required flag, fail2ban bans, last apt update, swap usage.

## Study tooling

**[mcq-portal](https://github.com/shanemc92/mcq-portal)** and **[markdown-portal](https://github.com/shanemc92/markdown-portal)** grew out of wanting a better way to study my own notes while working toward various certifications I've obtained -- an offline flashcard player and a single-file Markdown viewer, so revision material stays usable without a network connection or a bloated app.

## Older work

**[remobix-v2](https://github.com/shanemc92/remobix-v2)** -- a rebuild of an old college thesis project: an emoji-grid graphical password scheme that reshuffles and re-tokenises on every request.

---

Common thread across most of these: no build step, minimal dependencies, everything running from a single file where possible.

Demos of most of these apps are available at [sws.gltch.pro](https://sws.gltch.pro) and also via Github Pages on each repo. 

If you find any bugs or have any feature suggestions, you can send them through the issues tabs. 



I'm posting everything I've built here but if you like them and want to help towards development and hosting, feel free. 

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/01fsslj4kk)

