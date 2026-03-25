#!/usr/bin/env python3
"""Add measurements to domain YAML files."""
import re

# Domain 01 measurements - keyed by process number
MEASUREMENTS = {
    # Domain 1: Strategy & Governance
    "1.1.1": [
        {"id": "010101", "num": "M1", "name": "Mission Clarity Score", "what": "Employee understanding and alignment with enterprise mission", "why": "Unclear mission leads to strategic drift and disengagement", "how": "Annual survey score (1-10) on mission comprehension and relevance", "freq": "annually", "dir": "higher_is_better"},
        {"id": "010102", "num": "M2", "name": "Mission Review Cycle Adherence", "what": "Whether mission review occurs within planned cadence", "why": "Ensures mission stays relevant as markets evolve", "how": "Binary (1=on schedule, 0=overdue) tracked quarterly", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.1.2": [
        {"id": "010201", "num": "M1", "name": "Values Awareness Rate", "what": "Percentage of employees who can articulate core values", "why": "Values only drive behaviour when known and understood", "how": "Survey respondents correctly identifying values / Total respondents × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "010202", "num": "M2", "name": "Values-Behaviour Alignment Score", "what": "Degree to which observed behaviours reflect stated values", "why": "Gap between stated and lived values erodes culture and trust", "how": "360-degree assessment average score on values alignment (1-10)", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.1.3": [
        {"id": "010301", "num": "M1", "name": "Vision Refresh Timeliness", "what": "Whether vision is reviewed and refreshed on schedule", "why": "Stale vision leads to strategic misalignment with market reality", "how": "Days since last vision review vs planned review cycle (variance in days)", "freq": "annually", "dir": "lower_is_better"},
        {"id": "010302", "num": "M2", "name": "Strategic Ambition Stretch Ratio", "what": "Ratio of vision targets to current performance baseline", "why": "Ensures vision is aspirational enough to drive transformation", "how": "Vision target metric / Current baseline metric", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.1.4": [
        {"id": "010401", "num": "M1", "name": "Vision Communication Reach", "what": "Percentage of workforce who received vision communications", "why": "Vision only drives alignment when broadly communicated", "how": "Employees reached by vision communications / Total headcount × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "010402", "num": "M2", "name": "Vision Comprehension Rate", "what": "Percentage of employees who can articulate the strategic vision", "why": "Receiving communications does not guarantee understanding", "how": "Pulse survey correct responses / Total respondents × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.1.5": [
        {"id": "010501", "num": "M1", "name": "Business Concept Review Completion Rate", "what": "Whether periodic reviews are completed on schedule", "why": "Ensures the business concept remains relevant", "how": "Reviews completed on time / Reviews scheduled × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "010502", "num": "M2", "name": "Market Signal Response Time", "what": "Days between significant market shift and triggered review", "why": "Slow response to market changes risks competitive disadvantage", "how": "Review trigger date − market event identification date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.2.1": [
        {"id": "010601", "num": "M1", "name": "Environmental Scan Coverage", "what": "Number of external domains systematically analysed", "why": "Blind spots in environmental scanning lead to strategic surprises", "how": "Domains covered (political, economic, social, tech, legal, environmental) / 6 × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "010602", "num": "M2", "name": "Insight Freshness", "what": "Age of the most recent market analysis deliverable", "why": "Stale analysis leads to decisions based on outdated information", "how": "Current date − latest analysis publication date (calendar days)", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "1.2.2": [
        {"id": "010701", "num": "M1", "name": "Capability Gap Identification Rate", "what": "Percentage of strategic capabilities assessed for readiness", "why": "Unidentified gaps delay strategy execution", "how": "Capabilities assessed / Total strategic capabilities × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "010702", "num": "M2", "name": "Readiness Assessment Cycle Time", "what": "Days to complete a full capability readiness assessment", "why": "Faster assessments enable more responsive strategic planning", "how": "Assessment completion date − assessment start date (business days)", "freq": "annually", "dir": "lower_is_better"},
    ],
    "1.2.3": [
        {"id": "010801", "num": "M1", "name": "Strategic Options Evaluated", "what": "Number of distinct strategic options formally evaluated per cycle", "why": "Evaluating too few options increases risk of suboptimal strategy", "how": "Count of formally evaluated strategic options per planning cycle", "freq": "annually", "dir": "higher_is_better"},
        {"id": "010802", "num": "M2", "name": "Scenario Model Accuracy", "what": "Variance between scenario projections and actual outcomes", "why": "Accurate models improve confidence in strategic decisions", "how": "|Projected outcome − Actual outcome| / Actual outcome × 100", "freq": "annually", "dir": "lower_is_better"},
    ],
    "1.2.4": [
        {"id": "010901", "num": "M1", "name": "Strategic Decision Cycle Time", "what": "Days from option presentation to formal strategic commitment", "why": "Delayed decisions create uncertainty and slow execution", "how": "Commitment date − options presentation date (calendar days)", "freq": "annually", "dir": "lower_is_better"},
        {"id": "010902", "num": "M2", "name": "Stakeholder Alignment Score", "what": "Degree of leadership alignment on chosen strategic direction", "why": "Misalignment at the top cascades into execution dysfunction", "how": "Leadership survey agreement score on strategic direction (1-10)", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.2.5": [
        {"id": "011001", "num": "M1", "name": "Strategic Plan Completion Rate", "what": "Percentage of strategic plan sections fully documented", "why": "Incomplete plans lead to ambiguous execution mandates", "how": "Completed sections / Required sections × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "011002", "num": "M2", "name": "Plan Formalisation Cycle Time", "what": "Days from strategic decision to approved documented plan", "why": "Delays in documentation slow cascade and execution start", "how": "Plan approval date − strategic decision date (business days)", "freq": "annually", "dir": "lower_is_better"},
    ],
    "1.2.6": [
        {"id": "011101", "num": "M1", "name": "Strategy Cascade Completion Rate", "what": "Percentage of organisational units with localised strategic plans", "why": "Uncascaded strategy remains an executive abstraction", "how": "OUs with localised plans / Total OUs × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "011102", "num": "M2", "name": "Cascade Acknowledgement Rate", "what": "Percentage of unit leaders who acknowledged and confirmed understanding", "why": "Acknowledgement is the minimum bar for cascade effectiveness", "how": "Leaders confirming receipt and understanding / Total unit leaders × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.2.7": [
        {"id": "011201", "num": "M1", "name": "Assumption Monitoring Coverage", "what": "Percentage of strategic assumptions with active monitoring", "why": "Unmonitored assumptions become invisible risks", "how": "Assumptions with active monitors / Total documented assumptions × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "011202", "num": "M2", "name": "Assumption Breach Alert Latency", "what": "Time between assumption breach and alert to leadership", "why": "Faster alerts enable faster strategic response", "how": "Alert timestamp − breach detection timestamp (hours)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.3.1": [
        {"id": "011301", "num": "M1", "name": "Planning Calendar Adherence", "what": "Percentage of planning milestones completed on schedule", "why": "Missed milestones cascade delays through the planning process", "how": "Milestones completed on time / Total milestones × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "011302", "num": "M2", "name": "Planning Cycle Duration", "what": "Total elapsed days for the annual strategic planning cycle", "why": "Overly long cycles reduce agility and relevance", "how": "Cycle end date − cycle start date (calendar days)", "freq": "annually", "dir": "lower_is_better"},
    ],
    "1.3.2": [
        {"id": "011401", "num": "M1", "name": "Cross-Functional Input Completion Rate", "what": "Percentage of functions providing input on time", "why": "Missing inputs create blind spots in strategic plans", "how": "Functions submitting on time / Functions requested × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "011402", "num": "M2", "name": "Input Quality Score", "what": "Average quality rating of cross-functional contributions", "why": "Low-quality inputs degrade strategic plan quality", "how": "Average quality rating from planning team reviewers (1-10)", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.3.3": [
        {"id": "011501", "num": "M1", "name": "Review Session Completion Rate", "what": "Percentage of scheduled strategic reviews actually held", "why": "Skipped reviews reduce strategic oversight", "how": "Reviews held / Reviews scheduled × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "011502", "num": "M2", "name": "Review Action Item Closure Rate", "what": "Percentage of review action items completed by due date", "why": "Open action items undermine review effectiveness", "how": "Actions closed on time / Total actions assigned × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.3.4": [
        {"id": "011601", "num": "M1", "name": "Strategy-to-Initiative Translation Rate", "what": "Percentage of strategic objectives linked to funded initiatives", "why": "Untranslated strategies never reach execution", "how": "Objectives with linked initiatives / Total strategic objectives × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "011602", "num": "M2", "name": "Execution Readiness Score", "what": "Average readiness rating of initiatives entering execution", "why": "Poorly prepared initiatives fail during delivery", "how": "Average readiness checklist score across new initiatives (0-100%)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.3.5": [
        {"id": "011701", "num": "M1", "name": "Planning Horizon Coverage", "what": "Number of concurrent planning horizons actively maintained", "why": "Single-horizon planning misses long-term opportunities and threats", "how": "Count of actively maintained planning horizons", "freq": "annually", "dir": "higher_is_better"},
        {"id": "011702", "num": "M2", "name": "Cross-Horizon Alignment Score", "what": "Degree of consistency across short, medium, and long-term plans", "why": "Misaligned horizons create conflicting priorities", "how": "Assessment score from planning review (1-10)", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.4.1": [
        {"id": "011801", "num": "M1", "name": "Board Meeting Cadence Adherence", "what": "Percentage of board meetings held on schedule", "why": "Missed meetings impair governance oversight", "how": "Meetings held on schedule / Meetings planned × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "011802", "num": "M2", "name": "Board Pack Timeliness", "what": "Days before meeting that board packs are distributed", "why": "Late distribution reduces board preparation quality", "how": "Meeting date − pack distribution date (calendar days)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.4.2": [
        {"id": "011901", "num": "M1", "name": "Board Pack Completeness Score", "what": "Percentage of required sections included in board packs", "why": "Incomplete packs impair board decision-making", "how": "Sections included / Required sections × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "011902", "num": "M2", "name": "Board Pack Preparation Cycle Time", "what": "Days to assemble and approve the board pack", "why": "Shorter cycles allow more current information in packs", "how": "Approval date − assembly start date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.4.3": [
        {"id": "012001", "num": "M1", "name": "Governance Obligation Compliance Rate", "what": "Percentage of fiduciary and regulatory obligations met on time", "why": "Non-compliance creates legal, financial, and reputational risk", "how": "Obligations met on time / Total obligations due × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "012002", "num": "M2", "name": "Regulatory Filing Timeliness", "what": "Average days before deadline that regulatory filings are submitted", "why": "Cutting it close increases risk of missed deadlines", "how": "Average (filing deadline − submission date) across all filings (calendar days)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.4.4": [
        {"id": "012101", "num": "M1", "name": "Stakeholder Communication Timeliness", "what": "Percentage of stakeholder communications delivered on schedule", "why": "Late communications erode stakeholder confidence", "how": "Communications delivered on time / Planned communications × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "012102", "num": "M2", "name": "Stakeholder Satisfaction Score", "what": "Stakeholder satisfaction with quality and transparency of communications", "why": "Low satisfaction signals trust and transparency gaps", "how": "Average stakeholder survey score (1-10)", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.4.5": [
        {"id": "012201", "num": "M1", "name": "Policy Currency Rate", "what": "Percentage of governance policies reviewed within their review cycle", "why": "Outdated policies create compliance gaps", "how": "Policies reviewed on schedule / Total policies × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "012202", "num": "M2", "name": "Policy Gap Closure Time", "what": "Average days to close identified policy gaps", "why": "Open gaps represent governance exposure", "how": "Average (gap closure date − gap identification date) (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.5.1": [
        {"id": "012301", "num": "M1", "name": "KPI Definition Coverage", "what": "Percentage of strategic objectives with defined KPIs", "why": "Unmeasured objectives cannot be managed", "how": "Objectives with KPIs / Total strategic objectives × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "012302", "num": "M2", "name": "KPI Target Setting Rate", "what": "Percentage of KPIs with approved targets and thresholds", "why": "KPIs without targets provide data but not accountability", "how": "KPIs with targets / Total KPIs × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.5.2": [
        {"id": "012401", "num": "M1", "name": "Data Collection Automation Rate", "what": "Percentage of KPIs with automated data collection", "why": "Manual collection is slow, error-prone, and unsustainable", "how": "KPIs with automated feeds / Total KPIs × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "012402", "num": "M2", "name": "Data Freshness", "what": "Average lag between event occurrence and data availability", "why": "Stale data leads to delayed decisions", "how": "Average (data availability timestamp − event timestamp) in hours", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "1.5.3": [
        {"id": "012501", "num": "M1", "name": "Variance Detection Rate", "what": "Percentage of material variances identified before management review", "why": "Proactive detection enables faster corrective action", "how": "Variances detected proactively / Total material variances × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "012502", "num": "M2", "name": "Trend Analysis Delivery Timeliness", "what": "Days after period close that trend analysis is available", "why": "Late analysis reduces actionability of insights", "how": "Analysis delivery date − period close date (business days)", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "1.5.4": [
        {"id": "012601", "num": "M1", "name": "Performance Review Cadence Adherence", "what": "Percentage of scheduled performance reviews completed on time", "why": "Skipped reviews reduce accountability and strategic oversight", "how": "Reviews completed on schedule / Reviews planned × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "012602", "num": "M2", "name": "Review Decision Cycle Time", "what": "Days from review meeting to documented decisions and actions", "why": "Slow follow-through undermines review value", "how": "Decision documentation date − review meeting date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.5.5": [
        {"id": "012701", "num": "M1", "name": "Corrective Action Completion Rate", "what": "Percentage of corrective actions completed by target date", "why": "Incomplete corrective actions allow performance issues to persist", "how": "Actions completed on time / Total corrective actions × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "012702", "num": "M2", "name": "Intervention Effectiveness Rate", "what": "Percentage of interventions that achieved target improvement", "why": "Ineffective interventions waste resources without improving performance", "how": "Interventions achieving target / Total interventions × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.5.6": [
        {"id": "012801", "num": "M1", "name": "Performance Report Timeliness", "what": "Days after period close that governance reports are delivered", "why": "Late reports reduce board and stakeholder oversight quality", "how": "Report delivery date − period close date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "012802", "num": "M2", "name": "Report Accuracy Rate", "what": "Percentage of reports requiring no post-delivery corrections", "why": "Corrections erode credibility of performance reporting", "how": "Reports without corrections / Total reports delivered × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.6.1": [
        {"id": "012901", "num": "M1", "name": "Partner Pipeline Volume", "what": "Number of potential partners under active evaluation", "why": "Healthy pipeline ensures access to future strategic partnerships", "how": "Count of partners in evaluation pipeline", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "012902", "num": "M2", "name": "Partner Evaluation Cycle Time", "what": "Days from initial identification to go/no-go decision", "why": "Slow evaluation delays strategic partnership benefits", "how": "Decision date − identification date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.6.2": [
        {"id": "013001", "num": "M1", "name": "Partnership Agreement Cycle Time", "what": "Days from negotiation start to signed agreement", "why": "Protracted negotiations delay value realisation", "how": "Signature date − negotiation start date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "013002", "num": "M2", "name": "Partnership Terms Compliance Rate", "what": "Percentage of partnership terms successfully negotiated per requirements", "why": "Ensures agreements protect enterprise interests", "how": "Required terms included / Total required terms × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.6.3": [
        {"id": "013101", "num": "M1", "name": "Partner Satisfaction Score", "what": "Partner-reported satisfaction with the relationship", "why": "Dissatisfied partners disengage or underperform", "how": "Average partner survey score (1-10)", "freq": "annually", "dir": "higher_is_better"},
        {"id": "013102", "num": "M2", "name": "Partner Commitment Fulfilment Rate", "what": "Percentage of mutual commitments fulfilled on time", "why": "Unfulfilled commitments erode partnership trust", "how": "Commitments fulfilled on time / Total commitments × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.6.4": [
        {"id": "013201", "num": "M1", "name": "Partner ROI", "what": "Return on investment from strategic partnerships", "why": "Ensures partnerships deliver measurable value", "how": "Value generated from partnership / Investment in partnership × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "013202", "num": "M2", "name": "Partner Value Assessment Completion Rate", "what": "Percentage of partners with completed value assessments", "why": "Unassessed partnerships may consume resources without adequate return", "how": "Partners with completed assessments / Total active partners × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.6.5": [
        {"id": "013301", "num": "M1", "name": "Ecosystem Coordination Effectiveness", "what": "Rating of cross-partner coordination quality", "why": "Poor coordination reduces ecosystem synergy value", "how": "Coordination effectiveness rating from partner surveys (1-10)", "freq": "annually", "dir": "higher_is_better"},
        {"id": "013302", "num": "M2", "name": "Information Sharing Timeliness", "what": "Average time for critical information to reach all ecosystem partners", "why": "Delayed sharing reduces partnership responsiveness", "how": "Average distribution time for priority communications (hours)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.7.1": [
        {"id": "013401", "num": "M1", "name": "Operating Model Currency", "what": "Whether the operating model documentation is current", "why": "Outdated documentation leads to operating model drift", "how": "Days since last operating model review and update", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "013402", "num": "M2", "name": "Operating Model Drift Score", "what": "Degree of divergence between documented and actual operating model", "why": "Drift indicates governance gaps and undocumented changes", "how": "Audit findings of undocumented deviations (count)", "freq": "annually", "dir": "lower_is_better"},
    ],
    "1.7.2": [
        {"id": "013501", "num": "M1", "name": "Domain Map Completeness", "what": "Percentage of enterprise capabilities mapped and documented", "why": "Gaps in the capability map create strategic blind spots", "how": "Capabilities documented / Total identified capabilities × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "013502", "num": "M2", "name": "Capability Map Update Frequency", "what": "Average days between capability map updates", "why": "Infrequent updates reduce map relevance", "how": "Average days between consecutive map updates", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.7.3": [
        {"id": "013601", "num": "M1", "name": "Blended Workforce Design Maturity", "what": "Maturity rating of the human-agent workforce architecture", "why": "Immature design leads to suboptimal agent deployment", "how": "Maturity assessment score against framework benchmarks (1-5)", "freq": "annually", "dir": "higher_is_better"},
        {"id": "013602", "num": "M2", "name": "Workforce Composition Target Adherence", "what": "Deviation from planned human-agent workforce ratios", "why": "Large deviations indicate poor workforce planning or uncontrolled growth", "how": "|Actual ratio − Target ratio| / Target ratio × 100", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.7.4": [
        {"id": "013701", "num": "M1", "name": "Framework Adoption Rate", "what": "Percentage of applicable organisational units using the adopted framework", "why": "Partial adoption reduces framework value and creates inconsistency", "how": "OUs using framework / Applicable OUs × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "013702", "num": "M2", "name": "Framework Version Currency", "what": "Whether the enterprise is on the current framework version", "why": "Outdated versions miss improvements and create compatibility issues", "how": "Current version in use / Latest available version", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.7.5": [
        {"id": "013801", "num": "M1", "name": "Operating Model Maturity Score", "what": "Overall maturity rating from the latest assessment", "why": "Tracks progress in operating model sophistication", "how": "Maturity assessment aggregate score (1-5)", "freq": "annually", "dir": "higher_is_better"},
        {"id": "013802", "num": "M2", "name": "Assessment Recommendation Closure Rate", "what": "Percentage of assessment recommendations implemented", "why": "Unimplemented recommendations indicate stalled improvement", "how": "Recommendations implemented / Total recommendations × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.8.1": [
        {"id": "013901", "num": "M1", "name": "Transformation Opportunity Pipeline", "what": "Number of transformation opportunities under evaluation", "why": "Healthy pipeline ensures continuous improvement momentum", "how": "Count of opportunities in evaluation", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "013902", "num": "M2", "name": "Opportunity Prioritisation Cycle Time", "what": "Days from opportunity identification to prioritisation decision", "why": "Slow prioritisation delays transformation value", "how": "Decision date − identification date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.8.2": [
        {"id": "014001", "num": "M1", "name": "Roadmap Completeness Score", "what": "Percentage of transformation programmes with complete roadmaps", "why": "Incomplete roadmaps lead to execution confusion", "how": "Programmes with complete roadmaps / Total programmes × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "014002", "num": "M2", "name": "Programme Design Cycle Time", "what": "Days from programme approval to completed roadmap", "why": "Slow design delays transformation execution", "how": "Roadmap completion date − programme approval date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.8.3": [
        {"id": "014101", "num": "M1", "name": "Change Readiness Score", "what": "Average organisational readiness rating for active transformations", "why": "Low readiness predicts change failure and resistance", "how": "Average readiness survey score across affected populations (1-10)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "014102", "num": "M2", "name": "Stakeholder Engagement Rate", "what": "Percentage of identified stakeholders actively engaged in change", "why": "Disengaged stakeholders become blockers", "how": "Stakeholders actively participating / Total identified stakeholders × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.8.4": [
        {"id": "014201", "num": "M1", "name": "Transformation Milestone Adherence", "what": "Percentage of transformation milestones achieved on schedule", "why": "Missed milestones signal programme health issues", "how": "Milestones on time / Total milestones × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "014202", "num": "M2", "name": "Transformation Budget Variance", "what": "Percentage deviation from approved transformation budget", "why": "Budget overruns threaten programme viability", "how": "(Actual spend − Budget) / Budget × 100", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "1.8.5": [
        {"id": "014301", "num": "M1", "name": "Benefit Realisation Rate", "what": "Percentage of planned transformation benefits actually realised", "why": "Unrealised benefits represent wasted transformation investment", "how": "Benefits realised / Benefits planned × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "014302", "num": "M2", "name": "Outcome Measurement Timeliness", "what": "Days after milestone to completed outcome measurement", "why": "Delayed measurement reduces ability to course-correct", "how": "Measurement completion date − milestone date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "1.8.6": [
        {"id": "014401", "num": "M1", "name": "New Way of Working Adoption Rate", "what": "Percentage of target population consistently using new processes", "why": "Low adoption means transformation hasn't stuck", "how": "Users consistently using new process / Target population × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "014402", "num": "M2", "name": "Regression Incident Count", "what": "Number of instances where teams reverted to old ways of working", "why": "Regressions indicate insufficient embedding of change", "how": "Count of documented regression incidents per period", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "1.9.1": [
        {"id": "014501", "num": "M1", "name": "Risk Appetite Statement Currency", "what": "Whether the risk appetite statement has been reviewed within cycle", "why": "Outdated risk appetite may not reflect current strategic context", "how": "Days since last board-approved risk appetite review", "freq": "annually", "dir": "lower_is_better"},
        {"id": "014502", "num": "M2", "name": "Risk Appetite Awareness Rate", "what": "Percentage of senior leaders who can articulate risk appetite", "why": "Unknown risk appetite leads to inconsistent risk-taking", "how": "Leaders correctly describing appetite / Total senior leaders × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "1.9.2": [
        {"id": "014601", "num": "M1", "name": "Enterprise Risk Register Completeness", "what": "Percentage of identified risk categories with assessed risks", "why": "Gaps in the register represent unmanaged exposure", "how": "Categories with assessed risks / Total risk categories × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "014602", "num": "M2", "name": "Risk Assessment Refresh Rate", "what": "Percentage of enterprise risks reassessed within their review cycle", "why": "Stale assessments may not reflect current risk levels", "how": "Risks reassessed on schedule / Total risks × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.9.3": [
        {"id": "014701", "num": "M1", "name": "Risk Monitoring Uptime", "what": "Percentage of time continuous risk monitoring is operational", "why": "Monitoring downtime creates blind spots for emerging risks", "how": "Monitoring uptime hours / Total hours × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "014702", "num": "M2", "name": "Emerging Risk Detection Rate", "what": "Number of emerging risks identified through monitoring per quarter", "why": "Active monitoring should continuously surface new risks", "how": "Count of new risks identified through monitoring systems", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.9.4": [
        {"id": "014801", "num": "M1", "name": "Risk Report Delivery Timeliness", "what": "Days before governance meeting that risk reports are delivered", "why": "Late reports reduce board preparation and oversight quality", "how": "Meeting date − report delivery date (calendar days)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "014802", "num": "M2", "name": "Risk Report Completeness", "what": "Percentage of required risk dimensions covered in reports", "why": "Incomplete reporting creates governance blind spots", "how": "Dimensions covered / Required dimensions × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.9.5": [
        {"id": "014901", "num": "M1", "name": "Cross-Domain Risk Response Coordination Rate", "what": "Percentage of multi-domain risks with coordinated response plans", "why": "Uncoordinated responses to cross-cutting risks reduce effectiveness", "how": "Cross-domain risks with coordinated plans / Total cross-domain risks × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "014902", "num": "M2", "name": "Risk Action Completion Rate", "what": "Percentage of risk response actions completed by target date", "why": "Incomplete actions leave residual risk exposure", "how": "Actions completed on time / Total risk actions × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.10.1": [
        {"id": "015001", "num": "M1", "name": "M&A Target Pipeline Volume", "what": "Number of acquisition or divestiture targets under evaluation", "why": "Healthy pipeline supports strategic portfolio management", "how": "Count of targets in active evaluation", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "015002", "num": "M2", "name": "Target Screening Efficiency", "what": "Ratio of targets screened to targets advancing to due diligence", "why": "Indicates quality of initial screening criteria", "how": "Targets advancing / Targets screened × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.10.2": [
        {"id": "015101", "num": "M1", "name": "Due Diligence Completion Rate", "what": "Percentage of due diligence workstreams completed on schedule", "why": "Incomplete diligence increases transaction risk", "how": "Workstreams completed on time / Total workstreams × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "015102", "num": "M2", "name": "Critical Issue Discovery Rate", "what": "Number of material issues discovered during due diligence", "why": "Effective diligence surfaces deal-breaking issues before close", "how": "Count of material issues identified", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.10.3": [
        {"id": "015201", "num": "M1", "name": "Transaction Negotiation Cycle Time", "what": "Days from term sheet to signed agreement", "why": "Protracted negotiations increase deal risk and cost", "how": "Signing date − term sheet date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "015202", "num": "M2", "name": "Deal Term Achievement Rate", "what": "Percentage of priority deal terms achieved in final agreement", "why": "Measures negotiation effectiveness", "how": "Priority terms achieved / Total priority terms × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.10.4": [
        {"id": "015301", "num": "M1", "name": "Integration Milestone Achievement Rate", "what": "Percentage of integration milestones completed on schedule", "why": "Delayed integration erodes acquisition value", "how": "Milestones on time / Total milestones × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "015302", "num": "M2", "name": "Synergy Capture Rate", "what": "Percentage of planned synergies realised within target timeframe", "why": "Unrealised synergies undermine deal thesis", "how": "Synergies realised / Planned synergies × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "1.10.5": [
        {"id": "015401", "num": "M1", "name": "Divestiture Execution Timeliness", "what": "Whether divestiture completes within planned timeline", "why": "Delays increase complexity and reduce proceeds", "how": "Actual completion date − planned completion date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "015402", "num": "M2", "name": "Separation Completeness Rate", "what": "Percentage of separation activities completed by close", "why": "Incomplete separation creates ongoing entanglements", "how": "Activities completed / Total separation activities × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],

    # Domain 2: Product/Service & Innovation
    "2.1.1": [
        {"id": "020101", "num": "M1", "name": "Offering Vision Clarity Score", "what": "Stakeholder understanding of offering vision and positioning", "why": "Unclear vision leads to misaligned product decisions", "how": "Stakeholder survey score on vision clarity (1-10)", "freq": "annually", "dir": "higher_is_better"},
        {"id": "020102", "num": "M2", "name": "Positioning Differentiation Score", "what": "Degree of perceived differentiation from competitors", "why": "Weak differentiation reduces pricing power and market share", "how": "Customer perception survey differentiation score (1-10)", "freq": "annually", "dir": "higher_is_better"},
    ],
    "2.1.2": [
        {"id": "020201", "num": "M1", "name": "Market Opportunity Coverage", "what": "Percentage of addressable market segments evaluated", "why": "Unevaluated segments represent missed revenue opportunities", "how": "Segments evaluated / Total identified segments × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "020202", "num": "M2", "name": "Whitespace Identification Rate", "what": "Number of new market whitespace opportunities identified per quarter", "why": "Continuous identification fuels growth strategy", "how": "Count of new whitespace opportunities documented", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.1.3": [
        {"id": "020301", "num": "M1", "name": "Portfolio Balance Score", "what": "Distribution of investments across innovation horizons", "why": "Imbalanced portfolios create growth gaps or overexposure to risk", "how": "Deviation from target horizon allocation (percentage points)", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "020302", "num": "M2", "name": "Portfolio Alignment to Strategy", "what": "Percentage of portfolio investments linked to strategic priorities", "why": "Unlinked investments represent strategic drift", "how": "Investments linked to priorities / Total investments × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.1.4": [
        {"id": "020401", "num": "M1", "name": "Investment Criteria Application Rate", "what": "Percentage of funding decisions evaluated against defined criteria", "why": "Ad-hoc funding decisions reduce portfolio quality", "how": "Decisions using criteria / Total funding decisions × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "020402", "num": "M2", "name": "Investment Decision Cycle Time", "what": "Days from funding request to approved/rejected decision", "why": "Slow decisions delay time-to-market", "how": "Decision date − request date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.1.5": [
        {"id": "020501", "num": "M1", "name": "Portfolio Review Cadence Adherence", "what": "Percentage of scheduled portfolio reviews completed on time", "why": "Missed reviews allow underperforming offerings to persist", "how": "Reviews completed on time / Reviews scheduled × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "020502", "num": "M2", "name": "Rationalisation Actions Taken", "what": "Number of keep/kill/invest decisions made per review cycle", "why": "Active rationalisation ensures portfolio health", "how": "Count of formal portfolio decisions per review", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.1.6": [
        {"id": "020601", "num": "M1", "name": "Roadmap-Strategy Alignment Score", "what": "Percentage of roadmap items traceable to strategic objectives", "why": "Misaligned roadmaps waste development resources", "how": "Roadmap items with strategic links / Total roadmap items × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "020602", "num": "M2", "name": "Misalignment Resolution Time", "what": "Days to resolve identified roadmap-strategy misalignments", "why": "Unresolved misalignments compound over time", "how": "Average resolution date − identification date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.2.1": [
        {"id": "020701", "num": "M1", "name": "Customer Insight Volume", "what": "Number of customer needs and pain points documented per period", "why": "Rich insight volume fuels better product decisions", "how": "Count of documented customer insights", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "020702", "num": "M2", "name": "Insight Source Diversity", "what": "Number of distinct channels contributing customer insights", "why": "Single-source insights create bias", "how": "Count of unique channels providing insights", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.2.2": [
        {"id": "020801", "num": "M1", "name": "Concept Generation Rate", "what": "Number of new offering concepts generated per quarter", "why": "Higher volume increases chance of breakthrough ideas", "how": "Count of new concepts documented", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "020802", "num": "M2", "name": "Concept Advancement Rate", "what": "Percentage of generated concepts advancing to testing", "why": "Too few advancing suggests weak ideation; too many suggests weak filtering", "how": "Concepts advancing to testing / Total concepts generated × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.2.3": [
        {"id": "020901", "num": "M1", "name": "Prototype Cycle Time", "what": "Days from concept approval to testable prototype", "why": "Faster prototyping accelerates learning and time-to-market", "how": "Prototype delivery date − concept approval date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "020902", "num": "M2", "name": "Concept Test Completion Rate", "what": "Percentage of prototypes completing user testing within planned timeline", "why": "Delayed testing slows validation and decision-making", "how": "Tests completed on time / Total tests planned × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.2.4": [
        {"id": "021001", "num": "M1", "name": "Demand Validation Confidence Score", "what": "Statistical confidence level of market demand validation", "why": "Low confidence increases launch risk", "how": "Confidence level from demand analysis (percentage)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "021002", "num": "M2", "name": "Willingness-to-Pay Validation Rate", "what": "Percentage of new concepts with validated pricing", "why": "Unvalidated pricing risks revenue underperformance", "how": "Concepts with pricing validation / Total concepts in pipeline × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.2.5": [
        {"id": "021101", "num": "M1", "name": "Business Case Approval Rate", "what": "Percentage of submitted business cases approved", "why": "Very low rates suggest poor case quality; very high may indicate insufficient rigour", "how": "Cases approved / Cases submitted × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "021102", "num": "M2", "name": "Business Case Accuracy", "what": "Variance between business case projections and actual outcomes", "why": "Accurate cases build investment confidence", "how": "|Projected outcome − Actual outcome| / Projected outcome × 100", "freq": "annually", "dir": "lower_is_better"},
    ],
    "2.3.1": [
        {"id": "021201", "num": "M1", "name": "Requirements Stability Index", "what": "Percentage of requirements unchanged after baseline approval", "why": "Frequent changes indicate unclear scope and increase delivery risk", "how": "Unchanged requirements / Total baselined requirements × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "021202", "num": "M2", "name": "Requirements Completeness Score", "what": "Percentage of requirements with full acceptance criteria", "why": "Incomplete requirements lead to scope disputes and rework", "how": "Requirements with acceptance criteria / Total requirements × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "2.3.2": [
        {"id": "021301", "num": "M1", "name": "Design Review Pass Rate", "what": "Percentage of designs passing review on first submission", "why": "Low first-pass rates indicate design quality or communication issues", "how": "Designs approved first time / Total designs reviewed × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "021302", "num": "M2", "name": "Specification Completeness", "what": "Percentage of design specifications fully documented", "why": "Incomplete specs lead to implementation ambiguity", "how": "Complete specification sections / Total required sections × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "2.3.3": [
        {"id": "021401", "num": "M1", "name": "Development Velocity", "what": "Rate of development output per sprint or cycle", "why": "Tracks development team productivity and capacity utilisation", "how": "Story points completed / Sprint duration (or equivalent output measure)", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "021402", "num": "M2", "name": "Build Cycle Time", "what": "Average elapsed days from development start to build completion", "why": "Shorter cycles enable faster iteration and feedback", "how": "Build completion date − development start date (business days)", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "2.3.4": [
        {"id": "021501", "num": "M1", "name": "Defect Escape Rate", "what": "Percentage of defects found post-release vs total defects", "why": "High escape rates indicate insufficient testing", "how": "Post-release defects / Total defects found × 100", "freq": "monthly", "dir": "lower_is_better"},
        {"id": "021502", "num": "M2", "name": "Test Coverage", "what": "Percentage of requirements covered by test cases", "why": "Low coverage leaves untested functionality at risk", "how": "Requirements with test cases / Total requirements × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "2.3.5": [
        {"id": "021601", "num": "M1", "name": "Configuration Accuracy Rate", "what": "Percentage of configurations delivered without errors", "why": "Configuration errors cause customer dissatisfaction and rework", "how": "Error-free configurations / Total configurations × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "021602", "num": "M2", "name": "Variant Proliferation Index", "what": "Ratio of active variants to planned variants", "why": "Uncontrolled proliferation increases complexity and cost", "how": "Active variants / Planned variants", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.3.6": [
        {"id": "021701", "num": "M1", "name": "Accessibility Compliance Rate", "what": "Percentage of offerings meeting accessibility standards", "why": "Non-compliance excludes users and creates legal risk", "how": "Offerings meeting standards / Total offerings × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "021702", "num": "M2", "name": "Usability Test Score", "what": "Average user satisfaction score from usability testing", "why": "Poor usability reduces adoption and increases support costs", "how": "Average System Usability Scale (SUS) score (0-100)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.4.1": [
        {"id": "021801", "num": "M1", "name": "Idea Submission Volume", "what": "Number of new ideas submitted per period", "why": "Low volume indicates weak innovation culture or intake friction", "how": "Count of ideas submitted", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "021802", "num": "M2", "name": "Idea Evaluation Cycle Time", "what": "Average days from idea submission to initial evaluation", "why": "Slow evaluation discourages future submissions", "how": "Evaluation date − submission date (business days)", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "2.4.2": [
        {"id": "021901", "num": "M1", "name": "Experiment Completion Rate", "what": "Percentage of designed experiments completed within planned timeline", "why": "Incomplete experiments waste resources and delay learning", "how": "Experiments completed on time / Total experiments planned × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "021902", "num": "M2", "name": "Experiment Learning Rate", "what": "Number of validated learnings produced per experiment", "why": "Experiments should produce actionable insights regardless of outcome", "how": "Documented validated learnings / Total completed experiments", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.4.3": [
        {"id": "022001", "num": "M1", "name": "Innovation Pipeline Health Score", "what": "Distribution of initiatives across innovation stages", "why": "Empty stages create future innovation gaps", "how": "Stages with adequate initiatives / Total stages × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "022002", "num": "M2", "name": "Stage-Gate Throughput Rate", "what": "Percentage of initiatives passing each stage gate", "why": "Very low or very high rates indicate gate calibration issues", "how": "Initiatives passing gate / Initiatives presented at gate × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.4.4": [
        {"id": "022101", "num": "M1", "name": "Innovation-to-Core Conversion Rate", "what": "Percentage of validated innovations successfully scaled", "why": "Low conversion wastes innovation investment", "how": "Innovations scaled / Validated innovations × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "022102", "num": "M2", "name": "Scaling Cycle Time", "what": "Days from scaling decision to full integration", "why": "Slow scaling delays revenue capture from innovations", "how": "Integration completion date − scaling decision date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.4.5": [
        {"id": "022201", "num": "M1", "name": "Innovation Culture Score", "what": "Employee perception of innovation culture and psychological safety", "why": "Weak culture suppresses idea generation and risk-taking", "how": "Innovation culture survey score (1-10)", "freq": "annually", "dir": "higher_is_better"},
        {"id": "022202", "num": "M2", "name": "Internal Entrepreneurship Participation Rate", "what": "Percentage of employees participating in innovation programmes", "why": "Broad participation increases innovation diversity", "how": "Employees participating / Total eligible employees × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "2.4.6": [
        {"id": "022301", "num": "M1", "name": "External Innovation Source Count", "what": "Number of active external innovation partnerships", "why": "Diverse external sources accelerate innovation", "how": "Count of active external partnerships contributing to innovation", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "022302", "num": "M2", "name": "External Innovation Contribution Rate", "what": "Percentage of innovations originating from external sources", "why": "Tracks open innovation effectiveness", "how": "Externally sourced innovations / Total innovations × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "2.5.1": [
        {"id": "022401", "num": "M1", "name": "R&D Strategy Alignment Score", "what": "Percentage of R&D programmes aligned to strategic priorities", "why": "Misaligned R&D wastes scarce research resources", "how": "Aligned programmes / Total R&D programmes × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "022402", "num": "M2", "name": "Research Priority Refresh Rate", "what": "Whether research priorities are reviewed within planned cadence", "why": "Stale priorities misallocate research effort", "how": "Days since last priority review vs planned review cycle", "freq": "annually", "dir": "lower_is_better"},
    ],
    "2.5.2": [
        {"id": "022501", "num": "M1", "name": "R&D Budget Utilisation Rate", "what": "Percentage of allocated R&D budget actually spent", "why": "Underspending signals execution problems; overspending signals poor planning", "how": "Actual R&D spend / Allocated budget × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "022502", "num": "M2", "name": "R&D Cost per Output", "what": "Average cost per research output (paper, patent, prototype)", "why": "Tracks R&D efficiency and productivity", "how": "Total R&D spend / Count of research outputs", "freq": "annually", "dir": "lower_is_better"},
    ],
    "2.5.3": [
        {"id": "022601", "num": "M1", "name": "Research Programme Milestone Adherence", "what": "Percentage of research milestones achieved on schedule", "why": "Missed milestones delay technology readiness", "how": "Milestones on time / Total milestones × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "022602", "num": "M2", "name": "Research Output Volume", "what": "Number of research outputs produced per period", "why": "Tracks research productivity", "how": "Count of papers, patents filed, and prototypes produced", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.5.4": [
        {"id": "022701", "num": "M1", "name": "Technology Transfer Success Rate", "what": "Percentage of research outcomes successfully transferred to product teams", "why": "Untransferred research represents wasted investment", "how": "Outcomes transferred / Total transferable outcomes × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "022702", "num": "M2", "name": "Transfer Cycle Time", "what": "Days from research completion to product team handover", "why": "Slow transfer delays competitive advantage", "how": "Handover date − research completion date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.5.5": [
        {"id": "022801", "num": "M1", "name": "Technology Trend Coverage", "what": "Percentage of relevant technology domains under active monitoring", "why": "Gaps in monitoring create technology blind spots", "how": "Domains monitored / Total relevant domains × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "022802", "num": "M2", "name": "Competitive R&D Intelligence Freshness", "what": "Average age of competitive R&D intelligence in days", "why": "Stale intelligence reduces strategic value", "how": "Average (current date − latest update date) across monitored competitors (days)", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "2.6.1": [
        {"id": "022901", "num": "M1", "name": "Launch On-Time Rate", "what": "Percentage of offering launches delivered on the planned date", "why": "Delayed launches miss market windows and revenue targets", "how": "Launches on time / Total launches planned × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "022902", "num": "M2", "name": "Launch Readiness Score", "what": "Average readiness checklist completion at launch", "why": "Incomplete readiness increases launch risk", "how": "Average checklist completion percentage across launches", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.6.2": [
        {"id": "023001", "num": "M1", "name": "Offering Adoption Rate", "what": "Percentage of target customers adopting the offering within first 90 days", "why": "Slow adoption signals product-market fit or launch execution issues", "how": "Customers adopting / Target customers × 100 (at 90 days post-launch)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023002", "num": "M2", "name": "Customer Satisfaction Score (CSAT)", "what": "Average customer satisfaction with the offering", "why": "Low satisfaction predicts churn and negative word-of-mouth", "how": "Average CSAT survey score (1-10)", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "2.6.3": [
        {"id": "023101", "num": "M1", "name": "Iteration Cycle Time", "what": "Average days between offering updates or releases", "why": "Faster iterations enable quicker response to market feedback", "how": "Average days between consecutive releases", "freq": "monthly", "dir": "lower_is_better"},
        {"id": "023102", "num": "M2", "name": "Enhancement Delivery Rate", "what": "Percentage of planned enhancements delivered per cycle", "why": "Low delivery rates indicate capacity or prioritisation issues", "how": "Enhancements delivered / Enhancements planned × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "2.6.4": [
        {"id": "023201", "num": "M1", "name": "Retirement Plan Adherence", "what": "Percentage of offering retirements completed on schedule", "why": "Delayed retirements increase support costs and complexity", "how": "Retirements on schedule / Total planned retirements × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023202", "num": "M2", "name": "Customer Migration Rate", "what": "Percentage of customers migrated from retired offerings", "why": "Unmigrated customers represent revenue risk", "how": "Customers migrated / Total customers on retired offering × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "2.6.5": [
        {"id": "023301", "num": "M1", "name": "Regulatory Compliance Rate", "what": "Percentage of offerings compliant with applicable regulations", "why": "Non-compliance creates legal risk and market access barriers", "how": "Compliant offerings / Total offerings with regulatory requirements × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023302", "num": "M2", "name": "Regulatory Change Response Time", "what": "Days from regulatory change to offering compliance update", "why": "Slow response risks non-compliance penalties", "how": "Compliance update date − regulatory change effective date (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.7.1": [
        {"id": "023401", "num": "M1", "name": "IP Identification Rate", "what": "Number of protectable IP elements identified per quarter", "why": "Unidentified IP cannot be protected", "how": "Count of new IP elements identified", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023402", "num": "M2", "name": "IP Assessment Cycle Time", "what": "Days from identification to protection decision", "why": "Slow assessment risks loss of protection windows", "how": "Decision date − identification date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.7.2": [
        {"id": "023501", "num": "M1", "name": "Patent Filing Rate", "what": "Number of patent applications filed per period", "why": "Filing volume indicates innovation output and IP strategy execution", "how": "Count of patent applications filed", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023502", "num": "M2", "name": "Filing Approval Rate", "what": "Percentage of patent applications granted", "why": "Low approval rates indicate filing quality or strategy issues", "how": "Patents granted / Patents filed × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "2.7.3": [
        {"id": "023601", "num": "M1", "name": "IP Portfolio Renewal Rate", "what": "Percentage of IP assets renewed on schedule", "why": "Missed renewals result in lost IP protection", "how": "Assets renewed on time / Assets due for renewal × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023602", "num": "M2", "name": "IP Portfolio Value", "what": "Estimated commercial value of the IP portfolio", "why": "Tracks portfolio as a strategic asset", "how": "Sum of estimated commercial values across all IP assets", "freq": "annually", "dir": "higher_is_better"},
    ],
    "2.7.4": [
        {"id": "023701", "num": "M1", "name": "Infringement Detection Rate", "what": "Number of potential IP infringements detected per period", "why": "Active detection protects competitive advantage", "how": "Count of potential infringements detected", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023702", "num": "M2", "name": "Infringement Response Time", "what": "Days from detection to initial response action", "why": "Delayed response weakens legal position", "how": "Response action date − detection date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.7.5": [
        {"id": "023801", "num": "M1", "name": "IP Licensing Revenue", "what": "Revenue generated from IP licensing agreements", "why": "Measures commercial exploitation of IP assets", "how": "Total licensing revenue per period", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023802", "num": "M2", "name": "Active License Agreement Count", "what": "Number of active IP licensing agreements", "why": "Tracks breadth of IP commercialisation", "how": "Count of active licensing agreements", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.8.1": [
        {"id": "023901", "num": "M1", "name": "Offering Metric Coverage", "what": "Percentage of offerings with defined measurement frameworks", "why": "Unmeasured offerings cannot be effectively managed", "how": "Offerings with frameworks / Total offerings × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "023902", "num": "M2", "name": "KPI Freshness", "what": "Percentage of offering KPIs reviewed and updated within cycle", "why": "Stale KPIs measure the wrong things", "how": "KPIs reviewed on schedule / Total KPIs × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.8.2": [
        {"id": "024001", "num": "M1", "name": "Data Pipeline Uptime", "what": "Percentage of time usage data pipelines are operational", "why": "Pipeline downtime creates data gaps and delays decisions", "how": "Pipeline uptime hours / Total hours × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "024002", "num": "M2", "name": "Data Integration Completeness", "what": "Percentage of data sources successfully integrated", "why": "Unintegrated sources create incomplete analytics", "how": "Integrated sources / Total identified sources × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.8.3": [
        {"id": "024101", "num": "M1", "name": "A/B Test Completion Rate", "what": "Percentage of planned A/B tests reaching statistical significance", "why": "Inconclusive tests waste resources and delay decisions", "how": "Tests reaching significance / Total tests run × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "024102", "num": "M2", "name": "Experiment Throughput", "what": "Number of experiments completed per period", "why": "Higher throughput accelerates learning velocity", "how": "Count of completed experiments", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "2.8.4": [
        {"id": "024201", "num": "M1", "name": "Predictive Model Accuracy", "what": "Average accuracy of offering performance prediction models", "why": "Inaccurate models lead to poor decisions", "how": "1 − Mean Absolute Percentage Error (MAPE) × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "024202", "num": "M2", "name": "Model Refresh Frequency", "what": "Average days between model retraining cycles", "why": "Stale models degrade in accuracy over time", "how": "Average days between retraining runs", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "2.8.5": [
        {"id": "024301", "num": "M1", "name": "Insight Report Timeliness", "what": "Days after period close that insight reports are delivered", "why": "Late reports reduce actionability", "how": "Report delivery date − period close date (business days)", "freq": "monthly", "dir": "lower_is_better"},
        {"id": "024302", "num": "M2", "name": "Insight Actionability Score", "what": "Percentage of report recommendations acted upon", "why": "Unacted insights represent wasted analytical effort", "how": "Recommendations acted on / Total recommendations × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "2.8.6": [
        {"id": "024401", "num": "M1", "name": "Competitive Monitoring Coverage", "what": "Percentage of key competitors under active monitoring", "why": "Unmonitored competitors create strategic blind spots", "how": "Competitors monitored / Total key competitors × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "024402", "num": "M2", "name": "Competitive Intelligence Freshness", "what": "Average age of competitive intelligence data", "why": "Stale intelligence reduces strategic value", "how": "Average days since last update across monitored competitors", "freq": "monthly", "dir": "lower_is_better"},
    ],

    # Domain 3: Marketing
    "3.1.1": [
        {"id": "030101", "num": "M1", "name": "Marketing Objective Achievement Rate", "what": "Percentage of marketing objectives meeting or exceeding targets", "why": "Tracks overall marketing strategy effectiveness", "how": "Objectives meeting targets / Total objectives × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "030102", "num": "M2", "name": "Marketing Strategy Review Cadence", "what": "Whether marketing strategy reviews occur on schedule", "why": "Regular reviews ensure strategy remains relevant", "how": "Reviews completed on time / Reviews scheduled × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.1.2": [
        {"id": "030201", "num": "M1", "name": "Segment Identification Accuracy", "what": "Percentage of identified segments validated by actual buying behaviour", "why": "Invalid segments waste targeting resources", "how": "Validated segments / Total identified segments × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "030202", "num": "M2", "name": "Target Audience Reach Rate", "what": "Percentage of target audience reached by marketing programmes", "why": "Low reach indicates targeting or channel gaps", "how": "Unique audience reached / Total target audience × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.1.3": [
        {"id": "030301", "num": "M1", "name": "Marketing Plan Completion Rate", "what": "Percentage of planned marketing activities executed", "why": "Unexecuted plans represent missed market opportunities", "how": "Activities executed / Activities planned × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "030302", "num": "M2", "name": "Campaign Launch Timeliness", "what": "Percentage of campaigns launched on or before planned date", "why": "Delayed campaigns miss market timing windows", "how": "Campaigns launched on time / Total campaigns × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.1.4": [
        {"id": "030401", "num": "M1", "name": "Marketing Budget Variance", "what": "Percentage deviation of actual spend from approved budget", "why": "Budget discipline ensures efficient resource use", "how": "|Actual spend − Budget| / Budget × 100", "freq": "monthly", "dir": "lower_is_better"},
        {"id": "030402", "num": "M2", "name": "Marketing Budget Utilisation Rate", "what": "Percentage of approved budget actually deployed", "why": "Underspending signals execution problems or overly conservative planning", "how": "Actual spend / Approved budget × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.1.5": [
        {"id": "030501", "num": "M1", "name": "Message Consistency Score", "what": "Degree of messaging consistency across channels and campaigns", "why": "Inconsistent messaging confuses audiences and dilutes brand", "how": "Brand audit consistency score (1-10)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "030502", "num": "M2", "name": "Positioning Recall Rate", "what": "Percentage of target audience recalling key positioning messages", "why": "Low recall indicates messaging is not landing", "how": "Respondents recalling key messages / Total surveyed × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "3.1.6": [
        {"id": "030601", "num": "M1", "name": "Calendar Conflict Rate", "what": "Percentage of marketing activities with scheduling conflicts", "why": "Conflicts reduce campaign effectiveness and create internal friction", "how": "Activities with conflicts / Total activities × 100", "freq": "monthly", "dir": "lower_is_better"},
        {"id": "030602", "num": "M2", "name": "Cross-Functional Alignment Score", "what": "Rating of marketing alignment with sales, product, and other functions", "why": "Misalignment reduces marketing effectiveness and creates waste", "how": "Cross-functional survey alignment score (1-10)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.2.1": [
        {"id": "030701", "num": "M1", "name": "Brand Guideline Compliance Rate", "what": "Percentage of marketing assets compliant with brand guidelines", "why": "Non-compliance erodes brand consistency and equity", "how": "Compliant assets / Total assets audited × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "030702", "num": "M2", "name": "Brand Identity Refresh Cycle", "what": "Whether brand identity is reviewed within planned cadence", "why": "Stale brand identity loses relevance", "how": "Days since last brand identity review vs planned cycle", "freq": "annually", "dir": "lower_is_better"},
    ],
    "3.2.2": [
        {"id": "030801", "num": "M1", "name": "Brand Consistency Score", "what": "Cross-channel brand consistency rating from audit", "why": "Inconsistency undermines brand trust and recognition", "how": "Average consistency score across channels (1-10)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "030802", "num": "M2", "name": "Brand Deviation Resolution Time", "what": "Days to resolve identified brand consistency deviations", "why": "Unresolved deviations compound brand damage", "how": "Average resolution date − identification date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "3.2.3": [
        {"id": "030901", "num": "M1", "name": "Corporate Communication Reach", "what": "Percentage of target audience reached by corporate communications", "why": "Low reach indicates distribution channel gaps", "how": "Audience reached / Target audience × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "030902", "num": "M2", "name": "Communication Approval Cycle Time", "what": "Days from draft to approved corporate communication", "why": "Slow approval delays time-sensitive messaging", "how": "Approval date − draft submission date (business days)", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.2.4": [
        {"id": "031001", "num": "M1", "name": "Media Mention Volume", "what": "Number of earned media mentions per period", "why": "Media coverage amplifies brand awareness at low cost", "how": "Count of media mentions across tracked outlets", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "031002", "num": "M2", "name": "Media Sentiment Score", "what": "Ratio of positive to negative media coverage", "why": "Negative sentiment damages brand and demand", "how": "Positive mentions / (Positive + Negative mentions) × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.2.5": [
        {"id": "031101", "num": "M1", "name": "Brand Sentiment Score", "what": "Net sentiment across social media and review platforms", "why": "Negative sentiment erodes brand equity and demand", "how": "(Positive mentions − Negative mentions) / Total mentions × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "031102", "num": "M2", "name": "Net Promoter Score (NPS)", "what": "Customer willingness to recommend the brand", "why": "NPS correlates with growth and customer loyalty", "how": "% Promoters − % Detractors", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.2.6": [
        {"id": "031201", "num": "M1", "name": "Crisis Response Time", "what": "Minutes from crisis detection to first public response", "why": "Delayed response amplifies reputational damage", "how": "First response timestamp − crisis detection timestamp (minutes)", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "031202", "num": "M2", "name": "Crisis Communication Effectiveness", "what": "Stakeholder confidence score post-crisis communication", "why": "Effective crisis comms preserve trust and brand equity", "how": "Post-crisis stakeholder survey score (1-10)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.3.1": [
        {"id": "031301", "num": "M1", "name": "Marketing Qualified Leads (MQLs)", "what": "Number of marketing qualified leads generated per period", "why": "MQL volume drives pipeline and revenue growth", "how": "Count of leads meeting MQL criteria", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "031302", "num": "M2", "name": "Cost per MQL", "what": "Average cost to generate a marketing qualified lead", "why": "Tracks demand generation efficiency", "how": "Total demand generation spend / Total MQLs", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.3.2": [
        {"id": "031401", "num": "M1", "name": "Lead Capture Rate", "what": "Percentage of website visitors or event attendees converting to leads", "why": "Low capture rates indicate friction in lead capture process", "how": "Leads captured / Total visitors or attendees × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "031402", "num": "M2", "name": "Lead Data Enrichment Rate", "what": "Percentage of leads with complete firmographic and contact data", "why": "Incomplete data reduces scoring accuracy and sales effectiveness", "how": "Fully enriched leads / Total leads × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.3.3": [
        {"id": "031501", "num": "M1", "name": "Lead Score Accuracy", "what": "Correlation between lead scores and actual conversion outcomes", "why": "Inaccurate scoring misallocates sales effort", "how": "Correlation coefficient between score and conversion probability", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "031502", "num": "M2", "name": "MQL-to-SQL Conversion Rate", "what": "Percentage of MQLs accepted as sales qualified leads", "why": "Low conversion indicates misalignment between marketing and sales criteria", "how": "SQLs / MQLs × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.3.4": [
        {"id": "031601", "num": "M1", "name": "Nurture Engagement Rate", "what": "Percentage of leads actively engaging with nurture content", "why": "Disengaged leads are unlikely to convert", "how": "Leads with engagement actions / Total leads in nurture × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "031602", "num": "M2", "name": "Nurture-to-MQL Conversion Rate", "what": "Percentage of nurtured leads reaching MQL status", "why": "Tracks nurture programme effectiveness", "how": "Nurtured leads reaching MQL / Total leads entering nurture × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.3.5": [
        {"id": "031701", "num": "M1", "name": "Handover Acceptance Rate", "what": "Percentage of marketing-passed leads accepted by sales", "why": "Low acceptance indicates quality or timing issues in handover", "how": "Leads accepted by sales / Leads passed to sales × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "031702", "num": "M2", "name": "Handover Response Time", "what": "Average time for sales to action a passed lead", "why": "Slow follow-up reduces conversion probability", "how": "Average (first sales action timestamp − handover timestamp) in hours", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.3.6": [
        {"id": "031801", "num": "M1", "name": "Funnel Conversion Rate", "what": "Overall conversion rate from top of funnel to opportunity", "why": "Tracks end-to-end demand funnel effectiveness", "how": "Opportunities created / Total leads entering funnel × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "031802", "num": "M2", "name": "Conversion Rate Improvement", "what": "Period-over-period improvement in conversion rates", "why": "Tracks optimisation effectiveness over time", "how": "(Current period rate − Prior period rate) / Prior period rate × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.4.1": [
        {"id": "031901", "num": "M1", "name": "Content Strategy Alignment Score", "what": "Percentage of content mapped to buyer journey stages and personas", "why": "Unmapped content may not reach the right audience at the right time", "how": "Mapped content pieces / Total content pieces × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "031902", "num": "M2", "name": "Editorial Calendar Adherence", "what": "Percentage of planned editorial content published on schedule", "why": "Missed publications create content gaps", "how": "Content published on time / Content planned × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.4.2": [
        {"id": "032001", "num": "M1", "name": "Content Production Velocity", "what": "Number of content pieces produced per period", "why": "Tracks content team productivity and capacity", "how": "Count of content pieces published", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "032002", "num": "M2", "name": "Content Production Cycle Time", "what": "Average days from content brief to published piece", "why": "Shorter cycles improve content relevance and timeliness", "how": "Publication date − brief date (business days)", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.4.3": [
        {"id": "032101", "num": "M1", "name": "Content Engagement Rate", "what": "Average engagement rate across content pieces", "why": "Low engagement indicates content quality or distribution issues", "how": "Total engagements / Total impressions × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "032102", "num": "M2", "name": "Content Quality Score", "what": "Average editorial quality rating of published content", "why": "Quality drives engagement and brand perception", "how": "Average editorial review score (1-10)", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.4.4": [
        {"id": "032201", "num": "M1", "name": "Localisation Coverage Rate", "what": "Percentage of key content localised for target markets", "why": "Unlocalised content limits market penetration", "how": "Content localised / Content requiring localisation × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "032202", "num": "M2", "name": "Localisation Cycle Time", "what": "Average days to localise content for a new market", "why": "Slow localisation delays market entry and campaigns", "how": "Localised content delivery date − source content date (business days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "3.4.5": [
        {"id": "032301", "num": "M1", "name": "Content Repository Completeness", "what": "Percentage of content assets properly tagged and catalogued", "why": "Untagged content is effectively lost to the organisation", "how": "Tagged assets / Total assets × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "032302", "num": "M2", "name": "Content Freshness Rate", "what": "Percentage of content updated or reviewed within its lifecycle", "why": "Stale content damages credibility", "how": "Content reviewed within lifecycle / Total content × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.4.6": [
        {"id": "032401", "num": "M1", "name": "Content ROI", "what": "Revenue attributed to content marketing per dollar spent", "why": "Tracks content marketing investment effectiveness", "how": "Revenue attributed to content / Content marketing spend", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "032402", "num": "M2", "name": "Top-Performing Content Ratio", "what": "Percentage of content exceeding performance benchmarks", "why": "Identifies content strategy effectiveness", "how": "Content exceeding benchmarks / Total content published × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.5.1": [
        {"id": "032501", "num": "M1", "name": "Organic Search Traffic", "what": "Number of website visits from organic search per period", "why": "Organic traffic represents sustainable, low-cost demand generation", "how": "Count of organic search sessions from analytics", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "032502", "num": "M2", "name": "Search Ranking Position", "what": "Average position for priority keywords", "why": "Higher rankings drive more organic traffic and credibility", "how": "Average ranking position across priority keywords", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.5.2": [
        {"id": "032601", "num": "M1", "name": "Paid Media ROAS", "what": "Return on ad spend across paid media channels", "why": "Tracks efficiency of paid media investment", "how": "Revenue attributed to paid media / Paid media spend", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "032602", "num": "M2", "name": "Cost per Click (CPC)", "what": "Average cost per click across paid campaigns", "why": "Rising CPC reduces campaign profitability", "how": "Total paid media spend / Total clicks", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.5.3": [
        {"id": "032701", "num": "M1", "name": "Social Media Engagement Rate", "what": "Average engagement rate across social platforms", "why": "Engagement drives organic reach and brand affinity", "how": "(Likes + Comments + Shares) / Impressions × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "032702", "num": "M2", "name": "Social Audience Growth Rate", "what": "Month-over-month growth in social media followers", "why": "Growing audience expands organic reach", "how": "(New followers − Lost followers) / Prior period followers × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.5.4": [
        {"id": "032801", "num": "M1", "name": "Email Open Rate", "what": "Percentage of delivered emails opened", "why": "Open rates indicate subject line and sender relevance", "how": "Emails opened / Emails delivered × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "032802", "num": "M2", "name": "Email Click-Through Rate", "what": "Percentage of email recipients clicking on links", "why": "Click-through measures content relevance and call-to-action effectiveness", "how": "Unique clicks / Emails delivered × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "3.5.5": [
        {"id": "032901", "num": "M1", "name": "Emerging Channel Experiment Count", "what": "Number of new channels being tested per period", "why": "Active experimentation identifies future growth channels", "how": "Count of new channels with active experiments", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "032902", "num": "M2", "name": "Emerging Channel Performance Baseline", "what": "Percentage of tested channels with established performance baselines", "why": "Baselines enable informed investment decisions", "how": "Channels with baselines / Total tested channels × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.6.1": [
        {"id": "033001", "num": "M1", "name": "KPI Framework Coverage", "what": "Percentage of marketing activities with defined KPIs", "why": "Unmeasured activities cannot be optimised", "how": "Activities with KPIs / Total activities × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "033002", "num": "M2", "name": "Measurement Framework Review Rate", "what": "Whether measurement frameworks are reviewed within cadence", "why": "Outdated frameworks measure the wrong things", "how": "Frameworks reviewed on time / Total frameworks × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "3.6.2": [
        {"id": "033101", "num": "M1", "name": "Attribution Model Coverage", "what": "Percentage of marketing spend covered by attribution models", "why": "Unattributed spend cannot be optimised", "how": "Attributed spend / Total marketing spend × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "033102", "num": "M2", "name": "Attribution Model Confidence Score", "what": "Statistical confidence level of attribution models", "why": "Low confidence models provide unreliable allocation guidance", "how": "Average model confidence score (percentage)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.6.3": [
        {"id": "033201", "num": "M1", "name": "Data Pipeline Uptime", "what": "Percentage of time marketing data pipelines are operational", "why": "Downtime creates reporting gaps and delays decisions", "how": "Pipeline uptime hours / Total hours × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "033202", "num": "M2", "name": "Data Freshness", "what": "Average lag between marketing event and data availability", "why": "Stale data delays campaign optimisation", "how": "Average (data availability timestamp − event timestamp) in hours", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.6.4": [
        {"id": "033301", "num": "M1", "name": "Campaign Effectiveness Score", "what": "Average campaign performance vs target across all campaigns", "why": "Tracks overall campaign execution quality", "how": "Average (actual result / target) × 100 across campaigns", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "033302", "num": "M2", "name": "Channel Efficiency Ranking", "what": "Relative cost-effectiveness ranking of marketing channels", "why": "Identifies best-performing channels for budget reallocation", "how": "Revenue per dollar spent by channel, ranked", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.6.5": [
        {"id": "033401", "num": "M1", "name": "Marketing ROI", "what": "Return on marketing investment", "why": "Demonstrates marketing's financial contribution", "how": "(Revenue attributed to marketing − Marketing cost) / Marketing cost × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "033402", "num": "M2", "name": "Marketing Contribution to Pipeline", "what": "Percentage of sales pipeline sourced by marketing", "why": "Tracks marketing's role in revenue generation", "how": "Marketing-sourced pipeline value / Total pipeline value × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.6.6": [
        {"id": "033501", "num": "M1", "name": "Marketing Mix Model Accuracy", "what": "Accuracy of marketing mix model predictions", "why": "Inaccurate models misguide budget allocation", "how": "1 − |Predicted outcome − Actual outcome| / Actual outcome × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "033502", "num": "M2", "name": "Budget Reallocation Frequency", "what": "Number of data-driven budget reallocations per period", "why": "Active reallocation improves marketing efficiency", "how": "Count of formal budget reallocations based on model outputs", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "3.7.1": [
        {"id": "033601", "num": "M1", "name": "Research Study Completion Rate", "what": "Percentage of commissioned studies completed on time", "why": "Delayed research misses decision windows", "how": "Studies completed on time / Studies commissioned × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "033602", "num": "M2", "name": "Research Investment Efficiency", "what": "Cost per actionable insight from research studies", "why": "Tracks research productivity and value", "how": "Total research spend / Number of actionable insights produced", "freq": "annually", "dir": "lower_is_better"},
    ],
    "3.7.2": [
        {"id": "033701", "num": "M1", "name": "Research Data Coverage", "what": "Percentage of target markets with primary research data", "why": "Research gaps leave markets poorly understood", "how": "Markets with primary data / Total target markets × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "033702", "num": "M2", "name": "Research Freshness", "what": "Average age of market research data in months", "why": "Stale research leads to outdated assumptions", "how": "Average (current date − research completion date) in months", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "3.7.3": [
        {"id": "033801", "num": "M1", "name": "Persona Coverage Rate", "what": "Percentage of target segments with documented personas", "why": "Missing personas leave segments poorly served", "how": "Segments with personas / Total target segments × 100", "freq": "annually", "dir": "higher_is_better"},
        {"id": "033802", "num": "M2", "name": "Journey Map Currency", "what": "Percentage of customer journey maps updated within cycle", "why": "Outdated journey maps lead to poor experience design", "how": "Maps updated on schedule / Total journey maps × 100", "freq": "annually", "dir": "higher_is_better"},
    ],
    "3.7.4": [
        {"id": "033901", "num": "M1", "name": "Competitive Intelligence Coverage", "what": "Percentage of key competitors under active monitoring", "why": "Unmonitored competitors create strategic blind spots", "how": "Competitors monitored / Total key competitors × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "033902", "num": "M2", "name": "Competitive Insight Timeliness", "what": "Average days to analyse and distribute competitive intelligence", "why": "Delayed intelligence reduces strategic value", "how": "Average (distribution date − event date) in business days", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "3.7.5": [
        {"id": "034001", "num": "M1", "name": "Insight Distribution Reach", "what": "Percentage of target stakeholders receiving market intelligence", "why": "Undistributed insights have no impact on decisions", "how": "Stakeholders receiving insights / Target stakeholders × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "034002", "num": "M2", "name": "Insight Utilisation Rate", "what": "Percentage of distributed insights referenced in decisions", "why": "Unused insights represent wasted research investment", "how": "Insights cited in decisions / Total insights distributed × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],

    # Domain 4: Sales
    "4.1.1": [
        {"id": "040101", "num": "M1", "name": "Sales Strategy Achievement Rate", "what": "Percentage of strategic sales objectives meeting targets", "why": "Tracks overall sales strategy effectiveness", "how": "Objectives meeting targets / Total strategic objectives × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "040102", "num": "M2", "name": "Go-to-Market Plan Adherence", "what": "Percentage of GTM plan milestones completed on schedule", "why": "Delayed GTM execution misses market windows", "how": "Milestones completed on time / Total milestones × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.1.2": [
        {"id": "040201", "num": "M1", "name": "Territory Coverage Efficiency", "what": "Percentage of addressable market covered by territory assignments", "why": "Uncovered territories represent missed revenue", "how": "Covered addressable market / Total addressable market × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "040202", "num": "M2", "name": "Territory Balance Index", "what": "Standard deviation of revenue potential across territories", "why": "Imbalanced territories create unfair quotas and coverage gaps", "how": "Standard deviation of territory revenue potential / Mean territory potential", "freq": "annually", "dir": "lower_is_better"},
    ],
    "4.1.3": [
        {"id": "040301", "num": "M1", "name": "Quota Attainment Rate", "what": "Percentage of sales reps achieving or exceeding quota", "why": "Low attainment indicates unrealistic targets or execution issues", "how": "Reps at or above quota / Total quota-carrying reps × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "040302", "num": "M2", "name": "Quota Setting Accuracy", "what": "Variance between aggregate quota and actual revenue", "why": "Inaccurate quotas undermine planning and compensation", "how": "|Total quota − Actual revenue| / Total quota × 100", "freq": "annually", "dir": "lower_is_better"},
    ],
    "4.1.4": [
        {"id": "040401", "num": "M1", "name": "ICP Match Rate", "what": "Percentage of active opportunities matching the ideal customer profile", "why": "Pursuing non-ICP accounts wastes sales resources and reduces win rates", "how": "ICP-matching opportunities / Total active opportunities × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "040402", "num": "M2", "name": "Account Tier Distribution", "what": "Percentage of sales effort allocated to high-value account tiers", "why": "Misallocated effort reduces revenue potential", "how": "Time spent on Tier 1-2 accounts / Total selling time × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.1.5": [
        {"id": "040501", "num": "M1", "name": "Sales-Marketing Alignment Score", "what": "Rating of alignment between sales and marketing strategies", "why": "Misalignment wastes resources and creates pipeline gaps", "how": "Joint alignment survey score (1-10)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "040502", "num": "M2", "name": "Coverage Gap Count", "what": "Number of identified gaps between sales coverage and market strategy", "why": "Gaps represent unaddressed revenue opportunities", "how": "Count of documented coverage-strategy gaps", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.2.1": [
        {"id": "040601", "num": "M1", "name": "Pipeline Creation Rate", "what": "Value of new pipeline created per period", "why": "Insufficient pipeline creation threatens future revenue", "how": "Total value of new opportunities created", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "040602", "num": "M2", "name": "Pipeline Coverage Ratio", "what": "Ratio of pipeline value to revenue target", "why": "Insufficient coverage creates revenue risk", "how": "Total pipeline value / Revenue target", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "4.2.2": [
        {"id": "040701", "num": "M1", "name": "Stage Progression Rate", "what": "Percentage of opportunities advancing to next stage per period", "why": "Stalled opportunities consume resources without revenue", "how": "Opportunities advancing / Total active opportunities × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "040702", "num": "M2", "name": "Average Sales Cycle Length", "what": "Average days from opportunity creation to close", "why": "Longer cycles increase cost of sale and risk", "how": "Average (close date − creation date) across won deals (calendar days)", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.2.3": [
        {"id": "040801", "num": "M1", "name": "Forecast Accuracy", "what": "Percentage accuracy of revenue forecast vs actual results", "why": "Inaccurate forecasts undermine financial planning and credibility", "how": "1 − |Forecast − Actual| / Actual × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "040802", "num": "M2", "name": "Forecast Bias", "what": "Directional tendency of forecast errors (over vs under)", "why": "Systematic bias indicates process or cultural issues", "how": "Average (Forecast − Actual) / Actual × 100", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.2.4": [
        {"id": "040901", "num": "M1", "name": "Pipeline Review Cadence Adherence", "what": "Percentage of scheduled pipeline reviews completed on time", "why": "Missed reviews reduce pipeline visibility and deal support", "how": "Reviews completed / Reviews scheduled × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "040902", "num": "M2", "name": "Pipeline Health Score", "what": "Composite score of pipeline balance, velocity, and conversion", "why": "Holistic pipeline health predicts future revenue performance", "how": "Weighted composite of coverage, velocity, and conversion metrics (0-100)", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "4.2.5": [
        {"id": "041001", "num": "M1", "name": "At-Risk Deal Identification Rate", "what": "Percentage of deals flagged at-risk before they slip or are lost", "why": "Early identification enables intervention", "how": "Deals flagged before loss / Total lost deals × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041002", "num": "M2", "name": "Pipeline Gap Closure Rate", "what": "Percentage of identified pipeline gaps closed within target period", "why": "Open gaps threaten future revenue targets", "how": "Gaps closed / Total gaps identified × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.2.6": [
        {"id": "041101", "num": "M1", "name": "Forecast Deviation Trend", "what": "Period-over-period improvement in forecast accuracy", "why": "Improving accuracy demonstrates process maturation", "how": "Current period accuracy − Prior period accuracy (percentage points)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041102", "num": "M2", "name": "Methodology Refinement Actions", "what": "Number of forecast methodology improvements implemented", "why": "Active refinement drives continuous accuracy improvement", "how": "Count of documented methodology changes per period", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.3.1": [
        {"id": "041201", "num": "M1", "name": "Strategic Account Plan Coverage", "what": "Percentage of strategic accounts with current account plans", "why": "Unplanned accounts lack structured growth strategies", "how": "Accounts with current plans / Total strategic accounts × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041202", "num": "M2", "name": "Account Revenue Growth Rate", "what": "Year-over-year revenue growth in strategic accounts", "why": "Growth validates account strategy effectiveness", "how": "(Current year revenue − Prior year revenue) / Prior year revenue × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.3.2": [
        {"id": "041301", "num": "M1", "name": "Stakeholder Map Completeness", "what": "Average percentage of key stakeholders mapped per strategic account", "why": "Incomplete maps create relationship blind spots", "how": "Average (stakeholders mapped / estimated total) × 100 across accounts", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041302", "num": "M2", "name": "Executive Relationship Depth", "what": "Number of active C-level relationships per strategic account", "why": "Executive access drives strategic deal-making", "how": "Average C-level contacts with recent engagement per account", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.3.3": [
        {"id": "041401", "num": "M1", "name": "Cross-Sell Revenue", "what": "Revenue from cross-sell and up-sell in existing accounts", "why": "Cross-sell is more efficient than new customer acquisition", "how": "Revenue from cross-sell and up-sell transactions", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041402", "num": "M2", "name": "Product Penetration Rate", "what": "Average number of products per strategic account", "why": "Higher penetration deepens relationships and increases switching costs", "how": "Total products sold / Total strategic accounts", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.3.4": [
        {"id": "041501", "num": "M1", "name": "Multi-Team Coordination Effectiveness", "what": "Account team satisfaction with cross-team coordination", "why": "Poor coordination creates inconsistent customer experience", "how": "Average coordination satisfaction score from account teams (1-10)", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041502", "num": "M2", "name": "Commitment Delivery Rate", "what": "Percentage of customer commitments delivered on time across teams", "why": "Missed commitments damage trust and retention", "how": "Commitments delivered on time / Total commitments × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "4.3.5": [
        {"id": "041601", "num": "M1", "name": "EBR Completion Rate", "what": "Percentage of strategic accounts receiving executive business reviews", "why": "EBRs strengthen executive relationships and surface growth opportunities", "how": "Accounts with completed EBRs / Total strategic accounts × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041602", "num": "M2", "name": "EBR Action Item Follow-Through", "what": "Percentage of EBR action items completed by due date", "why": "Undelivered commitments from EBRs damage credibility", "how": "Actions completed on time / Total EBR actions × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.4.1": [
        {"id": "041701", "num": "M1", "name": "Proposal Win Rate", "what": "Percentage of submitted proposals resulting in won deals", "why": "Low win rates indicate proposal quality or targeting issues", "how": "Proposals won / Proposals submitted × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041702", "num": "M2", "name": "Proposal Cycle Time", "what": "Average days from proposal request to delivery", "why": "Slow proposals risk losing deals to faster competitors", "how": "Average (delivery date − request date) in business days", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.4.2": [
        {"id": "041801", "num": "M1", "name": "Average Deal Size", "what": "Average revenue value of closed-won deals", "why": "Tracks pricing effectiveness and deal quality", "how": "Total closed-won revenue / Number of closed-won deals", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041802", "num": "M2", "name": "Discount Rate", "what": "Average discount given as percentage of list price", "why": "Excessive discounting erodes margins", "how": "Average (list price − deal price) / list price × 100", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.4.3": [
        {"id": "041901", "num": "M1", "name": "Win Rate on Complex Deals", "what": "Percentage of complex (multi-stakeholder) deals won", "why": "Complex deal win rate indicates negotiation capability", "how": "Complex deals won / Complex deals pursued × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "041902", "num": "M2", "name": "Negotiation Cycle Time", "what": "Average days in negotiation stage before close", "why": "Extended negotiations increase deal risk and resource cost", "how": "Average days in negotiation stage for closed deals", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.4.4": [
        {"id": "042001", "num": "M1", "name": "Approval Cycle Time", "what": "Average days from approval request to decision", "why": "Slow approvals delay deal closure and frustrate customers", "how": "Average (approval date − request date) in business days", "freq": "monthly", "dir": "lower_is_better"},
        {"id": "042002", "num": "M2", "name": "Approval SLA Compliance Rate", "what": "Percentage of approvals completed within defined SLAs", "why": "SLA breaches indicate bottlenecks in deal governance", "how": "Approvals within SLA / Total approvals × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "4.4.5": [
        {"id": "042101", "num": "M1", "name": "Contract Execution Cycle Time", "what": "Average days from final terms to executed contract", "why": "Delays between agreement and signature risk deal changes", "how": "Average (execution date − terms agreement date) in business days", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "042102", "num": "M2", "name": "Contract Error Rate", "what": "Percentage of contracts requiring post-signature amendments", "why": "Errors create legal risk and customer friction", "how": "Contracts with amendments / Total executed contracts × 100", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.4.6": [
        {"id": "042201", "num": "M1", "name": "Win/Loss Analysis Completion Rate", "what": "Percentage of closed deals with completed win/loss analysis", "why": "Analysis drives strategic learning and process improvement", "how": "Deals with completed analysis / Total closed deals × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "042202", "num": "M2", "name": "Win Rate Trend", "what": "Period-over-period change in overall win rate", "why": "Improving win rates indicate growing competitive effectiveness", "how": "Current period win rate − Prior period win rate (percentage points)", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.5.1": [
        {"id": "042301", "num": "M1", "name": "CRM Data Accuracy Rate", "what": "Percentage of CRM records meeting data quality standards", "why": "Poor data quality undermines forecasting and reporting", "how": "Records meeting quality standards / Total records × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "042302", "num": "M2", "name": "Duplicate Record Rate", "what": "Percentage of CRM records identified as duplicates", "why": "Duplicates fragment customer views and waste effort", "how": "Duplicate records / Total records × 100", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "4.5.2": [
        {"id": "042401", "num": "M1", "name": "Sales Ramp Time", "what": "Average days for new sales reps to reach full productivity", "why": "Faster ramp accelerates revenue and reduces hiring costs", "how": "Average days from start date to first quota attainment", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "042402", "num": "M2", "name": "Training Completion Rate", "what": "Percentage of sales reps completing required training", "why": "Incomplete training reduces effectiveness and compliance", "how": "Reps completing training / Total reps × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.5.3": [
        {"id": "042501", "num": "M1", "name": "Playbook Adoption Rate", "what": "Percentage of sales reps actively using approved playbooks", "why": "Unused playbooks represent wasted enablement investment", "how": "Reps using playbooks / Total reps × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "042502", "num": "M2", "name": "Collateral Currency Rate", "what": "Percentage of sales collateral updated within review cycle", "why": "Outdated collateral damages credibility and effectiveness", "how": "Current collateral / Total collateral × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.5.4": [
        {"id": "042601", "num": "M1", "name": "Sales Tool Adoption Rate", "what": "Percentage of sales reps actively using core sales tools", "why": "Low adoption wastes technology investment", "how": "Active users / Total licensed users × 100", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "042602", "num": "M2", "name": "Sales Tech Stack ROI", "what": "Revenue generated per dollar of sales technology investment", "why": "Tracks sales technology investment effectiveness", "how": "Total revenue / Total sales tech spend", "freq": "annually", "dir": "higher_is_better"},
    ],
    "4.5.5": [
        {"id": "042701", "num": "M1", "name": "Sales Process Adherence Rate", "what": "Percentage of deals following the defined sales process", "why": "Non-adherence reduces forecast accuracy and deal quality", "how": "Deals following process / Total deals × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "042702", "num": "M2", "name": "Process Optimisation Actions", "what": "Number of process improvements implemented per period", "why": "Active optimisation drives continuous sales effectiveness gains", "how": "Count of documented process improvements", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.6.1": [
        {"id": "042801", "num": "M1", "name": "Channel Revenue Contribution", "what": "Percentage of total revenue from channel and partner sales", "why": "Tracks channel strategy effectiveness", "how": "Channel revenue / Total revenue × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "042802", "num": "M2", "name": "Channel Strategy Coverage", "what": "Percentage of target markets covered by channel partners", "why": "Coverage gaps limit market reach", "how": "Markets with partner coverage / Total target markets × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.6.2": [
        {"id": "042901", "num": "M1", "name": "Partner Recruitment Rate", "what": "Number of new channel partners onboarded per period", "why": "Recruitment velocity drives channel growth", "how": "Count of new partners onboarded", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "042902", "num": "M2", "name": "Partner Onboarding Cycle Time", "what": "Average days from partner agreement to first deal registration", "why": "Faster onboarding accelerates time to partner revenue", "how": "Average (first deal registration date − agreement date) in calendar days", "freq": "quarterly", "dir": "lower_is_better"},
    ],
    "4.6.3": [
        {"id": "043001", "num": "M1", "name": "Partner Certification Rate", "what": "Percentage of partners completing certification programmes", "why": "Certified partners sell more effectively", "how": "Certified partners / Total active partners × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "043002", "num": "M2", "name": "Partner Enablement Content Usage", "what": "Percentage of enablement materials accessed by partners", "why": "Unused materials indicate enablement gaps or poor content", "how": "Materials accessed / Total materials available × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.6.4": [
        {"id": "043101", "num": "M1", "name": "Partner Pipeline Value", "what": "Total value of partner-sourced pipeline", "why": "Partner pipeline drives channel revenue growth", "how": "Sum of partner-sourced opportunity values", "freq": "monthly", "dir": "higher_is_better"},
        {"id": "043102", "num": "M2", "name": "Co-Sell Engagement Rate", "what": "Percentage of partner deals with active co-selling", "why": "Co-selling improves win rates and deal sizes", "how": "Deals with co-selling / Total partner deals × 100", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.6.5": [
        {"id": "043201", "num": "M1", "name": "Partner Revenue per Partner", "what": "Average revenue generated per active channel partner", "why": "Tracks individual partner productivity", "how": "Total partner revenue / Number of active partners", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "043202", "num": "M2", "name": "Partner Incentive ROI", "what": "Revenue generated per dollar of partner incentive spend", "why": "Ensures incentive programmes drive profitable growth", "how": "Incremental partner revenue / Total incentive spend", "freq": "quarterly", "dir": "higher_is_better"},
    ],
    "4.7.1": [
        {"id": "043301", "num": "M1", "name": "Metric Definition Alignment Rate", "what": "Percentage of revenue metrics with consistent definitions across teams", "why": "Inconsistent definitions create reporting conflicts", "how": "Aligned metrics / Total shared metrics × 100", "freq": "quarterly", "dir": "higher_is_better"},
        {"id": "043302", "num": "M2", "name": "Cross-Team Data Reconciliation Rate", "what": "Percentage of data discrepancies resolved between marketing and sales systems", "why": "Unresolved discrepancies undermine trust in reporting", "how": "Discrepancies resolved / Total discrepancies identified × 100", "freq": "monthly", "dir": "higher_is_better"},
    ],
    "4.7.2": [
        {"id": "043401", "num": "M1", "name": "Lead-to-Cash Cycle Time", "what": "Average days from initial lead to revenue recognition", "why": "Shorter cycles improve cash flow and resource efficiency", "how": "Average (revenue recognition date − lead creation date) in calendar days", "freq": "quarterly", "dir": "lower_is_better"},
        {"id": "043402", "num": "M2", "name": "Process Handoff Error Rate", "what": "Percentage of handoffs with errors or missing information", "why": "Errors slow the process and frustrate internal teams", "how": "Handoffs with errors / Total handoffs × 100", "freq": "monthly", "dir": "lower_is_better"},
    ],
    "4.7.3": [
        {"id": "043501", "num": "M1", "name": "Revenue per Employee", "what": "Total revenue divided by number of revenue-generating employees", "why": "Tracks revenue team productivity and efficiency", "how