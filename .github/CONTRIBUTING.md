# Contributing: staged delivery

The normal change path for this repository is **`feature/* → staging → main`**.

1. Create a short-lived feature or fix branch from `staging` and open a reviewed
   pull request back to `staging`. This includes maintenance, dependency updates,
   documentation, and agent-authored changes.
2. Run the repository's required CI and validate the integrated candidate in its
   lower environment. Record the commit/artifact and smoke or acceptance results.
   For libraries and documentation, record the applicable package/test/build
   evidence; a branch name does not establish that a deployed environment exists.
3. Open a separate promotion PR from `staging` to `main` in this repository.
   Link the validated candidate, required human approvals, release checklist and
   rollback plan. A release includes every change in that candidate; unfinished
   work must stay out or be safely disabled.
4. Use the existing deployment procedure and verify the running version and
   relevant user-visible behavior. Branch merges alone do not prove deployment.

Do not direct-push normal work to `staging` or `main`, or open a feature PR
straight into `main`. An emergency exception requires the approved incident
process, explicit authorization, exact revision, validation and recovery evidence,
and subsequent reconciliation into `staging`. A label or a branch called
`hotfix` does not grant an exception.

When this guide is inherited by another repository, use that repository’s
explicitly documented `staging` or `qa` integration branch and its existing
production branch (`main`, or a documented legacy name). Local lane mappings
take precedence over this repository’s branch names, not over staged review.

## Enforcement and rollout

Where installed, the PR routing workflow checks branch and repository identity. It does not
verify application tests, approvals, deployed artifacts, or emergency authority.
A check is mandatory only when GitHub branch protection/rulesets require it.
Protect both integration and release branches with reviewed PRs, prohibit force
pushes/deletions, and preserve all existing stronger checks. Require the routing
check on release branches after the workflow is installed and has run there;
do not require a check that is not yet available. Review automation that writes
directly to protected branches before enabling restrictions, and route its
changes through PRs. Keep emergency bypass access narrow and audited.

Before promotion, reconcile any existing topic PRs aimed at production. Inspect
their diff against the integration branch before retargeting: changing a PR base
can change its contents. Do not bulk merge or retarget other contributors' PRs.

The organization standard is documented in the
[staged delivery guide](https://github.com/GapIntelligence/.github-private/blob/staging/docs/practices/staged-github-flow.md).
New contributors should walk through their first integration PR and a release
example with the repository owner; this file is not a training acknowledgment.
