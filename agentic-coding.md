# Agentic Coding Workflow

<i>The original Agentic Coding guide is available [via the confidential repo](https://github.com/GapIntelligence/.github-private/blob/main/docs/agentic-coding.md).  This snapshot of it was made public June 22, 2025</i>.
***

This document outlines a step-by-step process for creating new repositories
using automated agents at OpenBrand. The goal is to build consistent projects
with reliable tests and linting before adding complex features.

Treat each agent like a junior engineer with limitless stamina but no intuition.
Provide clear goals, spell out constraints, and redirect the agent when it
wanders. Tests are the agent's map and guardrail, so the harness must be tight
before leaning on automation.

## 1. Start With the License

Every repository must include the standard license statement:

```
All Rights Reserved, OpenBrand.
```

Create a `LICENSE` file at the repository root containing this exact text. See
the [License Guide](license-guide.md) for additional details. Commit this file
directly to `main` before creating any branches.

Failing to set the license up front will definitely generate bad results. As an
example:

<img src='https://github.com/user-attachments/assets/55548bbb-952e-4d03-9a69-4d03c462107c' width='450' title='dont let this happen to you'>

## 2. Add `AGENTS.md`

After the license, create an `AGENTS.md` in the root of the repository. This
file describes the rules and commands agents should follow when contributing to
the project. Include guidelines on commit style, required checks, and any
project-specific notes. Commit `AGENTS.md` to `main` alongside the license. See
[AGENTS Usage Guide](agents_usage.md) for more details.

Pin all dependencies early and commit lockfiles so agent builds remain
reproducible. Keep commits small and enforce short-lived feature branches so
emergent bugs are easier to spot.

Once the license and `AGENTS.md` are committed to `main`, create a new branch
for the remainder of the workflow. Steps 3 through 9 assume you are on that
branch.

## 3. Scan for Large or Binary Files

Before running automated agents, inspect the repository for binary data or
extremely large files. Such files can clutter an agent's context and slow down
analysis. Add ignore rules in `AGENTS.md` or `.gitignore` to keep them out of
the agent workflow.

Large diffs hide emergent bugs, so check commit size before pushing. A scripted
pre-commit hook can warn when a change exceeds a safe threshold.

## 4. Create a Development Branch

If you haven't created a development branch yet, do so now so the main branch
remains clean. Direct pushes to `main` are blocked for SOC 2 compliance, so all
further commits go on this branch through a pull request. Typical branch names
are `codex` or `staging`.

Add the `Branch Protection Enforcement` workflow to enforce these rules. It
rejects direct pushes and fails pull requests that lack at least one approval.

## 5. Minimal Tester

Set up a basic testing framework early on. A simple `pytest` or similar harness
is sufficient. The goal is to have a repeatable test command that can run in CI
from day one. Before writing extensive tests, add code coverage tracking to this
tester and place a coverage badge in the README so progress is visible. Add a CI
status badge as soon as the workflow is active so everyone can see if the build
is passing.

Keep dependencies slim by declaring them in `pyproject.toml`. List optional
development tools under `[project.optional-dependencies.dev]` and install them
with `pip install -e .[dev]` so the agent can run tests and documentation builds
quickly.

Verify that the environment builds quickly. Agents have limited runtime, so a
slow `pip install` consumes precious time. Double-check the setup completes
without errors before moving on.

Agentic tools run without internet access during CI. This constraint yields
high-quality builds but means all dependencies must be vendored or cached ahead
of time. Spend effort paying down technical debt and tightening the test harness
before relying on automation; debugging the generated code directly is often
unproductive.

## 6. Fix Build Tests

After creating the minimal tester, run `pytest` locally and resolve any failures
before moving on. Getting the build to pass early confirms that the test harness
is wired correctly and prevents unexpected issues later in CI.

## 7. GitHub Workflow and Linting

Configure a GitHub Actions workflow that runs the tests and a linter
automatically. Automated linting might use `flake8`, `black`, or another tool of
choice. The workflow should fail if either lint or tests fail. Include the
`staging` branch in the workflow triggers so tests run before merging to `main`.

Add structured JSON logs behind a feature flag so you can turn them on only when
debugging. Consider shadow deployments that diff each build against the last
stable release, and run a triage bot after merges to surface new exceptions.

## 8. Achieve Adequate Test Coverage

Before building major features, write tests until coverage reaches at least the
70% range. This ensures a solid foundation and reduces regressions as the
project evolves.

At 50%, 60%, and 70% coverage, pause for a quick bug hunt. Ask the agent to rank
uncovered lines by risk and patch the worst offenders. Mutation testing can
highlight logic the tests still miss. Use property-based fuzz tests alongside
your unit tests so agents do not overlook edge cases as they refactor.

## 9. Add New Features Last

Only once automated linting and tests are in place—and coverage is consistently
in the 70s—should development of new features begin. Maintain the habit of
adding tests for new functionality as you go so coverage stays high.

Following this sequence encourages disciplined, agent-friendly development
across all OpenBrand repositories.

Merge only after GitHub Actions reports a green check mark. Forcing through a
failing build wastes time and leads to additional cleanup.

As you iterate on a project, keep improvements small and frequent. Automated
checks should catch issues early so adjustments can happen without disrupting
ongoing work. Update the main `README.md` regularly so new contributors always
have accurate instructions. This approach keeps the codebase healthy while
development progresses.

## 10. Close the Feedback Loop

Once tests, coverage, and CI are stable, connect your pipeline to bug trackers,
customer support channels, and telemetry dashboards. Feed these signals back
into the agent so it can triage regressions and propose fixes automatically.

Next, review the [Contribution Guidelines](guidelines.md) and the
[CI and Testing Guide](ci-guide.md) to understand our standard workflow.

For a concrete example of these steps in action, browse the
[`sample_configs`](../sample_configs/README.md) directory in this repository. It
contains a minimal project with linting, tests, and a GitHub Actions workflow
that you can copy when starting a new repo.

## Example Prompts

Use these short messages when instructing Codex or another agent to follow the
steps above.

```
Add a LICENSE file containing "All Rights Reserved, OpenBrand." Commit it to main.
Create AGENTS.md with commit style guidelines and required test commands.
Set up a minimal pytest harness and add coverage and CI badges to the README.
Configure GitHub Actions to run flake8 and pytest on the staging branch.
Increase test coverage to at least 70% before adding new features.
```

Prompts should include the exact git diff and a list of paths the agent must not
touch. Set a cost cap so long generations abort rather than spiral.

## Agentic Coding Tips

- Start with small commits so automated agents can keep up. If you hit merge
  conflicts, you are likely moving too quickly.
- Keep build steps and development environments lightweight. Faster setup leads
  to quicker feedback from tests and linting.
- Large binary packages like `dlib` can dramatically increase build time. Long
  builds may exhaust GitHub Actions credits and cut into the agent's runtime.
  Prefer static builds where possible to keep CI lean.
- Make simple, incremental changes. When progress stalls, break work into even
  smaller commits.
- When tackling a large edit, write a TODO list with checkboxes and let the
  agent work down each item. If progress stalls, break the list into smaller
  tasks.
- Merge your staging branch into `main` frequently to avoid long-running
  branches that diverge.
- Adjust agent environments as needed, especially when modifying tests or CI/CD
  settings. If a branch becomes tangled, start over rather than force a
  difficult merge.
- Add tools like `ruff` to the agent configuration so they load during
  bootstrap.
- Use the `bootstrap-*.sh` helpers in `sample_configs` to set up offline
  environments quickly.
- Linting helps resolve conflicts, but watch for repeated pre-commit failures
  that bounce back and forth. Excessive reruns can exhaust the agent's runtime.
- Keep the pre-commit hooks local so they run without network access. This lets
  testers work offline if GitHub or Codex is unavailable.
- After the build finishes, most agentic platforms disable network access. Use
  mocks and offline data so tests pass without hitting real services.
- Favor boring code over clever abstractions. Stability beats elegance when
  agents are writing the patches.
- Snapshot the task description in each commit message so future agents can
  trace intent.
- Write every module as if it's the last time you'll see it; another agent may
  maintain it next month.
- Tag every green build and keep a simple revert script ready in case a rollout
  goes sideways.
- Zip the entire repository and upload it to O3 Pro. The service can generate
  targeted instructions for Codex when you need to fix a build or add a new
  feature.

## Stable Environments

Most agents only operate on the `main` branch and cannot switch to a different
environment if the setup breaks. Keep `pyproject.toml` valid so a fresh clone
can still run basic checks:

```
pre-commit run --all-files
flake8
pytest
pip-audit
```

When these commands pass locally you know the repository is ready for another
agent to continue working.
