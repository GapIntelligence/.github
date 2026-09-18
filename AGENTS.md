Normal change flow: feature/fix branch -> staging -> main.  
Open feature, maintenance, dependency and agent PRs against staging; use a separate staging -> main promotion PR.  
Do not direct-push to integration or release branches or bypass lower-environment validation.  
Emergency exceptions require explicit authorization, evidence and reconciliation into staging.  
Read .github/CONTRIBUTING.md for the repository lane, review, validation and release requirements.  
