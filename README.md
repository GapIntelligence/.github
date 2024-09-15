![OpenBrand](https://github.com/user-attachments/assets/cd96108a-f2ac-4e8f-af3b-68660b3c3b44)

# OpenBrand Internal Documentation

Welcome to the internal repository for OpenBrand. This document outlines the detailed structure, development processes, and key information to ensure smooth collaboration and adherence to company standards.

## Key Contacts

- **Greg Munves** - CEO
- **Kristopher Kubicki** - CTO
- **Jason Mick** - Technology Manager

For any issues or inquiries related to repository management or development, please contact the above personnel.

## Company Structure and Key Codebases

### Gap Intelligence
- **Primary Repositories**: GAPI (Gap API) layer, Gap Ecom layer
- **Language**: Mostly Ruby (legacy code with some deprecated repos)
- **Maintainer**: Tom Corelis
- **Notes**: Most old Ruby repos are deprecated, but active development continues on the GAPI and Gap Ecom layers.

### Deep.ad
- **Primary Repository**: Deep.ad Content Engine
- **AWS**: Operates on its own AWS accounts
- **Maintainer**: Huy "HT" Tong

### Competitive Promotion Report
- **Primary Components**: Main codebase, database processors, and schemas
- **Background**: Originally built by a third-party developer
- **Maintainer**: Bobby Mitchum

### Traqline
- **Primary Products**: HPOS, DurableIQ, SkuMetrix, FloorSight
- **Languages**: Various, with a majority in PHP
- **Maintainer**: Joshua Hill

## Development Standards

1. **Coding Standards**: All code should adhere to standard programming practices and be well-documented.
2. **Bots**: We use a range of bots, including subscriptions to Sweep.dev, Code Rabbit, and Amazon. Adding new bots requires prior approval.
3. **Workflows**: Code should use GitHub workflows, incorporate testing, and follow our CI/CD pipeline guidelines.
4. **Testing**: All code must pass tests before submitting a Pull Request (PR).
5. **Branching Strategy**:
   - PRs should be merged into a staging branch.
   - After verification, merge the staging branch into the main branch (avoid using “master” branches).
6. **CI/CD**: Repositories should be configured to include CI/CD processes, preferably with deployment to AWS. We are currently agnostic about IaaS tools.

## Repository Management

- **Approval Process**: All new repositories, including public ones, require approval through our helpdesk: [Helpdesk Portal](https://deepad.atlassian.net/jira/servicedesk/projects/GAPHELP/queues/custom/37).
- **Public Repositories**: Must be reviewed and approved prior to publishing.
- **Deprecated Repositories**: Focus on maintaining new and actively developed repositories rather than older, deprecated ones.

## Security and Access Control

- **Access Management**: Only authorized personnel should have access to sensitive codebases and documentation. Ensure your GitHub account is set up with the correct permissions.
- **Sensitive Data**: Follow company protocols for handling and storing sensitive information securely.

## Onboarding and Development Environment

1. **Onboarding**: New developers should be granted access by their team lead and familiarize themselves with our development and deployment guidelines.
2. **Development Tools**: Ensure you have the required tools, libraries, and access to repositories necessary for your work.
3. **Setting Up**: Refer to internal setup guides for configuring your local environment to match our production and staging setups.

## Compliance and Legal

- **Compliance Requirements**: Adhere to all company compliance rules, including data privacy standards and legal obligations regarding code and data handling.
- **Intellectual Property**: Respect all internal IP and proprietary technologies as outlined in your employment agreement.

## Troubleshooting and Support

- For support, contact your team lead or use the helpdesk for issues related to repository access, bug reports, or technical challenges.
- Refer to our internal wiki or Slack channels for immediate troubleshooting steps.

---

Thank you for your contributions to OpenBrand's ongoing success. Let’s keep our development standards high and continue delivering exceptional products!
