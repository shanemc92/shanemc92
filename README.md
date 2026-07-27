Working in IT and cybersecurity, mostly hands-on with security operations, infrastructure, and automation. What's uploaded here is a combination of scripts and apps that I've created to automate repetitive tasks and streamline my daily workflow.

## Tools I've built

**TimePilot** — self-hosted task board, day planner, single timer, and timesheet exporter for multiple users.

**security-assessment** — static HTML toolkit for running security maturity assessments against an industry framework (NIST CSF / CIS), then turning the result into a client-ready report. No backend required.

**change-manager** — browser-based tool for building and reusing IT change request templates (reason, steps, test plan, risks, backup plan, expected results).

**cert-tool** — single-file certificate/key toolkit, fully client-side, no server or dependencies.

**password-generator** — client-side password generator with theming and secure one-time sharing via scrt.link.

**ntfy-reminders** — self-hosted notification scheduler for [ntfy](https://ntfy.sh), with one-time and recurring reminders dispatched via cron.

## Server scripts

**debian-harden** — interactive hardening script for Debian-based systems. Sets up a sudo user/SSH key, hardens sshd, configures UFW and fail2ban, applies optional sysctl network hardening, and sets up unattended-upgrades and automatic cleanup — all from a handful of prompts.

**motd-stats** — login banner script showing server stats at a glance: failed systemd units, reboot-required flag, fail2ban bans, last apt update, swap usage.

## Study tooling

**mcq-portal** and **markdown-portal** grew out of wanting a better way to study my own notes while working toward various certifications I've obtained — an offline flashcard player and a single-file Markdown viewer, so revision material stays usable without a network connection or a bloated app.

## Older work

**remobix-v2** — a rebuild of an old college thesis project: an emoji-grid graphical password scheme that reshuffles and re-tokenises on every request.

---

Common thread across most of these: no build step, minimal dependencies, everything running from a single file where possible.

Demos of most of these apps are available at [sws.gltch.pro](https://sws.gltch.pro)
