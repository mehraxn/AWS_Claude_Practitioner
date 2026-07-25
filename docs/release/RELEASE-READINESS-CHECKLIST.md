# Release Readiness Checklist

## Phase and repository gates

- [x] Phase 6 closure records are present and internally consistent.
- [x] All 54 authorized backlog IDs are completed with zero closure blocker.
- [x] Canonical ownership and duplicate-name checks pass.
- [x] Certification badge consistency check passes.
- [x] Filename, link, empty-file, and whitespace validation passes.
- [x] No secret-path, environment-file, or unexpected tracked-binary issue was found.

## Learner and content QA

- [x] CPP and SAA learning paths are explicit and navigable.
- [x] Coverage gaps and depth limitations remain visible.
- [ ] Every knowledge check has an explained answer.
- [x] Original exam-preparation content is clearly distinguished from real exam material.
- [x] Pricing, Support, AI, migration, and product-status limitations are documented.
- [ ] Mermaid diagrams have been rendered with an automated Mermaid tool.

## Release documentation

- [x] Phase 7 QA reports are present.
- [x] Maintenance and freshness guide is present.
- [x] Known limitations are present.
- [x] Release notes and pull-request summary are present.
- [x] Final validation records issue counts and disposition.
- [x] Release-candidate manifest covers every changed and untracked path.
- [x] Final security and hygiene review found no secret or unsafe binary.
- [x] Human review guide, commit plan, pull-request draft, and final handoff exist.
- [x] Phase 6 and Phase 7 completion gates remain valid.
- [x] No duplicate canonical owner or broken primary navigation remains.
- [x] No real exam question or exam dump was found.

## Human actions

- [ ] Human reviewed all changed files.
- [ ] Human reviewed high-risk facts and current official exam guides.
- [ ] Human reviewed the complete Git diff and confirmed no unrelated work is lost.
- [ ] Human confirmed excluded files and temporary-script deletions.
- [ ] Human confirmed the target branch.
- [ ] Human confirmed the repository remote.
- [ ] Human approved commit creation.
- [ ] Human approved push.
- [ ] Human approved pull-request creation.
- [ ] Human sampled the CPP and SAA paths and accepted the documented editorial debt.
- [ ] Human reviewed CI results.

Unchecked items are intentional and must remain human decisions or documented limitations.
